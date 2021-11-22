from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Snack
from .serializers import SnackSerlizer
from .permissions import IsAuthorOrReadOnly

class SnackList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Snack.objects.all()
    serializer_class = SnackSerlizer

class SnackDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Snack.objects.all()
    serializer_class = SnackSerlizer