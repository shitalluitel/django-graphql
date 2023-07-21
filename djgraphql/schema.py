from collections import defaultdict

import graphene

from djgraphql.utils.routes import DefaultRouter

# from graphene_django.debug import DjangoDebug

__all__ = [
    'schema',
]


class SchemaParameters:
    # debug = graphene.Field(DjangoDebug, name='_debug')

    def __new__(cls, name, *args, **kwargs):
        klass = type(
            name,
            (
                *args,
                graphene.ObjectType
            ),
            {
                # 'debug': cls.debug
            }
        )
        return klass


class SchemaMeta(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]


class Schema(metaclass=SchemaMeta):
    _resolvers = defaultdict(list)

    def register(self, resolver: DefaultRouter):
        self._resolvers['query'].append(*resolver.query)
        self._resolvers['mutation'].append(*resolver.mutation)

    def generate(self):
        Query = SchemaParameters('Query', *self._resolvers['query'])  # noqa
        Mutation = SchemaParameters('Mutation', *self._resolvers['mutation'])  # noqa
        return graphene.Schema(
            query=Query,
            mutation=Mutation
        )


schema = Schema()
