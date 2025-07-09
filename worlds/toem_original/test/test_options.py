from typing import Any

from .bases import ToemTestBase


class TestDefault(ToemTestBase):
    pass


class TestMin(ToemTestBase):
    options: dict[str, Any] = {
        "include_basto": 0,
        "include_items": 0,
        "include_casettes": 0,
        "include_achievements": 0,
    }


class TestMax(ToemTestBase):
    options: dict[str, Any] = {
        "include_basto": 1,
        "include_items": 1,
        "include_casettes": 1,
        "include_achievements": 1,
    }
