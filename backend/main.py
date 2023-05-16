from fastapi import FastAPI
from connection.user_db import Connection

app = FastAPI()
conn = Connection()

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

    return {"message":"Hola"}

@app.get('/products/{product_id}')
def message_2(product_id: int):
    return f"Product: {product_id}"
    


@app.post('/products')
def look_product(product_id: int):
    return f"Producto: {product_id}"
    
