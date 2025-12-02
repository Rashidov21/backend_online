from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250,blank=False)
    about_text = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
# 1 ga 1 ulash OneToOneField
# 1 ga ko'p ulash > ForeignKey
# ko'pga ko'p ulash > ManyToManyField 

class Post(models.Model):
    title = models.CharField(max_length=250,blank=False)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="posts")
    author = models.CharField(max_length=250,blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=250,blank=False)
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.name