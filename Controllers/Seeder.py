from DB.dbconfig import get_conn, get_cursor

conn = get_conn()
cursor = get_cursor()

def seed_data():
    expenses_seed = [
    {"name": "Momo at Bota", "amount": 250, "category": "Food", "date": "2025-03-15 12:30:00"},
    {"name": "Lunch at college canteen", "amount": 180, "category": "Food", "date": "2025-03-16 13:00:00"},
    {"name": "Watched movie at QFX", "amount": 450, "category": "Entertainment", "date": "2025-03-17 18:45:00"},
    {"name": "Bought PUBG UC", "amount": 1200, "category": "Entertainment", "date": "2025-03-18 20:00:00"},
    {"name": "Microbus fare to Putalisadak", "amount": 40, "category": "Transportation", "date": "2025-03-19 08:30:00"},
    {"name": "Pathao ride to Jawalakhel", "amount": 150, "category": "Transportation", "date": "2025-03-20 09:15:00"},
    {"name": "Bought Data Structures book", "amount": 850, "category": "Education", "date": "2025-03-21 11:00:00"},
    {"name": "Online course fee", "amount": 3000, "category": "Education", "date": "2025-03-22 14:30:00"},
    {"name": "Tea with friends", "amount": 100, "category": "Michalleneous", "date": "2025-03-23 16:00:00"},
    {"name": "Bought gift for cousin", "amount": 600, "category": "Michalleneous", "date": "2025-03-24 17:30:00"},
    {"name": "Room rent for April", "amount": 8000, "category": "Rent", "date": "2025-04-01 10:00:00"},
    {"name": "Advance payment for hostel", "amount": 5000, "category": "Rent", "date": "2025-04-02 09:00:00"},
    {"name": "Dinner at local restaurant", "amount": 600, "category": "Food", "date": "2025-04-03 19:30:00"},
    {"name": "Taxi fare to Tinkune", "amount": 300, "category": "Transportation", "date": "2025-04-04 17:45:00"},
    {"name": "Purchased new phone case", "amount": 150, "category": "Michalleneous", "date": "2025-04-05 15:00:00"},
    {"name": "Bought groceries", "amount": 1000, "category": "Food", "date": "2025-04-06 10:30:00"},
    {"name": "Watched football match", "amount": 400, "category": "Entertainment", "date": "2025-04-07 21:00:00"},
    {"name": "Rent for parking space", "amount": 1200, "category": "Rent", "date": "2025-04-08 12:00:00"},
    {"name": "Attended online seminar", "amount": 500, "category": "Education", "date": "2025-04-09 13:15:00"},
    {"name": "Bought new shoes", "amount": 2500, "category": "Michalleneous", "date": "2025-04-10 18:00:00"},
    {"name": "Breakfast at cafe", "amount": 350, "category": "Food", "date": "2025-04-11 08:45:00"},
    {"name": "Paid monthly internet bill", "amount": 1500, "category": "Transportation", "date": "2025-04-12 09:00:00"},
    {"name": "Dinner at friend’s house", "amount": 800, "category": "Food", "date": "2025-04-13 19:30:00"},
    {"name": "Ticket for concert", "amount": 2500, "category": "Entertainment", "date": "2025-04-14 20:30:00"},
    {"name": "Bought a new laptop", "amount": 50000, "category": "Education", "date": "2025-02-15 14:00:00"},
    {"name": "Visited family in village", "amount": 5000, "category": "Michalleneous", "date": "2025-02-16 16:00:00"},
    {"name": "Room rent for May", "amount": 8000, "category": "Rent", "date": "2025-02-01 10:00:00"},
    {"name": "Fare to the airport", "amount": 500, "category": "Transportation", "date": "2025-02-02 11:00:00"},
    {"name": "Coffee with colleague", "amount": 150, "category": "Food", "date": "2025-02-03 15:30:00"},
    {"name": "Bought new desk chair", "amount": 1200, "category": "Michalleneous", "date": "2025-02-04 13:00:00"}
    ]

    budgets_seed = [
        {"category": "Food", "budget": 6000},
        {"category": "Entertainment", "budget": 3000},
        {"category": "Transportation", "budget": 1500},
        {"category": "Education", "budget": 5000},
        {"category": "Michalleneous", "budget": 2000},
        {"category": "Rent", "budget": 10000},
    ]

    # Insert expenses with hardcoded timestamps
    for entry in expenses_seed:
        cursor.execute(''' 
            INSERT INTO expenses (name, amount, category, date)
            VALUES (?, ?, ?, ?)
        ''', (entry["name"], entry["amount"], entry["category"], entry["date"]))

    # Insert budgets without month field
    for budget in budgets_seed:
        cursor.execute(''' 
            INSERT INTO budgets (category, budget)
            VALUES (?, ?)
        ''', (budget["category"], budget["budget"]))

    conn.commit()
    print("🌱 Seed data inserted with updated budgets and no month field.")
