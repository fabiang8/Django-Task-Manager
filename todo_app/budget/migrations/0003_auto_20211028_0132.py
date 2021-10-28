# Generated by Django 3.0.9 on 2021-10-28 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_budget_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='actual',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='balance',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='projected',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='budgetcategory',
            name='category',
            field=models.CharField(max_length=128, null=True, unique=True),
        ),
    ]