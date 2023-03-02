#test_gilded_rose_cyclomatic_complexity_19.py

import pytest
from gilded_rose_cyclomatic_complexity_19 import GildedRose, Item

def test_item_has_sell_in_attribute():
    """
    Все предметы имеют значение "продать в течение" (sell_in), которое обозначает количество дней, в течение которых мы должны продать предмет.
    """
    item = Item(name="Foo", sell_in=10, quality=1)
    assert item.sell_in == 10

def test_item_has_quality_attribute():
    """
    Все предметы имеют значение качества (quality), которое указывает, насколько ценен предмет.
    """
    item = Item(name="Foo", sell_in=10, quality=1)
    assert item.quality == 1

def test_system_decreases_quality_every_day():
    """
    В конце каждого дня наша система снижает оба значения для каждого элемента.
    """
    items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=1),]
    GildedRose(items).update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 0

def test_when_sell_in_expired_quality_decreases_twice_as_fast():
    """
    Как только срок продажи истек, качество ухудшается в два раза быстрее.
    """
    items = [Item(name="+5 Dexterity Vest", sell_in=0, quality=10),]
    GildedRose(items).update_quality()
    assert items[0].sell_in == -1
    assert items[0].quality == 8

def test_quality_never_becomes_negative():
    """
    Качество предмета никогда не бывает отрицательным
    """
    items = [Item(name="+5 Dexterity Vest", sell_in=1, quality=0),]
    GildedRose(items).update_quality()
    assert items[0].sell_in == 0
    assert items[0].quality == 0

def test_aged_brie_becomes_better_after_sell_in():
    """
    «Выдержанный бри» (Aged Brie) на самом деле тем лучше, чем старше он становится.
    """
    items = [Item(name="Aged Brie", sell_in=10, quality=1),]
    GildedRose(items).update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 2

def test_item_quality_never_exceeds_50():
    """
    Качество предмета никогда не превышает 50.
    """
    items = [Item(name="Aged Brie", sell_in=10, quality=50),]
    GildedRose(items).update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 50

def test_sulfuras_never_sells_in_and_never_looses_quality():
    """
    "Sulfuras", будучи легендарным предметом, никогда не продается и не теряет качества.
    """
    items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=80),]
    GildedRose(items).update_quality()
    assert items[0].sell_in == 10
    assert items[0].quality == 80

def test_backstage_passes_increase_quality_by_2_if_10_to_6_days_left():
    """
    «Проходы за кулисы» (Backstage passes to a TAFKAL80ETC concert) повышаются в качестве по мере приближения значения sell_in: качество повышается на 2, если осталось 10 дней или меньше.
    """
    items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=6),]
    GildedRose(items).update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 8

def test_backstage_passes_increase_quality_by_3_if_5_to_1_days_left():
    """
    «Проходы за кулисы» (Backstage passes to a TAFKAL80ETC concert), повышаются в качестве по мере приближения значения sell_in: качество повышается на 3, если осталось 5 дней или меньше.
    """
    items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=7),]
    GildedRose(items).update_quality()
    assert items[0].sell_in == 4
    assert items[0].quality == 10

def test_backstage_passes_drop_quality_to_zero_when_0_days_left():
    """
    «Проходы за кулисы» (Backstage passes to a TAFKAL80ETC concert), после концерта качество падает до 0.
    """
    items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=7),]
    GildedRose(items).update_quality()
    assert items[0].sell_in == -1
    assert items[0].quality == 0

def test_conjured_items_quality_decreases_twice_as_fast():
    """
    Качество «Сотворенных» (Conjured) предметов ухудшается в два раза быстрее, чем у обычных предметов.
    """
    items = [Item(name="Conjured +5 Dexterity Vest", sell_in=10, quality=5),]
    GildedRose(items).update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 3

def test_conjured_item_quality_never_exceeds_50():
    """
    Качество сотворенного предмета никогда не превышает 50.
    """
    items = [Item(name="Aged Brie", sell_in=10, quality=49),]
    GildedRose(items).update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 50

def test_conjured_sulfuras_does_not_sell_and_quality_does_not_decrease():
    """
    Качество «Сотворенного» Sulfuras не ухудшается и он не продается.
    """
    items = [Item(name="Conjured Sulfuras, Hand of Ragnaros", sell_in=10, quality=80),]
    GildedRose(items).update_quality()
    assert items[0].sell_in == 10
    assert items[0].quality == 80

def test_conjured_aged_brie_becomes_better_after_sell_in_twice_as_fast():
    """
    Сотворенный «Выдержанный бри» (Aged Brie) на самом деле становится тем лучше, чем старше он становится в 2 раза быстрее, чем не сотворенный.
    """
    items = [Item(name="Conjured Aged Brie", sell_in=10, quality=1),]
    GildedRose(items).update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 3

def test_conjured_backstage_passes_increase_quality_by_4_if_10_to_6_days_left():
    """
    Сотворенные «Проходы за кулисы» (Conjured Backstage passes to a TAFKAL80ETC concert) повышаются в качестве по мере приближения значения sell_in: качество повышается на 4, если осталось 10 дней или меньше.
    """
    items = [Item(name="Conjured Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=6),]
    GildedRose(items).update_quality()
    assert items[0].sell_in == 9
    assert items[0].quality == 10

def test_conjured_backstage_passes_increase_quality_by_6_if_5_to_1_days_left():
    """
    Сотворенные «Проходы за кулисы» (Conjured Backstage passes to a TAFKAL80ETC concert), повышаются в качестве по мере приближения значения sell_in: качество повышается на 6, если осталось 5 дней или меньше.
    """
    items = [Item(name="Conjured Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=7),]
    GildedRose(items).update_quality()
    assert items[0].sell_in == 4
    assert items[0].quality == 13

def test_conjured_backstage_passes_drop_quality_to_zero_when_0_days_left():
    """
    Сотворенные «Проходы за кулисы» (Conjured Backstage passes to a TAFKAL80ETC concert), после концерта качество падает до 0.
    """
    items = [Item(name="Conjured Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=7),]
    GildedRose(items).update_quality()
    assert items[0].sell_in == -1
    assert items[0].quality == 0