from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Computer, Cpu, Gpu
from .forms import ComputerForm

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


def pc_create(request):
    form = ComputerForm()

    if request.method =='POST':
        name = request.POST.get('name')
        cpu_id = request.POST.get('cpu')
        gpu_id = request.POST.get('gpu')

        cpu = get_object_or_404(Cpu, id=cpu_id)
        gpu = get_object_or_404(Gpu, id=gpu_id)

        Computer.objects.create(name=name,cpu=cpu, gpu=gpu)
    context = {
        'form':form,
    }
    return render(request, 'pc_create.html', context)