# Generated by Django 2.1 on 2018-08-29 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0014_auto_20180829_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailinfo',
            name='remark',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='charging_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='earnest_money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='esc_potential_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='esc_procurement_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='extension_insurance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='financial_advisory_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='first_payment',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='free_mortgage_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='fs_vps',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='gift_je',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='glass_insurance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='installment_bond',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='labor_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='listing_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='ln_vps',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='maintenance_package',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='mortgage_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='navigation_4G_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='personal_accident_insurance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='replacement_subsidy',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='scratch_risk',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='security_deposit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='theft_insurance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='time_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='transaction_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='value_added_package',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
