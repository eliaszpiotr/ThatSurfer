from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from surferhub import views

# Adding urls to the views
urlpatterns = [

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)