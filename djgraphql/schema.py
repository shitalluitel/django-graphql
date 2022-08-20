import graphene
from graphene_django.debug import DjangoDebug

from .settings import api_settings
from .utils import get_resolver_class


class SchemaGenerator(object):
    def Query(self) -> type:  # noqa
        """
        Collects all query related resolvers and create query class used
        during schema creation.
        """
        return type(
            'Query',
            (
                *self.get_classes(),
                graphene.ObjectType
            ),
            {
                'debug': graphene.Field(DjangoDebug, name='_debug')
            }
        )

    def Mutation(self) -> type:  # noqa
        """
        Collects all mutation related resolvers and create query class used
        during schema creation.
        """
        return type(
            'Mutation',
            (
                *self.get_classes(_type='Mutation'),
                graphene.ObjectType
            ),
            {
                'debug': graphene.Field(DjangoDebug, name='_debug')
            }
        )

    def generate(self):
        return graphene.Schema(
            query=self.Query(),
            mutation=self.Mutation()
        )

    @staticmethod
    def get_graphql_apps() -> list:
        return api_settings.GRAPHQL_APPS or []

    @staticmethod
    def import_resolver(schema_path, from_list):
        return __import__(schema_path, fromlist=[from_list])

    def get_classes(self, _type: str = 'Query') -> object:
        graphql_apps = self.get_graphql_apps()
        resolver = f'{_type.upper()}_RESOLVERS'
        for app in graphql_apps:
            schema_path = f"{app}.graphql.schema"
            mod = self.import_resolver(schema_path, resolver)
            if hasattr(mod, resolver):
                resolvers = getattr(mod, resolver)
                if resolvers:
                    yield get_resolver_class(resolvers)

