from django.urls import path, include

from djgraphql.urls import urlpatterns as graphql_urlpatterns

urlpatterns = [
    path('graphql', include(graphql_urlpatterns)),
]
