# Generated by Django 3.1.2 on 2020-10-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='home_link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_name', models.CharField(help_text='超链接名称', max_length=50, null=True)),
                ('link_content', models.CharField(help_text='超链接内容', max_length=1024, null=True)),
            ],
        ),
    ]
