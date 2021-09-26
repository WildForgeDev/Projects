# Generated by Django 3.2.7 on 2021-09-12 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnouncementType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleOfServicesType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SidebarAnnouncementTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SidebarWeeklySchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=500, null=True)),
                ('time', models.CharField(max_length=500, null=True)),
                ('service', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SidebarScheduleOfServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, null=True)),
                ('link', models.CharField(max_length=500, null=True)),
                ('type1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedule_of_services_type', to='main.scheduleofservicestype')),
            ],
        ),
        migrations.CreateModel(
            name='SidebarAdditionalAnnouncements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=3000, null=True)),
                ('type1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sidebar_announcement_types', to='main.sidebarannouncementtypes')),
            ],
        ),
        migrations.CreateModel(
            name='ChurchAnnouncement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, null=True)),
                ('body', models.CharField(max_length=3000, null=True)),
                ('author', models.CharField(max_length=100, null=True)),
                ('link', models.CharField(max_length=1000, null=True)),
                ('live_stream_link', models.CharField(max_length=1000, null=True)),
                ('image_link', models.CharField(max_length=1000, null=True)),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='announcement_types', to='main.announcementtype')),
            ],
        ),
    ]