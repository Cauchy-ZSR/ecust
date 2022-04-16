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
        fields = ('name', 'intro', 'tag', 'creater')

class topicSerializer(serializers.ModelSerializer):

    class Meta:
        model = topic
        fields = ('creater', 'pubForum', 'title', 'content', 'tag')

class topicListSerializer(serializers.ModelSerializer):

    creater = userDetailSerializer()
    class Meta:
        model = topic
        fields = "__all__"

class commentSerializer(serializers.ModelSerializer):
    topicComment = topicSerializer()
    class Meta:
        model = comment
        fields = ('puber', 'topicComment', 'content')

class commentListSerializer(serializers.ModelSerializer):
    puber = userDetailSerializer()
    class Meta:
        model = comment
        fields = "__all__"

class membershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = membership
        fields = ('m_forum', 'm_user')

class commentCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = comment
        fields = ('puber', 'topicComment', 'content')
        