from django.db import models

# Create your models here.

class Booking(models.Model):
    title = models.CharField(max_length=20)
    members = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}번: {self.title}'
    