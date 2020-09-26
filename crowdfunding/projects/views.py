from django.http import Http404
from rest_framework import status, permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge, Update
from .serializers import ProjectSerializer, ProjectDetailSerializer, PledgeSerializer, PledgeDetailSerializer, UpdateSerializer, UpdateDetailSerializer, PledgeAmountSerializer
from .permissions import IsOwnerOrReadOnly, IsAdminUser
from rest_framework import generics, filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db.models import Count, Sum
from users.models import CustomUser

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

    permission_classes = [
        permissions.IsAdminUser
    ]

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

    permission_classes = [
        permissions.IsAdminUser
    ]

    def delete(self, request, pk):
        pledge = self.get_object(pk)
        pledge.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateList(APIView):
    
    def get(self, request):
        updates = Update.objects.all()
        serializer = UpdateSerializer(updates, many=True)
        return Response(serializer.data)

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def post(self, request):
        serializer = UpdateSerializer(data=request.data)
        owner = Project.objects.get(pk=request.data['project_id']).owner_id
        if serializer.is_valid() and request.user==CustomUser.objects.get(pk=owner):
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
        username = self.kwargs['project_owner']
        return Project.objects.filter(owner__username=username)

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



class PledgeAmountList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        amount = Pledge.objects.all()
        serializer = PledgeAmountSerializer(amount, many=True)
        return Response(serializer.data)

class ProjectPledgeAmount(ProjectDetail):
    
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
        # return Response(serializer.data)
        
        pledged_so_far = serializer.data 

        time_pledged = {}
        time_pledged['total_pledged'] = 0
        for time in range(len(pledged_so_far['pledges'])):
            time_pledged['total_pledged'] += pledged_so_far['pledges'][time]['pledge_quantity']
        return Response(time_pledged)

class FacilitiesProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        facilities = Project.objects.filter(needs_facilities=True)
        return facilities

class ResourcesProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        resources = Project.objects.filter(needs_resources=True)
        return resources

class ExposureProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        exposure = Project.objects.filter(needs_exposure=True)
        return exposure

class ExpertiseProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        expertise = Project.objects.filter(needs_expertise=True)
        return expertise

class StartProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        stage = Project.objects.filter(project_stage='Start')
        return stage

class TrialProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        stage = Project.objects.filter(project_stage='Trial')
        return stage

class AdjustProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        stage = Project.objects.filter(project_stage='Adjust')
        return stage

class RetailProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        stage = Project.objects.filter(project_stage='Retail')
        return stage