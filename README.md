# Note taking app "ooh! Notes"

This Python ooh! Notes Project is a simple application for managing notes with ooh! Yes exclamations. 
It allows you to create, view, update, group and delete notes through a user-friendly interface.

## Features

- **Create Notes**: You can create new notes by providing a title, content, optional tags, and resources.
- **View Notes**: All notes are displayed in a list format, along with their associated tags.
- **Search Notes**: You can search for notes using keywords or tags, making it easy to find relevant information.
- **Group Management**: You can manage notes by creating groups.

## Check it out!

Check my project at render: [ooh!-notes](https://ooh-notes.onrender.com/)

## Installation instructions

I assume you already have Python3 installed.

In terminal write down following command:

```shell
git clone https://github.com/aLEKS-e3/ooh-notes.git
python -m venv venv
source venv/bin/activate  # for Windows use: venv\scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```

Also for testing you can load already prepared data:

```shell
python manage.py loaddata notes_db.json
```

## Have a nice experience!

![Home](home.png)
