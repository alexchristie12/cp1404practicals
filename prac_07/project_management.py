"""CP1404 Prac07: Project Mangement Task"""
import datetime
from project import Project

FILENAME = "projects.txt"
def main():
    """Program that manages a system of projects."""
    # TODO: Maybe I should load initial files from projects.txt
    projects = load_projects(FILENAME)
    # TODO: Print menu
    print_menu()
    # TODO: Get User Input
    user_input = get_user_input()
    while user_input != "Q":
        if user_input == "L":
            # Handle Loading the Projects
            projects = load_projects()
            pass
        elif user_input == "S":
            # Save Projects to file
            save_projects(projects)
            pass
        elif user_input == "D":
            # Display Projects
            display_projects(projects)
        elif user_input == "F":
            # Filter the projects by date
            # Need to work out datetime stuff first
            pass
        elif user_input == "A":
            # Add new project to system
            pass
        elif user_input == "U":
            # Update a preexisting project
            pass
        print_menu()
    # TODO: Handle User Input


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
            projects.append(projects)
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
    with open(FILENAME, 'w') as out_file:
        for project in projects:
            out_file.write(project.storage_format())


def display_projects(projects: list) -> None:
    """Display projects in two groups, incomplete projects and complete projects
    sorted by priority."""
    # Need to group the projects
    incomplete_projects = [project for project in projects if project.completion_percentage != 100]
    complete_projects = [project for project in projects if project.completion_percentage == 100]
    print("Incomplete Projects:")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Complete Projects:")
    for project in complete_projects:
        print(f"\t{project}")


def add_project(projects: list) -> list:
    """Add a new project to the system."""


