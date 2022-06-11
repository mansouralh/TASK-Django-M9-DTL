from django.contrib import admin

from shops import models

to_register = [
    models.ShopLocation,
    models.Shop,
    models.IceCreamFlavor,
    models.IceCream,
]

admin.site.register(to_register)
