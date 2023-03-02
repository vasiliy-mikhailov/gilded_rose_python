#test_gilded_rose_cyclomatic_complexity_5.py

import pytest
import gilded_rose_cyclomatic_complexity_5

from gilded_rose_cyclomatic_complexity_5 import Item, GildedRose, ItemEntity, Sulfuras, EntityFactory, AgedBrie, BackstagePasses

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
    item = EntityFactory.create(item=Item(name="+5 Dexterity Vest", sell_in=10, quality=1))
    item.update_quality()
    assert item.sell_in == 9
    assert item.quality == 0

def test_when_sell_in_expired_quality_decreases_twice_as_fast():
    """
    Как только срок продажи истек, качество ухудшается в два раза быстрее.
    """
    item = EntityFactory.create(Item(name="+5 Dexterity Vest", sell_in=0, quality=10))
    item.update_quality()
    assert item.sell_in == -1
    assert item.quality == 8

def test_quality_never_becomes_negative():
    """
    Качество предмета никогда не бывает отрицательным
    """
    item = EntityFactory.create(Item(name="+5 Dexterity Vest", sell_in=1, quality=0))
    item.update_quality()
    assert item.sell_in == 0
    assert item.quality == 0

def test_aged_brie_becomes_better_after_sell_in():
    """
    «Выдержанный бри» (Aged Brie) на самом деле тем лучше, чем старше он становится.
    """
    item = EntityFactory.create(Item(name="Aged Brie", sell_in=10, quality=1))
    item.update_quality()
    assert item.sell_in == 9
    assert item.quality == 2

def test_item_quality_never_exceeds_50():
    """
    Качество предмета никогда не превышает 50.
    """
    item = EntityFactory.create(Item(name="Aged Brie", sell_in=10, quality=50))
    item.update_quality()
    assert item.sell_in == 9
    assert item.quality == 50

def test_sulfuras_never_sells_in_and_never_looses_quality():
    """
    "Sulfuras", будучи легендарным предметом, никогда не продается и не теряет качества.
    """
    item = EntityFactory.create(Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=80))
    item.update_quality()
    assert item.sell_in == 10
    assert item.quality == 80

def test_backstage_passes_increase_quality_by_2_if_10_to_6_days_left():
    """
    «Проходы за кулисы» (Backstage passes to a TAFKAL80ETC concert) повышаются в качестве по мере приближения значения sell_in: качество повышается на 2, если осталось 10 дней или меньше.
    """
    item = EntityFactory.create(Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=6))
    item.update_quality()
    assert item.sell_in == 9
    assert item.quality == 8

def test_backstage_passes_increase_quality_by_3_if_5_to_1_days_left():
    """
    «Проходы за кулисы» (Backstage passes to a TAFKAL80ETC concert), повышаются в качестве по мере приближения значения sell_in: качество повышается на 3, если осталось 5 дней или меньше.
    """
    item = EntityFactory.create(Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=7))
    item.update_quality()
    assert item.sell_in == 4
    assert item.quality == 10

def test_backstage_passes_drop_quality_to_zero_when_0_days_left():
    """
    «Проходы за кулисы» (Backstage passes to a TAFKAL80ETC concert), после концерта качество падает до 0.
    """
    item = EntityFactory.create(Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=7))
    item.update_quality()
    assert item.sell_in == -1
    assert item.quality == 0

def test_item_entity_copies_attributes_from_item():
    """
    ItemEntity может быть создан из Item, при этом он копирует к себе поля Item
    """
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=7)
    item_entity = ItemEntity(item=item)
    assert item_entity.name == item.name
    assert item_entity.sell_in == item.sell_in
    assert item_entity.quality == item.quality

def test_item_entity_detects_conjured_item():
    """
    ItemEntity имеет атрибут conjured, устанавливаемый в True если название предмета начинается с "Conjured "
    """
    item = Item(name="Conjured Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=7)
    item_entity = ItemEntity(item=item)
    assert item_entity.is_conjured

def test_item_entity_converts_to_item():
    """
    ItemEntity может быть преобразован в Item, при этом он копирует свои поля в Item
    """
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=7)
    item_entity = ItemEntity(item=item)
    copied_item = item_entity.to_item()
    assert copied_item.name == "Backstage passes to a TAFKAL80ETC concert"
    assert copied_item.sell_in == 0
    assert copied_item.quality == 7

def test_sulfuras_produced_by_factory():
    """
    Предметы "Sulfuras, Hand of Ragnaros" производят сущность Sulfuras
    """
    sulfuras = EntityFactory.create(Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=80))
    assert isinstance(sulfuras, Sulfuras)

def test_aged_brie_produced_by_factory():
    """
    Предметы "Aged Brie" производят сущность AgedBrie
    """
    aged_brie = EntityFactory.create(Item(name="Aged Brie", sell_in=10, quality=80))
    assert isinstance(aged_brie, AgedBrie)

def test_backstage_passes_produced_by_factory():
    """
    Предметы "Backstage passes to a TAFKAL80ETC concert" производят сущность BackstagePasses
    """
    backstage_passes = EntityFactory.create(Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=80))
    assert isinstance(backstage_passes, BackstagePasses)

def test_conjured_items_quality_decreases_twice_as_fast():
    """
    Качество «Сотворенных» (Conjured) предметов ухудшается в два раза быстрее, чем у обычных предметов.
    """
    item = EntityFactory.create(item=Item(name="Conjured +5 Dexterity Vest", sell_in=10, quality=5))
    item.update_quality()
    assert item.sell_in == 9
    assert item.quality == 3

def test_conjured_item_quality_never_exceeds_50():
    """
    Качество сотворенного предмета никогда не превышает 50.
    """
    item = EntityFactory.create(item=Item(name="Conjured Aged Brie", sell_in=10, quality=49))
    item.update_quality()
    assert item.sell_in == 9
    assert item.quality == 50

def test_conjured_item_quality_never_becomes_negative():
    """
    Качество сотворенного предмета никогда не бывает отрицательным
    """
    item = EntityFactory.create(item=Item(name="Conjured +5 Dexterity Vest", sell_in=1, quality=1))
    item.update_quality()
    assert item.sell_in == 0
    assert item.quality == 0

def test_conjured_aged_brie_produce_aged_brie_by_factory():
    """
    Предметы "Conjured Aged Brie" производят сущность AgedBrie
    """
    aged_brie = EntityFactory.create(Item(name="Conjured Aged Brie", sell_in=10, quality=80))
    assert isinstance(aged_brie, AgedBrie)

def test_conjured_sulfuras_does_not_sell_and_quality_does_not_decrease():
    """
    Качество «Сотворенного» Sulfuras не ухудшается и он не продается.
    """
    item = EntityFactory.create(item=Item(name="Conjured Sulfuras, Hand of Ragnaros", sell_in=10, quality=80))
    item.update_quality()
    assert item.sell_in == 10
    assert item.quality == 80

def test_conjured_aged_brie_becomes_better_after_sell_in_twice_as_fast():
    """
    Сотворенный «Выдержанный бри» (Aged Brie) на самом деле становится тем лучше, чем старше он становится в 2 раза быстрее, чем не сотворенный.
    """
    item = EntityFactory.create(item=Item(name="Conjured Aged Brie", sell_in=10, quality=1))
    item.update_quality()
    assert item.sell_in == 9
    assert item.quality == 3

def test_conjured_backstage_passes_increase_quality_by_4_if_10_to_6_days_left():
    """
    Сотворенные «Проходы за кулисы» (Conjured Backstage passes to a TAFKAL80ETC concert) повышаются в качестве по мере приближения значения sell_in: качество повышается на 4, если осталось 10 дней или меньше.
    """
    item = EntityFactory.create(item=Item(name="Conjured Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=6))
    item.update_quality()
    assert item.sell_in == 9
    assert item.quality == 10

def test_conjured_backstage_passes_increase_quality_by_6_if_5_to_1_days_left():
    """
    Сотворенные «Проходы за кулисы» (Conjured Backstage passes to a TAFKAL80ETC concert), повышаются в качестве по мере приближения значения sell_in: качество повышается на 6, если осталось 5 дней или меньше.
    """
    item = EntityFactory.create(item=Item(name="Conjured Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=7))
    item.update_quality()
    assert item.sell_in == 4
    assert item.quality == 13

def test_conjured_backstage_passes_drop_quality_to_zero_when_0_days_left():
    """
    Сотворенные «Проходы за кулисы» (Conjured Backstage passes to a TAFKAL80ETC concert), после концерта качество падает до 0.
    """
    item = EntityFactory.create(item=Item(name="Conjured Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=7))
    item.update_quality()
    assert item.sell_in == -1
    assert item.quality == 0