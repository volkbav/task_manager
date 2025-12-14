import rollbar
from django.http import HttpResponse
from django.views.decorators.http import require_GET


# test Rollbar
@require_GET
def trigger_error(request):
    try:
        a = None
        a.hello()
    except:  # noqa: E722
        rollbar.report_exc_info()
        return HttpResponse("Error triggered!")