# class person
class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# class employee
class Employee(Person):
    def __init__(self, name, gender, department):
        #super.name = name
        #super.gender = gender
        super().__init__(name, gender)          # = better
        self.department = department            # 'self' refers to the specific instance being created

# class department
class Department():
    def __init__(self, name):
        self.name = name
        self.employee = []

    def add_employee(self, employee):
        self.employee.append(employee)

    def count_employee(self):
        return len(self.employee)

# class manager
class Manager(Employee):
    def __init__(self, name, gender, department):
        super().__init__(name, gender, department)
        self.is_manager = True

# class company
class Company:
    def __init__(self):
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def count_employees(self):
        total_employees = sum(department.count_employee() for department in self.departments)
        # total_managers = sum(1 for department in self.departments for employee in department.employees if isinstance(employee, Manager))
        # total_employees -= total_managers
        return total_employees#, total_managers

    def count_departments(self):
        return len(self.departments)

    # Department with the largest number of employees
    def largest_department(self):
        if not self.departments:
            return None

        max_department = max(self.departments, key=lambda d: d.count_employee())
        return max_department.name

    # Method for the percentage of women and men
    def gender_ratio(self):
        total_male = sum(1 for department in self.departments for employee in department.employee if employee.gender == 'male')
        total_female = sum(1 for department in self.departments for employee in department.employee if employee.gender == 'female')

        total_employees = total_male + total_female
        if total_employees == 0:
            return 0, 0

        percent_male = (total_male / total_employees) * 100
        percent_female = (total_female / total_employees) * 100

        return percent_female, percent_male


# add person
person1 = Person("Tim", "male")
person2 = Person("Mary", "female")
person3 = Person("Peter", "male")
person4 = Person("Tony", "female")

# add departments
f_department = Department("Financial")
mm_department = Department("Management")
it_department = Department("IT")
mt_department = Department("Marketing")

# add employees/manager to department
f_department.add_employee(Manager("Tom", "male", f_department))
f_department.add_employee(Employee("Michael", "male", f_department))
mm_department.add_employee(Manager("Claudia", "female", mm_department))
mm_department.add_employee(Employee("Nora", "female", mm_department))
it_department.add_employee(Manager("Mathias", "male", it_department))
it_department.add_employee(Employee("Anne", "female", it_department))
it_department.add_employee(Employee("Marcus", "male", it_department))
mt_department.add_employee(Manager("Patty", "female", mt_department))
mt_department.add_employee(Employee("Michaela", "female", mt_department))

# add company structure and departments
company = Company()
company.add_department(f_department)
company.add_department(mm_department)
company.add_department(it_department)
company.add_department(mt_department)

# method calls
total_employees = company.count_employees()
#total_employees, total_managers = company.count_employees()
#print(f"Total number of employees: {total_employees}")
#print(f"Total number of department heads: {total_managers}")
print(f"Number of departments: {company.count_departments()}")
print(f"Department with the most employees: {company.largest_department()}")


# Method call for the percentage of women and men
female_percent, male_percent = company.gender_ratio()
total_employees = company.count_employees()

# Calculate the number of females and males
female_percent, male_percent = company.gender_ratio()
total_employees = company.count_employees()
total_female = int((female_percent / 100) * total_employees)
total_male = int((male_percent / 100) * total_employees)

print(f"Total number of employees: {total_employees}")
print(f"Percentage of females: {female_percent:.2f}% ({total_female} Women)")
print(f"Percentage of males: {male_percent:.2f}% ({total_male} Men)")