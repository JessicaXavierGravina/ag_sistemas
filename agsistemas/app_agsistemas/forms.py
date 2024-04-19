from django import forms
from .models import Veiculo, Motorista, Controle
import re

class VeiculoForm(forms.ModelForm):

    class Meta:
        model = Veiculo
        fields = ['placa', 'marca', 'modelo', 'km_troca_oleo']
        labels = {
            'placa': 'Placa do Veículo',
            'marca': 'Marca do Veículo',
            'modelo': 'Modelo do Veículo',
            'km_troca_oleo': 'KM para Próxima Troca de Óleo',
        }
        widgets = {
            'km_troca_oleo': forms.NumberInput(attrs={'min': 0}),
        }

    def clean(self):
        cleaned_data = super().clean()
        placa = cleaned_data.get('placa')
        telefone = cleaned_data.get('telefone')

        pattern = re.compile(r'^([A-Z]{3}-\d{4}|[A-Z]{3}\d{1}[A-Z]\d{2})$')
        if not pattern.match(placa):
            raise forms.ValidationError("A placa do veículo não está em um formato válido.")
        if Veiculo.objects.filter(placa=placa).exists():
            raise forms.ValidationError("Veiculo com a placa ja adicionada anteriormente.")

        return cleaned_data


class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = ['nome', 'telefone', 'cnh']
        labels = {
            'nome': 'Nome do Motorista',
            'telefone': 'Telefone do Motorista',
            'cnh': 'CNH do Motorista',
        }
        widgets = {
            'telefone': forms.TextInput(attrs={'placeholder': 'Ex: (99) 99999-9999'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        cnh = cleaned_data.get('cnh')
        telefone = cleaned_data.get('telefone')

        if len(cnh) != 9 or not cnh.isdigit():
            raise forms.ValidationError("A CNH deve ter exatamente 9 caracteres numéricos.")
        if len(telefone) != 11 or not telefone.isdigit():
            raise forms.ValidationError("O número de telefone deve ter exatamente 11 caracteres numéricos.")

        if Motorista.objects.filter(cnh=cnh).exists():
            raise forms.ValidationError("Já existe um motorista cadastrado com este CNH.")
        if Motorista.objects.filter(telefone=telefone).exists():
            raise forms.ValidationError("Telefone já cadastrado.")

        return cleaned_data


class ControleForm(forms.ModelForm):
    class Meta:
        model = Controle
        fields = ['veiculo', 'motorista', 'data_saida', 'hora_saida', 'km_saida', 'destino', 'data_retorno', 'hora_retorno', 'km_retorno', 'km_percorrido']
        widgets = {
            'data_saida': forms.DateInput(attrs={'type': 'date'}),
            'hora_saida': forms.TimeInput(attrs={'type': 'time'}),
            'data_retorno': forms.DateInput(attrs={'type': 'date'}),
            'hora_retorno': forms.TimeInput(attrs={'type': 'time'}),
            'veiculo': forms.Select(),
            'motorista': forms.Select(),
        }
    def clean(self):
        cleaned_data = super().clean()
        data_saida = cleaned_data.get("data_saida")
        hora_saida = cleaned_data.get("hora_saida")
        data_retorno = cleaned_data.get("data_retorno")
        hora_retorno = cleaned_data.get("hora_retorno")
        km_saida = cleaned_data.get("km_saida")
        km_retorno = cleaned_data.get("km_retorno")

        if data_saida and data_retorno and data_retorno < data_saida:
            raise forms.ValidationError("A data de retorno não pode ser anterior à data de saída.")

        if data_saida == data_retorno and hora_saida and hora_retorno and hora_retorno < hora_saida:
            raise forms.ValidationError("A hora de retorno não pode ser anterior à hora de saída se ambas as datas forem iguais.")

        if km_saida is not None and km_retorno is not None:
            cleaned_data['km_percorrido'] = km_retorno - km_saida
        else:
            cleaned_data['km_percorrido'] = None

        return cleaned_data