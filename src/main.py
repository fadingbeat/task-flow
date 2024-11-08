from tasks.task_service import TaskService
from database.singleton_db import DatabaseConnection
from tasks.task_factory import TaskFactory

def main():
    # Create a singleton instance and connect to the database
    db1 = DatabaseConnection()
    db1.connect('taskflow.db')
    db1._initialize_tables()

    task_service = TaskService()

    # Creating different types of tasks using the factory 
    reminder = task_service.create_and_save_tasks("reminder", "Doctor's Appointment", "Remember to bring your insurance card", remind_time="2024-10-30 10:00 AM")
    limit = task_service.create_and_save_tasks("limit", "Project Submission", "Submit the project report to the client", limit = "2024-10-30 04:00 PM")
    recurring = task_service.create_and_save_tasks("recurring", "Weekly team meeting", "Discuss project updates with the team", frequency="every Monday at 9 AM")
 
     # Execute tasks to see their outputs
    print(reminder.execute())
    print(limit.execute())
    print(recurring.execute())

    all_tasks = task_service.singleton_db.get_tasks()
    print("Stored Tasks in Database:")
    for task in all_tasks:
        print(task)

if __name__ == "__main__":
    main()
