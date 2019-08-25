from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


# Create your models here.

class Account(User):
    identificator = models.CharField(max_length=16)
    patronymic = models.CharField("Отчество", max_length=64)
    passport = models.CharField("Номер паспорта", max_length=64)

    class Meta:
        ordering = ('identificator',)


class Project(models.Model):
    author = models.ForeignKey(Account, related_name='author', on_delete=models.CASCADE)
    investors = models.ManyToManyField(Account, related_name='investors')
    name = models.CharField("Название", max_length=32, unique=True)
    theme = models.CharField("Тема", max_length=8)
    short_description = models.TextField()
    number_of_investors = models.IntegerField(default=0)

    class Meta:
        ordering = ('theme', '-number_of_investors')


class ProjectFile(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to='%s' % project.name)


@receiver(m2m_changed, sender=Project.investors.through)
def investors_changed(sender, instance, **kwargs):
    instance.number_of_investors = len([i for i in instance.investors.all()])
