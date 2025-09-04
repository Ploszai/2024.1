from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView
from .models import Colaborador
from .forms import ColaboradorForm
class ColaboradorListView(ListView):
    model = Colaborador; template_name='colaboradores_app/colaborador_list.html'; context_object_name='colaboradores'
class ColaboradorCreateView(View):
    def get(self, request):
        form = ColaboradorForm(); return render(request,'colaboradores_app/colaborador_form.html',{'form':form})
    def post(self, request):
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save(); return redirect('colaborador_list')
        return render(request,'colaboradores_app/colaborador_form.html',{'form':form})
class ColaboradorUpdateView(View):
    def get(self, request, pk):
        colaborador = get_object_or_404(Colaborador, pk=pk)
        form = ColaboradorForm(instance=colaborador)
        return render(request,'colaboradores_app/colaborador_form.html',{'form':form,'colaborador':colaborador})
    def post(self, request, pk):
        colaborador = get_object_or_404(Colaborador, pk=pk)
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save(); return redirect('colaborador_list')
        return render(request,'colaboradores_app/colaborador_form.html',{'form':form,'colaborador':colaborador})
class ColaboradorDeleteView(View):
    def get(self, request, pk):
        colaborador = get_object_or_404(Colaborador, pk=pk)
        return render(request,'colaboradores_app/colaborador_confirm_delete.html',{'colaborador':colaborador})
    def post(self, request, pk):
        colaborador = get_object_or_404(Colaborador, pk=pk)
        colaborador.delete(); return redirect('colaborador_list')
