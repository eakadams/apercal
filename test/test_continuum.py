import unittest
from os import path

from apercal.modules.continuum import continuum

here = path.dirname(__file__)


class TestTransfer(unittest.TestCase):

    def test_prepare(self):
        p = continuum(path.join(here, 'test.cfg'))
        p.apercaldir = path.join(here, '../apercal')
        p.show(showall=True)
        p.go()
