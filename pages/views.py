from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Detail


# Create your views here.

def home(request):
    home_comm = Detail.objects.values('home_comm_paragraph').distinct()
    home_care = Detail.objects.values('home_care_paragraph').distinct()
    home_ontime = Detail.objects.values('home_ontime_paragraph').distinct()
    home_vision = Detail.objects.values('vision_paragraph').distinct()

    data = {
        'home_comm': home_comm,
        'home_care': home_care,
        'home_ontime': home_ontime,
        'home_vision': home_vision,
    }

    return render(request, 'pages/home.html', data)

def about(request):
    parag_one = Detail.objects.values('about_first_paragraph').distinct()
    parag_two = Detail.objects.values('about_second_paragraph').distinct()

    data = {
        'parag_one': parag_one,
        'parag_two': parag_two,
    }

    return render(request, 'pages/about.html', data)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = f'Newborn Inquiry: {subject}'
        message_body = f"""
                            Name: {name}\n
                            Email: {email}\n
                            Phone: {phone}\n
                            Message: {message}
                        """
        send_mail(
            email_subject,
            message_body,
            'newbornlyingin@gmail.com',
            ['newbornlyingin@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')
                


    return render(request, 'pages/contact.html')    
