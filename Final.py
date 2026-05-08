import time

# -----------------------------
# FEATURE 0: CREATE DATA FILE
# -----------------------------

def create_data_file():
    """Creates the data file so user doesn't need to add it manually."""
    with open("HotDogs.txt", "w") as file:
        file.write("""DD_056,Dolly Dogs,202313,40,140,10.5,1
DD_056,Dolly Dogs,202314,40,170,15.0,2
DD_056,Dolly Dogs,202315,60,100,14.5,1
DD_056,Dolly Dogs,202316,90,130,15.0,2
DD_056,Dolly Dogs,202317,40,170,25.5,4
DD_056,Dolly Dogs,202318,70,130,20.0,1
DD_056,Dolly Dogs,202319,50,180,15.5,4
DD_056,Dolly Dogs,202320,90,130,10.0,2
KK_745,Korner Kart,202313,60,130,10.5,2
KK_745,Korner Kart,202314,30,130,10.0,4
KK_745,Korner Kart,202315,80,150,25.5,2
KK_745,Korner Kart,202316,30,140,25.0,3
KK_745,Korner Kart,202317,80,160,20.5,4
KK_745,Korner Kart,202318,90,170,25.0,1
KK_745,Korner Kart,202319,80,150,20.5,3
KK_745,Korner Kart,202320,90,180,25.0,4""")

# -----------------------------
# FEATURE 1: READ FILE DATA
# -----------------------------

def load_data(filename):
    data = []
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 7:
                    record = {
                        "vendor_id": parts[0],
                        "vendor_name": parts[1],
                        "year_week": parts[2],
                        "vegan": int(parts[3]),
                        "meat": int(parts[4]),
                        "onions_kg": float(parts[5]),
                        "ketchup_l": float(parts[6])
                    }
                    data.append(record)
    except FileNotFoundError:
        print("Error: File not found.")
    return data

# -----------------------------
# FEATURE 2: SEARCHING ALGORITHMS
# -----------------------------

def linear_search(items, target):
    """Checks every item one by one."""
    for i in range(len(items)):
        if items[i].lower() == target.lower():
            return i
    return -1

def binary_search(items, target):
    """Splits the list in half repeatedly (requires sorted list)."""
    low = 0
    high = len(items) - 1
    target = target.lower()

    while low <= high:
        mid = (low + high) // 2
        mid_val = items[mid].lower()

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# -----------------------------
# FEATURE 3: SORTING ALGORITHMS
# -----------------------------

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j].lower() > arr[j + 1].lower():
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x.lower() < pivot.lower()]
    middle = [x for x in arr if x.lower() == pivot.lower()]
    right = [x for x in arr if x.lower() > pivot.lower()]
    return quick_sort(left) + middle + quick_sort(right)

# -----------------------------
# FEATURE 4: ANALYSIS
# -----------------------------

def analyse_data(data):
    total_vegan = sum(item["vegan"] for item in data)
    total_meat = sum(item["meat"] for item in data)
    return f"Total Vegan Sold: {total_vegan}\nTotal Meat Sold: {total_meat}"

def save_analysis(text, filename="results.txt"):
    with open(filename, "w") as file:
        file.write(text)

# -----------------------------
# FEATURE 5: TIMING
# -----------------------------

def compare_search_times(names):
    target = names[-1] 
    
    # Time Linear
    start = time.time()
    linear_search(names, target)
    linear_time = time.time() - start

    # Time Binary (including the necessary sort)
    start = time.time()
    sorted_names = quick_sort(names)
    binary_search(sorted_names, target)
    binary_time = time.time() - start

    return linear_time, binary_time

def compare_sort_times(names):
    start = time.time()
    bubble_sort(names)
    bubble_time = time.time() - start

    start = time.time()
    quick_sort(names)
    quick_time = time.time() - start

    return bubble_time, quick_time

# -----------------------------
# FEATURE 6: MENU SYSTEM
# -----------------------------

def display_menu():
    print("\n--- MAIN MENU ---")
    print("1. View data")
    print("2. Bubble sort (Names)")
    print("3. Quick sort (Names)")
    print("4. Linear search (Unsorted list)")
    print("5. Linear search (Sorted list)")
    print("6. Binary search (Sorted list)")
    print("7. Compare search times")
    print("8. Compare sort times")
    print("9. Generate analysis")
    print("10. Save analysis")
    print("0. Exit")

def get_vendor_names(data):
    return [item["vendor_name"] for item in data]

def menu(data):
    names = get_vendor_names(data)
    last_analysis = ""

    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            for record in data:
                print(record)

        elif choice == "2":
            print("Bubble Sorted Names:", bubble_sort(names))

        elif choice == "3":
            print("Quick Sorted Names:", quick_sort(names))

        elif choice == "4":
            target = input("Enter Vendor Name to find (Unsorted Linear): ").strip()
            result = linear_search(names, target)
            print(f"Linear Search found '{target}' at index {result}")

        elif choice == "5":
            target = input("Enter Vendor Name to find (Sorted Linear): ").strip()
            sorted_names = quick_sort(names)
            result = linear_search(sorted_names, target)
            print(f"Sorted Linear Search found '{target}' at index {result}")

        elif choice == "6":
            target = input("Enter Vendor Name to find (Binary Search): ").strip()
            sorted_names = quick_sort(names)
            result = binary_search(sorted_names, target)
            print(f"Binary Search found '{target}' at index {result}")

        elif choice == "7":
            l_time, b_time = compare_search_times(names)
            print(f"Linear Time: {l_time:.10f}s")
            print(f"Binary Time: {b_time:.10f}s (includes sorting)")

        elif choice == "8":
            b_time, q_time = compare_sort_times(names)
            print(f"Bubble Sort Time: {b_time:.10f}s")
            print(f"Quick Sort Time:  {q_time:.10f}s")

        elif choice == "9":
            last_analysis = analyse_data(data)
            print(last_analysis)

        elif choice == "10":
            if last_analysis:
                save_analysis(last_analysis)
                print("Saved results.txt")
            else:
                print("Generate analysis (Option 9) first!")

        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

# -----------------------------
# MAIN PROGRAM
# -----------------------------

create_data_file()
hotdog_data = load_data("HotDogs.txt")

if hotdog_data:
    menu(hotdog_data)
else:
    print("Program failed to load data.")
