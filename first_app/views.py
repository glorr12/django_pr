from django.http import HttpResponse


def first_view(request):
    return HttpResponse("Hello, Igor")