from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Author(models.Model):
    name = models.CharField(max_length=50, default="mike")
    genre = models.ForeignKey(Category, related_name="author_genre", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at', )


class Post(models.Model):
    BLOG_STATUS = (
        ('draft', 'DRAFT'),
        ('published', 'PUBLISHED'),
    )

    title = models.CharField(max_length=100, default='mike2')
    body = models.TextField()
    category = models.ForeignKey(Category, related_name="blog_category", on_delete=models.CASCADE)
    author = models.ForeignKey(Author, related_name="blog_author", on_delete=models.CASCADE)
    # featured_image = models.ImageField()
    status = models.CharField(choices=BLOG_STATUS, max_length=20, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} -- {self.body} -- {self.category}"