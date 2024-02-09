from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serialize import task_serializer

from django.contrib.auth import get_user_model
User = get_user_model()
users = User.objects.all()


def tasks_list(request):
    tasks = task.objects.all()
    return render(request, 'task/task_details.html', {'task': tasks})


def task_actions(request):
    tasks = task.objects.all()
    return render(request, 'task/tasks_actions.html', {'task': tasks})


@api_view(['GET','POST'])
def create_action(request,format=None):
    if request.method == 'GET':
        tasks = task.objects.all()
        serialized_task = task_serializer(tasks, many=True)
        print("serialized data :",serialized_task.data[0]['member'])
        return Response(serialized_task.data, status=status.HTTP_200_OK)
    else:
        if request.method == "POST":
            serialized_task = task_serializer(data=request.data)
            if serialized_task.is_valid():
                serialized_task.save()
                return Response(serialized_task.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serialized_task.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
def update_action(request, id, format=None):
    if request.method == 'GET':
        tasks = task.objects.get(pk=id)
        serialized_task = task_serializer(tasks)
        return Response(serialized_task.data, status=status.HTTP_200_OK)
    else:
        try:
            current_task = task.objects.get(pk=id)
        except task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serialized_task = task_serializer(current_task, data=request.data)
            if serialized_task.is_valid():
                serialized_task.save()
                return Response(serialized_task.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serialized_task.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_action(request, id, format=None):
    try:
        current_task = task.objects.get(pk=id)
    except task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        current_task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


