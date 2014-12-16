# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2014, Lars Asplund lars.anders.asplund@gmail.com

import unittest
from os.path import abspath, join, dirname
from vunit.ui import VUnit
from common import has_modelsim

@unittest.skipUnless(has_modelsim(), 'Requires modelsim')
class TestArray(unittest.TestCase):
    def run_sim(self, vhdl_standard):
        output_path = join(dirname(abspath(__file__)), 'array_out')
        src_path = join(dirname(abspath(__file__)), '..', 'vhdl', 'array')

        vu = VUnit(clean=True,
                   output_path=output_path,
                   vhdl_standard=vhdl_standard)

        vu.add_library("lib")
        vu.add_array_util("lib")
        vu.add_source_files(join(src_path, "test", "*.vhd"), "lib")

        try:
            vu.main()
        except SystemExit as e:
            self.assertEqual(e.code, 0)

    def test_array_vhdl_2008(self):
        self.run_sim('2008')
