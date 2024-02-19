from django.shortcuts import render , redirect
from .models import Consulta
from django.contrib import messages
from .forms import ConsultaForm

def index(request):
    consultas = Consulta.objects.all()
    context = {
        'consultas': consultas, 
    }
    return render (request, 'cad_consultas/index.html', context)

def cadrastro(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consulta agendada com sucesso!')
            form = ConsultaForm()
        else:
            messages.error(request, 'Erro ao cadastrar na agenda!')
    else:
        form = ConsultaForm
    return render (request, 'cad_consultas/cadastro.html', {'form': form})


def deletar(request, id):
    deleteme = Consulta.objects.get(id = id)
    if request.method == 'POST':
        deleteme.delete()
        return redirect('/')
    return render(request,'cad_consultas/deletar.html')
