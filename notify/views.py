from .serializers import noticeSerializer, pub_noticeSerializer, noticeListSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import pub_notice, notice_receive

# Create your views here.

class notifyPubViewSetList(viewsets.ViewSet):

    def retrieve(self, request, pk):
        try:
            publish = pub_notice.objects.filter(sender_id=pk)
        except len(publish)==0:
            return Response({
                'code': 201,
                'msg': 'Have not Published!'
            })
        serializer = noticeSerializer(publish, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def create(self, request):
        # 先在发布通知表中插入
        serializer1 = pub_noticeSerializer(data=request.data)
        serializer1.is_valid(raise_exception=True)
        serializer1.save()
        
        return Response({
            'msg': 'Successfully!',
            'code': 200
        })

class notifyViewSetList(viewsets.ViewSet):
    def retrieve(self,request,pk):
        try:
            queryset = notice_receive.objects.filter(receiver_userNo=pk)
        except len(queryset)==0:
            return Response({
                'msg':'No notice!',
                'code':201
            })
        serializer = noticeListSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
