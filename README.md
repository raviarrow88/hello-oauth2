# hello-oauth2
* This a simple scenario how to use oauth2 between two projects  using Django-rest Framework.

-> In the first project, "master_server"(consider this is a master project) ,application is created and client id and client secret key are generated and using the details access token is generated.

-> In the second project, "client_server"(consider thus is a child project), whatever the access token is generated in first project ,through that access token we will access the first project data.

Platform : Pycharm.

Steps:

1) Created a project 'hello-api2'.

2) Inside the project,created an app 'hello_api2'.

3) I have a created a model Books which contains the attributes Owner,title and author.

4) Registered the app created in the admin.py file.

5) To install oauth 2.0 in django rest  framework:

   ``` pip install django-oauth-toolkit djangorestframework```
    
6) After installing ,add ‘rest_framework’ and ‘oauth2_provider’ to your installed apps in settings.py file.

7)Add  the following class``` 'oauth2_provider.ext.rest_framework.OAuth2Authentication'```, to the ```DEFAULT_AUTHENTICATION_CLASSES``` in settings.py file.

8) add the following to the settings.py file

    ```OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}```

9) add the url
     ```url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),```
   to the urls.py file.
   
10) Run the commands,
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

11) After running the server enter the following url into the browser:```http://localhost:8000/o/applications/```

12) create an application,

```Name: just a name of your choice```
```Client Type: confidential```
```Authorization Grant Type: Resource owner password-based```

13) After creating the application, client id and client secret keys will be generated

14) To get the access token, run the following curl command in shell or terminal

```curl -X POST -d "grant_type=password&username=<user_name>&password=<password>" -u"<client_id>:<client_secret>" http://localhost:8000/o/token/```

```username: django admin username```
```password: django admin password```
```client id:oauth application clientid```
```client secret secret: oauth application client secret```

after executing the command output shown like:

```{
    "access_token": "<your_access_token>",
    "token_type": "Bearer",
    "expires_in": 36000,
    "refresh_token": "<your_refresh_token>",
    "scope": "read write groups"
}```

15) After generating the access token , open the second project "hello-api3" run the curl command

```curl -H "Authorization: Bearer <your_access_token>" http://localhost:8000/protectedurl/```

you can access the first project1 data.







