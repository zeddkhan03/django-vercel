# Create your tests here.
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Task
from datetime import date, timedelta 

class TaskViewTests(TestCase):

    def setUp(self):
        # Create a task that is incomplete and due today
        self.incomplete_task = Task.objects.create(
            title="Incomplete Task",
            description="This task is incomplete.",
            due_date=date.today(),
            priority=3,  # 'Low' priority as integer
            status="To Do"
        )
        # Create a task that is complete and past the due date
        self.completed_task = Task.objects.create(
            title="Completed Task",
            description="This task is complete.",
            due_date=date.today() - timedelta(days=1),
            priority=1,  # 'High' priority as integer
            status="Done"
        )

    def test_completed_task_moved_to_completed_section(self):
        # Fetch the task list
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)

        # Check if the completed task is in the completed tasks section
        self.assertContains(response, "Completed Task")
        # Check if the incomplete task is still in the incomplete tasks section
        self.assertContains(response, "Incomplete Task")
    
def test_incomplete_overdue_task_flagged(self):
    response = self.client.get('/tasks/')
    
    # Ensure overdue task is flagged
    self.assertContains(response, "⚠️ Overdue Task")

    
def test_new_task_is_added_correctly(self):
    # Simulate adding a new task
    response = self.client.post(reverse('add_task'), {
        'title': 'New Task',
        'description': 'This is a new task',
        'due_date': date.today(),
        'priority': 2,  # Medium priority
        'status': 'To Do'
    })
    
    # Ensure 3 tasks are now present
    self.assertEqual(Task.objects.count(), 3)  # Adjust as necessary
    self.assertContains(response, "New Task")

    
def test_edit_task_functionality(self):
    # Simulate editing the task's title
    edit_url = reverse('edit_task', args=[self.incomplete_task.id])
    response = self.client.post(edit_url, {
        'title': 'Updated Task',
        'description': 'Updated description',
        'due_date': date.today(),
        'priority': 2,  # Medium priority
        'status': 'In Progress'
    })
    
    # Refresh the task from the database
    self.incomplete_task.refresh_from_db()

    # Check that the title was updated
    self.assertEqual(self.incomplete_task.title, 'Updated Task')

    
def test_delete_task(self):
    # Delete the completed task (or use incomplete_task)
    delete_url = reverse('delete_task', args=[self.completed_task.id])
    response = self.client.post(delete_url)
    
    # Ensure the task has been deleted
    self.assertEqual(Task.objects.count(), 1)  # Assuming there were initially 2 tasks
    self.assertNotContains(response, "Completed Task")

