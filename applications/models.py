from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOICES = [
    ("Applied", "Applied"),
    ("Interview", "Interview"),
    ("Offered", "Offered"),
    ("Rejected", "Rejected"),
]

class Application(models.Model):
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    applied_date = models.DateField()
    source = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,default="Applied")
    notes = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.company_name} - {self.role}"