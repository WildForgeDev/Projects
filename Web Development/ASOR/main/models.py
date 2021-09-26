from django.db import models


class AnnouncementType(models.Model):
    type = models.CharField(max_length=100, null=True)


class SidebarAnnouncementTypes(models.Model):
    type_name = models.CharField(max_length=500, null=True)


class ScheduleOfServicesType(models.Model):
    type_name = models.CharField(max_length=500, null=True)


class ChurchAnnouncement(models.Model):
    type = models.ForeignKey(AnnouncementType, on_delete=models.CASCADE, blank=True, related_name="announcement_types")
    title = models.CharField(max_length=500, blank=True)
    body = models.CharField(max_length=3000, blank=True)
    author = models.CharField(max_length=100, blank=True)
    link = models.CharField(max_length=1000, blank=True)
    live_stream_link = models.CharField(max_length=1000, blank=True)
    image_link = models.CharField(max_length=1000, blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    title_ru = models.CharField(max_length=500, blank=True)
    body_ru = models.CharField(max_length=3000, blank=True)
    author_ru = models.CharField(max_length=100, blank=True)


class SidebarScheduleOfServices(models.Model):
    title = models.CharField(max_length=500, blank=True)
    link = models.CharField(max_length=500, blank=True)
    type = models.ForeignKey(ScheduleOfServicesType, on_delete=models.CASCADE, blank=True,
                             related_name="schedule_of_services_type")
    title_ru = models.CharField(max_length=500, blank=True)
    link_ru = models.CharField(max_length=500, blank=True)


class SidebarWeeklySchedule(models.Model):
    day = models.CharField(max_length=500, blank=True)
    time = models.CharField(max_length=500, blank=True)
    service = models.CharField(max_length=1000, blank=True)
    day_ru = models.CharField(max_length=500, blank=True)
    time_ru = models.CharField(max_length=500, blank=True)
    service_ru = models.CharField(max_length=1000, blank=True)


class SidebarAdditionalAnnouncements(models.Model):
    body = models.CharField(max_length=3000, blank=True)
    body_ru = models.CharField(max_length=3000, blank=True)
    type = models.ForeignKey(SidebarAnnouncementTypes, on_delete=models.CASCADE, null=True,
                             related_name="sidebar_announcement_types")
