from flask import Flask,jsonify,request,render_template,url_for,redirect
from flask_cors import CORS
from flask_material import Material

app= Flask(__name__)
Material(app)
CORS(app)
# from products import products
from User import User
import json
Users=[]
 
# CREANDO USUARIO ADMINISTRADO
Users.append(User("Cesar","Reyes","01-01-01","M","admin","1234","12345678"))
Users.append(User("Ariel","Bautista","01-01-01","M","admin2","1234","12345678"))

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

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        global Users
        username=request.form['username']
        password=request.form['password']
        print("hola")
        for user in Users:
            if user.username==username and user.password==password:
                ##return(jsonify(user.nombre))
                return redirect(url_for('getAdmins'))

    return render_template("login.html")

@app.route('/admin')
def getAdmins():
    global Users
    Datos=[]
    for user in Users:
       admin={
            'Nombre':user.nombre,
            'Apellido':user.appellido,
            'Telefono':user.telefono
        }
       Datos.append(admin)
            #Datos.append(admin)        
    return jsonify({
            "message":"Product Deleted",
            "product": Datos
        }) 
        
    ##return render_template("index.html")
    # global Users
    # Datos=[]
    # for user in Users:
    #     admin={
    #         'Nombre':user.nombre,
    #         'Apellido':user.appellido,
    #         'Telefono':user.telefono
    #     }
    #     Datos.append(admin) 
   ## return(jsonify(Datos))
    

if __name__=='__main__': 
    app.run(threaded=True,debug=True,port=4000)
