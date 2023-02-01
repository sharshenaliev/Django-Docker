from rest_framework import generics, permissions
from .serializers import PlotListSerializer
from .models import Plot, Farmer, Culture
from rest_framework.response import Response


class PlotsListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PlotListSerializer

    def get_queryset(self):
        return Plot.objects.filter(farmer=Farmer.objects.get(unique_key=self.kwargs['unique_key']))

    def patch(self, request, unique_key):
        try:
            Plot.objects.filter(pk=request.data['id']).update(culture=culture)
            data = {
                'message': "Культура была изменена",
                'key': unique_key
            }
        except:
            data = {
                'message': "Такой культуры нет",
                'key': unique_key
            }
        return Response(data)
