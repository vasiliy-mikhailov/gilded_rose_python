#gilded_rose_cyclomatic_complexity_5.py

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        self.items = [EntityFactory.create(item=item).update_quality().to_item() for item in self.items]

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ItemEntity:
    def __init__(self, item):
        name = item.name
        self.name = name
        self.sell_in = item.sell_in
        self.quality = item.quality
        self.is_conjured = name.startswith("Conjured ")
        self.quality_increase_factor = 1

    def increase_quality(self):
        self.quality = min(self.quality + 1 * self.quality_increase_factor, 50)

    def decrease_quality(self):
        self.quality = max(self.quality - 1 * self.quality_increase_factor, 0)

    def decrease_sell_in(self):
        self.sell_in = self.sell_in - 1

    def change_quality(self):
        self.decrease_quality()

    def change_quality_after_sell_in(self):
        self.decrease_quality()

    def update_quality(self):
        self.change_quality()

        self.decrease_sell_in()

        if self.sell_in < 0:
            self.change_quality_after_sell_in()

        return self

    def to_item(self):
        return Item(name=self.name, sell_in=self.sell_in, quality=self.quality)

class EntityFactory:
    def remove_conjured_if_exists(name):
        if name.startswith("Conjured "):
            return name[9:]
        else:
            return name

    def create(item):
        stripped_name = EntityFactory.remove_conjured_if_exists(item.name)

        if stripped_name == "Aged Brie":
            return AgedBrie(item=item)
        elif stripped_name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePasses(item=item)
        elif stripped_name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(item=item)
        else:
            return ItemEntity(item=item)

class AgedBrie(ItemEntity):
    def change_quality(self):
        self.increase_quality()

    def change_quality_after_sell_in(self):
        self.increase_quality()

class BackstagePasses(ItemEntity):
    def change_quality(self):
        self.increase_quality()

    def change_quality_after_sell_in(self):
        self.quality = 0

    def decrease_quality(self):
        super().decrease_quality()

    def increase_quality(self):
        super().increase_quality()

        if self.sell_in < 11:
            super().increase_quality()
        if self.sell_in < 6:
            super().increase_quality()

class Sulfuras(ItemEntity):
    def decrease_quality(self):
        pass

    def decrease_sell_in(self):
        pass

