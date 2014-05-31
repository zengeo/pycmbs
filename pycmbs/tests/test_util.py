# -*- coding: UTF-8 -*-
from unittest import TestCase

from nose.tools import assert_raises
from pycmbs.utils import Dict2TXT
import os
import tempfile
import numpy as np


class TestStatistic(TestCase):

    def setUp(self):
        d = dict([('a', 5), ('b', 10), ('c', {'x':1,'y': {'AA' : 77, 'BB' : 'test'}})])
        #~ d.update({'c' : {'x' : 3, 'y': 7}})
        self.x = d


    def test_init_false(self):
        x = 'nothing'
        with self.assertRaises(ValueError):
            D = Dict2TXT(x)

    def test_conversion(self):
        D = Dict2TXT(self.x)
        fname = tempfile.mktemp()
        h, s = D.convert(filename=fname, mode='w')
        self.assertTrue(os.path.exists(fname))

        def header_check(h1):
            self.assertEqual(h1[0], 'a')
            self.assertEqual(h1[1], 'b')
            self.assertEqual(h1[2], 'c:x')
            self.assertEqual(h1[3], 'y:AA')
            self.assertEqual(h1[4], 'y:BB')

        def value_check(s1):
            self.assertEqual(s1[0],'5')
            self.assertEqual(s1[1],'10')
            self.assertEqual(s1[2],'1')
            self.assertEqual(s1[3],'77')
            self.assertEqual(s1[4],'test')

        header_check(h.split('\t'))
        value_check(s.split('\t'))

        # read data from file
        d = np.loadtxt(fname, dtype='str')
        header_check(d[0])
        value_check(d[1])


