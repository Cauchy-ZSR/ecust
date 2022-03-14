from symtable import Class
from attr import field
from rest_framework import serializers
from .models import forum, topic, comment, membership
from user.serializers import userDetailSerializer


class forumListSerializer(serializers.ModelSerializer):
    creater = userDetailSerializer()
    class Meta:
        model = forum
        fields = "__all__"

class forumCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = forum
        fields = "__all__"

class topicSerializer(serializers.ModelSerializer):

    class Meta:
        model = topic
        fields = "__all__"

class topicListSerializer(serializers.ModelSerializer):

    creater = userDetailSerializer()
    class Meta:
        model = topic
        fields = "__all__"

class commentSerializer(serializers.ModelSerializer):

    class Meta:
        model = comment
        fields = "__all__"

class commentListSerializer(serializers.ModelSerializer):
    puber = userDetailSerializer()
    class Meta:
        model = comment
        fields = "__all__"

class membershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = membership
        fields = "__all__"

