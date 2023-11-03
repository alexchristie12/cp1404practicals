"""CP1404 Prac07: Project Management Task
Estimated Time: 3 hours
Actual Time   :
"""
import datetime
from operator import attrgetter
from project import Project

FILENAME = "projects.txt"


# TODO: Add in date filtering function
# Tomorrow I need to ask Lindsay about the filtering function. After this I should be good
# TODO: Add in error handling

def main():
    """Program that manages a system of projects."""
    # Load initial files from "projects.txt"
    projects = load_projects(FILENAME)
    for project in projects:
        print(project)
    print_menu()
    user_input = get_user_input()
    while user_input != "Q":
        if user_input == "L":
            # Handle Loading new Projects
            projects = load_projects()
        elif user_input == "S":
            # Save Projects to file
            save_projects(projects)
        elif user_input == "D":
            # Display Projects
            display_projects(projects)
        elif user_input == "F":
            # Filter the projects by date
            filter_projects(projects)
        elif user_input == "A":
            # Add new project to system
            add_project(projects)
        elif user_input == "U":
            # Update a preexisting project
            update_project(projects)
        else:
            print("Invalid User Input!")
        print_menu()
        user_input = get_user_input()


def print_menu() -> None:
    print("- (L)oad Projects")
    print("- (S)ave Projects")
    print("- (D)isplay Projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def get_user_input() -> str:
    return input(">>> ").upper()


def load_projects(filename="") -> list:
    """Loads projects from a .txt file."""
    projects = []
    if filename == "":
        filename = get_filename()
    with open(filename, 'r') as in_file:
        # Consume Header
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


def get_filename() -> str:
    """Gets a valid filename from the user"""
    valid_input = False
    while not valid_input:
        filename = input("Enter filename: ")
        if filename[-4:] == ".txt":
            valid_input = True
        else:
            print("Invalid File")
    return filename


def save_projects(projects: list) -> None:
    """Saves Projects back into .txt file"""
    with open(FILENAME, 'w') as out_file:
        for project in projects:
            out_file.write(project.storage_format())


def display_projects(projects: list) -> None:
    """Display projects in two groups, incomplete projects and complete projects
    sorted by priority."""
    # Need to group the projects
    incomplete_projects = [project for project in projects if project.completion_percentage != 100]
    complete_projects = [project for project in projects if project.completion_percentage == 100]
    incomplete_projects.sort()
    complete_projects.sort()
    print("Incomplete Projects:")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Complete Projects:")
    for project in complete_projects:
        print(f"\t{project}")


def add_project(projects: list):
    """Add a new project to the system."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    # Handle Date time stuff
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost Estimate: $"))
    percentage_completion = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, percentage_completion)
    projects.append(new_project)


def update_project(projects: list):
    """Updates a projects priority and/or completion percentage."""
    # Print Projects with number (0->N)
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project Choice: "))
    # Need to handle invalid input
    # Update relevant parts
    updated_project = projects[project_choice]
    new_completion_percentage = input("New Percentage: ")
    if new_completion_percentage != "":
        updated_project.percentage_completion = int(new_completion_percentage)
    new_priority = input("New Priority")
    if new_priority != "":
        updated_project.priority = int(new_priority)
    projects[project_choice] = updated_project


def filter_projects(projects: list):
    """Filters projects by start date from a specific date"""
    valid_input = False
    while not valid_input:
        try:
            input_start_date = input("Show projects that start after date (dd/mm/yyyy): ")
            start_date = datetime.datetime.strptime(input_start_date, "%d/%m/%Y")
            valid_input = True
        except ValueError:
            print("Date entered is either incorrect format or invalid.")

    # Get projects that are after a particular date, and then sort them based on date
    projects_after_start_date = [project for project in projects if project.start_date >= start_date.date()]
    sorted_projects = sorted(projects_after_start_date, key=attrgetter('start_date'))
    for project in sorted_projects:
        print(project)


if __name__ == "__main__":
    main()
