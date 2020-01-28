import os
import re
from functools import lru_cache

from future.utils import lmap

from foxylib.tools.entity.enrtity_tool import Entity
from foxylib.tools.function.function_tool import FunctionTool
from foxylib.tools.regex.regex_tool import RegexTool

FILE_PATH = os.path.realpath(__file__)
FILE_DIR = os.path.dirname(FILE_PATH)

class CardinalEntity:

    @classmethod
    @FunctionTool.wrapper2wraps_applied(lru_cache(maxsize=2))
    def pattern(cls):
        rstr_multidigit = r"[1-9][0-9]+"
        rstr_onedigit = r"[0-9]"
        rstr_number = RegexTool.rstr_list2or([rstr_multidigit,rstr_onedigit])

        return re.compile(rstr_number, re.I)

    @classmethod
    def m2entity(cls, m):
        text = m.group()
        return {Entity.F.SPAN: m.span(),
                Entity.F.TEXT: text,
                Entity.F.VALUE: int(text),
                }


    @classmethod
    def str2entity_list(cls, str_in):
        p = cls.pattern()

        m_list = list(p.finditer(str_in))
        entity_list = lmap(cls.m2entity, m_list)
        return entity_list

