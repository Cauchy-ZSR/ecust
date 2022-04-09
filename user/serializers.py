from rest_framework import serializers
from  .models import user

class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = user
        fields = ('userNo', 'nickname', 'email', 'identity')

class userDetailSerializer(serializers.ModelSerializer):
    class Meta:
        # 需要序列化的模型
        model = user
        # 需要序列化的字段，“_all_”表示所有字段
        fields = "__all__"
