from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import Team, News


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('id', 'team_name', 'email', 'password',)
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        if self.context['request'].user.is_authenticated and \
            self.context['request'].user.email == validated_data['email']:
            validated_data['password'] = make_password(validated_data['password'])
            return super().update(instance, validated_data)
        raise serializers.ValidationError('権限がありません。')


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('from_team', 'contents', 'send_date', 'news_status',)

    def create(self, validated_data):
        if self.context['request'].user.is_authenticated:
            return super().create(validated_data)
        raise serializers.ValidationError('権限がありません。')