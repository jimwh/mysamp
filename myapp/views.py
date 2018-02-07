import logging
import django_filters.rest_framework

from django.contrib.auth.models import User, Group
from rest_framework import generics, permissions, viewsets

from myapp.serializers import UserSerializer, GroupSerializer

from myapp.models import University, Student
from myapp.serializers import UniversitySerializer, StudentSerializer
from myapp.permissions import IsOwnerOrReadOnly


logger = logging.getLogger(__name__)


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

    def perform_create(self, serializer):
        # serializer.save(owner=self.request.user)

        # filter the Group model for current logged in user instance
        query_set = Group.objects.filter(user=self.request.user)

        # print to console for debug/checking
        for g in query_set:
            # this should print all group names for the user
            print(g.name)  # or id or whatever Group field that you want to display
        serializer.save(owner=1)


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)

    def perform_create(self, serializer):

        # filter the Group model for current logged in user instance
        query_set = Group.objects.filter(user=self.request.user)

        # print to console for debug/checking
        g = None
        for g in query_set:
            # this should print all group names for the user
            print(g.name)  # or id or whatever Group field that you want to display
            logger.info("group name=%s", g.name)
        if g is None:
            print("dude...................add group first")
        serializer.save(owner=g)

        # serializer.save(owner=self.request.user)
        # serializer.save(owner=self.request.group)


class UniversityFilter(django_filters.FilterSet):
    class Meta:
        model = University
        fields = ['name', 'last_mod_date']


    #def university_list(request):
    #    filter = UniversityFilter(request.GET, queryset=University.objects.all())
    #    return render(request, 'my_app/template.html', {'filter': filter})
    #