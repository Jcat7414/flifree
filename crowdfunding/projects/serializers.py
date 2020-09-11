from rest_framework import serializers
from .models import Project, Pledge, Update

class UpdateSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    update_content = serializers.CharField(max_length=5000)
    update_date = serializers.DateTimeField()
    project_id = serializers.IntegerField()
    update_author = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return Update.objects.create(**validated_data)

class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    pledge_quantity = serializers.IntegerField()
    pledge_description = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    terms_privacy = serializers.BooleanField()
    supporter = serializers.CharField(max_length=100)
    is_fulfilled = serializers.BooleanField()
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    project_name = serializers.CharField(max_length=100)
    project_intro = serializers.CharField(max_length=500)
    project_goal = serializers.IntegerField()
    category = serializers.CharField(max_length=20)
    project_stage = serializers.CharField(max_length=10)
    project_story = serializers.CharField(max_length=5000)
    project_faq = serializers.CharField(max_length=5000)
    project_image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    # owner = serializers.CharField(max_length=100)
    owner = serializers.ReadOnlyField(source='owner.id')

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    updates = UpdateSerializer(many=True, read_only=True)
