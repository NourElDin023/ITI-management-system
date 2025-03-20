from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from trainee_app.models import Trainee
from .serializers import TraineeSerializer
from rest_framework import generics
from trainee_app.models import Trainee
from .serializers import TraineeSerializer
from course_app.models import Course
from api.serializers import CourseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from course_app.models import Course
from .serializers import CourseSerializer
from rest_framework.generics import RetrieveUpdateAPIView

class ListTrainee(APIView):
    def get(self, request):
        trainees = Trainee.objects.all()
        serializer = TraineeSerializer(trainees, many=True)
        return Response(serializer.data)


class AddTrainee(APIView):
    def post(self, request):
        serializer = TraineeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateTrainee(RetrieveUpdateAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer


class DeleteTrainee(generics.DestroyAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer


from rest_framework.decorators import api_view


@api_view(["PUT"])
def course_update(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CourseSerializer(course, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import viewsets


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


@api_view(['PUT'])
def CourseUpdate(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CourseSerializer(course, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)