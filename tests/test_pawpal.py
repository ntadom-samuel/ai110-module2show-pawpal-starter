"""
Comprehensive tests for the PawPal+ system.
Tests core functionality for task management and pet care planning.
"""

import pytest
from pawpal_system import Owner, Pet, Task


class TestTaskCompletion:
    """Test suite for Task completion functionality."""
    
    def test_task_completion(self):
        """
        Test that a Task can be marked as complete.
        
        Verifies:
        - Task is initialized with "incomplete" status
        - mark_complete() method changes status to "complete"
        - mark_complete() returns True on successful completion
        """
        # Arrange: Create a task
        task = Task(
            name="Feed Max",
            duration_minutes=10,
            priority=5,
            category="feed"
        )
        
        # Assert: Verify initial status is "incomplete"
        assert task.status == "incomplete", "Task should start with 'incomplete' status"
        
        # Act: Mark the task as complete
        result = task.mark_complete()
        
        # Assert: Verify status changed to "complete" and method returned True
        assert task.status == "complete", "Task status should be 'complete' after marking"
        assert result is True, "mark_complete() should return True"


class TestPetTaskAddition:
    """Test suite for Pet task management functionality."""
    
    def test_pet_task_addition(self):
        """
        Test that tasks can be added to a Pet's care plan.
        
        Verifies:
        - Pet is initialized with 0 tasks
        - Tasks can be added using pet.add_task()
        - Task count increases correctly after each addition
        """
        # Arrange: Create a pet
        pet = Pet(
            name="Max",
            species="dog",
            age=3
        )
        
        # Assert: Verify initial task count is 0
        assert len(pet.tasks) == 0, "Pet should start with no tasks"
        
        # Act & Assert: Create and add first task
        task1 = Task(
            name="Morning walk",
            duration_minutes=30,
            priority=5,
            category="walk"
        )
        pet.add_task(task1)
        
        # Verify task count is now 1
        assert len(pet.tasks) == 1, "Pet should have 1 task after adding one"
        assert pet.tasks[0] == task1, "Added task should be available in pet.tasks"
        
        # Act & Assert: Create and add second task
        task2 = Task(
            name="Evening feeding",
            duration_minutes=15,
            priority=4,
            category="feed"
        )
        pet.add_task(task2)
        
        # Verify task count is now 2
        assert len(pet.tasks) == 2, "Pet should have 2 tasks after adding another"
        assert pet.tasks[1] == task2, "Second task should be at index 1"
