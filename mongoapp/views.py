from django.shortcuts import render
from rest_framework_mongoengine import viewsets
from rest_framework.views import APIView 
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status

from mongoapp import serializers, models 
# Create your views here.

def index(req):
	return render(req, 'index.html')
class ProfileViewSet(viewsets.ModelViewSet):

	# lookup_field = 'id'
	serializer_class = serializers.ProfileSerializer
	queryset = models.Profile.objects.all()
	search_field = ( 'name')
	# def list(self, req):
	# 	queryset = models.Profile.objects.all()	
	# 	return Response(queryset)
class ProfileApiView(APIView):
	# renderer_classes = [TemplateHTMLRenderer]
	# template_name = 'index.html'
	serializer_class = serializers.ProfileSerializer
	search_field = ('id', 'name')
	def get(self, request, format=None):
		# obj = models.Profile.objects.get(i)
		obj = models.Profile.objects.all()
		serializer = serializers.ProfileSerializer(obj, many=True)
		return Response(serializer.data)
		# queryset = models.Profile.objects.all()
		# return Response({'profiles': queryset})

	def post(self, request):
		# template_name = 'index.html'
		serializer = self.serializer_class(data=request.data)
		# print("serializer name", serializer.name)
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