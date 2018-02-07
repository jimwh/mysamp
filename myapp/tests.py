from django.test import TestCase

from datetime import datetime
from myapp.models import University


# ./manage.py test samapp.myapp.tests.UniversityTestCase
# ./manage.py test samapp.myapp.tests.UniversityTestCase.test_str
#
class UniversityTestCase(TestCase):

    def setUp(self):
        University.objects.create(name='NYU', last_mod_date=datetime.now())

    def test_str(self):
        last_mod_date = datetime.now()
        us = University.objects.all()
        cu = University.objects.get(name='NYU', last_mod_date=last_mod_date)
        print('id=%s,name=%s,last_mod_date=%s' % (cu.id, cu.name, cu.last_mod_date))
        self.assertEquals(cu.name, 'NYU')

