from django.db import models

class AddressModel(models.Model):
    uid = models.AutoField(primary_key=True)
    address = models.CharField(max_length=300)
    