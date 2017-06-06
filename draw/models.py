from django.db import models

class Design(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    code = models.TextField()

    def __str__(self):
        return self.title

