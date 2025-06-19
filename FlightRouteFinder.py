# Define flight routes and durations using a nested dictionary
flight_routes = {
    'SRI LANKA': {'UK': 11.45, 'JAPAN': 8, 'SINGAPORE': 4, 'AUSTRALIA': 9.25},
    'UK': {'USA': 8},
    'USA': {},
    'JAPAN': {'USA': 16, 'AUSTRALIA': 10},
    'SINGAPORE': {'AUSTRALIA': 7.25, 'JAPAN': 4},
    'AUSTRALIA': {}
}

# Main program
while True:
    print("FlightRoutes Company".center(70))
    print("Main Menu".center(70))
    print("1. Display All possible airline routes between two given countries with durations.")
    print("2. Display least time airline route between two given countries.")
    print("3. Exit")
    choice = input("                                                                    Your choice: ")
    
    if choice == '1':
        print('')
        print("FlightRoutes Company".center(70))
        print("All possible airline routes between two given countries with duration.".center(70))
        print('')
        start_country = input("Enter the starting country: ").upper()
        dest_country = input("Enter the destination country: ").upper()
        print('')

        routes = [([start_country], 0)]
        all_routes = []

        while routes:
            path, duration = routes.pop(0)
            current_country = path[-1]
            if current_country == dest_country:
                all_routes.append((path, duration))
            elif start_country not in flight_routes:
                print("The starting country provided by the user in not in our system ")
            elif dest_country not in flight_routes:
                print("The Destination country provided by the user in not in our system ")
            else:
                for destination, time in flight_routes[current_country].items():
                    if destination not in path:
                        new_path = path + [destination]
                        new_duration = duration + time
                        routes.append((new_path, new_duration))

        route_number = 1
        for path, duration in all_routes:
            print(f"Route {route_number}: {' -> '.join(path)}     Expected Duration: {duration} Hours")
            route_number += 1
        print('')

    elif choice == '2':
        print('')
        print("FlightRoutes Company".center(70))
        print("Least duration airline route between two given countries".center(70))
        print('')
        start_country = input("Enter the starting country: ").upper()
        dest_country = input("Enter the destination country: ").upper()
        print('')

        routes = [([start_country], 0)]
        min_duration = float('inf')
        min_route = []

        while routes:
            path, duration = routes.pop(0)
            current_country = path[-1]
            if current_country == dest_country and duration < min_duration:
                min_duration = duration
                min_route = path
            elif start_country not in flight_routes:
                print("The starting country provided by the user in not in our system ")
            elif dest_country not in flight_routes:
                print("The Destination country provided by the user in not in our system ")
            else:
                for destination, time in flight_routes[current_country].items():
                    if destination not in path:
                        new_path = path + [destination]
                        new_duration = duration + time
                        routes.append((new_path, new_duration))

        if min_route:
            print(f"Fastest Route: {' -> '.join(min_route)} Duration: {min_duration} Hours")
        else:
            print("No route found.")
        print('')
        exit_point = input('Do you want to Exit (Yes/NO)? ').upper()
        if exit_point == "YES":
            print("Thank you for using FlightRoutes Company. Goodbye!")
            exit()
        else:
            print('')
    elif choice == '3':
        second_exit_point = input('Do you want to Exit (Yes/NO)? ').upper()
        if second_exit_point == "YES":
            print("Thank you for using FlightRoutes Company. Goodbye!")
            exit()
            break
        else:
            print('')
        
    else:
        print("Invalid choice. Please try again.")
        print("")
