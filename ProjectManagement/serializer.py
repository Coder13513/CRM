from rest_framework import serializers
from .models import *

class Business_opportunitySerializer(serializers.ModelSerializer):
      class  Meta:
          model        =           Business_opportunity
          fields       =           '__all__'
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
          model         =           Project
          fields        =           '__all__'
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
          model         =           Team
          fields        =           '__all__'
