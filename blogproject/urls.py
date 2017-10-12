from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse

from blog.feeds import AllPostsRssFeed

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'', include('comments.urls')),
    url(r'^robots\.txt$', lambda r: HttpResponse('User-agent: *\nDisallow: /', content_type='text/plain')),
    url(r'^search/', include('haystack.urls')),
    url(r'^all/rss/$', AllPostsRssFeed(), name='rss'),
]
