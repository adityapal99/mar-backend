# Generated by Django 3.0 on 2020-08-06 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catName', models.CharField(max_length=500)),
                ('point', models.IntegerField(default=0)),
                ('maxPoints', models.IntegerField()),
                ('time_spent', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('auth', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('fname', models.CharField(max_length=50)),
                ('roll', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('collegeID', models.CharField(max_length=13, null=True)),
                ('dept', models.CharField(max_length=3, null=True)),
                ('points', models.IntegerField(default=0)),
                ('auth', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('mentor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Mentor')),
            ],
        ),
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkToProof', models.TextField()),
                ('desc_by_student', models.TextField()),
                ('submissiondate', models.DateTimeField(auto_now_add=True)),
                ('checkedByTeacher', models.BooleanField(default=False)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catagory', to='core.Catagories')),
                ('for_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_data', to='core.Student')),
            ],
        ),
    ]
