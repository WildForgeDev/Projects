# Generated by Django 3.2.5 on 2021-10-11 22:35

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
                ('day', models.CharField(blank=True, max_length=500)),
                ('time', models.CharField(blank=True, max_length=500)),
                ('service', models.CharField(blank=True, max_length=1000)),
                ('day_ru', models.CharField(blank=True, max_length=500)),
                ('time_ru', models.CharField(blank=True, max_length=500)),
                ('service_ru', models.CharField(blank=True, max_length=1000)),
                ('display_order', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeOverride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='SidebarScheduleOfServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500)),
                ('link', models.CharField(blank=True, max_length=500)),
                ('title_ru', models.CharField(blank=True, max_length=500)),
                ('link_ru', models.CharField(blank=True, max_length=500)),
                ('display_order', models.IntegerField(null=True)),
                ('type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedule_of_services_type', to='main.scheduleofservicestype')),
            ],
        ),
        migrations.CreateModel(
            name='SidebarAdditionalAnnouncements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(blank=True, max_length=3000)),
                ('body_ru', models.CharField(blank=True, max_length=3000)),
                ('display_order', models.IntegerField(null=True)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sidebar_announcement_types', to='main.sidebarannouncementtypes')),
            ],
        ),
        migrations.CreateModel(
            name='ChurchAnnouncement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500)),
                ('body', models.CharField(blank=True, max_length=3000)),
                ('author', models.CharField(blank=True, max_length=100)),
                ('title_ru', models.CharField(blank=True, max_length=500)),
                ('body_ru', models.CharField(blank=True, max_length=3000)),
                ('author_ru', models.CharField(blank=True, max_length=100)),
                ('link', models.CharField(blank=True, max_length=1000)),
                ('live_stream_link', models.CharField(blank=True, max_length=1000)),
                ('image_link', models.CharField(blank=True, max_length=1000)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('display_order', models.IntegerField(null=True)),
                ('date_override', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='time_override', to='main.timeoverride')),
                ('type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='announcement_types', to='main.announcementtype')),
            ],
        ),
    ]
