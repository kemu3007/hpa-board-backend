from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import Application, Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = (
            'id', 
            'created',
            'updated',
            'name', 
            'admin_team', 
            'start_datetime', 
            'end_datetime', 
            'application_start_datetime',
            'application_end_datetime',
            'place',
            'meeting_place',
            'details',
        )
        read_only_fields = (
            'id',
            'created',
            'updated',
        )
    
    def update(self, instance, validated_data):
        if self.context['request'].user.is_authenticated and \
            (self.context['request'].user == instance.admin_team or self.context['request'].team.is_superuser):
            return super().update(instance, validated_data)
        raise serializers.ValidationError('権限がありません。')


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ('id', 'team', 'people_num', 'remarks',)
        read_only_fields = ('id', 'team')

    def create(self, validated_data):
        if self.context['request'].user.is_authenticated:
            return super().create(validated_data)
        raise serializers.ValidationError('権限がありません。')
    
    def update(self, instance, validated_data):
        if self.context['request'].user.is_authenticated and self.context['request'].team == instance.team:
            return super().update(instance, validated_data)
        raise serializers.ValidationError('権限がありません。')