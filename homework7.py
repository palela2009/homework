import requests

# Task 1
sql1 = """
SELECT ProductName, CategoryID, Unit, Price
FROM Products
WHERE Price BETWEEN 18 AND 25
ORDER BY Price DESC;
"""
print("Task 1 SQL:")
print(sql1)

# Task 2
sql2 = """
SELECT *
FROM OrderDetails
WHERE Quantity = 15 OR Quantity = 12
ORDER BY Quantity ASC;
"""
print("Task 2 SQL:")
print(sql2)

# Task 3
products = [
    {"id": 1, "price": 50},
    {"id": 2, "price": 200},
    {"id": 3, "price": 150}
]
filtered = [p for p in products if p["price"] > 100]
print("Task 3:", filtered)

# Task 4
data = {
    "company": {
        "departments": [
            {"name": "IT", "employees": [{"name": "Ana"}, {"name": "Beka"}]},
            {"name": "HR", "employees": [{"name": "Nino"}]}
        ]
    }
}
employees = [emp["name"] for dept in data["company"]["departments"] for emp in dept["employees"]]
print("Task 4:", employees)

# Task 5
students = [
    {"name": "Ana", "grades": [90, 80, 95]},
    {"name": "Beka", "grades": [70, 85, 88]},
    {"name": "Nino", "grades": [100, 95, 99]}
]
best = max(students, key=lambda s: sum(s["grades"]) / len(s["grades"]))
print("Task 5:", best["name"])

# Task 6
companies = {
    "companies": [
        {
            "name": "TechCorp",
            "employees": [
                {"name": "Ana", "salary": 3000},
                {"name": "Beka", "salary": 4500}
            ]
        },
        {
            "name": "SoftPlus",
            "employees": [
                {"name": "Nino", "salary": 5000},
                {"name": "Giorgi", "salary": 2500}
            ]
        }
    ]
}
for company in companies["companies"]:
    for emp in company["employees"]:
        if emp["salary"] > 4000:
            print(f"Task 6: {emp['name']} - {company['name']}")

# Task 7
response7 = requests.get("https://jsonplaceholder.typicode.com/users")
users = response7.json()
print("Task 7:", users[0]["name"])

# Task 8
payload = {"title": "Test", "body": "Hello World", "userId": 5}
response8 = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
print("Task 8:", response8.json())

# Task 9
response9 = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = response9.json()
incomplete = [t for t in todos if not t["completed"]]
for t in incomplete:
    print(f"Task 9: {t['title']}")
print(f"Task 9 - Incomplete count: {len(incomplete)}")

# Task 10
response_posts = requests.get("https://jsonplaceholder.typicode.com/posts")
response_users = requests.get("https://jsonplaceholder.typicode.com/users")
posts = response_posts.json()
users = {u["id"]: u["name"] for u in response_users.json()}
for post in posts[:5]:
    author = users.get(post["userId"], "Unknown")
    print(f"Task 10: {post['title']} – {author}")