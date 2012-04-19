#-*- coding: utf-8 -*-
__author__ = 'iamsk'
__email__ = 'iamsk.info@gmail.com'

import unittest
import ParsePy
from config import APPLICATION_ID, REST_API_KEY

ParsePy.APPLICATION_ID = APPLICATION_ID
ParsePy.REST_API_KEY = REST_API_KEY

class TestParseObject(unittest.TestCase):
    def test_save(self):
        gameScore = ParsePy.ParseObject("GameScore")
        gameScore.score = 112358
        gameScore.playerName = "S K"
        gameScore.cheatMode = False
        gameScore.save()
        self.assertEqual(gameScore.score, 112358)
        self.assertEqual(type(gameScore.objectId()), unicode)

    def test_save(self):
        noti = ParsePy.ParseNotification()
        noti.push()

if __name__ == "__main__":
    testsuite = unittest.TestLoader().loadTestsFromTestCase(TestParseObject)
    unittest.TextTestRunner(verbosity=2).run(testsuite)
