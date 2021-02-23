from django.db import models
from django.utils import timezone

#clase post para las entradas del blog
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    #metodo publish para publicar la entrada
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title