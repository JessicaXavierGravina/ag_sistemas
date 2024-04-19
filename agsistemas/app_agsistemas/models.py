from django.db import models

class Veiculo(models.Model):
    placa = models.CharField(max_length=20)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    km_troca_oleo = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        self.placa = self.placa.upper()
        self.marca = self.marca.upper()
        self.modelo = self.modelo.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.placa

class Motorista(models.Model):
    cod_motorista = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    cnh = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

class Controle(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    data_saida = models.DateField()
    hora_saida = models.TimeField()
    km_saida = models.PositiveIntegerField()
    destino = models.CharField(max_length=200)
    data_retorno = models.DateField(null=True, blank=True)
    hora_retorno = models.TimeField(null=True, blank=True)
    km_retorno = models.PositiveIntegerField(null=True, blank=True)
    km_percorrido = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.destino = self.destino.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Controle de {self.veiculo} - {self.data_saida}"