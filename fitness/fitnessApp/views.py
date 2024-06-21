from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'HTML/home.html')

def userData(request):
    return render(request, 'HTML/userData.html')