import rollbar
from django.http import HttpResponse


# test Rollbar
def trigger_error(request):
    try:
        a = None
        a.hello()
    except:  # noqa: E722
        rollbar.report_exc_info()
        return HttpResponse("Error triggered!")