from django.shortcuts import get_object_or_404, render
from rest_framework import  viewsets, status
from .serializers import userDetailSerializer, userSerializer
from rest_framework.response import Response
from .models import user


# Create your views here.

class userDetailViewSetList(viewsets.ViewSet):

    def list(self,request):
        queryset = user.objects.all()
        serializer = userDetailSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk):
        try:
            selectUser = user.objects.get(userNo=pk)
        except user.DoesNotExist:
            return Response({
                'msg': 'NO!',
                'code': 404
            })
        serializer = userDetailSerializer(selectUser)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

class userViewSetList(viewsets.ViewSet):

    def retrieve(self, request, pk):
        password=request.data['password']
        try:
            user = user.objects.get(userNo=pk)
        except user.DoesNotExist:
            return Response({
                'msg':"账号或密码有误！", 
                'code': 404
                })
        if password==user.password:
            serializer=userDetailSerializer(user)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response({
               'msg':"账号或密码有误！", 
                'code': 404 
            })


    def create(self, request):
        serializer = userSerializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'msg': 'Successfully Created!',
            'code': 200
        })
    
    def update(self, request, pk):
        try:
            oldUser = user.objects.get(userNo=pk)
        except user.DoesNotExist:
            return Response({
                'msg': 'No Such User!',
                'code': 404
            })
        print(request.data)
        new_update = userSerializer(instance=oldUser,data=request.data,partial=False)
        new_update.is_valid(raise_exception=True)
        new_update.save()
        return Response({
            'msg': 'Update successfully!',
            'code': 200
        })
    