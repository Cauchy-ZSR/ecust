from rest_framework import serializers
from .models import pub_notice, notice_receive
from user.models import user
from user.serializers import userSerializer


class noticeSerializer(serializers.ModelSerializer):
    sender = userSerializer()
    class Meta:
        model = pub_notice
        fields = "__all__"

class pub_noticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = pub_notice
        fields = "__all__"

class noticeListSerializer(serializers.ModelSerializer):
    receiver = userSerializer()
    notice = noticeSerializer()
    class Meta:
        model = notice_receive
        fields = "__all__"
        