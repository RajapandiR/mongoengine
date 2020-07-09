from django.shortcuts import render
from rest_framework_mongoengine import viewsets
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status

from mongoapp import serializers, models 
# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):

	# lookup_field = 'id'
	serializer_class = serializers.ProfileSerializer
	queryset = models.Profile.objects.all()
	
	# def list(self, req):
	# 	queryset = models.Profile.objects.all()	
	# 	return Response(queryset)
class ProfileApiView(APIView):
	serializer_class = serializers.ProfileSerializer
	def get(self, request, format=None):
		obj = models.Profile.objects.all()
		serializer = serializers.ProfileSerializer(obj, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		print("serializer", serializer)
		if serializer.is_valid():
			serializer.save()
			return Response({"message":"Create Succesfull", "data": request.data})
		else:
			return Response(
				serializer.errors,
				status.HTTP_400_BAD_REQUEST)

	def put(self, request, pid):
		obj = models.Profile.objects.get(id=pid)
		serializer = self.serializer_class(data=request.data, instance=obj)
		if serializer.is_valid():
			serializer.save()
			return Response({'message':"Update Succesfull", "data": request.data})
		else:
			return Response(
				serializer.errors,
				status.HTTP_400_BAD_REQUEST)
		
	def patch(self, request):
		return Response({'message': 'PATCH'})

	def delete(self, request, pid):
		obj = models.Profile.objects.get(id=pid)
		obj.delete()
		return Response({'message':"Delete Succesfull"})
		# serializer = self.serializer_class(data=request.data, instance=obj)
		# if serializer.is_valid():
		# 	serializer.delete()
		# 	return Response({'message':"Delete Succesfull"})
		# else:
		# 	return Response(
		# 		serializer.errors,
		# 		status.HTTP_400_BAD_REQUEST)