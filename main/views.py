from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, 'main/index.html')

def church(request):
    return render(request, 'examples/church.html')

def restaraunt(request):
    return render(request, 'examples/restaraunt.html')

def product(request):
    return render(request, 'examples/product.html')