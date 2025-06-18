import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Constants
NUM_RECORDS = 500
PRODUCT_CATEGORIES = ['Électronique', 'Vêtements', 'Maison', 'Beauté', 'Sport'] 
SALES_CHANNELS = ['Retail', 'E-commerce']
REGIONS = ['Tunis', 'Sfax', 'Sousse', 'Gabès', 'Bizerte']

# Generate Products
product_ids = [f"P{1000+i}" for i in range(50)]
products = [{
    "product_id": pid,
    "product_name": fake.word().capitalize(),
    "category": random.choice(PRODUCT_CATEGORIES),
    "price": round(random.uniform(10, 500), 2),
    "cost": lambda price: round(price * random.uniform(0.5, 0.8), 2)
} for pid in product_ids]
for p in products:
    p["cost"] = p["cost"](p["price"])
products_df = pd.DataFrame(products)

# Generate Customers
customer_ids = [f"C{1000+i}" for i in range(100)]
customers = [{
    "customer_id": cid,
    "name": fake.name(),
    "email": fake.email(),
    "region": random.choice(REGIONS),
    "loyalty": random.choice(["Nouveau", "Fidèle", "VIP"])
} for cid in customer_ids]
customers_df = pd.DataFrame(customers)

# Generate Sales
sales = []
start_date = datetime(2024, 1, 1)
for _ in range(NUM_RECORDS):
    sale_date = start_date + timedelta(days=random.randint(0, 150))
    product = random.choice(products)
    customer = random.choice(customers)
    quantity = random.randint(1, 5)
    sales.append({
        "sale_id": fake.uuid4(),
        "date": sale_date.strftime("%Y-%m-%d"),
        "product_id": product["product_id"],
        "customer_id": customer["customer_id"],
        "quantity": quantity,
        "channel": random.choice(SALES_CHANNELS),
        "price": product["price"],
        "total": round(quantity * product["price"], 2)
    })
sales_df = pd.DataFrame(sales)

# Save to CSV
data_path = "C:/Retail project/data/"
products_df.to_csv(data_path + "products.csv", index=False)
customers_df.to_csv(data_path + "customers.csv", index=False)
sales_df.to_csv(data_path + "sales.csv", index=False)

sales_df.head()
