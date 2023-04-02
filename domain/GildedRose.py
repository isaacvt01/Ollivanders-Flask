from domain.AgedBrie import AgedBrie
from domain.Backstage import Backstage
from domain.ConjuredItem import ConjuredItem
from domain.NormalItem import NormalItem
from domain.Sulfuras import Sulfuras


class GildedRose():

    # Este es el inventario

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # lo que hacemos aquí es llamar a item, que contendrá una clase con su propio método update_quality
            # lo que significa que cada clase llamará a un método que se llama igual, pero que varía su comportamiento
            # polimorfismo.
            item.update_quality()

    def update_item_inventory(self, _id, name, sell_in, quality):

        for item in self.items:
            if item.get_id() == _id:
                item.set_name(name)
                item.change_sell_in(sell_in)
                item.change_quality(quality)

    def create_item(self, _id, name, sell_in, quality, type):
        item_types = {'normal': NormalItem, 'conjured': ConjuredItem, 'aged brie': AgedBrie, 'sulfuras': Sulfuras,
                      'backstage': Backstage}
        item_class = item_types.get(type.lower())
        try:
            item = item_class(_id, name, sell_in, quality)
            self.items.append(item)
        except:
            Exception("Error creating item")

    def __repr__(self) -> str:
        output = ''
        for item in self.items:
            output += str(item) + '\n'
        return output

    def delete_item_inventory(self, _id):
        for item in self.items:
            if item.get_id() == _id:
                self.items.remove(item)
