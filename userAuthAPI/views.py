from rest_framework.views import APIView
from rest_framework import permissions,status,generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import MultiPartParser, FormParser

from knox.models import AuthToken
from .models import *
from .serializers import *

#  User Profile API
class UserProfileAPI(APIView):
    serializer_class = userProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,format=None):

        # Filtering user profile
        userProfile = Profile.objects.filter(userLinked=self.request.user).values()
        
        context = {
            "username":self.request.user.username,
            "first_name":self.request.user.first_name,
            "last_name":self.request.user.last_name,
            "email":self.request.user.email,
            "profile": {
                "mobile_number":userProfile[0]['mobile_number'],
                "userPhoto":userProfile[0]['userPhoto'],
            }    
        }
        return Response(context,status=status.HTTP_200_OK)

#  registration api
class RegisterAPI(generics.GenericAPIView):
    serializer_class =  registerSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self,request, *args, **kwargs):

        # Getting data from user form
        registerData = {
            "username":request.data["username"],
            "email":request.data["email"],
            "first_name":request.data["first_name"],
            "last_name":request.data["last_name"],
            "password":request.data["password"],
            "password2":request.data["password2"]
        }

        # passing data to serializer
        serializer = self.get_serializer(data=registerData)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.first_name = request.data["first_name"]
        user.last_name = request.data["last_name"]
        user.save()
        
        profileData = {
            "userLinked":user.pk,
            "mobile_number":request.data["mobile_number"],
            "userPhoto":request.data["userPhoto"],
        }
        print("Pofile  ",profileData)

        userProfile = userProfileSerializer(data=profileData)
        try:
            if userProfile.is_valid():
                hotelData = userProfile.save()
                return Response({
                    "user": userSerializer(user, context=self.get_serializer_context()).data,
                    "userProfile": userProfile.data,
                    "token": AuthToken.objects.create(user)[1]
                })
            else:
                user.delete()
                raise ValidationError(userProfile.errors)
        except Exception as e:
            print(e)
            user.delete()
            return Response({'error_message':'Cool down'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        

        

#login api
class LoginAPI(generics.GenericAPIView):
    serializer_class = loginSerilaizer

    def post(self,request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        return Response({
            "user": userSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
            })