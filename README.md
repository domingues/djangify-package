# djangify-package

Transform any Python package into a Django Project and Application.

This approach allows you to use Django's ORM, migrations, and commands without the need
for the typical Django project boilerplate.

## Usage

1. Copy the `django_manage.py` file to your package folder.
2. Run `python -m my_package.django_manage` to access the full list of available Django
    commands.

### Using the ORM

To use Django's ORM, define your models in the `my_package/models.py` file. Be sure to
import the `django_manage` module before importing your models to properly initialize the
environment.

```python
from . import django_manage  # noqa: F401, I001

from .models import MyModel

print(MyModel.objects.count())
```

### Managing Migrations

Once you've defined or updated your models, you can use Django's migration system to
handle database schema changes.

1. Create new migrations for your models:
    ```
    mkdir my_package/migrations
    python -m my_package.django_manage makemigrations
    ```
2. Apply the generated migrations to update your database schema:
    ```
    python -m my_package.django_manage migrate
    ```
3. Inspect the migration history or view pending migrations with:
    ```
    python -m my_package.django_manage showmigrations
    ```

### Adding URL Routing and Views

1. Add `ROOT_URLCONF`, `SECRET_KEY` and `ALLOWED_HOSTS` to the settings:
    ```python
    conf.settings.configure(
        ...,
        ROOT_URLCONF="django_manage",
        SECRET_KEY=...,
        ALLOWED_HOSTS=...,
    )
    django.setup()
    ...
    ```
2. Add `urlpatterns` to the `django_manage` module:
    ```python
    ... django.setup()
    urlpatterns = [
        path("", lambda request: HttpResponse("Hello!")),
    ]

    def main():
    ...
    ```
3. Test the server:
    ```
    python -m my_package.django_manage runserver
    ```
