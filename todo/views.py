from .models import ToDo
from .serializers import ToDoSerializer
from rest_framework.generics import RetrieveAPIView, ListAPIView


class TodoListView(ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class TodoDetailView(RetrieveAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
