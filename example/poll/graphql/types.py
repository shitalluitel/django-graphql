from graphene_django import DjangoObjectType

from poll.models import Question


class QuestionNode(DjangoObjectType):
    class Meta:
        model = Question
        fields = '__all__'
