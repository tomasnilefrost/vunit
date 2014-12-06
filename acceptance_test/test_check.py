# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2014, Lars Asplund lars.anders.asplund@gmail.com

import unittest
from os.path import abspath, join, dirname, basename
from glob import glob
from vunit.ui import VUnit
from common import has_modelsim

@unittest.skipUnless(has_modelsim(), 'Requires modelsim')
class TestCheck(unittest.TestCase):
    def run_sim(self, vhdl_standard):
        output_path = join(dirname(abspath(__file__)), 'check_out')
        vhdl_path = join(dirname(abspath(__file__)), '..', 'vhdl', 'check', 'test')

        ui = VUnit(clean=True,
                   output_path=output_path,
                   vhdl_standard=vhdl_standard,
                   compile_builtins=False)
        ui.enable_check_preprocessing()
            
        ui.add_builtins('vunit_lib', mock_log=True)
        ui.add_library(r'lib') 
        ui.add_source_files(join(vhdl_path, "test_support.vhd"), 'lib')
        if vhdl_standard in ('2002', '2008'):
            ui.add_source_files(join(vhdl_path, "test_count.vhd"), 'lib')
            ui.add_source_files(join(vhdl_path, "test_types.vhd"), 'lib')
        elif vhdl_standard == '93':
            ui.add_source_files(join(vhdl_path, "test_count93.vhd"), 'lib')

        if vhdl_standard == '2008':
            ui.add_source_files(join(vhdl_path, "tb_check_relation.vhd"), 'lib')
        else:
            ui.add_source_files(join(vhdl_path, "tb_check_relation93_2002.vhd"), 'lib')

        for file_name in glob(join(vhdl_path, "tb_*.vhd")):
            if basename(file_name) == "tb_check_relation.vhd":
                continue
            ui.add_source_files(file_name, 'lib')

        try:
            ui.main()
        except SystemExit as e:            
            self.assertEqual(e.code, 0)

    def test_check_vhdl_93(self):
        self.run_sim('93')

    def test_check_vhdl_2002(self):
        self.run_sim('2002')

    def test_check_vhdl_2008(self):
        self.run_sim('2008')

