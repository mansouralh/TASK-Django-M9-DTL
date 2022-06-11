from collections.abc import Sequence

import pytest
from django.test import Client
from django.urls import reverse

from shops.models import IceCream, IceCreamFlavor, Shop, ShopLocation


@pytest.fixture
def ice_cream() -> IceCream:
    shop_location = ShopLocation.objects.create(latitude=0, longitude=0)
    shop = Shop.objects.create(name="kdd", location=shop_location)
    flavor = IceCreamFlavor.objects.create(name="Chocolate")
    obj: IceCream = IceCream.objects.create(
        name="Twister",
        shop=shop,
        stock=99,
    )
    obj.flavors.add(flavor)
    return obj


@pytest.fixture
def ice_creams() -> Sequence[IceCream]:
    kdd_location = ShopLocation.objects.create(latitude=0, longitude=0)
    kdd = Shop.objects.create(name="kdd", location=kdd_location)

    abc_location = ShopLocation.objects.create(latitude=0, longitude=0)
    abc = Shop.objects.create(name="abc", location=abc_location)

    chocolate = IceCreamFlavor.objects.create(name="Chocolate")
    vanilla = IceCreamFlavor.objects.create(name="Chocolate")
    strawberry = IceCreamFlavor.objects.create(name="Strawberry")

    ice_cream1: IceCream = IceCream.objects.create(
        name="Twister",
        shop=kdd,
        stock=10,
    )

    ice_cream2: IceCream = IceCream.objects.create(
        name="Rocket",
        shop=abc,
        stock=50,
    )

    ice_cream1.flavors.add(chocolate, vanilla)
    ice_cream2.flavors.add(strawberry)

    return [ice_cream1, ice_cream2]


@pytest.mark.detail
@pytest.mark.django_db
def test_present_ice_cream(client: Client, ice_cream: IceCream) -> None:
    path = reverse("ice-cream-detail", kwargs={"ice_cream_id": ice_cream.id})
    res = client.get(path)
    assert res.status_code == 200

    content = res.content.decode("utf-8")

    attrs = [ice_cream.name, ice_cream.shop.name, str(ice_cream.stock)]
    assert all(attr in content for attr in attrs)


@pytest.mark.detail_bonus
@pytest.mark.django_db
def test_missing_ice_cream(client: Client) -> None:
    path = reverse("ice-cream-detail", kwargs={"ice_cream_id": 0})
    res = client.get(path)
    assert res.status_code == 404


@pytest.mark.list
@pytest.mark.django_db
def test_ice_creams(client: Client, ice_creams: Sequence[IceCream]) -> None:
    res = client.get(reverse("ice-cream-list"))
    assert res.status_code == 200

    content = res.content.decode("utf-8")

    attrs = []
    for ice_cream in ice_creams:
        attrs.extend((ice_cream.name, ice_cream.shop.name))
        attrs.extend(ice_cream.flavors.values_list("name", flat=True))

    assert all(attr in content for attr in attrs)
