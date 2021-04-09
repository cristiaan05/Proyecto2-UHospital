from flask import Flask,jsonify,request
from flask_cors import CORS

app= Flask(__name__)
CORS(app)
from products import products

@app.route('/ping')

def ping():
    return  jsonify({"message":'pong'})

@app.route('/products')
def getProductos():
    return jsonify({"products": products,"message":"Product List"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound=[product for product in products if product['name']==product_name] 
    if (len(productsFound)>0):
        return jsonify({"product": productsFound[0]})
        
    return jsonify({"message": "Product not found"})

@app.route('/products',methods=['POST'])
def addProduct():
    new_product={
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "Producto agregado existosamente","products":products})

@app.route('/products/<string:product_name>',methods=['PUT'])
def editProduct(product_name):
    productFound=[product for product in products if product['name']==product_name]
    if (len(productFound)>0):
        productFound[0]['name']=request.json['name']
        productFound[0]['price']=request.json['price']
        productFound[0]['quantity']=request.json['quantity']
        return jsonify({
            "message":"Product Updated",
            "product": productFound[0]
        })
        return jsonify({"messsage": "Product not found"})
    
@app.route('/products/<string:product_name>',methods=['DELETE'])
def deleteProduct(product_name):
   productsFound=[product for product in products if product['name']==product_name]
   if len(productsFound)>0:
    products.remove(productsFound[0])   
    return jsonify({
            "message":"Product Deleted",
            "product": products
        }) 
    return jsonify({"message":"Product Not found"})  


if __name__=='__main__': 
    app.run(debug=True,port=4000)
