import inspect
from operator import itemgetter as ig

from future.utils import lfilter

class ClassTool:
    @classmethod
    def cls2name(cls, clazz): return clazz.__name__

    @classmethod
    def cls2name_lower(cls, clazz): return cls.cls2name(clazz).lower()

class ModuleTool:
    @classmethod
    def module2class_list(cls, module):
        m_list = inspect.getmembers(module, inspect.isclass)
        clazz_list = lfilter(lambda x:x.__module__ == module.__name__, map(ig(1), m_list))
        return clazz_list

    @classmethod
    def x2module(cls, x):
        return x.__module__


cls2name = ClassTool.cls2name
module2class_list = ModuleTool.module2class_list