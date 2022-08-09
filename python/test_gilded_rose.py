# -*- coding: utf-8 -*-
from logging import exception
import random
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def setUp(self):
        self.backstagePasses = [
            "Aged Brie",
            "Backstage passes to a TAFKAL80ETC concert",
        ]

    def test_lowersQualityAndSellInByOne(self):
        items = [Item("lowersByOne", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 9)
        self.assertEqual(items[0].sell_in, 9)

    def test_sellByPassed_qualityDecreasesTwiceAsFast(self):
        items = [Item("twiceAsBad", 0, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 3)

    def test_qualityNeverNegative(self):
        items = [Item("notNegative", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreater(items[0].quality, -1)

    def test_qualityNeverMoreThan50(self):
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertLessEqual(items[0].quality, 50)

    def test_exceptionBrie_qualityIncreases(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreater(items[0].quality, 10)

    def test_exceptionSulfuras_qualityNeverChanges(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80)

    def test_exceptionConjuredItems_qualityDecreasesTwiceAsFast(self):
        items = [Item("Conjured", 0, 15)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 13)

    def test_backstagePass10Days_qualityIncreasesByTwo(self):
        items = [Item(random.choice(self.backstagePasses), 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 12)
        self.assertEqual(items[0].sell_in, 9)

    def test_backstagePass5Days_qualityIncreasesByThree(self):
        items = [Item(random.choice(self.backstagePasses), 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 13)
        self.assertEqual(items[0].sell_in, 4)

    def test_backstagePass0Days_qualitySetTo0(self):
        items = [Item(random.choice(self.backstagePasses), 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].sell_in, 0)


if __name__ == "__main__":
    unittest.main()
