import graphene
from django.conf import settings
from graphene_django.debug import DjangoDebug


def generate_class(_type='Query'):
    for app in settings.SYSTEM_APPS:
        schema_path = f"{app}.graphql.schema"
        try:
            mod = __import__(schema_path, fromlist=[_type])
            if hasattr(mod, _type):
                klass = getattr(mod, _type)
                if klass:
                    yield klass
        except ModuleNotFoundError:
            ...
        except ImportError:
            ...


# Dynamic class creation using 'type' method
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
