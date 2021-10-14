from django.db import models


class Enquiry(models.Model):
    name      =models.CharField(max_length=150)
    email     =models.CharField(max_length=150)
    phone     =models.CharField(max_length=150)
    enquiry   =models.CharField(max_length=150)

    def __str__(self):
        return self.name