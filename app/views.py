from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.serializers import TaskSerializer
from app.models import Task


@api_view(['GET'])
def api_over_view(requeset):
	api_urls = {
		'List': '/task-list/',
		'Detail': '/task-detail/<str:pk>/',
		'Create': '/task-create/',
		'Update': '/task-update/<str:pk>/',
		'Delete': '/task-delete/<str:pk>/',
	}
	return Response(api_urls)


@api_view(['GET'])
def task_list(request):
	task_obj_list = Task.objects.all()
	serialized_task_obj_list = TaskSerializer(task_obj_list, many=True)
	return Response(data=serialized_task_obj_list.data)	


@api_view(['GET'])
def task_detail(request, pk):
	task_obj = Task.objects.get(id=pk)
	serialized_task_obj = TaskSerializer(task_obj, many=False)
	return Response(serialized_task_obj.data)


@api_view(['POST'])
def task_create(request):
	serializer = TaskSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['POST'])
def task_update(request, pk):
	task_obj = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task_obj, data=request.data)

	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['GET'])
def task_delete(request, pk):
	task_obj = Task.objects.get(id=pk)
	task_obj.delete()
	return Response({"message": "success", "status": "item_deleted"})