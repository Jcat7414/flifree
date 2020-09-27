from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics, filters
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserDetailSerializer, NewsletterSerializer
from .permissions import IsOwnerOrReadOnly, IsAdminUser

class CreateUserList(APIView):

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CustomUserList(APIView):

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)


class CustomUserDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
            self.check_object_permissions(self.request, user)
            return user
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        data = request.data
        serializer = CustomUserDetailSerializer(
            instance=user,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class AdminUserDetail(APIView):
    permission_classes = [
        permissions.IsAdminUser
    ]

    def get_object(self, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
            self.check_object_permissions(self.request, user)
            return user
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, pk):
        user = self.get_object(pk)
        data = request.data
        serializer = AdminUserDetailSerializer(
            instance=user,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class FoundersList(generics.ListAPIView):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        founders = CustomUser.objects.filter(founder=True)
        return founders

class SupportersList(generics.ListAPIView):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        supporters = CustomUser.objects.filter(supporter=True)
        return supporters

class StaffList(generics.ListAPIView):
    permission_classes = [
        permissions.IsAdminUser
    ]

    serializer_class = CustomUserSerializer

    def get_queryset(self):
        staff = CustomUser.objects.filter(is_staff=True)
        return staff

class NewsletterList(generics.ListAPIView):
    permission_classes = [
        permissions.IsAdminUser
    ]

    serializer_class = NewsletterSerializer

    def get_queryset(self):
        newsletter = CustomUser.objects.filter(newsletter_signup=True)
        return newsletter