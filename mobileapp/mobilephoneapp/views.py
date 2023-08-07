from django.http import HttpResponse
from rest_framework import viewsets, generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.views import APIView
from .models import Category
from .serializers import CategorySerializer


def index(request):
    return HttpResponse("hello")


class SampleView(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.filter(active=True)
    serializer_class = CategorySerializer

    def get_queryset(self):
        q = self.queryset

        kw = self.request.query_params.get('kw')
        if kw:
            q = q.filter(name__icontains=kw)
        return q
