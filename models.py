from tortoise.models import Model
from tortoise import fields


class Tariff(Model):
    id = fields.IntField(pk=True)
    cargo_type = fields.CharField(max_length=100)
    rate = fields.DecimalField(max_digits=10, decimal_places=5)
    date = fields.DateField(auto_now_add=True)
