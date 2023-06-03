from rest_framework import serializers


class ReceiveSErializer(serializers.Serializer):
    photo = serializers.ImageField()