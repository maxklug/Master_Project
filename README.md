# CSE-6242-Project-Team-15

### Full Github Repository: https://github.gatech.edu/mklug7/CSE-6242-Project-Team-15/

## Image Classification (not required to run the application) 

### This image classification training model may take upto 24 hour to run

### 1. Downloading the Dataset: 
In order for the backend program to run smoothly, you will need to download the picture datasets - fill/replace the following folders with the pictures from these github folders: 
  - Backend/Data/food_images/test/ - link: https://github.gatech.edu/mklug7/CSE-6242-Project-Team-15/tree/master/Backend/Data/food_images/test
  - Backend/Data/food_images/train/ - link: https://github.gatech.edu/mklug7/CSE-6242-Project-Team-15/tree/master/Backend/Data/food_images/train
  - Backend/Data/yelp_dataset/photos - link: https://github.gatech.edu/mklug7/CSE-6242-Project-Team-15/tree/master/Backend/Data/yelp_dataset/photos
  
### 2. Running the jupyter notebook "food_image_classification.ipynb":
  - `cd Backend`
  - `jupyter notebook`
  - Best way to run the notebook is via anaconda. 
  - Be aware that, depending on your computer, the training of the CNN can take up to 24 hours. If you do not want to train a new model, feel free to load them from the backendfolder. 

## Running the application

### Running Backend Service
The backend service consumes the result from the image classification module, formats it and passes to the frontend. We took the business.csv and image.csv (with probabilities) files. Django creates backend with imported database.

- Install django** (https://docs.djangoproject.com/en/3.0/topics/install/):
  - `python -m pip install Django`
  - `python -m pip install djangorestframework`
  - `python -m pip install django-cors-headers`

- Open Terminal/Command prompt 
- In the project directory, go to team15 folder 
  - `cd team15`
- Run below commands:
  - `$ python manage.py runserver`



### Running the UI
- Open Terminal/Command prompt 
- In the project directory, go to Frontend folder 
  - `cd Frontend`
- Run the following commands:
  - `brew install yarn`
  - `npm config set registry https://registry.npmjs.com/`
  - `npm config list`
  - `yarn`
  - `yarn start`
- This will run the app in the development mode.
- Open http://localhost:3000 to view it in the browser.
- Open a new terminal window and in the same path run below commands:
  - `node server.js`
- Refresh http://localhost:3000 The page will reload if you make edits.

### Demo video
[![Demo](https://img.youtube.com/vi/odTvNrISvCw/0.jpg)](https://youtu.be/odTvNrISvCw)
- https://youtu.be/odTvNrISvCw

### Screen shot of UI: 
![Screen shot of UI:](./pizza.png?raw=true "Title")		
