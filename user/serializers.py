from rest_framework import serializers
from  .models import user, userClass


class userClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = userClass
        fields = "__all__"

class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = user
        fields = "__all__"

class userDetailSerializer(serializers.ModelSerializer):
    userClass = userClassSerializer()
    class Meta:
        # 需要序列化的模型
        model = user
        # 需要序列化的字段，“_all_”表示所有字段
        fields = "__all__"
