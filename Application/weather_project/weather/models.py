from django.db import models

class SearchHistory(models.Model):
    city = models.CharField(max_length=100)
    search_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city

    class Meta:
        ordering = ['-search_at']




# Create your models here.