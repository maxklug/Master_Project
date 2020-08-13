## In this folder you may find backend of our project
### As output from classification folder, I took - business.csv and image.csv (with probabilities) files.Django creates backend with imported database.

- Here is the django documentation. Please review tutorial if you want to study this framework.
  - https://docs.djangoproject.com/en/3.0/
  - https://www.djangoproject.com/download/

- Install django** (https://docs.djangoproject.com/en/3.0/topics/install/):
  - `python -m pip install Django`
  - `python -m pip install djangorestframework`
  - `python -m pip install django-cors-headers`

- Open Terminal/Command prompt 
- In the project directory, go to team15 folder 
  - `cd team15`
- Run below commands:
  - `$ python manage.py runserver`

- After that, you need to open in your browser root to API 
  - http://127.0.0.1:8000/api/restaurant/?type=0    ÑÑ> for BURGER
  - http://127.0.0.1:8000/api/restaurant/?type=1     ÑÑ> for  PIZZA
  - http://127.0.0.1:8000/api/restaurant/?type=2    ÑÑ> for SALAD

- Each businessID returns 1 photoID with the best match and prob>70%

- React should send and pick up Ajax request to 
  - http://ourserver:8000/api/restaurant/?type=
  - http://127.0.0.1:8000/api/restaurant/?type=0

- or photos available for each restaurant
  - http://ourserver:8000/api/restaurant/businessid/
  - http://127.0.0.1:8000/api/restaurant/cs1qJvnWUg_f8g020z_3PQ/
