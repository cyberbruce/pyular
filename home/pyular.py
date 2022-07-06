import re
import string
from django.utils.safestring import mark_safe

class PyularParse:
    def __init__(self, expression, sample):
        self.expression = expression
        self.sample = sample
        self.pattern = re.compile(self.expression)
        
        
    def __str__(self):
        return self.expression
     
    
    def output(self):
        string_builder = []
        index = 0 
        for m in self.matches():  
            if index < m.start():
                string_builder.append(m.string[index:m.start()])

            seg = m.string[m.start():m.end()]
            string_builder.append(mark_safe("<div class='d-inline-block bg-warning'>"))
            string_builder.append(seg)  
            string_builder.append(mark_safe("</div>"))
            index = m.end()
            
        if index < len(self.sample):
            string_builder.append(self.sample[index:])

        return string_builder

    def matches(self):
        return self.pattern.finditer(self.sample)

    def match(self):         
        return re.match(self.expression, self.sample)

    def single_group(self):
        res = self.match()
        if res and res.group():
            return res.group()
        else:
            return ''
        
  

    def groups(self):
      #  breakpoint()
        res = self.match()        
        #breakpoint()
        if not res:
            return '---'
        if res.groupdict():            
            return ('groupdict', res.groupdict())
        elif res.groups():
            return ('groups', res.groups())
        else:
            return []
        
    def groups_formatted(self):
        res = self.match()       
        
        if (grpdict := res.groupdict()):           
            return {
                'name': '#groupdict',
                'items': grpdict.items()
            }
        elif (grps := res.groups()):            
            if grps:
                return {
                    'name': 'Groups',
                    'items': [('', x) for x in grps]
                }
                
        return {
            'name': 'Not defined',
            'items': []
        }

    def splits(self):
        re_result = re.split(
            self.expression,
            self.sample
        )

        if re_result:
            return re_result
        else:
            return []
