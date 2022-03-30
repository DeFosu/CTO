from django.conf import settings
from django.db import models
from django.utils import timezone


class Service(models.Model):
    description =  models.CharField(max_length=200)
    cost = models.IntegerField()

    def __str__(self):
        return self.description + ' - ' + (str(self.cost)) + ' UAH'

class Customer(models.Model):
    first_name =  models.CharField(max_length=200)
    last_name =  models.CharField(max_length=200)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.phone

class Order(models.Model):
    mark = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    number = models.CharField(max_length=20)
    data_start = models.DateField(blank=True)
    data_end = models.DateField(blank=True, null=True)
    id_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    id_service = models.ManyToManyField(Service)

    def __str__(self):
        return str(self.id_customer) + ' -- ' + self.number

class News(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
