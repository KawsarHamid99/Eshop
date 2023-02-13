# Generated by Django 4.1.3 on 2023-01-18 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0006_remove_product_catagory"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="catagory",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="store.category",
            ),
        ),
    ]