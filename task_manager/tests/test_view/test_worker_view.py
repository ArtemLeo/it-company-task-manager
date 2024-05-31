from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, reverse_lazy

from task_manager.models import Position

WORKER_URL = reverse("task_manager:worker-list")


class PublicWorkerTest(TestCase):
    def test_login_required(self):
        res = self.client.get(WORKER_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateWorkerTest(TestCase):
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

    def test_retrieve_workers(self):
        res = self.client.get(WORKER_URL)
        self.assertEqual(res.status_code, 200)
        workers = get_user_model().objects.all()
        self.assertEqual(
            list(res.context["worker_list"]),
            list(workers)
        )
        self.assertTemplateUsed(
            res,
            "task_manager/worker_list.html"
        )

    def test_search_workers(self):
        res = self.client.get(WORKER_URL + "?username=test")
        worker = get_user_model().objects.filter(username__icontains="test")
        self.assertEqual(
            list(res.context["worker_list"]),
            list(worker)
        )

    def test_detail_worker(self):
        res = self.client.get(reverse(
            "task_manager:worker-detail", args=[1]
        ))
        self.assertEqual(res.status_code, 200)

    def test_create_workers(self):
        response = self.client.post(
            reverse("task_manager:worker-create"),
            {
                "username": "new_username",
                "password1": "new_password",
                "password2": "new_password",
                "position": self.position.id,
                "first_name": "John",
                "last_name": "Doe",
            }
        )
        self.assertRedirects(response, reverse("task_manager:worker-list"))
        self.assertTrue(
            get_user_model().objects.filter(username="new_username").exists()
        )

    def test_update_worker(self):
        res = self.client.post(
            reverse_lazy("task_manager:worker-update", args=[1]),
            {
                "first_name": "update_name",
                "last_name": "update_lastname",
                "position": self.update_position.id,
                "username": "update_username",
                "email": "update_email@gmail.com",
            }
        )
        self.assertRedirects(res, reverse("task_manager:worker-list"))
        self.assertTrue(
            get_user_model().objects.filter(
                username="update_username"
            ).exists()
        )
        self.assertTrue(
            get_user_model().objects.filter(
                position=self.update_position
            ).exists()
        )
        self.assertTrue(
            get_user_model().objects.filter(
                email="update_email@gmail.com"
            ).exists()
        )
        self.assertTrue(
            get_user_model().objects.filter(first_name="update_name").exists()
        )
        self.assertTrue(
            get_user_model().objects.filter(
                last_name="update_lastname"
            ).exists()
        )

    def test_delete_worker(self):
        response = self.client.post(
            reverse(
                "task_manager:worker-delete",
                args=[1]
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            get_user_model().objects.filter(id=1).exists()
        )
