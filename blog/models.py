from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db.models import Sum
from bs4 import BeautifulSoup

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    thumbnail = models.ImageField(upload_to='category_thumbnails/', null=True, blank=True)
    order = models.IntegerField(default=0)  # برای ترتیب دسته‌بندی‌ها

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField() 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def content_length(self):
        # حذف تگ‌های HTML از محتوا
        clean_content = BeautifulSoup(self.content, "html.parser").get_text()
        return len(clean_content)
    
    def __str__(self):
        return self.title


class Advertisement(models.Model):
    page_name = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='banners/')
    link = models.URLField()
    expiration_date = models.DateField(null=True, blank=True)  # تاریخ انقضا

    def __str__(self):
        return self.page_name

    

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    
    @property
    def total_characters(self):
        # جمع کل کاراکترهای محتوای پست‌ها
        return Post.objects.filter(author=self.user).aggregate(total=Sum(models.functions.Length('content')))['total'] or 0


