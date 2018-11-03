
from django.contrib import admin
from django.urls import path, include
admin.site.site_header = 'BiblioSimple'


urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('libros/',  include('libros.urls')),
    path('prestamos/',  include('prestamos.urls')),

]