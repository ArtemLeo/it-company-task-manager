from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import Position


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(name="test_position")
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="testadmin123",
            position=self.position

        )
        self.client.force_login(self.admin_user)
        self.worker = get_user_model().objects.create_user(
            username="user",
            password="testuser123",
            position=self.position
        )

    def test_worker_position_listed(self):
        """
        Test if workers positions is in list_display on worker admin page
        """
        url = reverse("admin:task_manager_worker_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.worker.position)

    def test_worker_detail_position_listed(self):
        """
        Test if worker's position is on worker detail admin page
        """
        url = reverse(
            "admin:task_manager_worker_change",
            args=[self.worker.id]
        )
        res = self.client.get(url)
        self.assertContains(res, self.worker.position)

    def test_worker_add_fieldsets_listed(self):
        """
        Test if worker's first name, last name and
        position is on worker create admin page
        """
        url = reverse("admin:task_manager_worker_add")
        res = self.client.get(url)
        self.assertContains(res, "first_name")
        self.assertContains(res, "last_name")
        self.assertContains(res, "position")
