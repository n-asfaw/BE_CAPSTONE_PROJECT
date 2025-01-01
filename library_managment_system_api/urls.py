from django.urls import path
from .views import BookList, BookDetail, MemberList, LoanList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('members/', MemberList.as_view(), name='member-list'),
    path('loans/', LoanList.as_view(), name='loan-list'),
]
