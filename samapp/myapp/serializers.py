from django.contrib.auth.models import User, Group
from rest_framework import serializers

from samapp.myapp.models import University, Student


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    included_serializers = {
        'groups': GroupSerializer,
    }

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

    class JSONAPIMeta:
        included_resources = ['student']


class StudentSerializer(serializers.ModelSerializer):
    included_serializers = {
        'universities': UniversitySerializer
    }

    class Meta:
        model = Student
        fields = ('url', 'first_name', 'last_name', 'university')

    class JSONAPIMeta:
        included_resources = ['universities']

