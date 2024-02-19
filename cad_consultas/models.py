from django.db import models

class Consulta(models.Model):
    PROCEDIMENTOS_CHOICES = (
        ('LP', 'Limpeza de Pele'),
        ('SB', 'Sombrancelhas'),
        ('CL', 'Cílios'),
        ('MF', 'Massagem Facial'),
        ('MC', 'Massagem Corporal'),
        ('DP', 'Depilaçaõ'),
        ('CC', 'Corte de cabelo'),
    )
    nome = models.CharField(max_length = 50)
    data = models.DateField()
    horario = models.TimeField()
    procedimento = models.CharField(max_length = 2, choices = PROCEDIMENTOS_CHOICES, default = 'SB')
    imagem = models.ImageField(upload_to='imagem do procedimento', null = True, blank = True)


    def __str__(self):
        return self.nome