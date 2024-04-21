from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    special_code = models.TextField(max_length = 10, default = '000000')

    def __str__(self):
        return str(self.name)

class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Link(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to='images/')
    link_type = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    collections = models.ManyToManyField(Collection, through="CollectionLink")

    def __str__(self):
        return str(self.title)

class CollectionLink(models.Model):
    description = models.ForeignKey(Collection, on_delete=models.CASCADE)
    date_created = models.ForeignKey(Link, on_delete=models.CASCADE)