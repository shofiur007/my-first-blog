from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField( default=timezone.now)
    publshied_date = models.DateTimeField( blank=True, null=True)



    def publish(self):
        self.publshied_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title
