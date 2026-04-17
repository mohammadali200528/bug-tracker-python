# Bug Tracker System

bugs = []

def add_bug():
    title = input("Enter bug title: ")
    priority = input("Enter priority (Low/Medium/High): ")
    
    bug = {
        "title": title,
        "priority": priority,
        "status": "Open"
    }
    
    bugs.append(bug)
    print("Bug added successfully!\n")

def view_bugs():
    if not bugs:
        print("No bugs reported.\n")
        return
    
    for i, bug in enumerate(bugs):
        print(f"{i+1}. {bug['title']} | Priority: {bug['priority']} | Status: {bug['status']}")
    print()

def update_bug():
    view_bugs()
    index = int(input("Enter bug number to update: ")) - 1
    
    if 0 <= index < len(bugs):
        bugs[index]["status"] = "Closed"
        print("Bug marked as closed!\n")
    else:
        print("Invalid bug number.\n")

while True:
    print("1. Add Bug\n2. View Bugs\n3. Close Bug\n4. Exit")
    choice = input("Choose: ")
    
    if choice == "1":
        add_bug()
    elif choice == "2":
        view_bugs()
    elif choice == "3":
        update_bug()
    elif choice == "4":
        break
    else:
        print("Invalid choice\n")