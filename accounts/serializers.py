from rest_framework import serializers

from accounts.models import Database


class DataBaseSeializer(serializers.ModelSerializer):
    class Meta:
        model = Database
        fields = "__all__"