from django.shortcuts import render
from numpy import delete
from rest_framework import viewsets, status
from user import serializers
from .serializers import forumCreateSerializer, forumListSerializer, topicSerializer, topicListSerializer, commentSerializer, commentListSerializer, membershipSerializer, commentCreateSerializer
from rest_framework.response import Response
from .models import forum, topic, comment, membership
from user.models import user
from django.db.models import Q
# Create your views here.
class forumViewSetList(viewsets.ViewSet):

    def create(self,request):
        print(request.data)
        serializer = forumCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        forumid = forum.objects.filter(creater_id=request.data['creater']).last()
        queryset = membership.objects.create(m_forum=forumid, m_user_id=request.data['creater'], is_admin=True)
        queryset.save()
        return Response(status=status.HTTP_200_OK)

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
        return Response(status=status.HTTP_200_OK)
        

class forumDetailViewSetList(viewsets.ViewSet):

    def list(self, request):
        queryset1 = forum.objects.filter(tag="课程学习")
        queryset2 = forum.objects.filter(tag="考研保研")
        queryset3 = forum.objects.filter(tag="大创科研")
        queryset4 = forum.objects.filter(tag="竞赛前瞻")
        queryset5 = forum.objects.filter(tag="兴趣圈子")
        serializer1=forumListSerializer(queryset1, many=True)
        serializer2=forumListSerializer(queryset2, many=True)
        serializer3=forumListSerializer(queryset3, many=True)
        serializer4=forumListSerializer(queryset4, many=True)
        serializer5=forumListSerializer(queryset5, many=True)
        response = {
            'code':200,
            'msg':"Success!",
            'data':{
                '1':{
                    'id':1,                   
                    'classname':"课程学习",
                    'children':serializer1.data
                },
                '2':{
                    'id':2,
                    'classname':"考研保研",
                    'children':serializer2.data
                },
                '3':{
                    'id':3,
                    'classname':"大创科研",
                    'children':serializer3.data
                },
                '4':{
                    'id':4,
                    'classname':"竞赛前瞻",
                    'children':serializer4.data
                },
                '5':{
                    'id':5,
                    'classname':"兴趣圈子",
                    'children':serializer5.data
                }
            }
        }
        
        return Response(response)


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
        print(request.data)
        serializer = topicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        queryset = topic.objects.filter(pubForum=request.data['pubForum'])
        serializer = topicListSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

class topicDetailViewSet(viewsets.ViewSet):

    def list(self,request,pk):
        try:
            queryset = topic.objects.filter(pubForum=pk)
        except queryset.count()==0:
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
        serializer = topicListSerializer(queryset)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
class commentViewSet(viewsets.ViewSet):

    def create(self, request):
        print(request.data)
        serializer = commentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        topic = request.data['topicComment']
        queryset = comment.objects.filter(topicComment_id=topic)
        serializer = commentListSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

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
            querysets = comment.objects.filter(topicComment_id=pk)
        except  querysets.count()==0:
            return Response({
                'code': 201,
                'msg': 'No comment currently!'
            })
        serializer = commentListSerializer(querysets, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self,request,pk):

        querysets = comment.objects.filter(puber_id=pk)
        for queryset in querysets:
            if queryset.is_read==False:
                return Response({
                    'code':201
                })
        return Response({
            'code':200
        })

class commentIsReadViewSet(viewsets.ViewSet):

    def list(self,request,pk):
        sql = "select * from forum_comment,forum_topic where topicComment_id=forum_topic.id and forum_topic.creater_id=%s and puber_id<>%s"

        querysets = comment.objects.raw(sql,[pk,pk])

        serializer = commentListSerializer(querysets,many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def retrieve(self,request,pk):
        topicor = topic.objects.get(id=pk).creater
        if request.data['userNo']==topicor.userNo:
            querysets = comment.objects.filter(topicComment_id=pk)
            for queryset in querysets:
                if queryset.is_read==False:
                    querysets.update(is_read=True)
                    return Response(status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_200_OK)
    
class membershipViewSet(viewsets.ViewSet):

    def create(self,request):
        forumID = request.data['postid']
        follow = request.data['userid']
        following = forum.objects.get(id=forumID)
        follower = user.objects.get(userNo=follow)
        queryset = membership.objects.create(m_forum=following, m_user=follower)
        queryset.save()
        return Response({
            'code':200
        })

    def retrieve(self,request):
        print(request.data)

        try:
            ship=membership.objects.get(m_user_id=request.data['userid'],m_forum_id=request.data['postid'])
        except membership.DoesNotExist:
            return Response({
                'code':201,
                'msg':"Not!"
            })
        return Response({
            'code':200,
            'msg':"Yes!"
        })

    
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
            old = membership.objects.get(Q(m_forum_id=request.data['postid']), Q(m_user_id=request.data['userid']))
        except membership.DoesNotExist:
            return Response({
                'code': 401,
                'msg': 'Unexpected error!'
            })
        membership.objects.filter(Q(m_forum=request.data['postid']), Q(m_user=request.data['userid'])).delete()
        return Response({
            'code':201,
            'msg':"Success!"
        })
