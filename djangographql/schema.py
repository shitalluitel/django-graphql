import graphene
from graphene_django.debug import DjangoDebug

from .settings import api_settings


def generate_class(_type='Query'):
    graphql_apps = api_settings.GRAPHQL_APPS or []
    for app in graphql_apps:
        schema_path = f"{app}.graphql.schema"
        try:
            mod = __import__(schema_path, fromlist=[_type])
            if hasattr(mod, _type):
                klass = getattr(mod, _type)
                if klass:
                    yield klass
        except ModuleNotFoundError as e:
            ...
        except ImportError as e:
            ...


# Dynamic class creation using 'type' method
"""
Collects all query related resolvers and create query class used 
during schema creation.
"""
Query = type(
    'Query',
    (
        *generate_class(),
        graphene.ObjectType
    ),
    {
        'debug': graphene.Field(DjangoDebug, name='_debug')
    }
)


"""
Collects all mutation related resolvers and create query class used 
during schema creation.
"""
Mutation = type(
    'Mutation',
    (
        *generate_class(_type='Mutation'),
        graphene.ObjectType
    ),
    {
        'debug': graphene.Field(DjangoDebug, name='_debug')
    }
)


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)
