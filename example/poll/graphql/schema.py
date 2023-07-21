from djgraphql.schema import schema
from djgraphql.utils.routes import DefaultRouter, MethodType
from poll.graphql.resolvers import QuestionQueryResolver, QuestionMutationResolver

router = DefaultRouter()

router.register(
    QuestionQueryResolver,
    MethodType.QUERY
)

router.register(
    QuestionMutationResolver,
    MethodType.MUTATION
)

schema.register(router)
