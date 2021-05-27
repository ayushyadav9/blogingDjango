from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from articles import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/',include('articles.urls')),
    path('accounts/',include('accounts.urls')),
    path('about',views.about),
    path('',article_views.article_list,name="home"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
