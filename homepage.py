from django.http import HttpResponse
def home(request):
    return HttpResponse( '<h1>this is homepage</h1>')


def contact(request):
    return HttpResponse('<h1>contact us</h1> <br>this is mayank contact page')