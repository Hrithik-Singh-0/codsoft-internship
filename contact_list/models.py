from django.db import models

class Contacts(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name