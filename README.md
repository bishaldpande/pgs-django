# Step 0(optional):
- Create a repo for the code in github; including the python .gitignore and README.md files
- Clone the repo using ssh and move to the folder

# Step 1:
- Create virtual env
`python -m venv venv`
- Activate the virtual env

```bash
>>> source venv/bin/activate  # Mac/ Linux
>>> venv\Scripts\activate     # Windows
```

# Step 3:

```
>>> pip install django
>>> django-admin startproject <projectet_name> .
```
> the django admin command will create a folder by default since we have already created the folder for the project in setp 0/1 we can create the django project in the same place so using `.`. If you are fine with having a new folder created ignore the `.`.

Step 4 Getting Started:

```bash
>>> python manage.py migrate      # create the data base
>>> python manage.py createsuperuser
>>> python manage.py runserver
```

Check the links: 
- [http://localhost:8000/](http://localhost:8000/)
- [http://localhost:8000/admin/](http://localhost:8000/admin/)
