from django.urls import path
from .views import post_list, post_detail, about, category_posts, create_post, register_view, login_view, logout_view, profile, edit_profile, delete_post
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', post_list, name='post_list'),  # صفحه اصلی
    path('post/<int:id>/', post_detail, name='post_detail'),  # جزئیات پست
    path('about/', about, name='about'),  # صفحه درباره ما
    path('category/<int:id>/', category_posts, name='category_posts'),  # پست‌های یک دسته‌بندی
    path('post/create/', create_post, name='create_post'), 
    path('profile/', profile, name='profile'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
    path('edit-profile/',edit_profile, name='edit_profile'),
    path('login/',login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]

if settings.DEBUG:  # فقط در حالت توسعه فایل‌های رسانه‌ای را سرو کنید
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



