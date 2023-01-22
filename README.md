# DJango Project
This project will read the PC properties and return JSON as response.

Install Django
* $ pip3 install Django

To create a new Django project using the django-admin command line tool, you can use the startproject command. The basic syntax is as follows:
* $ django-admin startproject pcproject

In Django, an app is a self-contained module that encapsulates a specific functionality. To create a new app within a Django project, you can use the startapp command in the manage.py file. The basic syntax is as follows:
* $ python3 manage.py startapp pcapp

Start the server
* $ python3 manage.py runserver

# url
* http://localhost:8000/pcapp/system_info_json