import re


class PyularParse:
    def __init__(self, expression, sample):
        self.expression = expression
        self.sample = sample

    def __str__(self):
        return self.expression

    def match(self):         
        return re.match(self.expression, self.sample)

    def groups(self):
        res = self.match()        
        if res:            
            return res.groupdict()
        else:
            return []

    def splits(self):
        re_result = re.split(
            self.expression,
            self.sample
        )

        if re_result:
            return re_result
        else:
            return []
