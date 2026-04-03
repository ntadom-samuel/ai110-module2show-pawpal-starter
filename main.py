from pawpal_system import (
    Owner,
    Pet,
    Task,
    DailySchedule,
    Scheduler,
)


def main():
    """
    Demo script showcasing the PawPal scheduling system.
    Creates owners with multiple pets and tasks, then generates daily schedules.
    """
    
    # STEP 1: Create an Owner object
    print("=" * 60)
    print("Creating Owner: Jordan with 8 available hours")
    print("=" * 60)
    owner = Owner(name="Jordan", available_hours=8)
    print(f"Owner created: {owner.name} with {owner.available_hours} available hours\n")
    
    # STEP 2: Create multiple Pet objects with different species
    print("=" * 60)
    print("Creating Pets")
    print("=" * 60)
    pet1 = Pet(name="Mochi", species="Dog")
    pet2 = Pet(name="Whiskers", species="Cat")
    print(f"Pet 1 created: {pet1.name} ({pet1.species})")
    print(f"Pet 2 created: {pet2.name} ({pet2.species})\n")
    
    # STEP 3: Add pets to the owner
    print("=" * 60)
    print("Adding Pets to Owner")
    print("=" * 60)
    owner.add_pet(pet1)
    owner.add_pet(pet2)
    print(f"Pets added to owner. Total pets: {len(owner.pets)}\n")
    
    # STEP 4: Create Task objects for Pet 1 (Mochi the Dog)
    print("=" * 60)
    print(f"Creating Tasks for {pet1.name}")
    print("=" * 60)
    task1_1 = Task(name="Walk", duration_minutes=30, priority=4, category="Exercise")
    task1_2 = Task(name="Feed", duration_minutes=15, priority=5, category="Feeding")
    task1_3 = Task(name="Playtime", duration_minutes=45, priority=3, category="Entertainment")
    print(f"  - {task1_1.name}: {task1_1.duration_minutes} min, Priority: {task1_1.priority}, Category: {task1_1.category}")
    print(f"  - {task1_2.name}: {task1_2.duration_minutes} min, Priority: {task1_2.priority}, Category: {task1_2.category}")
    print(f"  - {task1_3.name}: {task1_3.duration_minutes} min, Priority: {task1_3.priority}, Category: {task1_3.category}")
    print()
    
    # STEP 5: Add tasks to Pet 1
    pet1.add_task(task1_1)
    pet1.add_task(task1_2)
    pet1.add_task(task1_3)
    print(f"Tasks added to {pet1.name}. Total tasks: {len(pet1.tasks)}\n")
    
    # STEP 6: Create Task objects for Pet 2 (Whiskers the Cat)
    print("=" * 60)
    print(f"Creating Tasks for {pet2.name}")
    print("=" * 60)
    task2_1 = Task(name="Feeding", duration_minutes=10, priority=5, category="Feeding")
    task2_2 = Task(name="Play Session", duration_minutes=20, priority=4, category="Entertainment")
    task2_3 = Task(name="Grooming", duration_minutes=25, priority=3, category="Grooming")
    print(f"  - {task2_1.name}: {task2_1.duration_minutes} min, Priority: {task2_1.priority}, Category: {task2_1.category}")
    print(f"  - {task2_2.name}: {task2_2.duration_minutes} min, Priority: {task2_2.priority}, Category: {task2_2.category}")
    print(f"  - {task2_3.name}: {task2_3.duration_minutes} min, Priority: {task2_3.priority}, Category: {task2_3.category}")
    print()
    
    # STEP 7: Add tasks to Pet 2
    pet2.add_task(task2_1)
    pet2.add_task(task2_2)
    pet2.add_task(task2_3)
    print(f"Tasks added to {pet2.name}. Total tasks: {len(pet2.tasks)}\n")
    
    # STEP 8: Create a Scheduler for Owner and Pet 1 (Mochi)
    print("=" * 60)
    print(f"Generating Daily Schedule for {owner.name} and {pet1.name}")
    print("=" * 60)
    scheduler1 = Scheduler(owner=owner, pet=pet1, time_limit=owner.available_hours * 60)  # Convert hours to minutes
    
    # Generate the daily plan for Pet 1
    schedule1 = scheduler1.generate_daily_plan()
    
    # Export and print the schedule
    plan_export1 = schedule1.export_plan()
    print("Daily Schedule Export:")
    print(plan_export1)
    print()
    
    # STEP 9: Repeat for Pet 2 (Whiskers)
    print("=" * 60)
    print(f"Generating Daily Schedule for {owner.name} and {pet2.name}")
    print("=" * 60)
    scheduler2 = Scheduler(owner=owner, pet=pet2, time_limit=owner.available_hours * 60)  # Convert hours to minutes
    
    # Generate the daily plan for Pet 2
    schedule2 = scheduler2.generate_daily_plan()
    
    # Export and print the schedule
    plan_export2 = schedule2.export_plan()
    print("Daily Schedule Export:")
    print(plan_export2)
    print()
    
    print("=" * 60)
    print("Demo Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()