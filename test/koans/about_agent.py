#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
from lib.core.agent import agent

class AboutAgent(Koan):

    def test_assert_agent_name(self):
        """
        test sqlmap main function
        """
        self.assertEqual("Agent", agent.__class__.__name__)

    def test_assert_agent_pyloadDirect(self):
        """
        test payloadDirect(self, query)
        """
