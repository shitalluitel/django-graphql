# Django-graphql

Django Graphql is built on top of django and graphene-django framework. Django-Graphql provides easier implementation of
graphql within django projects.

First time? We recommend you start by learning
about [Graphene-Django](https://docs.graphene-python.org/projects/django/en/latest/)
and [Django Docs](https://docs.djangoproject.com/).

## Installation

```shell
pip install django-graphql
```

We strongly recommend pinning against a specific version of Graphene-Django because new versions could introduce
breaking changes to your project.

Add `graphene_django` to the `INSTALLED_APPS` in the `settings.py` file of your Django project:

```python
INSTALLED_APPS = [
    ...,
    "django.contrib.staticfiles",
    "graphene_django",
]
```

We need to add a `graphql` URL to the `urls.py` of your Django project:

```python
from django.urls import path, include
from djangographql.urls import urlpatterns as graphql_urls

urlpatterns = [
    # ...
    path("", include(graphql_urls)),
]
```

## Settings

You need to list out all those apps which contains graphql within your project. For that you need to add name of each
app containing graphql as a list to `GRAPHQL_APPS` within `settings.py`.

```python
GRAPHQL_APPS = [
    ...,
    'foo',
]
```

Other settings are similar to graphene-django and django itself.

## Implementation
