#URLS propias de la app (modulo) luego se conectan con las urls de la app general (microblog)

from django.urls import path
from . import views

urlpatterns = [
#primer valor es la ruta /
# segundo parámetro es la función dentro de view.py que tiene que ser llamanda en esa ruta

    path('user/<int:id>',views.profile),
    path('user/seguidos/<int:id>',views.seguidos),
    path('user/seguidores/<int:id>',views.seguidores)
]
