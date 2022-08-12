from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from graphql import schema
from graphql.views import CustomGraphQLView

urlpatterns = [
    path('', csrf_exempt(CustomGraphQLView.as_view(graphql=True, schema=schema))),
]