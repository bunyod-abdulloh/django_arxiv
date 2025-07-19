from django.urls import path
from .views import contact_view, message_list_view

urlpatterns = [
    path('', contact_view, name='home'),
    path('xabarlar/', message_list_view, name='message_list'),
]
