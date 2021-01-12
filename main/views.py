from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index (request):
    return render(request, 'main/index.html')

def church(request):
    return render(request, 'examples/church.html')

def restaraunt(request):
    return render(request, 'examples/restaraunt.html')

def product(request):
    return render(request, 'examples/product.html')

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['contactName']
        message_choice = request.POST['contactChoice']
        message_email = request.POST['contactEmail']
        message = request.POST['contactMessage']
        message_date = request.POST['contactDate']
        message_time = request.POST['contactTime']

        context = {
            'name' : message_name,
            'choice' : message_choice,
            'email' : message_email,
            'message' : message,
            'date' : message_date,
            'time' : message_time,
        }

    else:
        context = {}

    
    return render(request, 'main/contact.html', context)