from rest_framework import viewsets
from . import serializer, models
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token

class PatientViewset(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializer.PatientSerializers

class UserRegistrationApiView(APIView):
    serializer_class = serializer.RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            
            try:
                # Generate token and UID
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                
                # Create confirmation link
                confirm_link = f'http://127.0.0.1:8000/patient/active/{uid}/{token}'
                
                # Email configuration
                email_subject = 'Please Confirm Your Email'
                email_body = render_to_string('confirm-email.html', {'confirm_link': confirm_link})
                
                # Send email
                email = EmailMultiAlternatives(email_subject, '', to=[user.email])
                email.attach_alternative(email_body, 'text/html')
                email.send()
                
                return Response('Check Your mail for Information')
            
            except Exception as e:
                # Handle email sending errors
                return Response(f'Error sending email: {str(e)}', status=500)
        else:
            return Response(serializer.errors, status=400)
        
def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)

    except(User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active=True
        user.save()
        return redirect('register')
    
    else:
        return redirect('register')

# class UserLoginApiView(APIView):
#     def post(self, request):
#         serializerS = serializer.UserLoginSerializer(data=request.data)

#         if serializerS.is_valid():
#             username = serializerS.validated_data['username']
#             password = serializerS.validated_data['password']

#             user = authenticate(request, username=username, password=password)
            
#             if user:
#                 token, _ = Token.objects.get_or_create(user=user)
#                 login(request, user)
#                 return Response({'token': token.key, 'user_id': user.id})
#             else:
#                 return Response({'error': 'Invalid Credentials'})
            
#         return Response(serializer.errors)

# class UserLogoutView(APIView):
#     def get(self, request):
#         request.user.auth_token.delete()
#         logout(request)
#         return redirect('login')


class UserLoginApiView(APIView):
    def post(self, request):
        serializerForm = serializer.UserLoginSerializer(data = self.request.data)
        if serializerForm.is_valid():
            username = serializerForm.validated_data['username']
            password = serializerForm.validated_data['password']

            user = authenticate(username= username, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request, user)
                return Response({'token' : token.key, 'user_id' : user.id})
            else:
                return Response({'error' : "Invalid Credential"})
        return Response(serializer.errors)

class UserLogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')