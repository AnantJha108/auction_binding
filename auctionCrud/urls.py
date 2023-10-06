from django.urls import path
from .views import AuctionList, AuctionDetail

urlpatterns = [
    path('', AuctionList.as_view(), name='allUser'),
    path('<int:pk>/', AuctionDetail.as_view(), name='getData'),
]