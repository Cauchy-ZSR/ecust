from django.shortcuts import render
from numpy import delete
from rest_framework import viewsets, status
from user import serializers
from .serializers import forumCreateSerializer, forumListSerializer, topicSerializer, topicListSerializer, commentSerializer, commentListSerializer, membershipSerializer
from rest_framework.response import Response
from .models import forum, topic, comment, membership
from django.db.models import Q
# Create your views here.
class forumViewSetList(viewsets.ViewSet):

    def create(self,request):
        serializer = forumCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'code': 200,
            'msg' : 'Successfully!'
        })

    def update(self,request, pk):

        try:
            old = forum.objects.get(id=pk)
        except forum.DoesNotExist:
            return Response({
                'code': 404,
                'msg': 'Failed!'
            })
        new = forumCreateSerializer(instance=old, data=request.data, partial=False)
        new.is_valid(raise_exception=True)
        new.save()
        return Response({
            'msg': 'Successfully',
            'code': 200
        })

class forumDetailViewSetList(viewsets.ViewSet):

    def list(self, request):
        queryset = forum.objects.all()
        serializer = forumListSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self,request,pk):
        try:
            select = forum.objects.get(id=pk)
        except forum.DoesNotExist:
            return Response({
                'code': 404,
                'msg': 'Not Found!'
            })
        serializer = forumListSerializer(select)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

class topicViewSetList(viewsets.ViewSet):

    def create(self,request):
        serializer = topicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'code': 200,
            'msg': 'Successfully'
        })

class topicDetailViewSet(viewsets.ViewSet):

    def list(self,request,pk):
        try:
            queryset = topic.objects.filter(pubForum=pk)
        except len(queryset)==0:
            return Response({
                'code': 201,
                'msg': 'No Topic Currently!'
            })
        serializer = topicListSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def retrieve(self, request, pk):
        try:
            queryset = topic.objects.get(id=pk)
        except topic.DoesNotExist:
            return Response({
                'code': 401,
                'msg': 'Unexpected error!'
            })
        serializer = topicListSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
class commentViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = commentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'code': 200,
            'msg': 'Created successfully!'
        })

    def delete(self,request,pk):
        try:
            queryset = comment.objects.get(id=pk)
        except comment.DoesNotExist:
            return Response({
                'code': 401,
                'msg': 'Unexcepeted error!'
            })
        comment.objects.filter(id=pk).delete()


class commentDetailViewSet(viewsets.ViewSet):

    def list(self,request,pk):
        try:
            queryset = comment.objects.filter(topicComment=pk)
        except len(queryset)==0:
            return Response({
                'code': 201,
                'msg': 'No comment currently!'
            })
        serializer = commentListSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
class membershipViewSet(viewsets.ViewSet):

    def create(self,request):
        serializer = membershipSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    
    def update(self,request):
        try:
            old = membership.objects.get(Q(m_forum=request.data[0]), Q(m_user=request.data[1]))
        except membership.DoesNotExist:
            return Response({
                'code': 401,
                'msg': 'Unexpected error!'
            })
        new = membershipSerializer(instance=old, data=request.data, partial=False)
        new.is_valid(raise_exception=True)
        new.save()
        return Response({
            'msg': 'Successfully',
            'code': 200
        })
    
    def delete(self,request):
        try:
            old = membership.objects.get(Q(m_forum=request.data[0]), Q(m_user=request.data[1]))
        except membership.DoesNotExist:
            return Response({
                'code': 401,
                'msg': 'Unexpected error!'
            })
        membership.objects.filter(Q(m_forum=request.data[0]), Q(m_user=request.data[1])).delete()
