from rest_framework import serializers
from woman.models import Woman


class WomanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Woman
        fields = ('title', 'content', 'time_create', 'time_update', 'is_published', 'cat')
        read_only_fields = ('time_create', 'time_update', 'is_published')
