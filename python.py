num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

ch = input("Enter a character: ").lower()

if ch in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest:", a)
else:
    print("Largest:", b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "abhay" and password == "2006":
    print("Login successful")
else:
    print("Invalid credentials")

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both")
    agents = []

def add_agent(**kwargs):
    name = kwargs.get("name")
    agent = {"name": name, "missions": []}
    agents.append(agent)
    print("Agent added successfully!")

def assign_mission(name, *scores):
    for agent in agents:
        if agent["name"] == name:
            for score in scores:
                agent["missions"].append(score)
            print("Mission scores added!")
            return
    print("Agent not found!")

def view_agents():
    for agent in agents:
        print(agent)

def calculate_average(agent):
    if len(agent["missions"]) == 0:
        return 0
    return sum(agent["missions"]) / len(agent["missions"])

def top_agent():
    top = None
    highest = 0

    for agent in agents:
        avg = calculate_average(agent)
        if avg > highest:
            highest = avg
            top = agent

    if top:
        print("Top Agent:", top["name"], "Score:", highest)

def assign_rank(avg):
    if avg >= 90:
        return "Elite Agent"
    elif avg >= 75:
        return "Senior Agent"
    elif avg >= 50:
        return "Junior Agent"
    else:
        return "Failed Agent"

def generate_report():
    for agent in agents:
        avg = calculate_average(agent)
        rank = assign_rank(avg)
        print("\nName:", agent["name"])
        print("Missions:", agent["missions"])
        print("Average:", avg)
        print("Rank:", rank)

while True:
    print("\n--- Spy Mission System ---")
    print("1. Add Agent")
    print("2. Assign Mission")
    print("3. View Agents")
    print("4. Show Top Agent")
    print("5. Generate Report")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter agent name: ")
        add_agent(name=name)

    elif choice == 2:
        name = input("Enter agent name: ")
        scores = list(map(int, input("Enter mission scores: ").split()))
        assign_mission(name, *scores)

    elif choice == 3:
        view_agents()

    elif choice == 4:
        top_agent()

    elif choice == 5:
        generate_report()

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
        set = set()

set.add(10)
set.add(20)
set.add(30)
set.add(40)
set.add(50)

print(set)

set = {1, 2, 3, 4}

set.remove(2)
print(set)

set.discard(10)
print(set)

set1 = {10, 20, 30}

set2 = set1.copy()

set1.add(40)

print("Original:", set1)
print("Copy:", set2)

set = {5, 10, 15}

set.clear()

print(set)

set = {1, 2, 3, 4}

print(2 in set)
print(10 in set)

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))

a = {1, 2, 3}
b = {2, 3, 4}

print(a.intersection(b))

a = {1, 2, 3}
b = {2, 4}

print(a.difference(b))

a = {1, 2, 3}
b = {2, 3, 4}

print(a.symmetric_difference(b))

a = {1, 2}
b = {3, 4}

a.update(b)

print(a)

def total_bill(amount):
    gst = amount * 0.18
    total = amount + gst
    return total
print(total_bill(1000))

#2.() to return average and grade
def student_result(marks):
    avg = sum(marks) / len(marks)

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "Fail"
    
    return avg, grade

print(student_result([80, 90, 85]))

#3.() to check voting eligibility
def check_vote(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible"
    
print(check_vote(20))

#4.() to calculate final price after discount
def final_price(price, discount):
    discount_amount = price * (discount / 100)
    return price - discount_amount

print(final_price(1000, 10))

#5.() to find smallest num in list
def smallest_number(numbers):
    return min(numbers)

print(smallest_number([5, 2, 8, 1]))

#6.()to count even num in list
def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count
print(count_even([1, 2, 3, 4, 6]))

