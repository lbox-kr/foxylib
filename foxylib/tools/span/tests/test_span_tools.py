import logging
from unittest import TestCase

import pytest

from foxylib.tools.log.logger_tool import FoxylibLogger
from foxylib.tools.span.span_tool import SpanTool


class TestSpanTool(TestCase):
    @classmethod
    def setUpClass(cls):
        FoxylibLogger.attach_stderr2loggers(logging.DEBUG)

    @pytest.mark.skip(reason="not supported any more")
    def test_01(self):
        span_list = [(0,3), (6,8), (18,19), (24,27), (28,29),(30,31),(32,33), (49,50)]
        hyp = SpanTool.span_list_limit2span_best(span_list, 20)
        ref = (30,50)

        self.assertEqual(hyp, ref)
