from rest_framework import serializers
from .models import User,ActivityPeriod

class activitySerializers(serializers.ModelSerializer):

    start_time_formatted = serializers.SerializerMethodField()
    finish_time_formatted = serializers.SerializerMethodField() 
    
    def get_start_time_formatted(self,obj):
        return obj.start_time.strftime('%B %d %Y, %I:%M%p')

    def get_finish_time_formatted(self,obj):
        return obj.finish_time.strftime('%B %d %Y, %I:%M%p')

    class Meta:
        model = ActivityPeriod
        fields = ['start_time_formatted','finish_time_formatted']

class userSerializers(serializers.ModelSerializer):

    activity = serializers.SerializerMethodField()

    def get_activity(self,obj):
        activity=ActivityPeriod.objects.filter(related_to=obj)
        return activitySerializers(activity,many=True).data

    class Meta:
        model = User
        fields = '__all__'

