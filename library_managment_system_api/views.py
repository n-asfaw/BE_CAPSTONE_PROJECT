from rest_framework import generics
from .models import Book, Member, Loan
from .serializers import BookSerializer, MemberSerializer, LoanSerializer
from rest_framework.permissions import IsAuthenticated


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class LoanList(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer



class BookList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Repeat for other views you want to protect
