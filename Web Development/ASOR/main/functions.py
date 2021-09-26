from datetime import datetime

from .models import ChurchAnnouncement, SidebarScheduleOfServices, SidebarWeeklySchedule, SidebarAdditionalAnnouncements


def get_announcements():
    announcements = ChurchAnnouncement.objects.all()
    return announcements


def get_schedule_of_services():
    schedule_of_services = SidebarScheduleOfServices.objects.all()
    return schedule_of_services


def get_weekly_schedule():
    weekly_schedule = SidebarWeeklySchedule.objects.all()
    return weekly_schedule


def get_additional_announcements():
    additional_announcements = SidebarAdditionalAnnouncements.objects.all()
    return additional_announcements


def get_date():
    today = datetime.date(datetime.now())
    return today




