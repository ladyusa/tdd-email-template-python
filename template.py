import re

class Template:

    def __init__(self, template_text):
        self.template_text = template_text
        self.variables = {}  # empty dictionary

    def set(self, variable, value):
        self.variables[variable] = value

    def evaluate(self):
        result = self.replace_variables()
        self.check_for_missing_value(result)    
        return result

    def replace_variables(self):
        result = self.template_text
        for variable, value in self.variables.items():
            regex = "${" + variable + "}"
            result = result.replace(regex, value)
        return result

    def check_for_missing_value(self, result):
        reg = re.compile(".*\${.+}.*")
        m = reg.match(result)
        if m:
            raise AttributeError("No value for " + m.group())