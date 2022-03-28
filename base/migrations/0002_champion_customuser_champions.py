# Generated by Django 4.0.3 on 2022-03-10 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('img_url', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Champions',
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='champions',
            field=models.ManyToManyField(blank=True, to='base.champion'),
        ),
    ]
