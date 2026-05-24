from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "daily"  
    priority = 0.8

    def items(self):
        return [
            'home',
            'reperatur-anfragen',
            'dienstleitungen',
            'blog_list',
        ]

    def location(self, item):
        return reverse(item)


from blog.models import BlogPost  # Importiere dein BlogPost-Modell

class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return f'/blog/{obj.slug}/'