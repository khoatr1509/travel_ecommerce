from django.test import TestCase

# Create your tests here.
class RunTest(TestCase):
    def test1(self):
        self.assertIs(1,1)