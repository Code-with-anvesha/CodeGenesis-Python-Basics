import calendar_generator
import event_manager

def main():
    while True:
        print("\n Calendar Menu")
        print("1. Display Monthly Calendar")
        print("2. Display Yearly Calendar")
        print("3. Add an Event")
        print("4. View Events")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            year = int(input("Enter year: "))
            month = int(input("Enter month (1-12): "))
            calendar_generator.display_month(year, month)
        elif choice == "2":
            year = int(input("Enter year: "))
            calendar_generator.display_year(year)
        elif choice == "3":
            date = input("Enter event date (YYYY-MM-DD): ")
            event = input("Enter event description: ")
            event_manager.add_event(date, event)
        elif choice == "4":
            event_manager.view_events()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()