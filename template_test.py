import unittest
from template import Template

class TemplateTest(unittest.TestCase):

    def setUp(self):
        self.template = Template("Hello, ${one}, ${two}, ${three}")
        self.template.set("one", "1")
        self.template.set("two", "2")
        self.template.set("three", "3")

    def test_evaluate_multiple_variables(self):
        self.assertEqual("Hello, 1, 2, 3", self.template.evaluate())

    def test_evaluate_unknown_variable_are_ignored(self):
        self.template.set("whatever", "hiiiii")
        self.assertEqual("Hello, 1, 2, 3", self.template.evaluate())

    def test_evaluate_missing_value_raise_exception(self):
        with self.assertRaisesRegex(AttributeError, "No value for \${foo}"):
            Template("${foo}").evaluate()