from django.db import models


class Customer(models.Model):
    ic_no = models.IntegerField(primary_key=True, verbose_name='No. Kad Pengenalan')
    name = models.CharField(max_length=100, verbose_name='Nama', blank=False)
    phone_no = models.IntegerField(verbose_name='No. Telefon', blank=False)
    address1 = models.CharField(max_length=100, verbose_name='Alamat 1')
    address2 = models.CharField(max_length=100, verbose_name='Alamat 2')
    city = models.CharField(max_length=20, verbose_name='Bandar')
    mukim = models.CharField(max_length=20, verbose_name='Mukim')
    parlimen = models.CharField(max_length=20, verbose_name='Parlimen')
    state = models.CharField(max_length=20, verbose_name='Negeri')
    poskod = models.IntegerField(verbose_name='Poskod')

