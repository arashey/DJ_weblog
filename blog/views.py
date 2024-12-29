from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post, Category, Advertisement
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import ProfileEditForm


@login_required
def create_post(request):
    if not request.user.groups.filter(name='نویسندگان').exists():
        return redirect('home')

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('post_list')

    return render(request, 'create_post.html', {'form': form})




def base_context(request):
    categories = Category.objects.all()
    return {'categories': categories}


def category_posts(request, id):
    category = get_object_or_404(Category, id=id)
    posts = category.posts.all()
    return render(request, 'category_posts.html', {'category': category, 'posts': posts})




def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    advertisement = Advertisement.objects.filter(page_name='post_list').first()
    paginator = Paginator(posts, 10)  # 10 پست در هر صفحه
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'post_list.html', {'page_obj': page_obj, 'advertisement': advertisement})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    advertisement = Advertisement.objects.filter(page_name='post_detail').first()
    return render(request, 'post_detail.html', {'post': post, 'advertisement': advertisement})




def about(request):
    about_text = getattr(settings, 'ABOUT_TEXT', 'اطلاعاتی در مورد وبلاگ وارد نشده است.')
    return render(request, 'about.html', {'about_text': about_text})

@login_required
def profile(request):
    user = request.user
    posts = Post.objects.filter(author=user)  # پست‌های کاربر

    # فرم ارسال پست جدید
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # ایجاد پست جدید و انتساب به نویسنده
            new_post = form.save(commit=False)
            new_post.author = user  # انتساب پست به کاربر جاری
            new_post.save()
            return redirect('profile')  # بعد از ذخیره پست، به صفحه پروفایل بروید
    else:
        form = PostForm()

    return render(request, 'profile.html', {'user': user, 'posts': posts, 'form': form})

@login_required
def delete_post(request, post_id):
    # دریافت پست بر اساس شناسه و چک کردن مالکیت آن
    post = get_object_or_404(Post, id=post_id, author=request.user)
    
    if request.method == 'POST':
        # حذف پست
        post.delete()
        return redirect('profile')  # بعد از حذف، به پروفایل بازگردید
    
    return render(request, 'confirm_delete.html', {'post': post})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=request.user)
    
    return render(request, 'edit_profile.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_list')  # یا مسیر دلخواه
        else:
            messages.error(request, 'نام کاربری یا رمز عبور نامعتبر است')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'رمزهای عبور مطابقت ندارند')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'نام کاربری از قبل وجود دارد')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'ایمیل قبلاً ثبت شده است')
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            login(request, user)
            return redirect('login')  
    return render(request, 'register.html')









