from django.urls import path, include

from blog.views import ShowParseView, ParseView


urlpatterns = [
    path('parser/', ParseView.as_view(), name='parser'),
    path('show/', ShowParseView.as_view(), name='show'),
]