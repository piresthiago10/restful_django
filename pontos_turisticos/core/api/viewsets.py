from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import PontoTuristico

from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    # Serializer são os campos para serem exibidos
    # no json
    serializer_class = PontoTuristicoSerializer
    # endpoints só para admin: https://www.django-rest-framework.org/api-guide/permissions/#isadminuser
    #permission_classes = (IsAuthenticated,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = (SearchFilter,)
    # endereco__linha1 busca por chave estrangeira
    # '^': 'istartswith',
    # '=': 'iexact',
    # '@': 'search',
    # '$': 'iregex',
    search_fields = ('nome', 'descricao', '=endereco__linha1')
    # lookup_field precisa ser unico no banco de dados
    lookup_field = 'nome'

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome=nome)

        if descricao:
            queryset = queryset.filter(descricao=descricao)

        return queryset

    ''' def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)'''

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        # o super obtem tudo que a classe mestra faz
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    ''' Actrions, é um meio de implementar funções sem inflingir
    os conceitos do rest.
    http://[ip:porta]/pontosturisticos/pk/denunciar/
    '''
    @action(methods=['post', 'get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    # action no endpoint como um todo
    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass
