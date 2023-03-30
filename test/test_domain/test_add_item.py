from domain.GildedRose import GildedRose
import pytest

def test_add_normal_item():
    items = []
    inventario = GildedRose(items)
    inventario.create_item(1, "item1", 10, 20, "normal")
    assert len(inventario.items) == 1
    assert inventario.items[0].get_id() == 1
    assert inventario.items[0].__class__.__name__ == "NormalItem"

def test_add_conjured():
    items = []
    inventario = GildedRose(items)
    inventario.create_item(2, "item2", 10, 20, "conjured")
    assert len(inventario.items) == 1
    assert inventario.items[0].get_id() == 2
    assert inventario.items[0].__class__.__name__ == "ConjuredItem"


def test_add_sulfuras():
    items = []
    inventario = GildedRose(items)
    inventario.create_item(3, "item3", 10, 20, "sulfuras")
    assert len(inventario.items) == 1
    assert inventario.items[0].__class__.__name__ == "Sulfuras"

def test_add_aged_brie():
    items = []
    inventario = GildedRose(items)
    inventario.create_item(4, "item4", 10, 20, "aged brie")
    assert len(inventario.items) == 1
    assert inventario.items[0].get_id() == 4
    assert inventario.items[0].__class__.__name__ == "AgedBrie"

def test_add_backstage():
    items = []
    inventario = GildedRose(items)
    inventario.create_item(5, "item5", 10, 20, "backstage")
    assert len(inventario.items) == 1
    assert inventario.items[0].__class__.__name__ == "Backstage"