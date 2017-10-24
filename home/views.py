from django.shortcuts import render

# Create your views here.
def index(request):
    x = 5
    x = 'hello'
    return render(
        request,
        'index.html',
        context={}
    )
