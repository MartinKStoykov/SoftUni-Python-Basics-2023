open_tabs = int(input())
salary = int(input())

for site in range(open_tabs):
    site_type = input()

    if site_type == "Facebook":
        salary -= 150
    elif site_type == "Instagram":
        salary -= 100
    elif site_type == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)
