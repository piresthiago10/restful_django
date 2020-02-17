from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from atracoes.api.serializers import AtracaoSerializer
from core.models import PontoTuristico


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto',
                  'atracoes', 'comentarios', 'endereco',
                  'descricao_completa', 'descricao_completa2')

    # incluindo informacoes adicionais com SerializerMethodField
    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
