from rest_framework.generics import ListAPIView
from .serializers import AstroRegisterSerializer
from ..models import AstroRegister
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView


class AstroRegisterAPIView(ListAPIView):
    serializer_class = AstroRegisterSerializer
    queryset = AstroRegister.objects.all()


@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = AstroRegister.objects.all()

        name = request.query_params.get('name', None)
        if name is not None:
            tutorials = tutorials.filter(name__icontains=name)

        tutorials_serializer = AstroRegisterSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = AstroRegisterSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = AstroRegister.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try:
        tutorial = AstroRegister.objects.get(pk=pk)
    except AstroRegister.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tutorial_serializer = AstroRegisterSerializer(tutorial)
        return JsonResponse(tutorial_serializer.data)

    elif request.method == 'PUT':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = AstroRegisterSerializer(tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tutorial.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class AstroRegisterList(APIView):
    # Устанавливаем json-тип данных для Response
    renderer_classes = [JSONRenderer]

    # обработка GET-запроса (вывод всех записей)
    @staticmethod
    def get(request):
        if request.GET.get('name', None):
            astro_register = AstroRegister.objects.filter(name__exact=request.GET.get('name'))
        else:
            astro_register = AstroRegister.objects.all()
        serializer = AstroRegisterSerializer(astro_register, many=True)
        return Response({'astro_register': serializer.data})

    # обработка POST-запроса (добавление новой записи)
    @staticmethod
    def post(self, request):
        serializer = AstroRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'ContactRequest Created!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View-класс реализующий Read, Update, Delete операции над отдельной сущностью (по Primary Key в БД)
class AstroRegisterDetail(APIView):
    renderer_classes = [JSONRenderer]

    # HTTP GET
    def get(self, request, pk):
        astro_register = self.get_object(pk)
        if not astro_register:
            return Response({'message': 'NOT FOUND'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AstroRegisterSerializer(astro_register)
        return Response(serializer.data)

    # HTTP PUT/PATCH
    def put(self, request, pk):
        astro_register = self.get_object(pk)
        if not astro_register:
            return Response({'message': 'NOT FOUND'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AstroRegisterSerializer(astro_register, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'ContactRequest Updated!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # HTTP DELETE
    def delete(self, request, pk):
        astro_register = self.get_object(pk)
        if not astro_register:
            return Response({'message': 'NOT FOUND'}, status=status.HTTP_404_NOT_FOUND)
        astro_register.delete()
        return Response({'message': 'ContactRequest Deleted!'}, status=status.HTTP_200_OK)

    @staticmethod
    def get_object(pk):
        try:
            return AstroRegister.objects.get(pk=pk)
        except AstroRegister.DoesNotExist:
            return None



