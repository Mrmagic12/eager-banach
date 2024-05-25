from django import forms
from .models import Admin, Announcements, Attendance, Employee, Events, MobileScanUsers, StaticTime
from .serializers import AdminSerializers, AnnouncementSerializers, EventsSerializers, AttendanceSerializers, EmployeesSerializers, MobileScanUserSerializers, StaticTimesSerializers


class AdminForms(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.PasswordInput()
    token = forms.CharField(label='Token', max_length=100)
    user_type = forms.CharField(label='User Type', max_length=100)

    class Meta:
        models = Admin
        serializers = AdminSerializers
        fields = ['username', 'password', 'token', 'user_type']


class AnnouncementsForms(forms.Form):
    date = forms.DateField(label='Date')
    title = forms.CharField(label='Title', max_length=255)
    description = forms.CharField(widget=forms.Textarea, label='Description')
    published = forms.BooleanField()

    class Meta:
        models = Announcements
        serializers = AnnouncementSerializers
        fields = ['date', 'title', 'description', 'published']


class EventsForms(forms.Form):
    date = forms.DateField(label='Date')
    title = forms.CharField(label='Title', max_length=255)
    description = forms.CharField(widget=forms.Textarea, label='Description')
    published = forms.BooleanField()

    class Meta:
        models = Events
        serializers = EventsSerializers
        fields = ['date', 'title', 'description', 'published']


class AttendanceForms(forms.Form):
    leaves = (
        ('A', 'Annual leave'),
        ('S', 'Sick leave'),
        ('E', 'Emergency leave'),
        ('H', 'Holiday leave'),
        ('M', 'Maternity Leave')
    )
    employee_id = forms.ModelChoiceField(queryset=Attendance.objects.all())
    am_in = forms.DateTimeField(label='AM In')
    am_mask_in = forms.BooleanField(label='AM in Mask')
    am_out = forms.DateTimeField(label='AM Out')
    am_mask_out = forms.BooleanField(label='AM out Mask')
    pm_in = forms.DateTimeField(label='PM In')
    pm_mask_in = forms.DateTimeField(label='PM in Mask')
    pm_out = forms.DateTimeField(label='PM Out')
    pm_mask_out = forms.DateTimeField(label='PM out Mask')
    remarks = forms.CharField(label='Remaks', max_length=255)
    leave_status = forms.ChoiceField(choices=leaves, label='Leave Reason')
    leave_reason = forms.CharField(widget=forms.Textarea, label='Description')

    class Meta:
        models = Attendance
        serialzers = AttendanceSerializers

        fields = ['employee_id', 'am_in', 'am_mask_in', 'am_out', 'am_mask_out',
                  'pm_in', 'pm_in_mask', 'pm_out', 'pm_out_mask', 'remarks', 'leave_status',
                  'leave_status'
                  ]


class EmployeeForms(forms.Form):
    lastname = forms.CharField(label='Last Name', max_length=255)
    firstname = forms.CharField(label='First Name', max_length=255)
    middlename = forms.CharField(label='Middle Name', max_length=255)
    ranks = forms.CharField(label='Ranks', max_length=255)
    assignment_level = forms.CharField(
        label='Assignment Level', max_length=255)
    password = forms.PasswordInput()

    class Meta:
        models = Employee
        serializers = EmployeesSerializers
        fields = ['firstname', 'lastname', 'middlename',
                  'ranks', 'assignment_level', 'password']


class MobileScanUsersForms(forms.Form):
    account_name = forms.CharField(label='Account Name', max_length=255)
    password = forms.PasswordInput()

    class Meta:
        models = MobileScanUsers
        serializers = MobileScanUserSerializers
        fields = ['account_name', 'password']


class StaticTimeForms(forms.Form):
    employee_type = forms.CharField(label='Employee Type', max_length=255)
    am_in = forms.DateTimeField(label='AM In')
    am_out = forms.DateTimeField(label='AM Out')
    pm_in = forms.DateTimeField(label='PM In')
    pm_out = forms.DateTimeField(label='PM Out')

    class Meta:
        models = StaticTime
        serializers = StaticTimesSerializers
        fields = ['employee_type', 'am_in', 'am_out', 'pm_in', 'pm_out']
