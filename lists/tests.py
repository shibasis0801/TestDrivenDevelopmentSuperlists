from django.test import TestCase

# Create your tests here.

class SmokeTest(TestCase):

    def tests_bad_maths(self):
        self.assertEqual(2+3, 2)