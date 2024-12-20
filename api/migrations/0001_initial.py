# Generated by Django 5.1.3 on 2024-11-13 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_number', models.CharField(max_length=50)),
                ('invoice_number', models.CharField(max_length=50)),
                ('time_spent', models.DurationField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
            ],
        ),
    ]
