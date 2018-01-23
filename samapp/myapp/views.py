import django_filters.rest_framework

from django.contrib.auth.models import User, Group
from rest_framework import generics, permissions, viewsets

from samapp.myapp.serializers import UserSerializer, GroupSerializer

from samapp.myapp.models import University, Student
from samapp.myapp.serializers import UniversitySerializer, StudentSerializer
from samapp.myapp.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


class UniversityFilter(django_filters.FilterSet):
    class Meta:
        model = University
        fields = ['name', 'last_mod_date']

    #def university_list(request):
    #    filter = UniversityFilter(request.GET, queryset=University.objects.all())
    #    return render(request, 'my_app/template.html', {'filter': filter})
    #