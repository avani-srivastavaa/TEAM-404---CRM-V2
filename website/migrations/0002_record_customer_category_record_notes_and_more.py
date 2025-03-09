# Generated by Django 5.1.7 on 2025-03-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="record",
            name="customer_category",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="record",
            name="notes",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="record",
            name="priority_score",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="record",
            name="sentiment_score",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
