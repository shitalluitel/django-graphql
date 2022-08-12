from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.template import loader
from graphene_django.views import GraphQLView, HttpError


@login_required
def dashboard_render(request):
    if not settings.USE_DEPLOY:
        template = loader.get_template('application.html')
    else:
        template = loader.get_template('deploy.html')
    context = {}
    return HttpResponse(template.render(context, request))


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("app")


class DevCustomGraphQLView(GraphQLView):
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
