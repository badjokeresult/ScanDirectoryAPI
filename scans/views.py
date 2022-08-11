from rest_framework import viewsets, generics
from .models import Scan
from .serializers import *
# Create your views here.


class ScanListView(generics.ListAPIView):
    queryset = Scan.objects.all()
    serializer_class = ScanSerializer


class ScanCreateView(generics.CreateAPIView):
    serializer_class = ScanSerializer


class ScanDeleteView(generics.DestroyAPIView):
    serializer_class = ScanSerializer
    queryset = Scan.objects.all()


class ScanDetailedView(generics.RetrieveAPIView):
    serializer_class = ScanSerializer
    queryset = Scan.objects.all()


class ScanUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ScanSerializer
    queryset = Scan.objects.all()