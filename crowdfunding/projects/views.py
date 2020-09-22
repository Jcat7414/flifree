from django.http import Http404
from rest_framework import status, permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge, Update
from .serializers import ProjectSerializer, ProjectDetailSerializer, PledgeSerializer, PledgeDetailSerializer, UpdateSerializer, UpdateDetailSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics, filters
from rest_framework.filters import SearchFilter, OrderingFilter

class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        filter_backends = [filters.SearchFilter]
        search_fields = ['project_name']
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance=project,
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
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class PledgeList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        pledge = Pledge.objects.all()
        serializer = PledgeSerializer(pledge, many=True)
        filter_backends = [filters.SearchFilter]
        search_fields = ['pledge_description']
        return Response(serializer.data)
   
    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class PledgeDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(pledge)
        return Response(serializer.data)

    def put(self, request, pk):
        pledge = self.get_object(pk)
        data = request.data
        serializer = PledgeDetailSerializer(
            instance=pledge,
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
        pledge = self.get_object(pk)
        pledge.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get(self, request):
        updates = Update.objects.all()
        serializer = UpdateSerializer(updates, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class UpdateDetail(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            update = Update.objects.get(pk=pk)
            self.check_object_permissions(self.request, update)
            return update
        except Update.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        update = self.get_object(pk)
        serializer = UpdateDetailSerializer(update)
        return Response(serializer.data)

    def put(self, request, pk):
        update = self.get_object(pk)
        data = request.data
        serializer = UpdateDetailSerializer(
            instance=update,
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
        update = self.get_object(pk)
        update.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class FounderProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        try:
            username = self.kwargs['project_owner']
            return Project.objects.filter(owner__username=username)
        except project_owner.DoesNotExist:
            raise Http404

class SupporterPledgeList(generics.ListAPIView):
    serializer_class = PledgeSerializer

    def get_queryset(self):
        username = self.kwargs['pledge_supporter']
        return Pledge.objects.filter(owner__username=username)

class FounderUpdateList(generics.ListAPIView):
    serializer_class = UpdateSerializer

    def get_queryset(self):
        username = self.kwargs['update_author']
        return Update.objects.filter(owner__username=username)



class ProjectPledgeList(generics.ListAPIView):
    serializer_class = PledgeSerializer

    def get_queryset(self):
        pledgesfor = self.kwargs['pledges']
        return Pledge.objects.filter(project__project_name=pledgesfor)

class ProjectUpdateList(generics.ListAPIView):
    serializer_class = UpdateSerializer

    def get_queryset(self):
        updatesfor = self.kwargs['updates']
        return Update.objects.filter(project__project_name=updatesfor)

class PledgeTotalList(generics.ListAPIView):
    serializer_class = PledgeSerializer

    def queryset(self):
        amount = self.kwargs['pledge_quantity']
        total = sum(amount)
        return total
        # if pledge_quantity in request.GET and request.get['pledge_quantity']:
        #     response.data['sum'] = Pledge.objects.filter(ref=int(request.GET['pledge_quantity'])
        #     ).aggregate(sum=SUM('pledge_quantity'))['sum']
        # return total
