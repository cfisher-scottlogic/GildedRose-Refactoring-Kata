# -*- coding: utf-8 -*-


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            decreaseSellIn(item)

            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            if (
                item.name == "Aged Brie"
                or item.name == "Backstage passes to a TAFKAL80ETC concert"
            ):
                increaseQuality(item)
            else:
                decreaseQuality(item)


def increaseQuality(item):
    itemsWhichIncreaseQuality = [
        "Aged Brie",
        "Backstage passes to a TAFKAL80ETC concert",
    ]

    if item.name not in itemsWhichIncreaseQuality:
        return item

    if item.sell_in == 0:
        item.quality = 0
        return item

    amount = 1

    if 5 < item.sell_in <= 10:
        amount = 2
    elif 0 < item.sell_in <= 5:
        amount = 3

    item.quality += amount

    if item.quality > 50:
        item.quality = 50

    return item


def decreaseQuality(item):

    if item.quality == 0:
        return item

    amount = 1

    if item.sell_in == 0 or item.name == "Conjured":
        amount = 2

    item.quality -= amount
    return item


def decreaseSellIn(item):
    if item.sell_in == 0:
        return item

    item.sell_in -= 1

    return item


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
