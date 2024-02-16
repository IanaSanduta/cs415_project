from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cs415.models import User, Expenses, Savings
from cs415.serializers import UserSerializer, ExpensesSerializer, SavingsSerializer

  
class UserAPIView(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})

class ExpensesAPIView(APIView):
    def get(self,request):
        expenses = Expenses.objects.all()
        serializer = ExpensesSerializer(expenses, many=True)
        return Response({'expenses': serializer.data})

class SavingsAPIView(APIView):
    def get(self,request):
        savings = Savings.objects.all()
        serializer = SavingsSerializer(savings, many=True)
        return Response({'savings': serializer.data})






    # def post(self, request, *args, **kwargs):
    #     if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'data': serializer.data})
    #     else:
    #         return Response({'errors': serializer.errors},
    #                             status=status.HTTP_400_BAD_REQUEST)
    # def get(self,request):
    #     if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
    #     users = User.objects.all()
    #     serializer = UserSerializer(users, many=True)
    #     return Response({'users': serializer.data})