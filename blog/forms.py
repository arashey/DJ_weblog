from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())  # استفاده از CKEditor برای ویرایشگر

    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'thumbnail']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),  # برای فیلد انتخابی دسته‌بندی
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),  # استایل برای بارگذاری تصویر
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError('عنوان پست ضروری است.')
        return title
    
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

