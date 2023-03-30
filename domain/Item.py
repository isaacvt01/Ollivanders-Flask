class Item:

    def __init__(self, _id, name, sell_in, quality):
        self._id = _id
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s, %s" % (self._id, self.name, self.sell_in, self.quality)
