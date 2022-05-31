from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views

urlpatterns=[
    re_path('^$',views.home,name = 'home'),
    re_path('^search/', views.search_results, name='search_results'),
    re_path('^locations/', views.navbar, name='navbar'),
    re_path('image/', views.image, name='image')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)