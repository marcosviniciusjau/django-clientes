from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'O número do CPF é inválido'})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'O nome deve conter apenas letras'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O RG deve ter 9 dígitos'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'O número de celular deve seguir esse modelo: 11 99999-9999, respeitando os espaços e traço'})
        return data
    