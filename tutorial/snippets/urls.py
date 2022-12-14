from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views
#USANDO IL ROUTER LO FA LUI IN AUTOMATICO
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet,basename="snippet")
router.register(r'users', views.UserViewSet,basename="user")
router.register(r'prova', views.ProvaViewSet,basename="prova")
router.register(r'home', views.HomeViewSet,basename="home")
router.register(r'album', views.AlbumViewSet,basename="album")
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('accounts/', include('rest_registration.api.urls')),
    path('', include(router.urls)),

]