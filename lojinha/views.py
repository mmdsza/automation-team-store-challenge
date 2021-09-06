from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from lojinha.models import Produto
from lojinha.serializers import ProdutoSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def lojinha_list(request):
    # GET Lista de produtos, POST new produto, DELETE ALL produtos
    if request.method == 'GET':
        produto = Produto.objects.all()
        name = request.GET.get('name', None)
        if name is not None:
            produto = produto.filter(name__icontains=name)
        produto_serializer = ProdutoSerializer(produto, many=True)
        return JsonResponse(produto_serializer.data, safe=False)


    elif request.method == 'POST':
        produto_data = JSONParser().parse(request)
        produto_serializer = ProdutoSerializer(data=produto_data)
        if produto_serializer.is_valid():
            produto_serializer.save()
            return JsonResponse(produto_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(produto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        qtd = Produto.objects.all().delete()
        return JsonResponse({'message': 'Todos os {} produtos foram deletados'.format(qtd[0])}, status=status.HTTP_200_OK)




@api_view(['GET', 'PUT', 'DELETE'])
def lojinha_detalhada(request, pk):
    try:
        produto = Produto.objects.get(pk=pk)
    except Produto.DoesNotExist:
        return JsonResponse({'message':'Produto nao encontrado'}, status=status.HTTP_404_NOT_FOUND)
