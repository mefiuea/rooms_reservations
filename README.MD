# Rooms reservation app
####This is a demo application. The application was created to improve skills in web application development. It was created in Python language using Django framework.
The application allows to create rooms with names. Give them a size and decide if a projector is available in the room.
The website also gives access to a list of all created rooms from where they can be edited, deleted and booked for a given day.

### Running project locally

First, clone the repository to your local machine:

```
git clone git@github.com:mefiuea/rooms_reservations.git
or
https://github.com/mefiuea/rooms_reservations.git
```

Install the requirements:

```
pip install -r requirements.txt

```

Set all environment variables. 
Go to the env folder, then create an .env file and copy the contents of the .env-default file into it. 
Once this is done, fill the .env file with the appropriate data. 
In the terminal, load the environment variables from this file with the command:

```
source env/.env
```

Change DEBUG mode in settings.py:

```
DEBUG = True
```

Apply the migrations:

```
python manage.py migrate
```

Finally, run the development server:

```
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.