# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2014, Lars Asplund lars.anders.asplund@gmail.com

# Make vunit python module importable
from os.path import join, dirname, basename
import sys
path_to_vunit = join(dirname(__file__), '..', '..')
sys.path.append(path_to_vunit)
#  -------

from vunit import VUnit

ui = VUnit.from_argv()
ui.enable_check_preprocessing()
lib = ui.add_library("lib")
lib.add_source_files(join(dirname(__file__), "check_example.vhd"))
ui.main()
