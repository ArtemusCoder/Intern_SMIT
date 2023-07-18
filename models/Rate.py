from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class Rate(models.Model):
    cargo_type = fields.CharField(max_length=255)
    rate = fields.FloatField()
    date = fields.DateField()

    class Meta:
        unique_together = ('date', 'cargo_type')


Rate_Pydantic = pydantic_model_creator(Rate, name="Rate")