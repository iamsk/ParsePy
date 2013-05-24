#-*- coding: utf-8 -*-
__author__ = 'iamsk'
__email__ = 'iamsk.info@gmail.com'

import unittest
import ParsePy
from config import APPLICATION_ID, REST_API_KEY


class TestParsePush(unittest.TestCase):
    def test_push(self):
        noti = ParsePy.ParseNotification(APPLICATION_ID, REST_API_KEY)
        channel = 'pm_c55d6c118b9141f20776588b0308e586'
        data = {'type': 'thread', 'alert': 'test for sending to yourself', 'badge': 1, 'url': ''}
        noti.push(channel=channel, type='ios', data=data)

if __name__ == "__main__":
    testsuite = unittest.TestLoader().loadTestsFromTestCase(TestParsePush)
    unittest.TextTestRunner(verbosity=2).run(testsuite)
