# Django-chatApp
Created a realtime chat App from basic to end and tested it on websocketking, will be integrating to a react application soon

Install the dependecies from requirements.txt

This doc will guide you how to make a realtime chat app using django using websocket and deploy it to the server. First we will go for chat app implementation and then we will deploy it.

Create a virtual env and activate it.
Install the dependencies django, channels, djangorestframework, daphne.
Change the database to postgres or keep it to SQLite if it's for testing.
Create django project using django-admin startproject chatAppProj
Navigate to project directory created using cd chatAppProj
Run command python manage.py runserver to run the application
Open Websocketking.com to test your app.


Created a detailed doc how to develop a realtime chatapp from scratch and how to deploy it using apache + daphne server config on aws.
Details docs here : https://docs.google.com/document/d/12IPZuTxgHzyb3axOZ8nbVAVZHDDUCRseU2lNLz63bLI/edit
