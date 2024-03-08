from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cs415.models import User, Expenses, Savings
from cs415.serializers import UserSerializer, ExpensesSerializer, SavingsSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from cs415.settings import JWT_AUTH
from cs415.authentication import JWTAuthentication

# class LoginAPIView(APIView):
#     def post(self, request):
        
#         email = request.data.get('email')
#         password = request.data.get('password')
#         user = authenticate(username=email, password=password)  # Assuming the username is the email
#         if user is not None:
#             jwt_token = JWTAuthentication.create_jwt(user)
#             return Response({'token': jwt_token}, status=status.HTTP_200_OK)
#             # token, _ = Token.objects.get_or_create(user=user)
#             # return Response({'token': token.key}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({'success': False,
                             'error': 'Email and Password must have a value'},
                             status = status.HTTP_400_BAD_REQUEST)

        check_user = User.objects.filter(email=email).exists()
        if check_user == False:
            return Response({'success': False,
                             'error': 'User with this email does not exist'},
                             status=status.HTTP_404_NOT_FOUND)

        check_pass = User.objects.filter(email = email, password=password).exists()
        if check_pass == False:
            return Response({'success': False,
                             'error': 'Incorrect password for user'},
                             status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.get(email = email, password=password)

        # add last login to User table
        # serializer = UserSerializer(user, data={'last_login': str(datetime.datetime.now())}, partial=True)
        # if serializer.is_valid():
        #     serializer.save()

        if user is not None:
            jwt_token = JWTAuthentication.create_jwt(user)
            data = {
                'token': jwt_token
            }
            return Response({'success': True,
                             'user_id': user.username_id,
                             'token': jwt_token},
                             status=status.HTTP_200_OK)
        else:
            return Response({'success': False,
                             'error': 'Invalid Login Credentials'},
                             status=status.HTTP_400_BAD_REQUEST)

class RegisterAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        username = request.data.get("username")  # Assuming you want to collect this

        if not email or not password or not username:
            return Response({'error': 'Email, username, and password are required'},
                             status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email is already in use'},
                             status=status.HTTP_409_CONFLICT)

        user = User(email=email, password=password, username=username)
        user.save()

        return Response({'success': 'User registered successfully'}, status=status.HTTP_201_CREATED)        
        
class UserAPIView(APIView):
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
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