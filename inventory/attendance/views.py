"""
@Description: This Script defines the views for the Attendance Application
@Author: Jobet Casquejo
@Date Modified: 5-25-24
@Last Date Modified: 5-25-24
@Modified By: Jobet Casquejo
"""
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Admin, Announcements, Attendance, Employee, Events, MobileScanUsers, StaticTime
from .serializers import AdminSerializers, AnnouncementSerializers, AttendanceSerializers, EventsSerializers, MobileScanUserSerializers, StaticTimesSerializers
from .forms import AdminForms, AnnouncementsForms, AttendanceForms, EmployeeForms, EventsForms, MobileScanUsersForms, StaticTimeForms
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.utils.html import escape
from django.views.generic.edit import CreateView


@method_decorator(csrf_exempt, name='dispatch')
class AdminView(CreateView):
    model = Admin
    form_class = AdminForms
    template_name = 'admin.html'
    success_url = ''

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = {k: escape(v) for k, v in request.POST.items()}
        form = self.form_class(data)

        if form.is_valid():
            instance = form.save()
            return JsonResponse({'status': 'success', 'data': str(instance)}, status=200)
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    def put(self, request, *args, **kwargs):
        raw_data = request.body.decode('utf-8')
        data = json.loads(raw_data)
        sanitized_data = {k: escape(v) for k, v in data.items()}
        form = self.form_class(sanitized_data)

        if form.is_valid():
            instance = form.save()
            return JsonResponse({'status': 'success', 'data': str(instance)}, status=200)

        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            admin = self.get_object()
            admin.delete()
            return JsonResponse({'status': 'success'}, status=200)
        except Admin.DoesNotExist:
            return JsonResponse({'status': 'error', 'errors': 'Object not found'}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class AnnouncementsView(CreateView):
    model = Announcements
    form_class = AnnouncementsForms
    template_name = 'announcement.html'
    success_url = ''

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = {k: escape(v) for k, v in request.POST.items()}
        form = self.form_class(data)

        if form.is_valid():
            instance = form.save()
            return JsonResponse({'status': 'success', 'data': str(instance)}, status=200)
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    def put(self, request, *args, **kwargs):
        raw_data = request.body.decode('utf-8')
        data = json.loads(raw_data)
        sanitized_data = {k: escape(v) for k, v in data.items()}
        form = self.form_class(sanitized_data)

        if form.is_valid():
            instance = form.save()
            return JsonResponse({'status': 'success', 'data': str(instance)}, status=200)

        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            announcement = self.get_object()
            announcement.delete()
            return JsonResponse({'status': 'success'}, status=200)
        except Admin.DoesNotExist:
            return JsonResponse({'status': 'error', 'errors': 'Object not found'}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeView(CreateView):
    model = Employee
    form_class = EmployeeForms
    template_name = 'employee.html'
    success_url = ''

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = {k: escape(v) for k, v in request.POST.items()}
        form = self.form_class(data)

        if form.is_valid():
            instance = form.save()
            return JsonResponse({'status': 'success', 'data': str(instance)}, status=200)
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    def put(self, request, *args, **kwargs):
        raw_data = request.body.decode('utf-8')
        data = json.loads(raw_data)
        sanitized_data = {k: escape(v) for k, v in data.items()}
        form = self.form_class(sanitized_data)

        if form.is_valid():
            instance = form.save()
            return JsonResponse({'status': 'success', 'data': str(instance)}, status=200)

        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            employee = self.get_object()
            employee.delete()
            return JsonResponse({'status': 'success'}, status=200)
        except Employee.DoesNotExist:
            return JsonResponse({'status': 'error', 'errors': 'Object not found'}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class EventsView(CreateView):
    model = Events
    form_class = EventsForms
    template_name = 'event.html'
    success_url = ''

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = {k: escape(v) for k, v in request.POST.items()}
        form = self.form_class(data)

        if form.is_valid():
            instance = form.save()
            return JsonResponse({'status': 'success', 'data': str(instance)}, status=200)
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    def put(self, request, *args, **kwargs):
        raw_data = request.body.decode('utf-8')
        data = json.loads(raw_data)
        sanitized_data = {k: escape(v) for k, v in data.items()}
        form = self.form_class(sanitized_data)

        if form.is_valid():
            instance = form.save()
            return JsonResponse({'status': 'success', 'data': str(instance)}, status=200)

        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            event = self.get_object()
            event.delete()
            return JsonResponse({'status': 'success'}, status=200)
        except Events.DoesNotExist:
            return JsonResponse({'status': 'error', 'errors': 'Object not found'}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class MobileScanUsersView(CreateView):
    model = MobileScanUsers
    form_class = MobileScanUsersForms
    template_name = 'mobile_scan_user.html'
    success_url = ''

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = {k: escape(v) for k, v in request.POST.items()}
        form = self.form_class(data)

        if form.is_valid():
            instance = form.save()
            return JsonResponse({'status': 'success', 'data': str(instance)}, status=200)
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    def put(self, request, *args, **kwargs):
        raw_data = request.body.decode('utf-8')
        data = json.loads(raw_data)
        sanitized_data = {k: escape(v) for k, v in data.items()}
        form = self.form_class(sanitized_data)

        if form.is_valid():
            instance = form.save()
            return JsonResponse({'status': 'success', 'data': str(instance)}, status=200)

        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            mobile = self.get_object()
            mobile.delete()
            return JsonResponse({'status': 'success'}, status=200)
        except MobileScanUsers.DoesNotExist:
            return JsonResponse({'status': 'error', 'errors': 'Object not found'}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class StaticTimeView(CreateView):
    model = StaticTime
    form_class = StaticTimeForms
    template_name = 'static_time.html'
    success_url = ''

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = {k: escape(v) for k, v in request.POST.items()}
        form = self.form_class(data)

        if form.is_valid():
            instance = form.save()
            return JsonResponse({'status': 'success', 'data': str(instance)}, status=200)
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    def put(self, request, *args, **kwargs):
        raw_data = request.body.decode('utf-8')
        data = json.loads(raw_data)
        sanitized_data = {k: escape(v) for k, v in data.items()}
        form = self.form_class(sanitized_data)

        if form.is_valid():
            instance = form.save()
            return JsonResponse({'status': 'success', 'data': str(instance)}, status=200)

        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            statictime = self.get_object()
            statictime.delete()
            return JsonResponse({'status': 'success'}, status=200)
        except Admin.DoesNotExist:
            return JsonResponse({'status': 'error', 'errors': 'Object not found'}, status=400)


@api_view(['GET', 'POST'])
def admin_list(request):
    if request.method == 'GET':
        data = Admin.objects.all()

        serializers = AdminSerializers(
            data, context={'request': request}, many=True)

        return Response(serializers.data)

    elif request.method == 'POST':
        serializers = AdminSerializers(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def admin_details(request, pk):
    try:
        admin = Admin.objects.get(pk=pk)
    except Admin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializers = AdminSerializers(
            admin, data=request.data, context={'request': request})
        if serializers.is_valid():
            serializers.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        admin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
