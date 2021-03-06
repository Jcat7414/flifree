from rest_framework import serializers
from .models import CustomUser
from django.utils import timezone


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    image = serializers.URLField(max_length=200)
    bio = serializers.CharField(max_length=1000)
    phone = serializers.CharField(max_length=13)
    location = serializers.CharField(max_length=100)
    newsletter_signup = serializers.BooleanField(default=True, write_only=True)
    terms_privacy = serializers.BooleanField(default=True, write_only=True)
    founder = serializers.BooleanField(default=False, write_only=True)
    supporter = serializers.BooleanField(default=False, write_only=True)
    is_staff = serializers.BooleanField(default=False, write_only=True)
    created_on = serializers.DateTimeField(default=timezone.now, write_only=True)

    def create(self,validated_data):
        return CustomUser.objects.create_user(**validated_data)


class CustomUserDetailSerializer(CustomUserSerializer):

    def update(self, instance, validated_data):
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.image = validated_data.get('image', instance.image)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance

class AdminUserDetailSerializer(CustomUserSerializer):

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.image = validated_data.get('image', instance.image)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.location = validated_data.get('location', instance.location)
        instance.founder = validated_data.get('founder', instance.founder)
        instance.supporter = validated_data.get('supporter', instance.supporter)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.save()
        return instance

class NewsletterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']