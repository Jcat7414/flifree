from rest_framework import serializers
# from .models import Project, Pledge, Update
from . import models

class UpdateSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    update_content = serializers.CharField(max_length=5000)
    update_date = serializers.DateTimeField()
    project_id = serializers.IntegerField()
    owner = serializers.ReadOnlyField(source='owner.id')

    def create(self, validated_data):
        return Update.objects.create(**validated_data)

class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    pledge_quantity = serializers.IntegerField()
    pledge_description = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    terms_privacy = serializers.BooleanField()
    owner = serializers.ReadOnlyField(source='owner.id')
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
    owner = serializers.ReadOnlyField(source='owner.id')

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    updates = UpdateSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.project_name = validated_data.get('project_name', instance.project_name)
        instance.project_intro = validated_data.get('project_intro', instance.project_intro)
        instance.project_goal = validated_data.get('project_goal', instance.project_goal)
        instance.category = validated_data.get('category', instance.category)
        instance.project_stage = validated_data.get('project_stage', instance.project_stage)
        instance.project_story = validated_data.get('project_story', instance.project_story)
        instance.project_faq = validated_data.get('project_faq', instance.project_faq)
        instance.project_image = validated_data.get('project_image', instance.project_image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

class PledgeDetailSerializer(PledgeSerializer):

    def update(self, instance, validated_data):
        instance.pledge_quantity = validated_data.get('pledge_quantity', instance.pledge_quantity)
        instance.pledge_description = validated_data.get('pledge_description', instance.pledge_description)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.terms_privacy = validated_data.get('terms_privacy', instance.terms_privacy)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.is_fulfilled = validated_data.get('is_fulfilled', instance.is_fulfilled)
        instance.project_id = validated_data.get('project_id', instance.project_id)
        instance.save()
        return instance

class UpdateDetailSerializer(UpdateSerializer):
    
    def update(self, instance, validated_data):
        instance.update_content = validated_data.get('update_content', instance.update_content)
        instance.update_date = validated_data.get('update_date', instance.update_date)
        instance.project_id = validated_data.get('project_id', instance.project_id)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
