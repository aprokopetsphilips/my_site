from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializer import WomenSerializer


# Create your views here.

"""class WomenViewSet(viewsets.ModelViewSet):  # в юрл в виде словаря нужно указать методы и соответсвующие вызовы
    queryset = Women.objects.all()
    serializer_class = WomenSerializer  # https://www.django-rest-framework.org/api-guide/viewsets/
    # def get_queryset(self):
        #return Women.objects.all()[:3] # здесь мы переопределяем queryset для вывода только первых 3 записей
    # в этом случае queryset = Women.objects.all() из класса удаляется а в роутере прописывается basename = 'somename'
    # при этом чтобы получить конкретную запись нужно дописать:
    #pk = self.kwargs.get('pk')
    #if not pk:
    #   return Women.objects.all()[:3]
    # return Women.objects.filter(pk=pk)


    @action(methods=['get'],
            detail=False)  # используется для создания доп функций вывода информации.В данном случае выводим список категорий.Если поставить Тру-выведет одну категорию.

    def category(self, request):
        cats = Category.objects.all()
        return Response({'cats': [c.name for c in cats]})"""


class WomenAPIList(generics.ListCreateAPIView):  # get и post запросы обрабатывает
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,) # только чтение для авторизированых

class WomenApiUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated,) # только чтение и редактирование для владельца записи
    #authentication_classes = (TokenAuthentication,) # авторизация только по токенам


class WomenApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)  # собственный классюЧитают все а удаляет только админ



"""stage 1 class WomenApiView(APIView):
    def get(self, request):
        w = Women.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Women.objects.get(pk=pk)

        except:
            return Response({'error': 'Object does not exist'})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self,request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return Response({'error':'Object does not exist'})
        instance = Women.objects.filter(id=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""
