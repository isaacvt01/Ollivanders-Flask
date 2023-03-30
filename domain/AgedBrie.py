from domain.Item import Item
from domain.NormalItem import NormalItem


class AgedBrie(NormalItem):

    def __init__(self, _id, name, sell_in, quality):
        NormalItem.__init__(self, _id, name, sell_in, quality)  # Utilizamos el constructor de Item.

    def get_id(self):
        NormalItem.get_id(self)

    def set_name(self, name):
        NormalItem.set_name(self, name)

    def change_sell_in(self, sell_in):
        NormalItem.change_sell_in(self, sell_in)

    def change_quality(self, quality):
        NormalItem.change_quality(self, quality)
    def setQuality(self, valor):
        NormalItem.setQuality(self, valor)

    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)
        self.setSell_in()
