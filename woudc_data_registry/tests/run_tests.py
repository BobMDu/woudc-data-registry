# =================================================================
#
# Terms and Conditions of Use
#
# Unless otherwise noted, computer program source code of this
# distribution # is covered under Crown Copyright, Government of
# Canada, and is distributed under the MIT License.
#
# The Canada wordmark and related graphics associated with this
# distribution are protected under trademark law and copyright law.
# No permission is granted to use them outside the parameters of
# the Government of Canada's corporate identity program. For
# more information, see
# http://www.tbs-sct.gc.ca/fip-pcim/index-eng.asp
#
# Copyright title to all 3rd party software distributed with this
# software is held by the respective copyright holders as noted in
# those files. Users are asked to read the 3rd Party Licenses
# referenced with those assets.
#
# Copyright (c) 2017 Government of Canada
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

import os
import unittest

from woudc_data_registry import util


def resolve_test_data_path(test_data_file):
    """
    helper function to ensure filepath is valid
    for different testing context (setuptools, directly, etc.)
    """

    if os.path.exists(test_data_file):
        return test_data_file
    else:
        path = os.path.join('woudc_data_registry', 'tests', test_data_file)
        if os.path.exists(path):
            return path


class DataRegistryTest(unittest.TestCase):
    """Test suite for data registry"""

    def test_test(self):
        """stub"""

        self.assertTrue(1 == 1, 'Expected equality')


class UtilTest(unittest.TestCase):
    """Test suite for util.py"""

    def test_read_file(self):
        """test reading files"""

        contents = util.read_file(resolve_test_data_path(
            'data/20040709.ECC.2Z.2ZL1.NOAA-CMDL.csv'))

        self.assertIsInstance(contents, str)

        with self.assertRaises(UnicodeDecodeError):
            contents = util.read_file(resolve_test_data_path(
                'data/wmo_acronym_vertical_sm.jpg'))

    def test_is_test_file(self):
        """test if file is text-based"""

        res = resolve_test_data_path('data/20040709.ECC.2Z.2ZL1.NOAA-CMDL.csv')
        self.assertTrue(res, True)

        res = resolve_test_data_path('data/wmo_acronym_vertical_sm.jpg')
        self.assertTrue(res, False)

    def test_point2ewkt(self):
        """test point WKT creation"""

        point = util.point2ewkt(-75, 45)
        self.assertEqual(point, 'SRID=4326;POINT(-75 45)')

        point = util.point2ewkt(-75, 45, 333)
        self.assertEqual(point, 'SRID=4326;POINTZ(-75 45 333)')

        point = util.point2ewkt(-75, 45, srid=4269)
        self.assertEqual(point, 'SRID=4269;POINT(-75 45)')

        point = util.point2ewkt(-75, 45, 111, srid=4269)
        self.assertEqual(point, 'SRID=4269;POINTZ(-75 45 111)')

    def test_str2bool(self):
        """test boolean evaluation"""

        self.assertEqual(util.str2bool(True), True)
        self.assertEqual(util.str2bool(False), False)
        self.assertEqual(util.str2bool('1'), True)
        self.assertEqual(util.str2bool('0'), False)
        self.assertEqual(util.str2bool('true'), True)
        self.assertEqual(util.str2bool('false'), False)


if __name__ == '__main__':
    unittest.main()