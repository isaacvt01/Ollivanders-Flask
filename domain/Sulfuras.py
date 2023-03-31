from domain.NormalItem import NormalItem


class Sulfuras(NormalItem):

    def __init__(self, _id,  name, sell_in, quality):
        NormalItem.__init__(self, _id,  name, sell_in, quality)  # Utilizamos el constructor de Item.

    def get_id(self):
        return NormalItem.get_id(self)

    def set_name(self, name):
        self.name = name

    def change_sell_in(self, sell_in):
        self.sell_in = sell_in

    def change_quality(self, quality):
        self.quality = quality
    def update_quality(self):
        assert self.quality == 80, "quality de %s distinta de 80" % self.__class__.__name__
        pass