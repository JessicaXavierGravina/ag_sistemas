from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Veiculo, Motorista, Controle
from .forms import VeiculoForm, MotoristaForm, ControleForm

class PaginaInicialView(View):
    def get(self, request):
        veiculos_count = Veiculo.objects.count()
        motoristas_count = Motorista.objects.count()
        return render(request, 'pagina_inicial.html', {'veiculos_count': veiculos_count, 'motoristas_count': motoristas_count})



#Controle
class ControleListView(ListView):
    model = Controle
    template_name = 'controle_list.html'
    context_object_name = 'controles'
    ordering = ['-data_saida']


class ControleCreateView(CreateView):
    model = Controle
    form_class = ControleForm
    template_name = 'controle_form.html'
    success_url = reverse_lazy('controle_list')


class ControleUpdateView(UpdateView):
    model = Controle
    form_class = ControleForm
    template_name = 'controle_form.html'
    success_url = reverse_lazy('controle_list')


class ControleDeleteView(DeleteView):
    model = Controle
    template_name = 'controle_confirm_delete.html'
    success_url = reverse_lazy('controle_list')


class ControleDetailView(DetailView):
    model = Controle
    template_name = 'controle_detail.html'
    context_object_name = 'controle'



#veiculos
class VeiculosView(View):
    def get(self, request):
        veiculos = Veiculo.objects.all()
        return render(request, 'veiculos.html', {'veiculos': veiculos})


class CriarVeiculoView(View):
    def get(self, request):
        form = VeiculoForm()
        return render(request, 'criar_veiculo.html', {'form': form, 'mensagem_aviso': None})

    def post(self, request):
        form = VeiculoForm(request.POST)
        if form.is_valid():
            placa = form.cleaned_data['placa']
            if not Veiculo.objects.filter(placa=placa).exists():
                form.save()
                return redirect('pagina_inicial')
            else:
                mensagem_aviso = 'Placa já cadastrada.'
                return render(request, 'criar_veiculo.html', {'form': form, 'mensagem_aviso': mensagem_aviso})

        return render(request, 'criar_veiculo.html', {'form': form, 'mensagem_aviso': None})


class EditarVeiculoView(View):
    def get(self, request, veiculo_id):
        veiculo = Veiculo.objects.get(pk=veiculo_id)
        form = VeiculoForm(instance=veiculo)
        return render(request, 'editar_veiculo.html', {'form': form})

    def post(self, request, veiculo_id):
        veiculo = Veiculo.objects.get(pk=veiculo_id)
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            return redirect('veiculos')
        return render(request, 'editar_veiculo.html', {'form': form})


class ExcluirVeiculoView(View):
    def get(self, request, veiculo_id):
        veiculo = Veiculo.objects.get(pk=veiculo_id)
        return render(request, 'excluir_veiculo.html', {'veiculo': veiculo})

    def post(self, request, veiculo_id):
        veiculo = Veiculo.objects.get(pk=veiculo_id)
        veiculo.delete()
        return redirect('veiculos')


class VeiculoDetailView(DetailView):
    model = Veiculo
    template_name = 'veiculo_detail.html'
    context_object_name = 'veiculo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        veiculo = self.get_object()

        controles = Controle.objects.filter(veiculo=veiculo)

        motoristas_datas = []

        for controle in controles:
            motoristas_datas.append((controle.motorista.nome, controle.data_saida, controle.data_retorno))

        context['motoristas_datas'] = motoristas_datas

        return context



#motoristas
class MotoristasView(View):
    def get(self, request):
        motoristas = Motorista.objects.all()
        return render(request, 'motoristas.html', {'motoristas': motoristas})


class CriarMotoristaView(View):
    def get(self, request):
        form = MotoristaForm()
        return render(request, 'criar_motorista.html', {'form': form, 'mensagem_aviso': None})

    def post(self, request):
        form = MotoristaForm(request.POST)
        if form.is_valid():
            cnh = form.cleaned_data['cnh']
            telefone = form.cleaned_data['telefone']
            if not Motorista.objects.filter(cnh=cnh).exists() and not Motorista.objects.filter(telefone=telefone).exists():
                form.save()
                return redirect('pagina_inicial')
            elif Motorista.objects.filter(cnh=cnh).exists():
                mensagem_aviso = 'CNH já cadastrada.'
            else:
                mensagem_aviso = 'Telefone já cadastrado.'
            return render(request, 'criar_motorista.html', {'form': form, 'mensagem_aviso': mensagem_aviso})
        return render(request, 'criar_motorista.html', {'form': form, 'mensagem_aviso': None})


class ExcluirMotoristaView(View):
    def get(self, request, motorista_id):
        motorista = Motorista.objects.get(pk=motorista_id)
        return render(request, 'excluir_motorista.html', {'motorista': motorista})

    def post(self, request, motorista_id):
        motorista = Motorista.objects.get(pk=motorista_id)
        motorista.delete()
        return redirect('motoristas')


class EditarMotoristaView(View):
    def get(self, request, motorista_id):
        motorista = Motorista.objects.get(pk=motorista_id)
        form = MotoristaForm(instance=motorista)
        return render(request, 'editar_motorista.html', {'form': form, 'motorista': motorista})

    def post(self, request, motorista_id):
        motorista = Motorista.objects.get(pk=motorista_id)
        form = MotoristaForm(request.POST, instance=motorista)
        if form.is_valid():
            form.save()
            return redirect('motoristas')
        return render(request, 'editar_motorista.html', {'form': form, 'motorista': motorista})


class MotoristaDetailView(DetailView):
    model = Motorista
    template_name = 'motorista_detail.html'
    context_object_name = 'motorista'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        motorista = self.get_object()

        controles = Controle.objects.filter(motorista=motorista)

        if controles:
            context['controles'] = controles

        return context