from django.db import models

# Create your models here.


class Phone(models.Model):
    brand=models.CharField(max_length=200)
    model=models.CharField(max_length=200)
    image=models.ImageField(upload_to="olx",blank=True,null=True)
    price=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table="phone"

    def __str__(self):
        return self.brand
