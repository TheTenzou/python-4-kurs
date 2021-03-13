from django.shortcuts import render
from django.http import HttpResponse
from .models import Computer
from django.shortcuts import get_object_or_404

# Create your views here.

def pc_home(request):
    querySet = Computer.objects.all()
    context = {
        'queryset': querySet
    }
    print(querySet)
    for i in querySet:
        print(i)
        print(type(i))
        print('=========')
        print(i.name)
        print(i.cpu)
        print(type(i.cpu))
        print(type(i.gpu))
    return render(request, 'index.html', context)   


def pc_details(request, id):
    instance = get_object_or_404(Computer, id=id)
    context = {
        'title': 'Detail',
        'instance': instance
    }
    return render(request, 'pc_details.html', context)