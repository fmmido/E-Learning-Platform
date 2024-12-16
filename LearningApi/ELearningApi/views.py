from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class RegisterView(APIView):
    def post(self, request):
        # Get the data from the request
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')
        email = request.data.get('email')

        # Validate the required fields
        if not first_name or not last_name or not password or not email:
            return Response({'error': 'All fields are required: first_name, last_name, password, email'}, 
                            status=status.HTTP_400_BAD_REQUEST)

        # Check if the email is already used
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already in use'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the user
        user = User.objects.create_user(
            username=email,  # Use email as username
            password=password, 
            email=email, 
            first_name=first_name, 
            last_name=last_name
        )

        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Check if email and password are provided
        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Try to get user by email
        try:
            user = User.objects.get(email=email)  # Get the user by email
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate the user
        user = authenticate(username=user.username, password=password)

        if user is not None:
            # If authentication is successful, generate or fetch the token
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            # If authentication fails, return an error response
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
