# Generated by Django 2.2.1 on 2019-05-02 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('price', models.PositiveSmallIntegerField()),
                ('period', models.PositiveSmallIntegerField(verbose_name='周期(月)')),
                ('outline', models.TextField()),
            ],
            options={
                'verbose_name': '课程表',
                'verbose_name_plural': '课程表',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='Administrators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('department', models.SmallIntegerField(choices=[(0, '研发部'), (1, '运营部'), (2, '人力资源部'), (3, '财务部'), (4, '运维部')])),
                ('position', models.CharField(blank=True, max_length=32, null=True)),
                ('qq', models.CharField(max_length=64, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('consult_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gecko.Course', verbose_name='咨询课程')),
                ('tags', models.ManyToManyField(blank=True, to='gecko.Tag')),
            ],
            options={
                'verbose_name': '维护人',
                'verbose_name_plural': '维护人',
            },
        ),
    ]