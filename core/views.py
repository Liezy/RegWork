from django.shortcuts import render, redirect, get_object_or_404
from .models import Registro

def home(request):
    if request.method == 'POST':
        conteudo = request.POST.get('conteudo')
        if conteudo:
            Registro.objects.create(conteudo=conteudo)
            return redirect('home')
        
    registros = Registro.objects.all().order_by('-data_hora')
    editar_id = request.GET.get('editar')
    return render(request, 'core/home.html', {
        'registros': registros,
        'editar_id': int(editar_id) if editar_id else None,
    })

def editar(request, id):
    registro = get_object_or_404(Registro, id=id)
    
    if request.method == 'POST':
        conteudo = request.POST.get('conteudo')
        if conteudo:
            registro.conteudo = conteudo
            registro.save()
        return redirect('home')
    
    # Redireciona com o ID a ser editado via query param
    return redirect(f"/?editar={id}")

def excluir(request, id):
    registro = get_object_or_404(Registro, id=id)
    registro.delete()
    return redirect('home')