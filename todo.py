import os

# Function to display the main menu
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add a new task")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Save and exit")
    choice = input("Please select an option (1-5): ")
    return choice

# Function to view all tasks
def view_tasks(tasks):
    if tasks:
        print("\nCurrent To-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task['task']} - {'Completed' if task['completed'] else 'Pending'}")
    else:
        print("\nYour to-do list is empty.")

# Function to add a new task
def add_task(tasks):
    task_name = input("\nEnter the new task: ")
    task = {"task": task_name, "completed": False}
    tasks.append(task)
    print(f"Task '{task_name}' added to the list.")

# Function to mark a task as completed
def mark_completed(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the number of the task you want to mark as completed: "))
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print(f"Task '{tasks[task_num - 1]['task']}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the number of the task you want to delete: "))
        if 0 < task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"Task '{deleted_task['task']}' has been deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to save tasks to a file
def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        for task in tasks:
            status = 'completed' if task['completed'] else 'pending'
            file.write(f"{task['task']} | {status}\n")
    print("Your tasks have been saved.")

# Function to load tasks from a file
def load_tasks(filename):
    tasks = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                task_name, status = line.strip().split(' | ')
                tasks.append({"task": task_name, "completed": status == 'completed'})
    return tasks

# Main function to run the application
def main():
    tasks_file = 'tasks.txt'  # File where tasks will be saved
    tasks = load_tasks(tasks_file)  # Load tasks from file when the program starts

    while True:
        user_choice = display_menu()

        if user_choice == '1':
            view_tasks(tasks)
        elif user_choice == '2':
            add_task(tasks)
        elif user_choice == '3':
            mark_completed(tasks)
        elif user_choice == '4':
            delete_task(tasks)
        elif user_choice == '5':
            save_tasks(tasks, tasks_file)
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()