from rest_framework import viewsets
from .models import ToDo
from .serializers import ToDoSerializer


class ToDoViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()


# from rest_framework.generics import (
#     RetrieveAPIView,
#     ListAPIView,
#     CreateAPIView,
#     DestroyAPIView,
#     UpdateAPIView
# )

# class TodoCreateView(CreateAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer
#
#
# class TodoListView(ListAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer
#
#
# class TodoDetailView(RetrieveAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer
#
#
# class TodoUpdateView(UpdateAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer
#
#
# class TodoDeleteView(DestroyAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer

