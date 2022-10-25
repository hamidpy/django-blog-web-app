from django.shortcuts import render, redirect
from app.models import Post, Category, Tag


def BASE(request):
    return render(request, 'Main/base.html')


def INDEX(request):
    popular_post = Post.objects.filter(section='Popular', status=1).order_by('-id')[0:4]
    recent_post = Post.objects.filter(section='Recent', status=1).order_by('-id')[0:4]
    main_post = Post.objects.filter(Main_post=True, status=1)[0:1]
    Editor_pick = Post.objects.filter(section='Editors_Pick', status=1).order_by('-id')
    Trending = Post.objects.filter(section='Trending', status=1).order_by('-id')
    Inspiration = Post.objects.filter(section='Inspiration', status=1).order_by('-id')[0:2]
    Latest_Posts = Post.objects.filter(section='Latest Posts', status=1).order_by('-id')[0:4]

    category = Category.objects.all()
    tag = Tag.objects.all()

    context = {
        'popular_post': popular_post,
        'recent_post': recent_post,
        'main_post': main_post,
        'Editor_pick': Editor_pick,
        'Trending': Trending,
        'Inspiration': Inspiration,
        'Latest_Posts': Latest_Posts,
        'category': category,
        'tag': tag,
    }
    return render(request, 'Main/index.html', context)


def ABOUT(request):
    return render(request, 'Main/about.html')


def BLOGSINGLE(request):
    return render(request, 'Main/blog-single.html')


def BLOGSINGLEALT(request):
    return render(request, 'Main/blog-single-alt.html')


def CATEGORY(request):
    return render(request, 'Main/category.html')


def CLASSIC(request):
    return render(request, 'Main/classic.html')


def CONTACT(request):
    return render(request, 'Main/contact.html')


def MINIMAL(request):
    return render(request, 'Main/minimal.html')


def PERSONAL(request):
    return render(request, 'Main/personal.html')


def PERSONALALT(request):
    return render(request, 'Main/personal-alt.html')
