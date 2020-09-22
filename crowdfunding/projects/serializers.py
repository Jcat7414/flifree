from rest_framework import serializers
from .models import Project, Pledge, Update

class UpdateSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    update_content = serializers.CharField(label='project update')
    update_date = serializers.DateTimeField(label='updated on')
    project_id = serializers.IntegerField()
    owner = serializers.ReadOnlyField(source='owner.id')

    def create(self, validated_data):
        return Update.objects.create(**validated_data)

class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    pledge_quantity = serializers.IntegerField(label='amount pledged', default=1)
    pledge_description = serializers.CharField(label='description of pledge', max_length=200)
    anonymous = serializers.BooleanField(label='remain anonymous', default=False)
    terms_privacy = serializers.BooleanField(label='accept Terms and Privacy', default=True)
    owner = serializers.ReadOnlyField(source='owner.id')
    is_fulfilled = serializers.BooleanField(label='pledge fulfilled', default=False)
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

# CAT_CHOICES=(
#     ('Facilities', 'Facilities'),
#     ('Resources', 'Resources'),
#     ('Exposure', 'Exposure'),
#     ('Expertise', 'Expertise')
# )


class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    project_name = serializers.CharField(label='project')
    project_intro = serializers.CharField(label='introduction', default="'A brief intro to the Project goes here.")
    project_goal = serializers.IntegerField(label="project_goal", default=12)
    # category = serializers.MultipleChoiceField(
    category = serializers.ChoiceField(
        choices=('Facilities', 'Resources', 'Exposure', 'Expertise'),
        # choices=CAT_CHOICES,
        default='Expertise',
        label='needs'
    )
    project_stage = serializers.ChoiceField(
        choices=('Start', 'Trial', 'Adjust', 'Retail'),
        default='Start',
        label='stage'
    )
    project_story = serializers.CharField(label='story', default="The project owners background story goes here.")
    project_faq = serializers.CharField(label='FAQ', default="A list of FAQ goes here.")
    project_image = serializers.URLField(label='project image', default="https://via.placeholder.com/300.jpg")
    is_open = serializers.BooleanField(label='project status', default=True)
    date_created = serializers.DateTimeField(label='project commenced')
    date_amended = serializers.DateTimeField(label='project last amended')
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
        instance.date_amended = validated_data.get('date amended', instance.date_amended)
        instance.save()
        return instance
        

class PledgeDetailSerializer(PledgeSerializer):

    def update(self, instance, validated_data):
        instance.pledge_quantity = validated_data.get('pledge_quantity', instance.pledge_quantity)
        instance.pledge_description = validated_data.get('pledge_description', instance.pledge_description)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.terms_privacy = validated_data.get('terms_privacy', instance.terms_privacy)
        instance.is_fulfilled = validated_data.get('is_fulfilled', instance.is_fulfilled)
        instance.project_id = validated_data.get('project_id', instance.project_id)
        instance.save()
        return instance

class UpdateDetailSerializer(UpdateSerializer):
    
    def update(self, instance, validated_data):
        instance.update_content = validated_data.get('update_content', instance.update_content)
        instance.update_date = validated_data.get('update_date', instance.update_date)
        instance.project_id = validated_data.get('project_id', instance.project_id)
        instance.save()
        return instance

# class ProjectPledgeSerializer(PledgeSerializer):

#     def read(self, validated_data):
#             return Pledge.objects.all(**validated_data)
         