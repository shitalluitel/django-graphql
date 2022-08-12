from django.conf import settings
from django.http.response import JsonResponse
from graphene_django.views import GraphQLView, HttpError


class CustomGraphQLView(GraphQLView):
    def _has_permission(self):
        if not settings.DEBUG:
            raise HttpError(
                JsonResponse({}),
                'This endpoint is only accessible when DEBUG is True.',
            )

    def dispatch(self, request, *args, **kwargs):
        try:
            self._has_permission()
            return super().dispatch(request, *args, **kwargs)
        except HttpError as e:
            response = e.response
            response["Content-Type"] = "application/json"
            response.content = self.json_encode(
                request, {"errors": [self.format_error(e)]}
            )
            return response
