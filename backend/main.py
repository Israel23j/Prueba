from fastapi import FastAPI
import psycopg2
from connection.connection import Connection

app = FastAPI()
conn = Connection()

#ef conn_database():
#
#   try:
#
#       conn = psycopg2.connect(host="database", database="test", user="postgres", password="password")
#       cursor = conn.cursor()
#       cursor.execute("SELECT * FROM datos;")
#       result = cursor.fetchone()
#
#   except:
#       
#       result = "Error de conexion"
#
#   return result

@app.get('/')
def message():

   data = conn.read_all("providers")
   items = {}
   for item in data:
       provider = {}
       provider["name"] = item [1]
       provider["cif"] = item [2]
       provider["direction"] = item [3]
       provider["phone"] = item [4]
       provider["email"] = item [5]
       provider["contact"] = item [6]
       provider["schedule"] = item [7]
       items[item[0]] = provider
   return items
    
@app.get('/products')
def message_2():

    return conn_database()

@app.get('/products/{product_id}')
def message_2(product_id: int):
    return f"Product: {product_id}"
    


@app.post('/products')
def look_product(product_id: int):
    return f"Producto: {product_id}"
    
