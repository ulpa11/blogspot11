from django.db import models
from froala_editor.fields import FroalaField
# Create your models here.
class BlogDetail(models.Model):
    title = models.CharField(max_length=200)
    content=FroalaField()
    image=models.ImageField(upload_to="blog")
    into=models.TextField(null=True,blank=True)
    slug = models.SlugField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        self.slug=self.title
        super(BlogDetail,self).save(*args,**kwargs)