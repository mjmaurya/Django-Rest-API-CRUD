# Django Rest API CRUD

*This is a Django Rest API Project In this Project I have Implemented RUD operation in Rest API.*

### CRUD
   - C- Create- POST
   - R- Read or Retrive - GET
   - U- Update- PUT
   - D- Delete or Remove- DELETE

# Installation 

### 1. Clone this repository

### 2. Open CMD in the folder where you cloned this project and switch to ```restapi``` folder by ```cd Django-Rest-API-CRUD```

## Now install some library by running below command

```
pip install djangorestframework
```

``` 
pip install psycopg2 
```


* Now Open settings.py folder and update 

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': # YOUR_DATABASE_NAME,
        'USER':'postgres',
        'PASSWORD':# POSTGRESS PASSWORD,
        'HOST':'localhost'
    }
}
```

## Now Run

```
python manage.py migrate
```
```
python manage.py runserver
```

## Now Open Browser and paste below url

```
http://127.0.0.1:8000/api/employee/
```