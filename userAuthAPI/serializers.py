from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate

# User Data Serializer
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email')


# Register serializer
class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name','password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'])
        user.first_name = validated_data['first_name']        
        user.last_name = validated_data['last_name']        
        return user

# Login Serializer
class loginSerilaizer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
            
        raise serializers.ValidationError("Incorrect Credentials")

# User Profile Serializer
class userProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'