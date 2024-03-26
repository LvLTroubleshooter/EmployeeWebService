from EmployeeDirectory.models import Employee

employees_to_add = [
    ('John Doe', 'Software Engineer'),
    ('Jane Smith', 'Project Manager'),
    ('Emily Johnson', 'Data Analyst'),
    
]

for name, position in employees_to_add:
    Employee.objects.create(name=name, position=position)

print("Added employees to the database.")
