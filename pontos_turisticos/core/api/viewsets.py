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
        return Response({'teste': 123})
    
    def create(self, request, *args, **kwargs):
        return Response({'Hello': request.data['nome']})
    
    def destroy(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def partial_update(self, request, *args, **kwargs):
        pass

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