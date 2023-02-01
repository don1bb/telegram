import sqlite3
from pathlib import Path


def init_db():
    global db, cur
    DB_NAME = 'db.sqlite3'
    MAIN_PATH = Path(__file__).parent.parent
    db = sqlite3.connect(MAIN_PATH/DB_NAME)
    cur = db.cursor()


def create_table():
    cur.execute(
        """CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        namme TEXT,
        description TEXT,
        price INTEGER,
        phone TEXT
         )"""
        )
    cur.execute(
        """CREATE TABLE IF NOT EXISTS order(
         order_id INTEGER PRIMARY KEY,
         user_name TEXT,
         address TEXT,
         weeks TEXT,
         product_id INTEGER,
         FOREIGN KEY (product_id)
              REFERENCES products (product_id)
              ON DELETE CASCADE
        )
        """
    )
    db.commit()
def populate_products ():
    """
        запоняем таблицу
        """
    db.execute("""INSERT INTO products(
    name, description, price, photo
        )
    VALUES ('кроссовки', 'li-ning', 200, '/images/gg.jpg'),
        ('ботинки', 'зимние', 199, '/images/gg.jpg'),
        """)
    db.commit()

def get_products():
    print(cur)
    cur.execute("""
    SELECT * FROM products
    """)
    return cur.fetchall()
def create_order(data):
    '''
    Создаем заказ
    '''
    print(data.as_dict())
    data = data.as_dict()
    cur.execute("""INSERT INTO orders (
       user_name,
       address,
       week_day,
       product_id
    ) VALUES (:user_name, :address, :week_day, :product_id"""),
    {'user_name': data['name'],
     'address': data['address'],
     'week_day': data['day'],
     'product_id': data['product_id']
     }

    db.commit()

