# Create a virtualenv
```
mkvirtualenv youtube_countdown_stream
```

You can find your python3 path with:

```
which python3
```

# Add postactivate and predeactivate files to the virtualenv
```
vim ~/.virtualenvs/youtube_countdown_stream/bin/postactivate
vim ~/.virtualenvs/youtube_countdown_stream/bin/predeactivate
```

You can find an example of this files in the docs folder on the root of the repo.
Remember to fill it with your on configuration.

# On /dfiid/project/ folder
```
deactivate
workon youtube_countdown_stream
pip install -r requirements.txt
python manage.py makemigrations user content
python manage.py migrate
python manage.py syncdb
python manage.py runserver
```
