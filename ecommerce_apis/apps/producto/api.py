from .models import Producto
from rest_framework import viewsets, permissions
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = ProductoFilter
    # ordering_fields = ['dni', 'nombre_completo']
    # lookup_field = 'uuid'