from django.db import models


class ShopLocation(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self) -> str:
        return f"{self.latitude}, {self.longitude}"


class Shop(models.Model):
    name = models.CharField(max_length=40)
    location = models.OneToOneField(
        ShopLocation, on_delete=models.CASCADE, related_name="shop"
    )

    def __str__(self) -> str:
        return self.name


class IceCreamFlavor(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class IceCream(models.Model):
    name = models.CharField(max_length=40)
    flavors = models.ManyToManyField(IceCreamFlavor, related_name="ice_creams")
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name="ice_creams",
    )
    stock = models.PositiveIntegerField(default=99)

    def __str__(self) -> str:
        return self.name
