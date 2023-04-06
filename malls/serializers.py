from rest_framework import serializers

from malls.models import Mall


class MallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mall
        fields = "__all__"
