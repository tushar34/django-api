from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.contrib.auth import authenticate
from .serializer import *
# Create your views here.
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from rest_framework.generics import *
import json
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


class LoginView(APIView):
    # serializers = UserLoginSerializer
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user_data = authenticate(username=username, password=password)
        if(user_data):
            data = User.objects.get(username=username)
            refresh = RefreshToken.for_user(user_data)
            data = {
                'message': 'login successfully',
                'refresh': str(refresh),
                'token': str(refresh.access_token),
                'id': data.id
            }
            return JsonResponse(data)
        else:
            print('user not found')
            # return JsonResponse({'error':'your username and password are incorrect'})
            return Response(status=HTTP_400_BAD_REQUEST)


class BoardCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.data['user_id']
        board_name = request.data['board_name']
        user_data = User.objects.get(id=user_id)
        if(user_data):
            data = Board.objects.create(
                board_name=board_name, user_id=user_data)
            data.save()
            res_data = {
                'name': board_name,
                'message': 'add successfully'
            }
            return JsonResponse(res_data)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)

    def get(self, request, id, *args, **kwargs):
        print(id)
        user_data = Board.objects.filter(user_id=id).values()
        print(user_data)
        if(user_data):
            return Response({'data': user_data, 'message': 'get successfully'})
        else:
            return Response(status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        data = Board.objects.get(id=id)
        data.delete()
        # data.save()
        return Response({'message': 'delete successfully'})

    def patch(self, request, id, *args, **kwargs):
        name = request.data['name']
        data = Board.objects.filter(id=id).update(board_name=name)
        return Response({'message': 'update successfully'})


class ListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        print(id)
        list_data = List.objects.filter(board_id=id).values()
        if(list_data):
            return Response({'listdata': list_data, 'get': 'get successfully'})
        else:
            return Response({'error': 'Invalid Request'})

    def post(self, request):
        name = request.data['name']
        order = request.data['order']
        board_id = request.data['board_id']
        print(name)
        print(order)
        print(board_id)

        cheack_data = List.objects.filter(Q(list_name=name))
        if(cheack_data):
            return Response({'error': 'name already exist'})
        else:
            board_data = Board.objects.get(id=board_id)
            data = List.objects.create(
                list_name=name, list_order=order, board_id=board_data)
            data.save()
            return Response({'msg': 'add successfully'})

    def delete(self, request, id):
        data = List.objects.get(id=id)
        data.delete()
        return Response({'message': 'delete successfully'})

    def patch(self, request, id):
        name = request.data['name']
        data = List.objects.filter(id=id).update(list_name=name)
        return Response({'message': 'update successfully'})


class CardView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # host=HttpRequest.get_host()
        # print(host)
        card_data = Card.objects.all().values()

        data = list(card_data)
        for ddata in range(len(data)):
            print(data[ddata])
            if(data[ddata]['image'] == ''):
                data[ddata]['image']=None
            else:
                print(data[ddata]['image'])
                image_url = 'http://127.0.0.1:8000/media/'+(data[ddata]['image'])
                data[ddata]['image']=image_url
    
             # print(image_url)
        # print(data[0]['image'])
        # image_url = 'http://127.0.0.1:8000/media/'+data[0]['image']
        # print(image_url)
        # print(card_data[image])
        # c_data=list(card_data)
        # data={
        #     'card_data':c_data,
        #     'msg':'get successfully'
        # }
        # return JsonResponse(data)
        return Response({'card_data':data})

    def post(self, request):
        name = request.data['name']
        listid = request.data['list_id']
        boardid = request.data['board_id']
        order = request.data['order']

        board_data = Board.objects.get(id=boardid)
        list_data = List.objects.get(id=listid)

        card_data = Card.objects.create(
            card_name=name, card_order=order, list_id=list_data, board_id=board_data)
        card_data.save()
        return Response({'msg': 'add successfully'})

    def delete(self, request, id):
        card_data = Card.objects.get(id=id)
        card_data.delete()
        return Response({'msg': 'delete successfully'})

    def patch(self, request, id):
        name = request.data['name']
        description = request.data['description']
        image = request.data['image']
        print("image",image)
        if(request.data['description'] == ''):
            description = None

        else:
            description = request.data['description']
        if(request.data['image'] == ''):
            image = None
        else:
            iamge = request.data['image']

        card_data = Card.objects.filter(id=id).update(
            card_name=name, description=description, image=image)
        return Response({'msg': 'update successfully'})
