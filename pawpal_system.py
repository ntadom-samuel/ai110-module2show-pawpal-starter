"""
PawPal+ System
A pet care planning assistant that schedules daily tasks based on constraints and priorities.
"""

from datetime import date
from typing import List, Dict, Optional
from abc import ABC, abstractmethod


class Owner:
    """Represents a pet owner with pets and time availability."""
    
    def __init__(self, name: str, available_hours: int):
        self.name = name
        self.available_hours = available_hours
        self.pets = []
    
    def add_pet(self, pet):
        """Add a pet to the owner's care."""
        self.pets.append(pet)
    
    def get_available_time(self) -> int:
        """Return available time in minutes."""
        return self.available_hours * 60


class Pet:
    """Represents a pet with specific care needs."""
    
    def __init__(self, name: str, species: str, age: int = None):
        self.name = name
        self.species = species
        self.age = age
        self.special_needs = []
        self.personality_traits = []
        self.tasks = []
    
    def add_task(self, task: 'Task') -> None:
        """Add a task to the pet's care plan."""
        self.tasks.append(task)
    
    def get_tasks(self) -> List['Task']:
        """Return the list of tasks for this pet."""
        return self.tasks


class Task:
    """Represents a pet care task with duration, priority, and category."""
    
    def __init__(
        self,
        name: str,
        duration_minutes: int,
        priority: int,
        category: str,
        required_frequency: str = "daily"
    ):
        self.name = name
        self.duration_minutes = duration_minutes
        self.priority = priority  # 1-5, where 5 is highest
        self.category = category  # walk, feed, med, groom, enrichment, etc.
        self.required_frequency = required_frequency
        self.owner_preference = True
        self.status = "incomplete"
    
    def mark_complete(self) -> bool:
        """Mark the task as complete. Returns True if successful."""
        self.status = "complete"
        return True
    
    def is_urgent(self) -> bool:
        """Check if task is urgent (high priority)."""
        pass
    
    def get_cost(self) -> int:
        """Return the time cost of this task in minutes."""
        return self.duration_minutes


class DailySchedule:
    """Represents a daily schedule of pet care tasks."""
    
    def __init__(self, schedule_date: date, owner: Owner, pet: Pet):
        self.date = schedule_date
        self.tasks = []
        self.total_duration = 0
        self.owner = owner
        self.pet = pet
    
    def add_task(self, task: Task) -> None:
        """Add a task to the schedule."""
        self.tasks.append(task)
        self.total_duration += task.duration_minutes
    
    def remove_task(self, task: Task) -> None:
        """Remove a task from the schedule."""
        if task in self.tasks:
            self.tasks.remove(task)
            self.total_duration -= task.duration_minutes
    
    def get_task_order(self) -> List[Task]:
        """Return tasks in scheduled order."""
        return self.tasks
    
    def calculate_gaps(self) -> int:
        """Calculate free time gaps in the schedule."""
        available_time = self.owner.get_available_time()
        gaps = available_time - self.total_duration
        return max(0, gaps)
    
    def export_plan(self) -> str:
        """Export the plan as a formatted string."""
        output = f"🐾 Today's Schedule for {self.pet.name} ({self.date})\n"
        output += f"Owner: {self.owner.name}\n"
        output += f"Available Time: {self.owner.get_available_time()} minutes\n"
        output += "\nTasks:\n"
        
        for idx, task in enumerate(self.tasks, 1):
            output += f"{idx}. {task.name} ({task.duration_minutes} min, Priority: {task.priority})\n"
        
        remaining_time = self.owner.get_available_time() - self.total_duration
        output += f"\nTotal Time: {self.total_duration} minutes\n"
        output += f"Remaining Time: {remaining_time} minutes\n"
        
        return output





class Scheduler:
    """Main scheduler that creates daily plans for pet care."""
    
    def __init__(self, owner: Owner, pet: Pet, time_limit: int):
        self.owner = owner
        self.pet = pet
        self.time_limit = time_limit  # in minutes
    
    def generate_daily_plan(self, schedule_date: date = None) -> DailySchedule:
        """Generate an optimized daily schedule."""
        if schedule_date is None:
            schedule_date = date.today()
        
        schedule = DailySchedule(schedule_date, self.owner, self.pet)
        
        # Add tasks to schedule if they fit within time limit
        for task in self.pet.get_tasks():
            if schedule.total_duration + task.duration_minutes <= self.time_limit:
                schedule.add_task(task)
        
        return schedule
