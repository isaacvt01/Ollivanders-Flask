from domain.GildedRose import GildedRose
import pytest


@pytest.fixture
def inventario():
    inventario = GildedRose([])
    inventario.create_item(1, "item1", 10, 20, "normal")
    inventario.create_item(2, "item2", 10, 20, "conjured")
    inventario.create_item(3, "item3", 10, 80, "sulfuras")
    inventario.create_item(4, "item4", 10, 20, "aged brie")
    inventario.create_item(5, "item5", 10, 20, "backstage")
    return inventario



def test_update_quality(inventario):
    inventario.update_quality()
    assert inventario.items[0].quality == 19
    assert inventario.items[1].quality == 18
    assert inventario.items[2].quality == 80
    assert inventario.items[3].quality == 21
    assert inventario.items[4].quality == 22
    assert inventario.items[0].sell_in == 9
    assert inventario.items[1].sell_in == 9
    assert inventario.items[2].sell_in == 10
    assert inventario.items[3].sell_in == 9
    assert inventario.items[4].sell_in == 9

