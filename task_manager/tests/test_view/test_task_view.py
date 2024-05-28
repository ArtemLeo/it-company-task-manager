from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import TaskType, Position, Task

TASK_URL = reverse("task_manager:task-list")


class PublicTaskTest(TestCase):
    def test_login_required(self):
        res = self.client.get(TASK_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTaskTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(
            name="test_position"
        )
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="test123",
            position=self.position
        )
        self.client.force_login(self.user)

        self.task_type = TaskType.objects.create(
            name="test_task_type"
        )
        self.task = Task.objects.create(
            name="test_task",
            task_type=self.task_type,
            priority="Urgent",
            description="test_description",
            deadline="2025-01-01",
            is_completed=False,
        )
        self.task.assignees.add(self.user)

    def test_retrieve_tasks(self):
        res = self.client.get(TASK_URL)
        self.assertEqual(res.status_code, 200)
        tasks = Task.objects.all()
        self.assertEqual(
            list(res.context["task_list"]),
            list(tasks)
        )

    def test_search_task(self):
        res = self.client.get(TASK_URL + "?name=test_task")
        task = Task.objects.filter(name__icontains="test_task")
        self.assertEqual(
            list(res.context["task_list"]),
            list(task)
        )

    def test_detail_task(self):
        res = self.client.get(reverse(
            "task_manager:task-detail", args=[1]
        ))
        self.assertEqual(res.status_code, 200)

    def test_create_task(self):
        data = {
            "name": "new_task",
            "task_type": self.task_type.id,
            "priority": "Urgent",
            "description": "test_description",
            "deadline": date(2025, 1, 1),
            "is_completed": False,
            "assignees": [self.user.id]
        }
        response = self.client.post(reverse("task_manager:task-create"), data)
        task = Task.objects.get(name="new_task")

        self.assertRedirects(response, reverse("task_manager:task-list"))
        self.assertEqual(task.name, "new_task")
        self.assertEqual(task.task_type, self.task_type)
        self.assertEqual(task.priority, "Urgent")
        self.assertEqual(task.description, "test_description")
        self.assertEqual(task.deadline.__str__(), "2025-01-01")
        self.assertEqual(task.is_completed, False)
        self.assertEqual(task.assignees.first(), self.user)

    def test_update_task(self):
        self.update_task_type = TaskType.objects.create(
            name="update_task_type"
        )
        self.update_user = get_user_model().objects.create_user(
            username="update_username",
            password="update123",
            position=self.position
        )
        res = self.client.post(
            reverse("task_manager:task-update", args=[1]),
            {
                "name": "updated_task",
                "task_type": self.update_task_type.id,
                "priority": "Low-priority",
                "description": "updated_description",
                "deadline": date(2025, 1, 2),
                "is_completed": True,
                "assignees": [self.user.id, self.update_user.id]
            }
        )
        self.assertRedirects(res, reverse("task_manager:task-list"))
        task = Task.objects.get(name="updated_task")

        self.assertRedirects(res, reverse("task_manager:task-list"))

        self.assertEqual(task.name, "updated_task")
        self.assertEqual(task.task_type, self.update_task_type)
        self.assertEqual(task.priority, "Low-priority")
        self.assertEqual(task.description, "updated_description")
        self.assertEqual(task.deadline.__str__(), "2025-01-02")
        self.assertEqual(task.is_completed, True)
        self.assertEqual(task.assignees.first(), self.user)
        self.assertEqual(task.assignees.last(), self.update_user)

    def test_delete_task(self):
        response = self.client.post(
            reverse(
                "task_manager:task-delete",
                args=[1]
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Task.objects.filter(id=1).exists()
        )
