from django.urls import path
from .views import publication_list, publication_details


urlpatterns = [
    path('', publication_list, name='publication-list'),
    path('<int:pk>/', publication_details, name='publication-details')
]
