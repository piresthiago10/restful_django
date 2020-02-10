from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.decorators import action


class PontoTuristicoViewSet(ModelViewSet):
    # Serializer são os campos para serem exibidos
    # no json
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

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