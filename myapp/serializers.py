from .models import Channel,Video,Comment,Like
from accounts.serializers import RegisterUser
from accounts.models import Users
from rest_framework import serializers


class LikeSerializes(serializers.ModelSerializer):
    created_at=serializers.DateTimeField(read_only=True)
    user=RegisterUser(read_only=True)
    user_id=serializers.PrimaryKeyRelatedField(
        queryset=Users.objects.all(),
        source='user',
        write_only=True
    )
    video_id=serializers.PrimaryKeyRelatedField(
        queryset=Video.objects.all(),
        source='video',
        write_only=True
    )
    class Meta:
        model=Like
        fields=['user','created_at','user_id','video_id']

class CommentSerializers(serializers.ModelSerializer):
    created_at=serializers.DateTimeField(read_only=True)
    user=RegisterUser(read_only=True)
    user_id=serializers.PrimaryKeyRelatedField(
        queryset=Users.objects.all(),
        source='user',
        write_only=True
    )
    video_id=serializers.PrimaryKeyRelatedField(
        queryset=Video.objects.all(),
        source='video',
        write_only=True
    )
    class Meta:
        model=Comment
        fields=['user','text','created_at','user_id','video_id']


class ChannelSerializers(serializers.ModelSerializer):
    created_at=serializers.DateTimeField(read_only=True)
    owner=RegisterUser(read_only=True)
    owner_id=serializers.PrimaryKeyRelatedField(
        queryset=Users.objects.all(),
        source='owner',
        write_only=True
    )
    class Meta:
        model=Channel
        fields=['owner','title','description','avatar','created_at','owner_id']

        


class VideoSerializer(serializers.ModelSerializer):
    created_at=serializers.DateTimeField(read_only=True)
    comments = CommentSerializers(many=True, read_only=True) 
    channel=ChannelSerializers(read_only=True)
    channel_id=serializers.PrimaryKeyRelatedField(
        queryset=Channel.objects.all(),
        source='channel',
        write_only=True
    )
    like_count=serializers.SerializerMethodField()
    class Meta:
        model=Video
        fields=['channel','video_file','title','description','created_at', 'channel_id','like_count','comments']

    def get_like_count(self,obj):
        return Like.objects.filter(video=obj).count()


