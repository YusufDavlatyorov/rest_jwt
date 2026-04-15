from django.urls import path
from .views import *

urlpatterns=[
    path('videos/', ListVideo.as_view()),
    path('video/<int:pk>/', DetailVideo.as_view()),
    path('video/<int:pk>/comments',VideoComment.as_view()),
    path('channels/',ChannelList.as_view()),
    path('channel/<int:pk>/videos', ChannelVideo.as_view()),
    path('channels_create', ChannelCreate.as_view()),
    path('my_channels', MyChannels.as_view()),
    path('channels/<int:id>/',ChannelDetail.as_view(),),
    path('video_create',VideoCreate.as_view()),
    path('video/<int:id>/', VideoDetail.as_view()),
    path('comment_create',CommentCreate.as_view()),
    path('comment_delete/<int:pk>/',CommentDelete.as_view())
]