from fastapi import HTTPException, Depends
from firebase_admin import firestore_async
from google.cloud.firestore_v1 import DocumentSnapshot, FieldFilter
from Api.data_classes import CreateUserDto, UserLoginDto
from typing import Union
from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext


class User:
    def __init__(self, email: str, firstname: str, lastname: str, uid: str):
        self.email: str = email
        self.firstname: str = firstname
        self.lastname: str = lastname
        self.uid: str = uid

    @classmethod
    def from_firestore_document(cls, doc: DocumentSnapshot) -> 'User':
        data = doc.to_dict()
        return cls(
            email=data.get("email", ""),
            firstname=data.get("firstname", ""),
            lastname=data.get("lastname", ""),
            uid=doc.id
        )

    def to_dict(self):
        return {
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "uid": self.uid
        }


class UserAuthenticationRepository:
    def __init__(self, env) -> None:
        self.collectionRef = firestore_async.client().collection('users')
        self.signingKey = env.jwt_signing_key
        self.signingAlgorithm = "HS256"
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __verify_password(self, plaintext, hashed_password):
        return self.pwd_context.verify(plaintext, hashed_password)

    def __hash_password(self, plaintext):
        return self.pwd_context.hash(plaintext)

    def create_access_token(self, user: User) -> str:
        data: dict = {"usr": user.email}
        to_encode = data.copy()
        expiration_date = datetime.now(timezone.utc) + timedelta(days=10)
        to_encode.update({"exp": expiration_date})
        token = jwt.encode(to_encode, self.signingKey, self.signingAlgorithm)
        return token

    async def authenticate_access_token_async(self, token: str) -> User:
        try:
            payload = jwt.decode(token, self.signingKey, [self.signingAlgorithm])
            identification = payload.get("usr")
            expiration = payload.get("exp")
            if identification is None:
                raise InvalidTokenError
            if expiration is None or expiration < datetime.now(timezone.utc).timestamp():
                print("expired token Received")
                raise HTTPException(status_code=401, detail="Token is expired")
        except InvalidTokenError:
            print("Credentials could not be validated! Invalid Token Error")
            raise HTTPException(status_code=401, detail="Could not validate credentials")
        user = await self.get_user_from_email(identification)
        if user is None:
            print("Could not validate credentials, User does not exist")
            raise HTTPException(status_code=401, detail="Could not validate credentials")
        return user

    async def get_user_from_login(self, login_dto: UserLoginDto) -> Union[User, None]:
        try:
            query = self.collectionRef.where(filter=FieldFilter("email", "==", login_dto.email))
            users = [user async for user in query.stream()]
            if len(users) == 0:
                return None
            user_document = users[0]
            if self.__verify_password(login_dto.password, user_document.get("password")):
                return User.from_firestore_document(user_document)
            else:
                return None
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def get_user_from_email(self, email: str):
        try:
            query = self.collectionRef.where(filter=FieldFilter("email", "==", email))
            users = [user async for user in query.stream()]
            if len(users) == 0:
                return None
            user_document = users[0]
            return User.from_firestore_document(user_document)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def __create_user_snapshot(self, create_user_dto: CreateUserDto):
        return {
            "email": create_user_dto.email,
            "firstname": create_user_dto.firstname,
            "lastname": create_user_dto.lastname,
            "password": self.__hash_password(create_user_dto.password)
        }

    async def create_user_async(self, create_user_dto: CreateUserDto) -> User:
        new_user_document_dict = self.__create_user_snapshot(create_user_dto)
        try:
            new_user_document = await self.collectionRef.add(new_user_document_dict)
            uid = new_user_document[1].id  # this gets the document ID that was just created
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        newUser = User(create_user_dto.email, create_user_dto.firstname, create_user_dto.lastname, uid)
        return newUser
