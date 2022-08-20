import graphene
from django.utils import timezone

from poll.graphql.types import QuestionNode
from poll.models import Question


class QuestionMutation(graphene.Mutation):
    class Arguments:
        question_text = graphene.String(required=True)

    question = graphene.Field(QuestionNode)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        question = Question(**kwargs, pub_date=timezone.now())
        question.save()
        return QuestionMutation(question=question)


class QuestionQueryResolver(object):
    all_question = graphene.List(QuestionNode)
    question_by_id = graphene.Field(QuestionNode, id=graphene.String())

    def resolve_all_question(self, info, **kwargs):
        return Question.objects.all()

    def resolve_question_by_id(self, info, id):
        return Question.objects.filter(id=id).first()


class QuestionMutationResolver(object):
    add_question = QuestionMutation.Field()
