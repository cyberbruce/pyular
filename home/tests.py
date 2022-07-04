from django.test import TestCase
from .pyular import PyularParse


# Create your tests here.
class TestPyular(TestCase):
  
  def test_simple_matches(self):
      subject = PyularParse(r"(?P<name>l)(o)", "hello there jello")
      print("Starting!")
      for match in subject.matches():
        print(match)
        print(match.groups())
        print(match.groupdict())
        