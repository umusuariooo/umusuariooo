from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuario.urls')),
    path('cliente/', include('cliente.urls')),
    path('estoque/', include('estoque.urls')),
    path('myfitness/', include('myfitness.urls'))
]