from rest_framework import serializers
from lojinha.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('id', 'name', 'price', 'description','size')
