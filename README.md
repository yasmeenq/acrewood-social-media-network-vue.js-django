


## Vue. js

1. create vue project: 
    1. have the latest version of Node.js
    2. npm init vue@latest  (using vite)
    3. press y to proceed then name the project, hecto_frontend
    4. choose yes for the following (and No for the rest):
        a. Add Vue Router for Single Page Application development? » No / Yes
        b. Add Pinia for state management? ... No / Yes
    5. cd hecto_frontend
    6. npm install
    7. npm run dev


2. install dependencies:
    1. install axios and add it to main.js: npm install axios
    2. install Tailwind: 
        (follow documentations for vue + vite on tailwind website )
        https://v3.tailwindcss.com/docs/guides/vite#vue
    3. download Vue extension 

    
icons are from heroicon.com


##Django 
Installation:
python -m venv env 
env/scripts/activate
pip install Django
pip install djangorestframework
pip install djangorestframework-simplejwt (to use jwt tokens)
pip install pillow (python library to handle images, resizing, saving them to the server)
django-admin startproject arcrewood_backend 
pip install django-cors-headers
python manage.py startapp account
create models 