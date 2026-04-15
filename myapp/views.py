from django.shortcuts import render,get_object_or_404
from .serializers import *
from rest_framework.generics import DestroyAPIView,RetrieveAPIView,ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .permissions import IsOwner
# Create your views here.

class ListVideo(ListAPIView):
    queryset=Video.objects.all()
    serializer_class=VideoSerializer

class DetailVideo(RetrieveAPIView):
    queryset=Video.objects.all()
    serializer_class=VideoSerializer
    lookup_field='id'

class VideoComment(ListAPIView):
    serializer_class=CommentSerializers

    def get_queryset(self):
        video_id=self.kwargs.get('id')
        return Comment.objects.filter(video_id=video_id)
    
class ChannelList(ListAPIView):
    queryset=Channel.objects.all()
    serializer_class=ChannelSerializers

class ChannelVideo(ListAPIView):
    serializer_class=VideoSerializer

    def get_queryset(self):
        channel_id=self.kwargs.get('id')
        return Video.objects.filter(channel_id=channel_id)
    
class ChannelCreate(CreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Channel.objects.all()
    serializer_class=ChannelSerializers

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class MyChannels(ListAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=ChannelSerializers

    def get_queryset(self):
        return Channel.objects.filter(owner=self.request.user)
    
class ChannelDetail(RetrieveUpdateDestroyAPIView):
    queryset=Channel.objects.all()
    serializer_class=ChannelSerializers
    lookup_field='id'
    permission_classes=[IsOwner]

class VideoCreate(ListCreateAPIView):
    serializer_class=VideoSerializer
    queryset=Video.objects.all()
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        channel=serializer.validated_data.get('channel')
        if channel.owner!=self.request.user:
            raise PermissionDenied("Вы можете загружать видео только в свой канал!")
        serializer.save()

class VideoDetail(RetrieveUpdateDestroyAPIView):
    serializer_class=VideoSerializer
    permission_classes=[IsOwner]
    lookup_field='id'
    queryset = Video.objects.all()


class CommentCreate(CreateAPIView):
    serializer_class=CommentSerializers
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        video_id=self.kwargs.get('id')
        serializer.save(user=self.request.user, video_id=video_id)

class CommentDelete(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

class LikeCreate(CreateAPIView):
    serializer_class=LikeSerializes
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        video_id=self.kwargs.get('id')
        if not Like.objects.filter(user=self.request.user, video_id=video_id).exists():
            serializer.save(user=self.request.user, video_id=video_id)

class LikeDelete(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        video_id = self.kwargs.get('id')
        like = get_object_or_404(Like, user=request.user, video_id=video_id)
        
        like.delete()
    