from django.urls import path
from .views import author, blog

urlpatterns = [
    path('', author),
    path('<int:author_id>/blogs/', blog)
]
