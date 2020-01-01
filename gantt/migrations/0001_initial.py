from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.URLField(
                    default='https://www.csie.ntust.edu.tw/var/file/38/1038/pictures/654/m/mczh-tw1920x400_small74292_355196687813.jpg')),
            ],
        ),
        migrations.CreateModel(
            name='TimeLine',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_type', models.CharField(max_length=255)),
                ('start_time', models.CharField(max_length=255)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gantt.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=255)),
                ('skill_type', models.CharField(max_length=255)),
                ('duration', models.FloatField()),
                ('addtional_time', models.FloatField()),
                ('description', models.CharField(max_length=255)),
                ('is_weapon', models.BooleanField(default=False, max_length=255)),
                ('character_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='gantt.Character')),
            ],
        ),
    ]
