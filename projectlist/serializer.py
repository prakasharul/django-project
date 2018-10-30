from rest_framework import serializers

from . models import projects



class projectListSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = projects
		fields = ( 'id','name', 'client', 'target_date', 'email','budget','mobile','duration', 'resource', 'status', 'created_date')



