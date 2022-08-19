import graphene


def get_resolver_class(resolvers: list, _type='Query') -> type:
    return type(
        _type,
        (
            *resolvers,
            graphene.ObjectType
        ),
        {}
    )
