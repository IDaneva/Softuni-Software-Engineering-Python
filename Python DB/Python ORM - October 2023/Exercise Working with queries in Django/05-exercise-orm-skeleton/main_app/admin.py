from django.contrib import admin

from main_app.models import Laptop, Dungeon


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    fields = ["brand",
              "processor",
              "memory",
              "storage",
              "operation_system",
              "price",
              ]


@admin.register(Dungeon)
class DungeonAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "difficulty",
        "location",
        "boss_name",
        "recommended_level",
        "boss_health",
        "reward",
    ]
