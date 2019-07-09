from booksale.views import  api_root
from booksale import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url
schema_view = get_swagger_view(title='Pastebin API')


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'category', views.CategoryViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', api_root),
    path('', include(router.urls)),

]
urlpatterns += [
    url(r'schema/', schema_view)
]
