from django.db import models

class Registro(models.Model):
    conteudo = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.data_hora.strftime('%d/%m/%Y %H:%M')} - {self.conteudo[:30]}"