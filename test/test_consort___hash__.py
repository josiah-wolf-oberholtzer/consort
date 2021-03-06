import abjad
import inspect
import pytest
from abjad.tools import documentationtools


classes = documentationtools.list_all_classes('consort')
@pytest.mark.parametrize('class_', classes)
def test_consort___hash___01(class_):
    r'''All concrete classes with __hash__ can hash.
    '''

    if not inspect.isabstract(class_):
        if getattr(class_, '__hash__', None):
            instance = class_()
            value = hash(instance)
            assert isinstance(value, int)
