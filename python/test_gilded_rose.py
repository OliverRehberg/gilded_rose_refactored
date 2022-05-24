# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items()
        self.assertEqual("foo", items[0].name)

    def test_Sulfuras_constant_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items()
        self.assertEqual(80, items[0].quality)

    def test_tickets_drop_quality_to_zero_when_expired(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items()
        self.assertEqual(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()
