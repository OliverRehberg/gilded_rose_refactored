# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_items(self):
        for item in self.items:
            item.update_quality()
            item.update_sell_in()
 
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_quality(self):
        if self.name != "Aged Brie" and self.name != "Backstage passes to a TAFKAL80ETC concert":
            self.decrease_quality_if_feasible()
        else:
            self.increase_quality_if_feasible()
            if self.name == "Backstage passes to a TAFKAL80ETC concert":
                if self.sell_in < 11:
                    self.increase_quality_if_feasible()
                if self.sell_in < 6:
                    self.increase_quality_if_feasible()
        if self.sell_in == 0:
            if self.name != "Aged Brie":
                if self.name != "Backstage passes to a TAFKAL80ETC concert":
                    self.decrease_quality_if_feasible()
                else:
                    self.quality = 0
            else:
                self.increase_quality_if_feasible()

    def increase_quality_if_feasible(self):
        if self.quality < 50:
            self.quality = self.quality + 1

    def decrease_quality_if_feasible(self):
        if self.quality > 0:
            if self.name != "Sulfuras, Hand of Ragnaros":
                    self.quality = self.quality - 1

    def update_sell_in(self):
        if self.name != "Sulfuras, Hand of Ragnaros":
            self.sell_in = self.sell_in - 1
