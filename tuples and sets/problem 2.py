# Dictionary

directory = [{"name": "Ron Swanson", "age": 55,"department": "Management","phone": "555-1234","salary": "2,000"}, 
{ "name": "John Smith", "age": 23,"department": "marketing","phone": "223-1234","salary": "4,000"},
{ "name": "Rani ahmad", "age": 45,"department": "sales","phone": "555-2222","salary": "6,000"},
{ "name": "suzanaon", "age": 64,"department": "accounting","phone": "222-1234","salary": "7,000"},
{ "name": "Ramon Swarz", "age": 35,"department": "construction","phone": "234-1234","salary": "2,000"},
{ "name": "Lily", "age": 30,"department": "Management","phone": "433-1234","salary": "2,000"},
{ "name": "William", "age": 64,"department": "technology","phone": "655-1244","salary": "2,000"}]

for i in directory: 
    print(f"{i['name']} in {i['department']} can be reached at {i['phone']}")