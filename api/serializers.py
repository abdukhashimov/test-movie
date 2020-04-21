from rest_framework.serializers import ModelSerializer
from api.models import Movie

class MovieSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'year_of_release',)
        model = Movie
        extra_kwargs = {'id':{'read_only':True}}