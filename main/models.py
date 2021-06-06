from django.db import models


class AstroRegister(models.Model):
    name = models.CharField('Ваше имя', max_length=50)
    mail = models.CharField('Ваша почта', max_length=50)

    def __str__(self):
        return str({'name': self.name, 'mail': self.mail})