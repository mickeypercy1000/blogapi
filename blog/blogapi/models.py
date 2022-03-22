from django.db import models


# Create your models here.
#class BlogCategories(models.Model):
 
class Categories(models.Model):
  blog_categories = models.CharField(max_length=100)
  category_summary = models.TextField(max_length=100, null=True)
  category_img = models.ImageField(max_length=500, null = True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.blog_categories
        

class Post(models.Model):
    blog_state= [
      ('Draft', 'draft'),
      ('Published', 'published')
    ]
  
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    status = models.CharField(choices = blog_state, default = 'Published', max_length=20)
    category = models.ForeignKey(Categories, on_delete = models.SET_NULL, null = True, blank = True)
    post_img = models.ImageField(null=True)


    #author = 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']