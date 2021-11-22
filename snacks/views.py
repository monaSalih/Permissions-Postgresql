from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Snack
from .serializers import SnackSerlizer

class SnackList(ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerlizer

class SnackDetail(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerlizer