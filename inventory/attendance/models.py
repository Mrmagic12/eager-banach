"""
@Description: This Script defines the models for the Attendance Application
@Author: Jobet Casquejo
@Date Modified: 5-22-24
@Last Date Modified: 5-22-24
@Modified By: Jobet Casquejo
"""
from django.db import models
from django.utils import timezone


class Admin(models.Model):
    """
    This model represents the Admin
    """
    user_id = models.AutoField(primary_key=True, null=False, blank=False)
    username = models.CharField(max_length=255, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    token = models.CharField(max_length=255, null=False, blank=False)
    user_type = models.CharField(max_length=255, null=False, blank=False)

    @staticmethod
    def get_user(user_id):
        return Admin.objects.get(user_id=user_id)

    @staticmethod
    def get_user_by_username(username):
        return Admin.objects.get(username=username).user_id

    def __str__(self):
        return self.username


class Employee(models.Model):
    """
    This model represents and Employee
    """
    employee_id = models.AutoField(primary_key=True, null=False, blank=False)
    lastname = models.CharField(max_length=255, null=False, blank=False)
    firstname = models.CharField(max_length=255, null=False, blank=False)
    middlename = models.CharField(max_length=255, null=False, blank=False)
    ranks = models.CharField(max_length=255, null=False, blank=False)
    assignment_level = models.CharField(
        max_length=255, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)

    def addEmployee(self):
        self.save()

    @staticmethod
    def get_employee(employee_id):
        return Employee.objects.get(employee_id=employee_id)

    @staticmethod
    def get_employee_by_username(username):
        return Employee.objects.get(username=username).employee_id

    def __str__(self):
        return self.firstname


class Announcements(models.Model):
    """
    This model represents the announcements made by the admin.
    """
    announcement_id = models.AutoField(primary_key=True, null=False, blank=False)
    when_date = models.DateField(null=False, blank=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    published = models.BooleanField(null=False, blank=False)

    def saveAnnouncement(self):
        self.save()

    @staticmethod
    def get_announcements(announcement_id):
        return Announcements.objects.get(announcement_id=announcement_id)

    @staticmethod
    def get_announcements_by_title(title):
        return Announcements.objects.get(title=title).announcement_id

    def __str__(self):
        return self.title


class Attendance(models.Model):
    """
    This model tracks the attendance of each employee. 
    It also tracks leave status and leave reason in case an employee is on leave.
    """
    leaves = (
        ('A', 'Annual leave'),
        ('S', 'Sick leave'),
        ('E', 'Emergency leave'),
        ('H', 'Holiday leave'),
        ('M', 'Maternity Leave')
    )
    attendance_id = models.AutoField(primary_key=True, null=False, blank=False)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date_log = models.DateTimeField(null=False, blank=False)
    am_in = models.DateTimeField(null=False, blank=False)
    am_in_mask = models.BooleanField(null=False, blank=False)
    am_out = models.DateTimeField(null=False, blank=False)
    am_out_mask = models.BooleanField(null=False, blank=False)
    pm_in = models.DateTimeField(null=False, blank=False)
    pm_in_mask = models.BooleanField(null=False, blank=False)
    pm_out = models.DateTimeField(null=False, blank=False)
    pm_out_mask = models.BooleanField(null=False, blank=False)
    remarks = models.CharField(max_length=255, null=False, blank=False)
    leave_status = models.CharField(
        null=True, blank=True, max_length=1, choices=leaves)
    leave_reason = models.TextField()

    @staticmethod
    def get_attendance(attendance_id):
        return Attendance.objects.get(attendance_id=attendance_id)

    @staticmethod
    def get_attendance_by_employee_id(employee_id):
        return Attendance.objects.get(employee_id=employee_id).attendance_id

    def __str__(self):
        return self.remarks


class Events(models.Model):
    """
    This model represents the public events published by the admin.
    """
    event_id = models.AutoField(primary_key=True, null=False, blank=False)
    event_date = models.DateField(null=False, blank=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    published = models.BooleanField(null=False, blank=False)

    @staticmethod
    def get_events(event_id):
        return Events.objects.get(event_id=event_id)

    @staticmethod
    def get_events_by_title(title):
        return Events.objects.get(title=title).event_id

    def __str__(self):
        return self.title


class MobileScanUsers(models.Model):
    """
    This model represents the users of the mobile scan feature.
    """
    user_id = models.AutoField(primary_key=True, null=False, blank=False)
    account_name = models.CharField(max_length=255, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)

    @staticmethod
    def get_user(user_id):
        return MobileScanUsers.objects.get(user_id=user_id)

    @staticmethod
    def get_user_by_account_name(account_name):
        return MobileScanUsers.objects.get(account_name=account_name).user_id

    def __str__(self):
        return self.account_name


class StaticTime(models.Model):
    """
    This model holds the static attendance times for different types of employees.
    """
    time_id = models.AutoField(primary_key=True, null=False, blank=False)
    employee_type = models.CharField(max_length=255, null=False, blank=False)
    am_in = models.DateTimeField(null=False, blank=False)
    am_out = models.DateTimeField(null=False, blank=False)
    pm_in = models.DateTimeField(null=False, blank=False)
    pm_out = models.DateTimeField(null=False, blank=False)
