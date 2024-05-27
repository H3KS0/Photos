from django.db import models
from users.models import Users
class PhotoCategory(models.Model):
    category_id = models.IntegerField(auto_created=True, primary_key=True, serialize=False)
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name
class Pictures(models.Model):
    picture_id = models.IntegerField(auto_created=True, primary_key=True, serialize=False)
    user = models.ForeignKey(to=Users, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='main_images')
    name = models.CharField(max_length=128)
    date_download = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(to=PhotoCategory, on_delete=models.PROTECT)

class Post(models.Model):
    user = models.ForeignKey(to=Users, on_delete=models.PROTECT)
    picture = models.ForeignKey(to=Pictures, on_delete= models.PROTECT)
    description = models.TextField(null= True, blank= True)

class Like(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.PROTECT)
    user = models.ForeignKey(to=Users, on_delete=models.PROTECT)
