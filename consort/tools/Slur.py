import abjad


class Slur(abjad.Slur):

    def _attachment_test(self, component):
        return isinstance(component, abjad.Leaf)

    def _attachment_test_all(self, component_expression):
        return True
