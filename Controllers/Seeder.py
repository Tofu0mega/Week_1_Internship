from DB.dbconfig import get_conn,get_cursor

conn=get_conn()
cursor=get_cursor()

def seed_data():
    expenses_seed = [
        {"name": "Momo at Bota", "amount": 250, "category": "Food"},
        {"name": "Lunch at college canteen", "amount": 180, "category": "Food"},
        {"name": "Watched movie at QFX", "amount": 450, "category": "Entertainment"},
        {"name": "Bought PUBG UC", "amount": 1200, "category": "Entertainment"},
        {"name": "Microbus fare to Putalisadak", "amount": 40, "category": "Transportation"},
        {"name": "Pathao ride to Jawalakhel", "amount": 150, "category": "Transportation"},
        {"name": "Bought Data Structures book", "amount": 850, "category": "Education"},
        {"name": "Online course fee", "amount": 3000, "category": "Education"},
        {"name": "Tea with friends", "amount": 100, "category": "Michalleneous"},
        {"name": "Bought gift for cousin", "amount": 600, "category": "Michalleneous"},
        {"name": "Room rent for April", "amount": 8000, "category": "Rent"},
        {"name": "Advance payment for hostel", "amount": 5000, "category": "Rent"},
    ]

    budgets_seed = [
        {"category": "Food", "budget": 6000},
        {"category": "Entertainment", "budget": 3000},
        {"category": "Transportation", "budget": 1500},
        {"category": "Education", "budget": 5000},
        {"category": "Michalleneous", "budget": 2000},
        {"category": "Rent", "budget": 10000},
    ]

    for entry in expenses_seed:
        cursor.execute('''
            INSERT INTO expenses (name, amount, category)
            VALUES (?, ?, ?)
        ''', (entry["name"], entry["amount"], entry["category"]))

    for budget in budgets_seed:
        cursor.execute('''
            INSERT INTO budgets (category, budget)
            VALUES (?, ?)
        ''', (budget["category"], budget["budget"]))

    conn.commit()
    print("🌱 Seed data inserted")
