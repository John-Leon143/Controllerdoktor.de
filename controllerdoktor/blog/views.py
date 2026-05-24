from django.shortcuts import render, get_object_or_404
from .models import BlogPost

import markdown




def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    content_html = markdown.markdown(post.content)  # Markdown in HTML umwandeln
    return render(request, 'blog/blog_detail.html', {'post': post, 'content_html': content_html})