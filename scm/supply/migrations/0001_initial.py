# Generated by Django 4.0.5 on 2022-06-24 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sku', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('default_transit_time_ms', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('created', 'Created'), ('dispatched', 'Dispatched'), ('delivered', 'Delivered'), ('revoked', 'Revoked')], default='created', max_length=50)),
                ('created_datetime', models.DateTimeField(auto_now=True)),
                ('estimated_delivery_datetime', models.DateTimeField()),
                ('actual_delivery_datetime', models.DateTimeField()),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='purchase_orders', to='supply.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchased_quantity', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('delivered_quantity', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('purchase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='supply.purchaseorder')),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sku.sku')),
            ],
        ),
    ]
