from django.db import models


class Program(models.Model):
    title = models.CharField(max_length=100)
    organs = models.ManyToManyField('Organ')
    text = models.TextField()
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title


class Organ(models.Model):
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)


    def __str__(self):
        return self.name
