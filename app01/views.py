from django.shortcuts import render, HttpResponse


# Create your views here.
def notice(request):
    return render(request, 'notice.html')
