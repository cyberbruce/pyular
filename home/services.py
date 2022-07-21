import re
from functools import cache

from django.urls import is_valid_path

class RegIt:
    def __init__(self, *, expression, sample):
      self.expression = expression
      self.sample = sample
      
    @cache
    def pattern(self):
      return re.compile(self.expression)

    def is_valid(self):
        try:
            self.pattern()  
            return True
        except:
          return False


    def matched_items(self):
        if not self.is_valid():
          return []


        return self.build_matches()


    def build_matches(self):
        unamed_matchs = []
        named_matches = []
        for match in self.pattern().finditer(self.sample):
            for named_match in match.groupdict():
              result

        return result
