from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    categories = (
        ('sports', 'Sports'),
        ('travelling', 'Travelling'),
        ('youtube', 'YouTube'),
        ('other', 'Other')
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=15, choices=categories)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    emailContact = models.EmailField()
    image = models.ImageField(upload_to="images/")

    class Meta:
        ordering = ['user', 'date']

    def __str__(self):
        return f"{self.name}"