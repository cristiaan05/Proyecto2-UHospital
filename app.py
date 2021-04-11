import json
from User import User
from flask import Flask, jsonify, request, render_template, url_for, redirect
from flask_cors import CORS
from flask_material import Material

app = Flask(__name__)
Material(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# from products import products
Users = []

# CREANDO USUARIO ADMINISTRADO
Users.append(User("Cesar", "Reyes", "01-01-01",
             "M", "admin", "1234", "12345678",0))
Users.append(User("Ariel", "Bautista", "01-01-01",
             "M", "admin2", "1234", "12345678",0))


@app.route('/ping')
def ping():
    return jsonify({"message": 'pong'})


@app.route('/products')
def getProductos():
    return jsonify({"products": products, "message": "Product List"})


@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [
        product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})

    return jsonify({"message": "Product not found"})


@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "Producto agregado existosamente", "products": products})


@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [
        product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Product Updated",
            "product": productFound[0]
        })
        return jsonify({"messsage": "Product not found"})


@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [
        product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            "message": "Product Deleted",
            "product": products
        })
        return jsonify({"message": "Product Not found"})


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        global Users
        username = request.form['username']
        password = request.form['password']
        print("hola")
        for user in Users:
            if user.username == username and user.password == password:
                if user.tipoUsuario==0:                   
                # return(jsonify(user.nombre))
                    return redirect(url_for('getAdmins'))
                    
            
                if user.tipoUsuario==3:
                    return redirect(url_for('getPacientes'))
                    # return jsonify({
                    #     "message":"HOLA USTED ES DOCTOR"
                    # })
                    
                    

    return render_template("login.html")


@app.route('/registroPaciente', methods=['POST'])
def registroPaciente():
    if request.method == 'POST':
        global Users
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        fechaNacimiento = request.form['fechaNacimiento']
        sexo = request.form['sexo']
        username = request.form['username']
        password = request.form['password']
        telefono = request.form['telefono']
        for user in Users:
            print(user.username)
            if username == user.username:
                return jsonify({
                    "message": "Este usuario ya existe"
                })
        if len(password)>=8:
            Users.append(User(nombre,apellido,fechaNacimiento,sexo,username,password,telefono,3))
            return jsonify({
            "message":"Usuario Cliente Agregado"
            })
        return jsonify({
            "message": "La contrasena debe al menos 8 caracteres"
        })
            
            
        

    # if len(password)>7:
    #     Users.append(User(nombre,apellido,fechaNacimiento,sexo,username,password,telefono))
    #     return jsonify({
    #         "message":"Product Agregado"
    #     })
    # return jsonify({"message":"Product Not found"})

    # for user in Users:
    #     print("HOOLAA"+user.username)
    #     if user.username==username:
    #         return jsonify({
    #         "message":"Este usuario ya existe"
    #         })
    #     print("HOOLAA22"+user.username)
    #     Users.append(User(nombre,apellido,fechaNacimiento,sexo,username,password,telefono))
    #     return jsonify({
    #         "message":"Hola no existe ningun usuario parecido y la contrasena tiene mas de 8 caracteres",
    #     })


@app.route('/admin')
def getAdmins():
    return render_template("modAdmin.html")
    global Users
    Datos = []
    for user in Users:
        admin = {
        'Nombre': user.nombre,
        'Apellido': user.appellido,
        'Telefono': user.telefono,
        'Usuario': user.username
        }
        Datos.append(admin)
        # Datos.append(admin)
            
    return jsonify({
        "message": "Product Deleted",
        "product": Datos
    })

@app.route('/paciente')
def getPacientes():
    global Users
    Datos=[]
    for user in Users:
        if user.username==username:
            paciente={
            'Nombre': user.nombre,
            'Apellido': user.appellido,
            'Telefono': user.telefono,
            'Usuario': user.username   
            }
        Datos.append(paciente)
    return jsonify({
        "message": "Usuario loggeado",
        "product": Datos
    })

    # return render_template("index.html")
    # global Users
    # Datos=[]
    # for user in Users:
    #     admin={
    #         'Nombre':user.nombre,
    #         'Apellido':user.appellido,
    #         'Telefono':user.telefono
    #     }
    #     Datos.append(admin)
    # return(jsonify(Datos))


if __name__ == '__main__':
    app.run(threaded=True, debug=True, port=4000)
