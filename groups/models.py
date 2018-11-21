from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField()
    members = models.ManyToManyField(User,through='GroupMember')
    
    def __str__(self):
        return self.name
        
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)
        
    def get_absolute_url(self):
        return reverse('groups:detail',kwargs={'slug':self.slug}) 
    
    class Meta:
        ordering=['name']

class GroupMember(models.Model):
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
        
    class Meta:
        unique_together = ('group','user')