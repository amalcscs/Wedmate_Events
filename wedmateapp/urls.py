
from django.contrib import admin
from django.urls import re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from wedmateapp import views


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$',views.base, name='base'),
    re_path(r'^wedmate_quotationpdf$',views.wedmate_quotationpdf, name='wedmate_quotationpdf'),
    re_path(r'^wedmate_quotationadd$',views.wedmate_quotationadd, name='wedmate_quotationadd'),
    # re_path(r'^books/(?P<id>\d+)/$',views.books, name='books'),  
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
