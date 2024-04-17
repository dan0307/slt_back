from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.db import models
from django.db import models

from django.contrib.auth.models import User

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    book_id = models.IntegerField(unique=False)
    title = models.CharField(max_length=255)
    content = models.TextField()
    user_id = models.IntegerField(unique=False)

    def __str__(self):
        return self.title
    class Meta:
        unique_together = ('user_id', 'book_id')
    
class BookProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)  # Progress percentage (0-100)

    def __str__(self):
        return f"{self.user.username}'s progress on {self.book.title}"
