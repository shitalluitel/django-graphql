# Django-graphql

Django Graphql is built on top of django and graphene-django framework. Django-Graphql provides easier implementation of
graphql within django projects.

First time? We recommend you start by learning
about [Graphene-Django](https://docs.graphene-python.org/projects/django/en/latest/)
and [Django Docs](https://docs.djangoproject.com/).

## Installation

```shell
pip install djgraphql
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

We will be assuming all our folder structure to be same as our example project. Within our example project we have an
app called `poll` if we want to add desired graphql within that application we need to follow these instructions.

1. Create a directory `graphql` within your application on same level as `app.py`.
2. Add `__init__.py` file within graphql directory.
3. Add three different files within graphql directory: `resolvers.py`, `schema.py`, and `types.py`
    1. `resolvers.py` will contain all the codes related to resolvers. Resolvers are nothing but implementation of query
       parameters out of query class which will be inherited within Query class later. Not just query, mutation has
       similar implementation.
    3. `schema.py` will help us to load all resolvers into schema.
   ```python
   ...
   QUERY_RESOLVERS = [...]
   
   MUTATION_RESOLVERS = [...]
   ```
    3. By the help of `DjangoObjectType` Graphene-Django automatically transfers a Django model into a `ObjectType` for
       us. So all these `ObjectType` class definition will be kept within `types.py`. Related filters and custom fields
       are also included within this file.
   