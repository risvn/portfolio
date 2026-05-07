=== some cmds you should know before starting the project ====
install django
django-admin startproject <project-name>
cd project-name
run: python manage.py runserver
python manage.py startapp <app-name>



make sure you seperate each feature as a application and keep one main app for handling the domain url
which can be easily changed

==== view.py(blog) ====

browser->request->function->return

def home(request):
  return(<html>)

==== urls.py ====
  map the urls to corresponds to function

  urlpatterns=[
    path('',views.home,name=''),
  ]

=== how to add database in django ===

python manage.py makemigrations
python manage.py migrate


== adding superuser ===
python manage.py createsuperuser


=== creating data base tables ===

each classs is different table and each attribute is different field in the db

class Post(modesl.Model):
  title=models.CharField(max_length=100)
  content=models.TextField()
  date_posted=modes.DateTimeField(auto_now_add=True)

make migration and migrate


=== how to acces this objects or data from the db =====

User.objects.all() -> return qurey set to acess ind .first or .filter(username)
.id or .pk to get the id we can also use this id to filter as well

adding data to database for example:

post_1 = Post(tilte,content,author)

//in model section
def __str__(self):
  return self.title

post_1.save()


to acess models on admin site

admin.py-> admin.site.register(model)

====== using form and validating users ========

we can use forms from django or use json to get the data render html or return html
with csrf tokken



portfolio/
│
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
│
├── config/                     # Main Django project config
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── apps/
│   ├── users/
│   │   ├── migrations/
│   │   ├── templates/users/
│   │   ├── static/users/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   └── tests.py
│   │
│   ├── blog/
│   │   ├── migrations/
│   │   ├── templates/blog/
│   │   ├── static/blog/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   ├── projects/
│   │   ├── migrations/
│   │   ├── templates/projects/
│   │   ├── static/projects/
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
│   │
│   ├── posts/
│   └── contact/
│
├── templates/                  # Global templates
│   ├── base.html
│   ├── navbar.html
│   └── footer.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/                      # User uploads
│
├── utils/                      # Shared helper functions
│
└── docs/



















