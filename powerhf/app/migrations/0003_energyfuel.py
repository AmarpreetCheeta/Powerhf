# Generated by Django 5.0 on 2024-01-09 07:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_sitefixed'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnergyFuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tasks', models.CharField(choices=[('Energy Reading and Diesel Filling', 'Energy Reading and Diesel Filling'), ('Energy Reading', 'Energy Reading')], max_length=50, verbose_name='Tasks')),
                ('DG_Serial_Number', models.TextField(verbose_name='DG Serial Number')),
                ('DG_HMR_Status', models.CharField(choices=[('Working', 'Working'), ('Not-Working', 'Not-Working'), ('Missing', 'Missing')], max_length=30, verbose_name='DG HMR Status')),
                ('DG_HMR_Reading', models.IntegerField(verbose_name='DG HMR Reading')),
                ('DG_PIU_Status', models.CharField(choices=[('Working', 'Working'), ('Not-Working', 'Not-Working'), ('Missing', 'Missing')], max_length=30, verbose_name='DG PIU Status')),
                ('Current_DG_PIU_Reading', models.IntegerField(verbose_name='Current DG PIU Reading')),
                ('Diesel_Filling_Done', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, verbose_name='Diesel Filling Done')),
                ('Date_Of_Diesel_Filling', models.DateField(verbose_name='Date of Diesel Filling')),
                ('Diesel_Balance_Before_Filling', models.IntegerField(verbose_name='Diesel Balance Before Filling')),
                ('Fuel_Qty_Filled', models.IntegerField(verbose_name='Fuel Qty. Filled')),
                ('Current_Diesel_Balance', models.IntegerField(verbose_name='Current Diesel Balance')),
                ('EB_Meter_Status', models.CharField(choices=[('Working', 'Working'), ('Not-Working', 'Not-Working'), ('Missing', 'Missing')], max_length=30, verbose_name='EB Meter Status')),
                ('Current_EB_MTR_KWH', models.IntegerField(verbose_name='Current EB MTR (KWH)')),
                ('EB_PIU_Meter_Status', models.CharField(choices=[('Working', 'Working'), ('Not-Working', 'Not-Working'), ('Missing', 'Missing')], max_length=30, verbose_name='EB PIU Meter Status')),
                ('Current_EB_PIU_Reading', models.IntegerField(verbose_name='Current EB PIU Reading')),
                ('Total_DC_Load', models.IntegerField(verbose_name='Total DC Load')),
                ('Total_EB_KWH_Reading_from_all_Channels', models.IntegerField(verbose_name='Total EB KWH Reading from all channels')),
                ('Remarks', models.TextField(verbose_name='Remarks')),
                ('FT_ID', models.CharField(max_length=50, verbose_name='FT ID')),
                ('FT_name', models.CharField(max_length=200, verbose_name='FT Name')),
                ('FT_mobile_no', models.CharField(max_length=10, verbose_name='FT Mobile No')),
                ('Receipt_No', models.CharField(max_length=200, null=True, verbose_name='Receipt Number')),
                ('Card_Number', models.CharField(max_length=200, null=True, verbose_name='Card Number')),
                ('Vehicle_Plate', models.CharField(max_length=200, null=True, verbose_name='Vehicle Plate')),
                ('Before_Fuel_CM_Photo', models.ImageField(upload_to='Before Fuel Filling (CM)/%y', verbose_name='Before Fuel (CM) Photo')),
                ('After_Fuel_Filling_CM_Photo', models.ImageField(upload_to='After Fuel Filling (CM)/%y', verbose_name='After Fuel Filling(CM) Photo')),
                ('DG_Running_HRS', models.TextField(verbose_name='DG Running Hrs')),
                ('CPH_CPH_Comparison_With_Last_CPH', models.TextField(verbose_name='CPH and CPH Comparioson with Approved')),
                ('CPH', models.TextField(verbose_name='CPH')),
                ('EB_KWH', models.TextField(verbose_name='EB KWH')),
                ('global_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sitefixed')),
            ],
        ),
    ]
