# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_items(self):
        for item in self.items:
            item.update_quality()
            item.update_sell_in()
 
class Item:
    MAX_DEFAULT_QUALITY = 50
    MIN_DEFAULT_QUALITY = 0
    EARLY_TICKET_QUALITY_INCREMENT_THRESHOLD = 11
    LATE_TICKET_QUAILTY_INCREMENT_THRESHOLD = 6

    def __init__(self, name, sell_in, quality, conjured = False):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.conjured = conjured

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def get_name(self):
        return self.name

    def get_quality(self):
        return self.quality

    def set_quality(self, new_quality):
        self.quality = new_quality

    def get_sell_in(self):
        return self.sell_in

    def set_sell_in(self, new_sell_in):
        self.sell_in = new_sell_in

    def get_conjured(self):
        return self.conjured

    def update_quality(self):
        if self.get_name() != "Aged Brie" and self.get_name() != "Backstage passes to a TAFKAL80ETC concert":
            self.decrease_quality_if_feasible()
        else:
            self.increase_quality_if_feasible()
            if self.get_name() == "Backstage passes to a TAFKAL80ETC concert":
                if self.get_sell_in() < self.EARLY_TICKET_QUALITY_INCREMENT_THRESHOLD:
                    self.increase_quality_if_feasible()
                if self.get_sell_in() < self.LATE_TICKET_QUAILTY_INCREMENT_THRESHOLD:
                    self.increase_quality_if_feasible()
        if self.get_sell_in() == 0:
            if self.get_name() != "Aged Brie":
                if self.get_name() != "Backstage passes to a TAFKAL80ETC concert":
                    self.decrease_quality_if_feasible()
                else:
                    self.set_quality(0)
            else:
                self.increase_quality_if_feasible()

    def increase_quality_if_feasible(self):
        if self.get_quality() < self.MAX_DEFAULT_QUALITY:
            self.set_quality(self.quality + 1)
        if self.get_conjured():
            if self.get_quality() < self.MAX_DEFAULT_QUALITY:
                self.set_quality(self.quality + 1)

    def decrease_quality_if_feasible(self):
        if self.get_quality() > self.MIN_DEFAULT_QUALITY:
            if self.get_name() != "Sulfuras, Hand of Ragnaros":
                self.set_quality(self.quality - 1)
        if self.get_conjured():
            if self.get_quality() > self.MIN_DEFAULT_QUALITY:
                if self.get_name() != "Sulfuras, Hand of Ragnaros":
                    self.set_quality(self.quality - 1)

    def update_sell_in(self):
        if self.get_name() != "Sulfuras, Hand of Ragnaros":
            self.set_sell_in(self.sell_in - 1)
