-- This Source Code Form is subject to the terms of the Mozilla Public
-- License, v. 2.0. If a copy of the MPL was not distributed with this file,
-- You can obtain one at http://mozilla.org/MPL/2.0/.
--
-- Copyright (c) 2015, Lars Asplund lars.anders.asplund@gmail.com

entity tb_magic_paths is
  generic (
    tb_path : string;
    output_path : string);
end entity;

architecture vunit_test_bench of tb_magic_paths is
  signal vunit_finished : boolean := false;
begin
  test_runner : process

    procedure check_equal(got, expected : string) is
    begin
      assert got = expected report "Got '" & got & "' expected '" & expected & "'";
    end procedure;

    procedure check_has_suffix(value : string; suffix : string) is
    begin
      check_equal(value(value'length+1-suffix'length to value'length), suffix);
    end procedure;
  begin
    check_has_suffix(tb_path, "acceptance_test/vhdl/");
    check_has_suffix(output_path, "acceptance_test/end to end out/tests/lib.tb_magic_paths/");
    vunit_finished <= true;
    wait;
  end process;
end architecture;
