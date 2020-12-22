from django.shortcuts import render
from .models import Service

# Create your views here.
def service(request):
    featured_service = Service.objects.order_by('-created_date').filter(is_featured=True)[0:3]

    data = {
        'featured_service': featured_service,
    }
    return render(request, 'service/service.html', data)