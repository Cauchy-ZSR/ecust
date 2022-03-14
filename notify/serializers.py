from django.dispatch import receiver
from rest_framework import serializers

from user.serializers import userClassSerializer
from .models import pub_notice, notice_receive
from user.models import user


class noticeSerializer(serializers.ModelSerializer):
    sender = userClassSerializer()
    class Meta:
        model = pub_notice
        fields = "__all__"

class pub_noticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = pub_notice
        fields = "__all__"

class noticeListSerializer(serializers.ModelSerializer):
    receiver = userClassSerializer()
    notice = noticeSerializer()
    class Meta:
        model = notice_receive
        fields = "__all__"
        