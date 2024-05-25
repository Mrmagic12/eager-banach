from django.test import TestCase, Client
from models import Admin, Announcements, Employee


class AdminTestCase(TestCase):
    def setUp(self):
        self.admin = Admin.objects.create(
            username='jobet1995',
            password='weaknaweak',
            token='admin123',
            user_type='admin'
        )

    def test_admin_create(self):
        admin = Admin.objects.create(
            username='jobet1995',
            password='admin1234',
            token='token1',
            user_type='admin'
        )
        self.assertEqual(admin.token, 'token1')
        self.assertEqual(admin.token, 'token1')

        data = {'username': 'jobet1995', 'password': 'testpass',
                'token': 'new_token', 'user_type': 'admin'}
        response = self.client.post('/api/admin_list', data)
        self.assertEqual(response.status_code, 302)

    def test_admin_update(self):
        self.admin.username = 'hanjiro'
        self.admin.save()
        admin = Admin.objects.get(username='hanjiro',)
        self.assertEqual(admin.username, 'hanjiro')
        assert self.admin.username == 'hanjiro'

        data = {'username': 'jobet1995', 'password': 'testpass',
                'token': 'new_token', 'user_type': 'admin'}
        response = self.client.post('/api/admin_details', data)
        self.assertEqual(response.status_code, 302)

    def test_admin_delete(self):
        pk = self.admin.pk
        self.admin.delete()

        with self.assertRaises(Admin.DoesNotExist):
            Admin.objects.get(username='jobet1995')
        assert Admin.objects.filter(pk=pk).count() == 0


class AnnouncementsTest(TestCase):
    def setUp(self):
        self.announcement = Announcements.objects.create(
            when_date='2024-05-25',
            title='Some Title',
            description='Simplified',
            published=True
        )
        self.client = Client()

    def announcement_test_post(self):
        announcement = Announcements.objects.get(
            when_date='2024-05-25',
            title='Some Title',
            description='Simplified',
            published=True
        )
        data = {
            'when_date': '2024-05-25',
            'title': 'Some Title',
            'description': 'Simplified',
            'published': True
        }
        response = self.client.post('/api/announcements_list/', data)
        self.assertEqual(response.status_code, 302)

        announcement = Announcements.objects.get(id=response.json()['id'])

        self.assertEqual(announcement.when_date, '2024-05-25')
        self.assertEqual(announcement.title, 'Some Title')
        self.assertEqual(announcement.description, 'Simplified')
        self.assertEqual(announcement.published, True)

    def test_announcement_update(self):
        self.announcement.when_date = '2025-05-25'
        self.announcement.title = 'Samples'
        self.announcement.save()
        announcement = Announcements.objects.get(title='Samples')
        self.assertEqual(announcement.title, 'Samples')
        assert self.announcement.title == 'Samples'

        data = {'when_date': '2024-05-25', 'title': 'Samples',
                'description': 'Test', 'published': 'True'}

        response = self.client.post('/api/announcement_details', data)
        self.assertEqual(response.status_code, 302)


class EmployeeTest(TestCase):
    def setUp(self):
        Employee.objects.create(
            firstname='Jobet',
            lastname='Casquejo',
            middlename='Pulgo',
            ranks='Admin',
            assignment_level='level 1',
            password='admin1234'
        )

        self.client = Client()

    def test_create_employee(self):
        employee = Employee.objects.create(
            lastname='Casquejo',
            firstname='Jobet',
            middlename='Pulgo',
            ranks='Rank 1',
            assignment_level='Level 1',
            password='secrets'
        )
        self.assertEqual(employee.ranks, 'Rank 1')

        data = {
            'lastname': 'Casquejo',
            'firstname': 'Jobet',
            'middlename': 'Pulgo',
            'ranks': 'Rank 1',
            'assignment_level': 'Level 1',
            'password': 'secrets'
        }
        response = self.client.post('/api/employee_list', data)
        self.assertEqual(response.status_code, 302)
