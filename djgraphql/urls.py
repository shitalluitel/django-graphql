from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from djgraphql.schema import SchemaGenerator

schema = SchemaGenerator()

urlpatterns = [
    path('', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema.generate()))),
]
