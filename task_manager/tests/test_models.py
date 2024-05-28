from django.contrib.auth import get_user_model
from django.test import TestCase

from task_manager.models import Position, TaskType, Task


class TaskTypeTests(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(
            name="Bug fix"
        )

    def test_task_type_str(self):
        self.assertEqual(
            str(self.task_type),
            self.task_type.name
        )


class PositionTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(
            name="Developer"
        )

    def test_position_str(self):
        self.assertEqual(
            str(self.position),
            self.position.name
        )


class WorkerTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(
            name="Developer"
        )

        self.worker = get_user_model().objects.create_user(
            username="test",
            first_name="test_name",
            last_name="test_lastname",
            password="test_password",
            position=self.position
        )

    def test_create_worker_with_position(self):
        self.assertEqual(self.worker.username, "test")
        self.assertTrue(self.worker.check_password("test_password"))
        self.assertTrue(self.worker.position.name, self.position.name)

    def test_worker_str(self):
        self.assertEqual(
            str(self.worker),
            (f"{self.worker.position.name} "
             f"({self.worker.first_name} {self.worker.last_name})")
        )


class TaskTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(
            name="Developer"
        )

        self.worker = get_user_model().objects.create_user(
            username="test",
            first_name="test_name",
            last_name="test_lastname",
            password="test_password",
            position=self.position
        )
        self.task_type = TaskType.objects.create(
            name="Bug fix"
        )
        self.task = Task.objects.create(
            name="test_name",
            description="test_description",
            deadline="2021-01-01",
            is_completed=False,
            priority="Urgent",
            task_type=self.task_type
        )

        self.task.assignees.set((self.worker,))

    def test_task_str(self):
        self.assertEqual(str(self.task), self.task.name)
