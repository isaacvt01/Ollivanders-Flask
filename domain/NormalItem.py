from domain.Item import Item
from domain.Updatable import Updatable


class NormalItem(Item, Updatable):

    def __init__(self, _id, name, sell_in, quality):
        Item.__init__(self, _id, name, sell_in, quality)  # Utilizamos el constructor de Item.

    def get_id(self):
        return self._id

    def set_name(self, name):
        self.name = name

    def change_sell_in(self, sell_in):
        self.sell_in = sell_in

    def change_quality(self, quality):
        self.quality = quality

    def setSell_in(self):  # La caducidad debe reducirse en 1 cada vez que se ejecute
        self.sell_in = self.sell_in - 1

    def setQuality(self, valor):
        if self.quality + valor > 50:
            self.quality = 50
        elif self.quality + valor >= 0:
            self.quality = self.quality + valor
        else:
            self.quality = 0

    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)
        self.setSell_in()


def __repr__(self) -> str:
    return f"Normal item: {self.name}, {self.sell_in}, {self.quality} \n"
