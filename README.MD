# Rooms reservation app
####This is a demo application. The application was created to improve skills in web application development. It was created in Python language using Django framework.
The application allows to create rooms with names. Give them a size and decide if a projector is available in the room.
The website also gives access to a list of all created rooms from where they can be edited, deleted and booked for a given day.

### Running project locally

First, clone the repository to your local machine:

```
git clone git@github.com:mefiuea/ssa.git
or
https://github.com/mefiuea/ssa.git
```

Install the requirements:

```
pip install -r requirements.txt

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