# -*- encoding: utf-8 -*-
import inspect
import pickle
import pytest
from abjad.tools import documentationtools


_classes_to_fix = ()

classes = documentationtools.list_all_classes('consort')
@pytest.mark.parametrize('class_', classes)
def test_consort___pickle___01(class_):
    r'''All storage-formattable classes are pickable.
    '''

    if ('_storage_format_specification' not in dir(class_) or
        '_get_format_specification' not in dir(class_)):
        return
    if inspect.isabstract(class_):
        return
    if class_ in _classes_to_fix:
        return
    instance_one = class_()
    pickle_string = pickle.dumps(instance_one)
    instance_two = pickle.loads(pickle_string)
    instance_one_format = format(instance_one, 'storage')
    instance_two_format = format(instance_two, 'storage')
    assert instance_one_format == instance_two_format
