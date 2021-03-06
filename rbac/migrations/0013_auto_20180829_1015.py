# Generated by Django 2.1 on 2018-08-29 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0012_auto_20180825_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailMaxNo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=6)),
                ('max_no', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='dep_code',
            field=models.CharField(blank=True, max_length=5, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='detailmaxno',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbac.Department'),
        ),
    ]
