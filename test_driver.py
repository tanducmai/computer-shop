#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
# |
# |        File:  test_driver.py
# |      Author:  Tan Duc Mai
# |          Id:  517925
# | Description:  A pytest for the PartList class.
# | This is my own work as defined by the Academic Integrity policy.
# |
# ----------------------------------------------------------------------------

# ------------------------------- Module Import -------------------------------
import pytest
from computer_shop import *


# ---------------------------- Function Definitions ---------------------------
@pytest.fixture
def part_list():
    shop = ComputerPartShop(CommandPrompt())  # Construct object
    cmd = shop.get_cmd()
    part_list = cmd.get_part_list()
    return part_list

def test_len(part_list):
    # Safe case
    assert len(part_list) == 24

    # Dangerous case
    with pytest.raises(AssertionError):
        assert len(part_list) == 0

def test_get_part_using_name(part_list):
    # Safe cases
    assert isinstance(part_list.get_part_using_name('Toshiba P300'), Storage)
    assert isinstance(part_list.get_part_using_name('AMD Ryzen 5'), CPU)

    # Dangerous cases
    with pytest.raises(icontract.errors.ViolationError):
        part_list.get_part_using_name('')
        part_list.get_part_using_name(2)

    with pytest.raises(AssertionError):
        assert isinstance(part_list.get_part_using_name('Toshiba'), Storage)
        assert isinstance(part_list.get_part_using_name('AMD Ryzen 5'), Memory)

def test_get_part_using_postion(part_list):
    # Safe cases
    assert isinstance(part_list.get_part_using_position(23), Storage)
    assert isinstance(part_list.get_part_using_position(2), CPU)

    # Dangerous cases
    with pytest.raises(icontract.errors.ViolationError):
        part_list.get_part_using_position('')
        part_list.get_part_using_position(2.0)

    with pytest.raises(AssertionError):
        assert isinstance(part_list.get_part_using_position(3), GraphicsCard)
        assert isinstance(part_list.get_part_using_position(25), Memory)

def test_remove_part_using_name(part_list):
    # Safe cases
    part_list.remove_part_using_name('WD Red')
    assert len(part_list) == 23

    part_list.remove_part_using_name('AMD Ryzen 3')
    assert len(part_list) == 22

    # Dangerous cases
    with pytest.raises(icontract.errors.ViolationError):
        part_list.remove_part_using_name('')

    with pytest.raises(AssertionError):
        part_list.remove_part_using_name('WD')
        assert len(part_list) == 21

def test_remove_part_using_postion(part_list):
    # Safe cases
    part_list.remove_part_using_position(12)
    assert len(part_list) == 23

    part_list.remove_part_using_position(-12)
    assert len(part_list) == 22

    # Dangerous cases
    with pytest.raises(icontract.errors.ViolationError):
        part_list.remove_part_using_position('')
        part_list.remove_part_using_position(12.0)

    with pytest.raises(AssertionError):
        part_list.remove_part_using_position(25)
        assert len(part_list) == 21
