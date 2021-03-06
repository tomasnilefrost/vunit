-- This Source Code Form is subject to the terms of the Mozilla Public
-- License, v. 2.0. If a copy of the MPL was not distributed with this file,
-- You can obtain one at http://mozilla.org/MPL/2.0/.
--
-- Copyright (c) 2014, Lars Asplund lars.anders.asplund@gmail.com

entity tb_two_architectures is
end entity;

architecture pass of tb_two_architectures is
  signal vunit_finished : boolean := false;
begin
  test_runner : process
  begin
    vunit_finished <= true;
    wait;
  end process;
end architecture;

architecture fail of tb_two_architectures is
  signal vunit_finished : boolean := false;
begin
  test_runner : process
  begin
    assert false;
    vunit_finished <= true;
    wait;
  end process;
end architecture;
