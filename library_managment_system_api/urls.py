from django.urls import path
from .views import BookList, BookDetail, MemberList, LoanList
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshViw,

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('members/', MemberList.as_view(), name='member-list'),
    path('loans/', LoanList.as_view(), name='loan-list'),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
