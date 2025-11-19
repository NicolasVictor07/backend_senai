from rest_framework import serializers
from .models import Personagem, AtorDublador, Obra, Habilidade, PersonagemHabilidades, Relacionamento

class AtorDubladorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtorDublador
        fields = '__all__'

class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra
        fields = '__all__'

class PersonagemSerializer(serializers.ModelSerializer):
    ator_dublador = AtorDubladorSerializer()
    obra = ObraSerializer()

    class Meta:
        model = Personagem
        fields = '__all__'

class HabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidade
        fields = '__all__'

class PersonagemHabilidadesSerializer(serializers.ModelSerializer):
    personagem = PersonagemSerializer()
    habilidade = HabilidadeSerializer()

    class Meta:
        model = PersonagemHabilidades
        fields = '__all__'

class RelacionamentoSerializer(serializers.ModelSerializer):
    personagem1 = PersonagemSerializer()
    personagem2 = PersonagemSerializer()

    class Meta:
        model = Relacionamento
        fields = '__all__'

