from django.contrib.auth.models import User, Group
from rest_framework import serializers

from samapp.myapp.models import University, Student


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

    class JSONAPIMeta:
        included_resources = ['groups']


# you need to have 'url' in the fields
class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('url', 'name', 'last_mod_date')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('url', 'first_name', 'last_name', 'university')

    # Uncomment this and the locations will be included by default.
    # otherwise '?include=locations' must be added to the URL.
    # class JSONAPIMeta:
    #    included_resources = ['university']

