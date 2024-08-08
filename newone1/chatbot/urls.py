from django.urls import path
from .views import *
urlpatterns = [
    path('topics/', TopicListCreateView.as_view(), name='topic-list-create'),
    # path('messages/', NewMessageListCreateView.as_view(), name='message-list-create'),
    path('usermessage/', MessageListCreateView.as_view(), name='usermessage'),
    # path('superuserview/', SuperuserBroadcastView.as_view(), name='message-create'),


    path('export/', ExportAPIView.as_view(), name='export'),
    # path('exportview/', ExportToExcelView.as_view(), name='exportview'),
    path('exportdoctor/', NewExportDoctorAPIView.as_view(), name='exportdoctor'),
]