# Chameleon App
An app to help homeowners and interior designers to reimagine interior surfaces with different paints. The app utilizes machine learning models to crop out surfaces to recolour in a photo and recolours them with the desired paint colour by the user. The app also features a robust profile system to allow users to leave reviews on paints, save paints as favourites and view history of paints used for recolouring in the past

Group members: Kevin Hu (20883031), Peter Huang (20872914), Brian Chae (20891074), Myles Esteban (20882330), Frank Yu (20898350), Jugal Bilimoria (20885692)

# App demo link
The following demo shows a run through of how to use the app (different from the demo, users can sign up to create an account):

https://www.youtube.com/watch?v=evf0q-GEjXs

# User Flow
- [User Login](#user-login)
- [Navigate all colors](#navigate-all-colors)
- [review color](#review-color)
- [Feavorite a color](#favorite-a-color)
- [select wall to revisualize](#select-wall-to-revisualize)
- [select color(s)](#select-colors)
- [Reviewing the revisualized wall](#reviewing-the-revisualized-wall)
- [User Profile Tab](#user-profile-tab)


## User Login

The app allows users to create an account and login to their created account. By doing so, users are able to keep track of their previously colored walls, previously used colors and their favorited colors

![image](https://github.com/user-attachments/assets/635837da-4402-40ab-a159-c4f3b6d7dade)


## Navigate all colors

The colors tab shows all avaliable colors the user can choose to revisualize their walls with. The user has the option to search the colors using different criteria such as their brand, product name, color group (i.e red, blue, yellow, etc.), rgb and hsl.
The user can also sort the colors based on name, brand and color group

![image](https://github.com/user-attachments/assets/b8254e8f-c746-4db3-a377-4c1eaf914a85)

## Review color

Upon selecting a color, a summary will be shown for the selected color. The summary will include information such as user reviews, user favorite status, brand, product ID and an option for users to leave their own review (or update already posted reviews).
The user can also press the "try" button to automatically have the paint selected next time they want to use the paint visualization feature

![image](https://github.com/user-attachments/assets/f726cf3b-3fd1-45e2-b0b8-fc6c598bacbe)

## Favorite a color

If chosen to favorite a color, it will immediately be reflected on the color summary page with the heart icon being filled red. Furthermore, the user can navigate to the user summary tab where the user's favorited colors as well as their usage history will be shown

![image](https://github.com/user-attachments/assets/116f76d1-8189-4e1e-92f8-f544b02b01b8)

### User summary tab
![image](https://github.com/user-attachments/assets/d1596ddc-72d4-4a64-b8f6-094656dbbec5)

## Select wall to revisualize

Using the application, the user can take a picture of any wall that they wish to revisualize. Clicking the transparent circle will immediately take an image using the camera's back camera and save the image to storage. 

![image](https://github.com/user-attachments/assets/55017ac6-5557-4b1b-a924-47aa977ba885)

## Select color(s)

After an image has been taken, the user will be prompted to select upto 3 colors to revisualize the wall with. As we can see, grape green is already selected as a color automatically as the "try" option was previously selected for this color.
The user can filter colors by color group, brand and name

### Color being automatically selected as a result of "try" feature
![image](https://github.com/user-attachments/assets/06615fcd-d2bf-4e05-9e2f-9d7f69df4a11)

### Second color being selected along with automatically selected color
![image](https://github.com/user-attachments/assets/d55647ea-6055-4f31-89ae-cbddc9326c94)

## Reviewing the revisualized wall

After the colors have been selected, the images and color data will be sent for processing. The processed data will then automatically be displayed to the user. If multiple colors were selected, the user can freely switch between colors and the original image

### Grape Green
![image](https://github.com/user-attachments/assets/55c12155-5b96-4874-96f6-04a14adf1ce1)

### Light Blue
![image](https://github.com/user-attachments/assets/b7cd46f1-be19-4f86-8815-bbc3fbf446a4)

### Original Wall
![image](https://github.com/user-attachments/assets/77cabdf5-f05d-4e1d-ae11-97cfdc1c171a)

## User Profile Tab

The user profile tab holds data regarding the user's favorited colors as well as their visualization history. The favorited colors section holds a list of color cards. Users may click on the color cards to easily pull out the color's summary.
The visualization history shows all past walls the users revisualized along with the selected colors. The users may click on the history look at the original image and all its revisualizations

![image](https://github.com/user-attachments/assets/1fb8f51a-21cb-4270-8005-20b56c5c2d71)

### Original image from history
![image](https://github.com/user-attachments/assets/bd3a15b4-80ca-4e8b-8ac0-1de1acda2825)

### Revisualization from history
![image](https://github.com/user-attachments/assets/19c8f6a3-3b33-4cfc-99be-d131f7471548)


