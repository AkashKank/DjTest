from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from .models import *
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
import pandas as pd
from .serializer import TopicSerializer, MessageSerializer
from io import BytesIO
import json

# Create your views here
class TopicListCreateView(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticated]

#Working
class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            # Superuser broadcasting
            content = request.data.get('content', '')
            if not content:
                return Response({'error': 'content is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            topics = Topic.objects.all()
            for topic in topics:
                Message.objects.create(topic=topic, user=request.user, content=content)
            
            return Response({'status': 'messages broadcasted'}, status=status.HTTP_201_CREATED)
        
        # Regular user can send a message to a specific topic
        return super().post(request, *args, **kwargs)
    
# Class for Export Model as a excel
class ExportAPIView(APIView):
    def post(self, request):
        try:
            # empty list
            data = []

            topics = Topic.objects.all()
            for topic in topics:
                # data.append({'Topic':topic.name})

                messages = Message.objects.filter(topic=topic).select_related('user')
                first_msg = True
                for message in messages:
                    if first_msg:
                        data.append({
                            'Topic': topic.name,
                            'User': message.user.username,
                            'Message from user': message.content,
                        })
                        first_msg = False
                    else:
                        data.append({
                            # 'Topic': topic.name,
                            'User': message.user.username,
                            'Message from user': message.content,
                        })

            df = pd.DataFrame.from_records(data)
            df.columns = ['Topic','User', 'Message from user']
            df.to_excel('MessagesExportss5.xlsx', index=False)

            return Response({
                'status': True,
                'message':'Messages exported Sucessfully'
            },status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                'status':False,
                'message':'We could not complete Export'
            }, status=status.HTTP_400_BAD_REQUEST)
        



class NewExportDoctorAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # try:
            # empty list
            json_data = {
                "status": "success",
                "message": "data",
                "data": [
                     {
            "id": 42,
            "doctor": {
                "id": 1,
                "tm": {
                    "id": 1,
                    "rbm": {
                        "id": 1,
                        "abm": {
                            "id": 2,
                            "zbm": {
                                "id": 1,
                                "head_quarter": {
                                    "id": 1,
                                    "zone": {
                                        "id": 1,
                                        "name": "test zone",
                                        "created_date": "2024-08-08T00:00:00+05:30",
                                        "updated_date": "2024-08-08T00:00:00+05:30",
                                        "deleted_date": "2024-08-08T00:00:00+05:30",
                                        "created_by": 1,
                                        "updated_by": 1,
                                        "deleted_by": 1
                                    },
                                    "name": "head q test\n",
                                    "created_date": "2024-08-08T00:00:00+05:30",
                                    "updated_date": "2024-08-08T00:00:00+05:30",
                                    "deleted_date": "2024-08-08T00:00:00+05:30",
                                    "created_by": 1,
                                    "updated_by": 1,
                                    "deleted_by": 1
                                },
                                "name": "phelbo11",
                                "mobile": "null",
                                "email": "null",
                                "address": "null",
                                "created_date": "2024-07-30T19:12:17.789040+05:30",
                                "updated_date": "2024-07-30T19:12:17.789040+05:30",
                                "deleted_date": "2024-07-30T19:12:17.789040+05:30",
                                "user": 31,
                                "state": 1,
                                "city": 1,
                                "pincode": 1,
                                "created_by": 1,
                                "updated_by": 1,
                                "deleted_by": 1
                            },
                            "name": "Abm 3",
                            "mobile": "null",
                            "email": "null",
                            "address": "null",
                            "created_date": "2024-08-05T19:03:56.494579+05:30",
                            "updated_date": "null",
                            "deleted_date": "null",
                            "user": 28,
                            "state": 1,
                            "city": 1,
                            "pincode": 1,
                            "created_by": 30,
                            "updated_by": "null",
                            "deleted_by": "null"
                        },
                        "name": "rbm1 =i[date",
                        "mobile": "null",
                        "email": "null",
                        "address": "null",
                        "created_date": "2024-08-05T21:13:59.179798+05:30",
                        "updated_date": "null",
                        "deleted_date": "null",
                        "user": 52,
                        "state": 1,
                        "city": 1,
                        "pincode": 1,
                        "created_by": 30,
                        "updated_by": 30,
                        "deleted_by": "null"
                    },
                    "name": "tm1 -update",
                    "mobile": "null",
                    "email": "null",
                    "address": "null",
                    "created_date": "2024-08-06T11:43:25.710904+05:30",
                    "updated_date": "2024-08-06T11:43:25.710904+05:30",
                    "deleted_date": "2024-08-06T11:43:25.710904+05:30",
                    "user": 53,
                    "state": 1,
                    "city": 1,
                    "pincode": 1,
                    "created_by": 30,
                    "updated_by": 30,
                    "deleted_by": "null"
                },
                "name": "test Doctro",
                "mobile": "23659874563",
                "email": "Test@gmail.com",
                "clinic_address": "null",
                "latitude": "null",
                "longitude": "null",
                "doctor_consent_file": "null",
                "P_code": "null",
                "mci_reg_no": "null",
                "status": 1,
                "is_dnd": 0,
                "created_date": "2024-07-31T11:53:39.699654+05:30",
                "updated_date": "2024-07-31T11:53:39.699654+05:30",
                "deleted_date": "null",
                "state": 1,
                "city": 1,
                "pincode": 1,
                "created_by": 1,
                "updated_by": 1,
                "deleted_by": 1
            },
            "scheduled_date": "2024-08-01T00:00:00+05:30",
            "start_time": "11:00",
            "end_time": "13:00",
            "is_accepted": "true",
            "accepted_by": "null",
            "accepted_date": "null",
            "created_date": "2024-08-01T15:33:00.056641+05:30",
            "rejected_date": "null",
            "reject_remark": "null",
            "updated_date": "null",
            "deleted_date": "null",
            "phelbo": 17,
            "inventory_id": 6,
            "created_by": 1,
            "rejected_by": 1,
            "updated_by": 1,
            "deleted_by": 1,
            "status": 1,
            "record": 32
        },
        {
            "id": 44,
            "doctor": {
                "id": 1,
                "tm": {
                    "id": 1,
                    "rbm": {
                        "id": 1,
                        "abm": {
                            "id": 2,
                            "zbm": {
                                "id": 1,
                                "head_quarter": {
                                    "id": 1,
                                    "zone": {
                                        "id": 1,
                                        "name": "test zone",
                                        "created_date": "2024-08-08T00:00:00+05:30",
                                        "updated_date": "2024-08-08T00:00:00+05:30",
                                        "deleted_date": "2024-08-08T00:00:00+05:30",
                                        "created_by": 1,
                                        "updated_by": 1,
                                        "deleted_by": 1
                                    },
                                    "name": "head q test\n",
                                    "created_date": "2024-08-08T00:00:00+05:30",
                                    "updated_date": "2024-08-08T00:00:00+05:30",
                                    "deleted_date": "2024-08-08T00:00:00+05:30",
                                    "created_by": 1,
                                    "updated_by": 1,
                                    "deleted_by": 1
                                },
                                "name": "phelbo11",
                                "mobile": "null",
                                "email": "null",
                                "address": "null",
                                "created_date": "2024-07-30T19:12:17.789040+05:30",
                                "updated_date": "2024-07-30T19:12:17.789040+05:30",
                                "deleted_date": "2024-07-30T19:12:17.789040+05:30",
                                "user": 31,
                                "state": 1,
                                "city": 1,
                                "pincode": 1,
                                "created_by": 1,
                                "updated_by": 1,
                                "deleted_by": 1
                            },
                            "name": "Abm 3",
                            "mobile": "null",
                            "email": "null",
                            "address": "null",
                            "created_date": "2024-08-05T19:03:56.494579+05:30",
                            "updated_date": "null",
                            "deleted_date": "null",
                            "user": 28,
                            "state": 1,
                            "city": 1,
                            "pincode": 1,
                            "created_by": 30,
                            "updated_by": "null",
                            "deleted_by": "null"
                        },
                        "name": "rbm1 =i[date",
                        "mobile": "null",
                        "email": "null",
                        "address": "null",
                        "created_date": "2024-08-05T21:13:59.179798+05:30",
                        "updated_date": "null",
                        "deleted_date": "null",
                        "user": 52,
                        "state": 1,
                        "city": 1,
                        "pincode": 1,
                        "created_by": 30,
                        "updated_by": 30,
                        "deleted_by": "null"
                    },
                    "name": "tm1 -update",
                    "mobile": "null",
                    "email": "null",
                    "address": "null",
                    "created_date": "2024-08-06T11:43:25.710904+05:30",
                    "updated_date": "2024-08-06T11:43:25.710904+05:30",
                    "deleted_date": "2024-08-06T11:43:25.710904+05:30",
                    "user": 53,
                    "state": 1,
                    "city": 1,
                    "pincode": 1,
                    "created_by": 30,
                    "updated_by": 30,
                    "deleted_by": "null"
                },
                "name": "test Doctro",
                "mobile": "23659874563",
                "email": "Test@gmail.com",
                "clinic_address": "null",
                "latitude": "null",
                "longitude": "null",
                "doctor_consent_file": "null",
                "P_code": "null",
                "mci_reg_no": "null",
                "status": 1,
                "is_dnd": 0,
                "created_date": "2024-07-31T11:53:39.699654+05:30",
                "updated_date": "2024-07-31T11:53:39.699654+05:30",
                "deleted_date": "null",
                "state": 1,
                "city": 1,
                "pincode": 1,
                "created_by": 1,
                "updated_by": 1,
                "deleted_by": 1
            },
            "scheduled_date": "2024-11-01T00:00:00+05:30",
            "start_time": "11:00",
            "end_time": "13:00",
            "is_accepted": "null",
            "accepted_by": "null",
            "accepted_date": "null",
            "created_date": "2024-08-06T18:50:22.415334+05:30",
            "rejected_date": "null",
            "reject_remark": "null",
            "updated_date": "null",
            "deleted_date": "null",
            "phelbo": "null",
            "inventory_id": 6,
            "created_by": 28,
            "rejected_by": "null",
            "updated_by": "null",
            "deleted_by": "null",
            "status": 2,
            "record": 35
        },
        {
            "id": 43,
            "doctor": {
                "id": 1,
                "tm": {
                    "id": 1,
                    "rbm": {
                        "id": 1,
                        "abm": {
                            "id": 2,
                            "zbm": {
                                "id": 1,
                                "head_quarter": {
                                    "id": 1,
                                    "zone": {
                                        "id": 1,
                                        "name": "test zone",
                                        "created_date": "2024-08-08T00:00:00+05:30",
                                        "updated_date": "2024-08-08T00:00:00+05:30",
                                        "deleted_date": "2024-08-08T00:00:00+05:30",
                                        "created_by": 1,
                                        "updated_by": 1,
                                        "deleted_by": 1
                                    },
                                    "name": "head q test\n",
                                    "created_date": "2024-08-08T00:00:00+05:30",
                                    "updated_date": "2024-08-08T00:00:00+05:30",
                                    "deleted_date": "2024-08-08T00:00:00+05:30",
                                    "created_by": 1,
                                    "updated_by": 1,
                                    "deleted_by": 1
                                },
                                "name": "phelbo11",
                                "mobile": "null",
                                "email": "null",
                                "address": "null",
                                "created_date": "2024-07-30T19:12:17.789040+05:30",
                                "updated_date": "2024-07-30T19:12:17.789040+05:30",
                                "deleted_date": "2024-07-30T19:12:17.789040+05:30",
                                "user": 31,
                                "state": 1,
                                "city": 1,
                                "pincode": 1,
                                "created_by": 1,
                                "updated_by": 1,
                                "deleted_by": 1
                            },
                            "name": "Abm 3",
                            "mobile": "null",
                            "email": "null",
                            "address": "null",
                            "created_date": "2024-08-05T19:03:56.494579+05:30",
                            "updated_date": "null",
                            "deleted_date": "null",
                            "user": 28,
                            "state": 1,
                            "city": 1,
                            "pincode": 1,
                            "created_by": 30,
                            "updated_by": "null",
                            "deleted_by": "null"
                        },
                        "name": "rbm1 =i[date",
                        "mobile": "null",
                        "email": "null",
                        "address": "null",
                        "created_date": "2024-08-05T21:13:59.179798+05:30",
                        "updated_date": "null",
                        "deleted_date": "null",
                        "user": 52,
                        "state": 1,
                        "city": 1,
                        "pincode": 1,
                        "created_by": 30,
                        "updated_by": 30,
                        "deleted_by": "null"
                    },
                    "name": "tm1 -update",
                    "mobile": "null",
                    "email": "null",
                    "address": "null",
                    "created_date": "2024-08-06T11:43:25.710904+05:30",
                    "updated_date": "2024-08-06T11:43:25.710904+05:30",
                    "deleted_date": "2024-08-06T11:43:25.710904+05:30",
                    "user": 53,
                    "state": 1,
                    "city": 1,
                    "pincode": 1,
                    "created_by": 30,
                    "updated_by": 30,
                    "deleted_by": "null"
                },
                "name": "test Doctro",
                "mobile": "23659874563",
                "email": "Test@gmail.com",
                "clinic_address": "null",
                "latitude": "null",
                "longitude": "null",
                "doctor_consent_file": "null",
                "P_code": "null",
                "mci_reg_no": "null",
                "status": 1,
                "is_dnd": 0,
                "created_date": "2024-07-31T11:53:39.699654+05:30",
                "updated_date": "2024-07-31T11:53:39.699654+05:30",
                "deleted_date": "null",
                "state": 1,
                "city": 1,
                "pincode": 1,
                "created_by": 1,
                "updated_by": 1,
                "deleted_by": 1
            },
            "scheduled_date": "2024-04-01T00:00:00+05:30",
            "start_time": "11:00",
            "end_time": "13:00",
            "is_accepted": "null",
            "accepted_by": "null",
            "accepted_date": "null",
            "created_date": "2024-08-02T15:19:37.362088+05:30",
            "rejected_date": "null",
            "reject_remark": "null",
            "updated_date": "null",
            "deleted_date": "null",
            "phelbo": "null",
            "inventory_id": 6,
            "created_by": 1,
            "rejected_by": 1,
            "updated_by": 1,
            "deleted_by": 1,
            "status": 1,
            "record": 33
        },
        {
            "id": 45,
            "doctor": {
                "id": 1,
                "tm": {
                    "id": 1,
                    "rbm": {
                        "id": 1,
                        "abm": {
                            "id": 2,
                            "zbm": {
                                "id": 1,
                                "head_quarter": {
                                    "id": 1,
                                    "zone": {
                                        "id": 1,
                                        "name": "test zone",
                                        "created_date": "2024-08-08T00:00:00+05:30",
                                        "updated_date": "2024-08-08T00:00:00+05:30",
                                        "deleted_date": "2024-08-08T00:00:00+05:30",
                                        "created_by": 1,
                                        "updated_by": 1,
                                        "deleted_by": 1
                                    },
                                    "name": "head q test\n",
                                    "created_date": "2024-08-08T00:00:00+05:30",
                                    "updated_date": "2024-08-08T00:00:00+05:30",
                                    "deleted_date": "2024-08-08T00:00:00+05:30",
                                    "created_by": 1,
                                    "updated_by": 1,
                                    "deleted_by": 1
                                },
                                "name": "phelbo11",
                                "mobile": "null",
                                "email": "null",
                                "address": "null",
                                "created_date": "2024-07-30T19:12:17.789040+05:30",
                                "updated_date": "2024-07-30T19:12:17.789040+05:30",
                                "deleted_date": "2024-07-30T19:12:17.789040+05:30",
                                "user": 31,
                                "state": 1,
                                "city": 1,
                                "pincode": 1,
                                "created_by": 1,
                                "updated_by": 1,
                                "deleted_by": 1
                            },
                            "name": "Abm 3",
                            "mobile": "null",
                            "email": "null",
                            "address": "null",
                            "created_date": "2024-08-05T19:03:56.494579+05:30",
                            "updated_date": "null",
                            "deleted_date": "null",
                            "user": 28,
                            "state": 1,
                            "city": 1,
                            "pincode": 1,
                            "created_by": 30,
                            "updated_by": "null",
                            "deleted_by": "null"
                        },
                        "name": "rbm1 =i[date",
                        "mobile": "null",
                        "email": "null",
                        "address": "null",
                        "created_date": "2024-08-05T21:13:59.179798+05:30",
                        "updated_date": "null",
                        "deleted_date": "null",
                        "user": 52,
                        "state": 1,
                        "city": 1,
                        "pincode": 1,
                        "created_by": 30,
                        "updated_by": 30,
                        "deleted_by": "null"
                    },
                    "name": "tm1 -update",
                    "mobile": "null",
                    "email": "null",
                    "address": "null",
                    "created_date": "2024-08-06T11:43:25.710904+05:30",
                    "updated_date": "2024-08-06T11:43:25.710904+05:30",
                    "deleted_date": "2024-08-06T11:43:25.710904+05:30",
                    "user": 53,
                    "state": 1,
                    "city": 1,
                    "pincode": 1,
                    "created_by": 30,
                    "updated_by": 30,
                    "deleted_by": "null"
                },
                "name": "test Doctro",
                "mobile": "23659874563",
                "email": "Test@gmail.com",
                "clinic_address": "null",
                "latitude": "null",
                "longitude": "null",
                "doctor_consent_file": "null",
                "P_code": "null",
                "mci_reg_no": "null",
                "status": 1,
                "is_dnd": 0,
                "created_date": "2024-07-31T11:53:39.699654+05:30",
                "updated_date": "2024-07-31T11:53:39.699654+05:30",
                "deleted_date": "null",
                "state": 1,
                "city": 1,
                "pincode": 1,
                "created_by": 1,
                "updated_by": 1,
                "deleted_by": 1
            },
            "scheduled_date": "2024-05-11T00:00:00+05:30",
            "start_time": "18:00",
            "end_time": "23:00",
            "is_accepted": "null",
            "accepted_by": "null",
            "accepted_date": "null",
            "created_date": "2024-08-06T18:53:29.130021+05:30",
            "rejected_date": "null",
            "reject_remark": "null",
            "updated_date": "null",
            "deleted_date": "null",
            "phelbo": "null",
            "inventory_id": 6,
            "created_by": 28,
            "rejected_by": "null",
            "updated_by": "null",
            "deleted_by": "null",
            "status": 1,
            "record": 36
        }
                ]
            }
        
            records = json_data['data']

            print("***********************************")
            print(records)
            # print(json_data["data"])

            rows = []
            for item in records:
                doctor = item['doctor']
                tm = doctor['tm']
                rbm = tm['rbm']
                abm = rbm['abm']
                zbm = abm['zbm']
                head_quarter = zbm['head_quarter']
                zone = head_quarter['zone']

                row = ({
                    'ID': item['id'],
                    'Doctor ID': doctor['id'],
                    'Doctor Name': doctor['name'],
                    'TM ID': tm['id'],
                    'TM ID': tm['name'],
                    'RBM ID': rbm['id'],
                    'RBM Name': rbm['name'],
                    'ABM ID': abm['id'],
                    'ABM Name': abm['name'],
                    'ZBM ID': zbm['id'],
                    'ZBM Name': zbm['name'],
                    'Head Quarter ID': head_quarter['id'],
                    'Zone ID': zone['id'],
                    'Zone Name': zone['name'],
                    'Phelbo': item['phelbo'],
                    'Status': item['status'],
                })
                rows.append(row)

            df = pd.DataFrame.from_records(rows)
            df.to_excel('Doctor1.xlsx', index=False)

            return Response({
                'status': True,
                'message':'Messages exported Sucessfully'
            },status=status.HTTP_200_OK)
        
        # except Exception as e:
            # return Response({
            #     'status':False,
            #     'message':'We could not complete Export'
            # }, status=status.HTTP_400_BAD_REQUEST)


# class NewOneExportDoctorAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         # try:
#             # empty list
#             json_data = {
#             }
        
#             records = json_data['data']

#             print("***********************************")
#             print(records)
#             # print(json_data["data"])

#             rows = []
#             for item in records:
#                 doctor = item['doctor']
#                 tm = doctor['tm']
#                 rbm = tm['rbm']
#                 abm = rbm['abm']
#                 zbm = abm['zbm']
#                 head_quarter = zbm['head_quarter']
#                 zone = head_quarter['zone']

#                 row = ({
#                     'ID': item['id'],
#                     'Doctor ID': doctor['id'],
#                     'Doctor Name': doctor['name'],
#                     'TM ID': tm['id'],
#                     'TM ID': tm['name'],
#                     'RBM ID': rbm['id'],
#                     'RBM Name': rbm['name'],
#                     'ABM ID': abm['id'],
#                     'ABM Name': abm['name'],
#                     'ZBM ID': zbm['id'],
#                     'ZBM Name': zbm['name'],
#                     'Head Quarter ID': head_quarter['id'],
#                     'Zone ID': zone['id'],
#                     'Zone Name': zone['name'],
#                     'Phelbo': item['phelbo'],
#                     'Status': item['status'],
#                 })
#                 rows.append(row)

#             df = pd.DataFrame.from_records(rows)
#             df.to_excel('Doctor1.xlsx', index=False)

#             return Response({
#                 'status': True,
#                 'message':'Messages exported Sucessfully'
#             },status=status.HTTP_200_OK)

# try:
        #     messages = Message.objects.select_related('topic', 'user').all()
        #     df = pd.DataFrame.from_records(
        #         messages.values('topic__name', 'user__username', 'content'),
        #         columns=['topic__name', 'user__username', 'content']
        #     )
            
        #     df.columns = ['Topic', 'User', 'Message from user']
        #     df.to_excel('MessagesExportss1.xlsx', index=False)

        #     return Response({
        #         'status': True,
        #         'message':'Messages exported Sucessfully'
        #     },status=status.HTTP_200_OK)



# class ExportAPIView(APIView):
#     def post(self, request):
#         try:
#             messages = Message.objects.all()
#             df = pd.DataFrame.from_records(messages.values('topic','user','content'))
#             df.columns = ['Topic', 'User', 'Message from user']
#             df.to_excel('MessagesExport.xlsx', index=False)
#             return Response({
#                 'status': True,
#                 'message':'Messages exported Sucessfully'
#             },status=status.HTTP_200_OK)
        
#         except Exception as e:
#             return Response({
#                 'status':False,
#                 'message':'We could not complete Export'
#             }, status=status.HTTP_400_BAD_REQUEST)

# Testing  
# class NewMessageListCreateView(generics.ListCreateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         topic_id = self.request.data.get('topic')
#         user = self.request.user
#         print(user)
#         topic_id = self.request.data.get('topic')

#         if user.is_superuser:
#             topics = Topic.objects.all()
#             print(topics)
#             for topic in topics:
#                 serializer.save(user=user, topic=topic)
#         else:
#             topic = Topic.objects.get(id=topic_id)
#             serializer.save(user=user, topic=topic)


# data = []

#             topics = Topic.objects.all()
#             for topic in topics:
#                 messages = Message.objects.filter(topic=topic).select_related('user')
#                 for message in messages:
#                     data.append({
#                         'Topic': topic.name,
#                         'User': message.user.username,
#                         'Message from user': message.content,
#                     })

#             df = pd.DataFrame.from_records(data)
#             df.columns = ['Topic','User', 'Message from user']
#             df.to_excel('MessagesExportss4.xlsx', index=False)