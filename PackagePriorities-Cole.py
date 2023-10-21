def resolve_packages(packages):
    time = 1
    remaining_packages = packages.copy()

    while len(remaining_packages) > 0:
        # Check which packages have arrived
        arrived_packages = packages_in_time_slot(time, remaining_packages)
        if len(arrived_packages) == 1:
            id = arrived_packages[0][0]
            for i in range(len(remaining_packages)):
                if remaining_packages[i][0] == id:
                    print(id)
                    time += 2 * remaining_packages[i][2]
                    remaining_packages.pop(i)
                    break
            continue

        # First, handle by recipient priority
        highest_recipient_priority = return_highest_recipient_priority(arrived_packages)
        if len(highest_recipient_priority) == 1:
            id = highest_recipient_priority[0][0]
            for i in range(len(remaining_packages)):
                if remaining_packages[i][0] == id:
                    print(id)
                    time += 2 * remaining_packages[i][2]
                    remaining_packages.pop(i)
                    break
            continue

        # Next, handle by sender priority
        highest_sender_priority = return_highest_sender_priority(highest_recipient_priority)
        if len(highest_sender_priority) == 1:
            id = highest_sender_priority[0][0]
            for i in range(len(remaining_packages)):
                if remaining_packages[i][0] == id:
                    print(id)
                    time += 2 * remaining_packages[i][2]
                    remaining_packages.pop(i)
                    break
            continue

        # Now, handle by smallest arrival time
        smallest_arrival_time = return_smallest_arrival_time(highest_sender_priority)

        # Remove package from packages and update time
        id = smallest_arrival_time[0][0]
        for i in range(len(remaining_packages)):
            if remaining_packages[i][0] == id:
                print(id)
                time += 2 * remaining_packages[i][2]
                remaining_packages.pop(i)


def packages_in_time_slot(time, packages):
    arrived_packages = []
    for package in packages:
        if package[1] <= time:
            arrived_packages.append(package)

    return arrived_packages

def return_highest_recipient_priority(packages):
    highest_priority = 0
    for package in packages:
        highest_priority = max(highest_priority, package[4])
    
    highest_priority_packages = []
    for package in packages:
        if package[4] == highest_priority:
            highest_priority_packages.append(package)

    return highest_priority_packages

def return_highest_sender_priority(packages):
    highest_priority = 0
    for package in packages:
        highest_priority = max(highest_priority, package[3])
    
    highest_priority_packages = []
    for package in packages:
        if package[3] == highest_priority:
            highest_priority_packages.append(package)

    return highest_priority_packages

def return_smallest_arrival_time(packages):
    smallest_time = -1
    for package in packages:
        if smallest_time == -1 or package[1] < smallest_time:
            smallest_time = package[1]
    
    smallest_time_packages = []
    for package in packages:
        if package[1] == smallest_time:
            smallest_time_packages.append(package)

    return smallest_time_packages

if __name__ == "__main__":
    # Getting input
    n = int(input())
    packages = []
    count = 0
    while count < n:
        package = input().split()
        for i in range(len(package)):
            package[i] = int(package[i])
        packages.append(package)
        count += 1

    # Resolve packages
    resolve_packages(packages)