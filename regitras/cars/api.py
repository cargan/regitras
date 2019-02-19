from rest_framework import serializers, viewsets
from . import models

# Serializers define the API representation.
class LicenzeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Licenze
        fields = ('first_name', 'last_name', 'car_brand', 'car_model')

# ViewSets define the view behavior.
class LicenzeViewSet(viewsets.ModelViewSet):
    queryset = models.Licenze.objects.all()
    serializer_class = LicenzeSerializer
