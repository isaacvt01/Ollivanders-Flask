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


def test_update_item(inventario):
    inventario.update_item_inventory(1, "actualizado", 5, 10)
    assert inventario.items[0].name == "actualizado"
    assert inventario.items[0].sell_in == 5
    assert inventario.items[0].quality == 10
    inventario.update_item_inventory(2, "actualizado2", 5, 10)
    assert inventario.items[1].name == "actualizado2"
    assert inventario.items[1].sell_in == 5
    assert inventario.items[1].quality == 10
