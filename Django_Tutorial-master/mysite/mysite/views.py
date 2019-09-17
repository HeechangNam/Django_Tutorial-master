from django.http import HttpResponse, HttpResponseRedirect


def home_view(request):
    return HttpResponse("<h1>Hellow!</h1>")
