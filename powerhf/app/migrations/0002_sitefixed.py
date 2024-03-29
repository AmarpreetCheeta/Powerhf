# Generated by Django 5.0 on 2024-01-09 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteFixed',
            fields=[
                ('global_id', models.CharField(max_length=7, primary_key=True, serialize=False, verbose_name='global ID')),
                ('site_name', models.CharField(max_length=100, verbose_name='Site Name')),
                ('site_address', models.TextField(verbose_name='Site Address')),
                ('cluster', models.CharField(max_length=100, verbose_name='Cluster')),
                ('CE', models.CharField(max_length=250, verbose_name='SE')),
                ('site_tenancy', models.CharField(max_length=250, verbose_name='Site Tenancy')),
                ('DG_NON_DG', models.CharField(max_length=20, verbose_name='DG / Non DG')),
                ('DG_capacity_kva', models.CharField(max_length=100, verbose_name='DG Capacity (Kva)')),
                ('EB_status', models.CharField(max_length=50, verbose_name='EB Status')),
                ('card_number', models.CharField(max_length=100, verbose_name='Card Number')),
                ('last_month_approved_CPH', models.CharField(verbose_name='Last Month Approved CPH')),
            ],
        ),
    ]
