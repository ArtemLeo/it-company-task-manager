from django.contrib.auth import get_user_model
from django.test import TestCase

from django.urls import reverse

from task_manager.models import Position, TaskType

INDEX_URL = reverse("task_manager:index")


class PublicIndexView(TestCase):
    def test_index_login_required(self):
        res = self.client.get(INDEX_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateIndexView(TestCase):
    def setUp(self):
        self.position = Position.objects.create(
            name="test_position"
        )
        self.update_position = Position.objects.create(
            name="update_position"
        )
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="test123",
            position=self.position
        )
        self.client.force_login(self.user)

    def test_index_context(self):
        for i in range(5):
            position = Position.objects.create(
                name=f"test_name{i}",
            )
            get_user_model().objects.create_user(
                username=f"test{i}",
                password="test123",
                position=position
            )
            TaskType.objects.create(
                name=f"test_name{i}"
            )
        res = self.client.get(INDEX_URL)
        self.assertEqual(
            res.context["num_workers"],
            get_user_model().objects.count()
        )
        self.assertEqual(
            res.context["num_positions"],
            Position.objects.count()
        )
        self.assertEqual(
            res.context["num_task_types"],
            TaskType.objects.count()
        )
