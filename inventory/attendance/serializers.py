"""
@Description: This Script defines the serializers for the Attendance Application
@Author: Jobet Casquejo
@Date Modified: 5-25-24
@Last Date Modified: 5-25-24
@Modified By: Jobet Casquejo
"""
from rest_framework import serializers
from .models import *


class AdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"


class AnnouncementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Announcements
        fields = "__all__"


class EventsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = "__all__"


class AttendanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"


class EmployeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = "__all__"


class MobileScanUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = MobileScanUsers
        fields = "__all__"


class StaticTimesSerializers(serializers.ModelSerializer):
    class Meta:
        model = StaticTime
        fields = "__all___"
