import json
from User import User
from Doctor import Doctor
from Medicamento import Medicamento
from Paciente import Paciente
from Enfermera import Enfermera
from Cita import Cita
from Pedido import Pedido
from flask import Flask, jsonify, request, render_template, url_for, redirect
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
# from flask_material import Material

app = Flask(__name__)
# Material(app)
cors = CORS(app)
app.config['CORS_HEADERS', 'UPLOAD_FOLDER'] = 'Content-Type', './Backend'
# from products import products
Users = []
Doctores = []
Medicamentos = []
Pacientes = []
Enfermeras = []
Citas = []
Pedidos = []
Productos = []

# CREANDO USUARIO ADMINISTRADO
Users.append(User("Cesar", "Reyes", "01-01-01",
             "M", "admin", "1234", "12345678", 0))
Users.append(User("Ariel", "Bautista", "01-01-01",
             "M", "admin2", "1234", "12345678", 0))

# ----------------------------CARGAS--------MASIVAS-----------------------------------------------------------------


@app.route('/cargarPacientes', methods=['POST'])
def cargar():
    global Pacientes
    contador_pacientes = len(Pacientes)
    import csv
    results = []
    f = request.files['archivo']
    print("nombreaa", f)
    filename = secure_filename(f.filename)
    print("asdfa"+filename)
    # f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    with open(filename) as File:
        reader = csv.DictReader(File)
        for row in reader:
            contador_pacientes += 1
            nombre = row['Nombre']
            apellido = row['Apellido']
            fechaNacimiento = row['Fecha']
            sexo = row['Sexo']
            username = row['Username']
            password = row['Contrasena']
            telefono = row['Telefono']
            Users.append(User(nombre, apellido, fechaNacimiento,
                         sexo, username, password, telefono, 3))
            Pacientes.append(Paciente(
                contador_pacientes, nombre, apellido, fechaNacimiento, sexo, username, password, telefono))
        # print (results)
    return jsonify({
        "message": "Datos cargados",
    })


@app.route('/cargarDoctores', methods=['POST'])
def cargarDcotores():
    global Doctores
    contador_doctores = len(Doctores)
    import csv
    results = []
    f = request.files['archivo']
    filename = secure_filename(f.filename)
    # f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    with open(filename) as File:
        reader = csv.DictReader(File)
        x = 0
        for row in reader:
            contador_doctores += 1
            nombre = row['Nombre']
            apellido = row['Apellido']
            fechaNacimiento = row['Fecha']
            sexo = row['Sexo']
            username = row['Username']
            password = row['Contrasena']
            especialidad = row['Especialidad']
            telefono = row['Telefono']
            Users.append(User(nombre, apellido, fechaNacimiento,
                         sexo, username, password, telefono, 1))
            Doctores.append(Doctor(contador_doctores, nombre, apellido, fechaNacimiento,
                            sexo, username, password, especialidad, telefono))
        # print (results)
    return jsonify({
        "message": "Datos cargados",
    })


@app.route('/cargarEnfermeras', methods=['POST'])
def cargarEnfermeras():
    import csv
    global Enfermeras
    contador_enfermeras = len(Enfermeras)
    results = []
    f = request.files['archivo']
    filename = secure_filename(f.filename)
    # f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    with open(filename) as File:
        reader = csv.DictReader(File)
        x = 0
        for row in reader:
            contador_enfermeras += 1
            nombre = row['Nombre']
            apellido = row['Apellido']
            fechaNacimiento = row['Fecha']
            sexo = row['Sexo']
            username = row['Username']
            password = row['Contrasena']
            telefono = row['Telefono']
            Users.append(User(nombre, apellido, fechaNacimiento,
                         sexo, username, password, telefono, 2))
            Enfermeras.append(Enfermera(
                contador_enfermeras, nombre, apellido, fechaNacimiento, sexo, username, password, telefono))
        # print (results)
    return jsonify({
        "message": "Datos cargados",
    })


@app.route('/cargarMedicamentos', methods=['POST'])
def cargarMedicamentos():
    import csv
    global Medicamentos
    contador_med = len(Medicamentos)
    results = []
    f = request.files['archivo']
    filename = secure_filename(f.filename)
    # f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    with open(filename) as File:
        reader = csv.DictReader(File)
        for row in reader:
            contador_med += 1
            nombre = row['Nombre']
            precio = row['Precio']
            descripcion = row['Descripcion']
            cantidad = row['Cantidad']
            Medicamentos.append(Medicamento(
                contador_med, nombre, precio, descripcion, cantidad))
        # print (results)
    return jsonify({
        "message": "Datos cargados",
    })
# ---------------------------------------------------------------------------------------------------------------------


@app.route('/medicamentos')
def getMedicamentos():
    global Medicamentos
    Datos = []
    for med in Medicamentos:
        admin = {
            'Id': med.id,
            'Nombre': med.nombre,
            'Precio': med.precio,
            'Descripcion': med.descripcion,
            'Cantidad': med.cantidad,
        }
        Datos.append(admin)

    return jsonify({
        "message": "Medicamentos",
        "medicamentos": Datos
    })


@app.route('/pacientes', methods=['GET'])
def getPacientes():
    # return render_template("modAdmin.html")
    global Users, Pacientes
    Datos = []
    for user in Pacientes:
        paciente = {
            'Id': user.id,
            'Nombre': user.nombre,
            'Apellido': user.apellido,
            'FechaNacimiento': user.fechaNacimiento,
            'Sexo': user.sexo,
            'Username': user.username,
            'Passsword': user.password,
            'Telefono': user.telefono
        }
        Datos.append(paciente)
    return jsonify({
        "message": "Pacientes",
        "pacientes": Datos
    })


@app.route('/doctores', methods=['GET'])
def getDoctores():
    # return render_template("modAdmin.html")
    global Doctores
    Datos = []
    for doctor in Doctores:
        doctor = {
            'Id': doctor.id,
            'Nombre': doctor.nombre,
            'Apellido': doctor.apellido,
            'FechaNacimiento': doctor.fechaNacimiento,
            'Sexo': doctor.sexo,
            'Username': doctor.username,
            'Passsword': doctor.password,
            'Especialidad': doctor.especialidad,
            'Telefono': doctor.telefono
        }
        Datos.append(doctor)
    return jsonify({
        "message": "Doctores",
        "doctores": Datos
    })


@app.route('/enfermeras', methods=['GET'])
def getEnfermeras():
    # return render_template("modAdmin.html")
    global Enfermeras
    Datos = []
    for enfermera in Enfermeras:
        enfermera = {
            'Id': enfermera.id,
            'Nombre': enfermera.nombre,
            'Apellido': enfermera.apellido,
            'FechaNacimiento': enfermera.fechaNacimiento,
            'Sexo': enfermera.sexo,
            'Username': enfermera.username,
            'Passsword': enfermera.password,
            'Telefono': enfermera.telefono
        }
        Datos.append(enfermera)
    return jsonify({
        "message": "Enfermeras",
        "enfermeras": Datos
    })


@app.route('/citas', methods=['GET'])
def getCitas():
    # return render_template("modAdmin.html")
    global Citas
    Datos = []
    for cita in Citas:
        citaa = {
            'Id': cita.id,
            'Id Paciente': cita.idPaciente,
            'Fecha': cita.fecha,
            'Hora': cita.hora,
            'Motivo': cita.motivo,
            'Estado': cita.estado
        }
        Datos.append(citaa)
        # Datos.append(admin)
    return jsonify({
        "message": "Citas",
        "product": Datos
    })

# -----------------GET--1 PACIENTE,DOCTOR,ENFERMMERA,MEDICAMENTO---------------------------------------------------------


@app.route('/paciente/<int:pacienteId>', methods=['GET'])
def getPacienteId(pacienteId):
    Datos = []
    for paciente in Pacientes:
        if paciente.id == pacienteId:
            pacientee = {
                'Id': paciente.id,
                'Nombre': paciente.nombre,
                'Apellido': paciente.apellido,
                'FechaNacimiento': paciente.fechaNacimiento,
                'Sexo': paciente.sexo,
                'Username': paciente.username,
                'Password': paciente.password,
                'Telefono': paciente.telefono
            }
            Datos.append(pacientee)
    if len(Datos) > 0:
        return jsonify({
            "message": "Paciente Encontrado",
            "paciente": Datos
        })
    elif len(Datos) <= 0:
        return jsonify({
            "message": "No se encontro ningun paciente"
        })


@app.route('/doctor/<int:doctorId>', methods=['GET'])
def getDoctorId(doctorId):
    DatosDoctor = []
    for doctor in Doctores:
        if doctor.id == doctorId:
            doctorr = {
                'Id': doctor.id,
                'Nombre': doctor.nombre,
                'Apellido': doctor.apellido,
                'Fecha Nacimiento': doctor.fechaNacimiento,
                'Sexo': doctor.sexo,
                'Username': doctor.username,
                'Passsword': doctor.password,
                'Especialidad': doctor.especialidad,
                'Telefono': doctor.telefono
            }
            DatosDoctor.append(doctorr)
    if len(DatosDoctor) > 0:
        return jsonify({
            "message": "Doctor Encontrado",
            "doctor": DatosDoctor
        })
    elif len(DatosDoctor) == 0:
        return jsonify({
            "message": "No se encontro ningun doctor"
        })


@app.route('/enfermera/<int:enfermeraId>', methods=['GET'])
def getEnfermeraId(enfermeraId):
    Datos = []
    for enfermera in Enfermeras:
        if enfermera.id == enfermeraId:
            enfermeraa = {
                'Nombre': enfermera.nombre,
                'Apellido': enfermera.appellido,
                'FechaNacimiento': enfermera.fechaNacimiento,
                'Sexo': enfermera.sexo,
                'Username': enfermera.username,
                'Passsword': enfermera.password,
                'Telefono': enfermera.telefono
            }
            Datos.append(enfermeraa)
    if len(Datos) > 0:
        return jsonify({
            "message": "Enfermera Encontrada",
            "enfermera": Datos
        })
    elif len(Datos) <= 0:
        return jsonify({
            "message": "No se encontro ninguna enfermera"
        })


@app.route('/medicamento/<int:medicamentoId>', methods=['GET'])
def getMedicamentoId(medicamentoId):
    Datos = []
    for medicamento in Medicamentos:
        if medicamento.id == medicamentoId:
            medicamentoo = {
                'Id': medicamento.id,
                'Nombre': medicamento.nombre,
                'Precio': medicamento.precio,
                'Descripcion': medicamento.descripcion,
                'Cantidad': medicamento.cantidad
            }
            Datos.append(medicamentoo)
    if len(Datos) > 0:
        return jsonify({
            "message": "Medicamento Encontrado",
            "medicamento": Datos
        })
    elif len(Datos) <= 0:
        return jsonify({
            "message": "No se encontro ningun medicamento"
        })


@app.route('/cita/<int:pacienteId>', methods=['GET'])
def geCitaPaciente(pacienteId):
    global Citas
    Datos = []
    for cita in Citas:
        if cita.idPaciente == pacienteId:
            citas = {
                'Id': cita.id,
                'IdPaciente': cita.idPaciente,
                'Fecha': cita.fecha,
                'Hora': cita.hora,
                'Motivo': cita.motivo,
                'Estado': cita.estado
            }
            Datos.append(citas)
    return jsonify({
        "message": "Citas Encontradas",
        "citas": Datos
    })

# ------------------FUNCIONES---------EDITAR-----------------------------------------------------------


@app.route('/modificarPaciente/<int:pacienteId>', methods=['PUT'])
def editarPaciente(pacienteId):
    Datos = []
    for paciente in Pacientes:
        if paciente.id == pacienteId:
            paciente.nombre = request.json['nombre']
            paciente.apellido = request.json['apellido']
            paciente.fechaNacimiento = request.json['fechaNacimiento']
            paciente.sexo = request.json['sexo']
            paciente.username = request.json['username']
            paciente.password = request.json['password']
            paciente.telefono = request.json['telefono']
            pacientee = {
                'Nombre': paciente.nombre,
                'Apellido': paciente.apellido,
                'Fecha Nacimiento': paciente.fechaNacimiento,
                'Sexo': paciente.sexo,
                'Username': paciente.username,
                'Passsword': paciente.password,
                'Telefono': paciente.telefono
            }
            Datos.append(pacientee)
            return jsonify({
                "message": "Paciente modificado",
                "paciente": Datos
            })
    if len(Datos) <= 0:
        return jsonify({
            "message": "No se encontro el paciente"
        })


@app.route('/modificarDoctor/<int:doctorId>', methods=['PUT'])
def editarDoctor(doctorId):
    Datos = []
    for doctor in Doctores:
        if doctor.id == doctorId:
            doctor.nombre = request.json['nombre']
            doctor.apellido = request.json['apellido']
            doctor.fechaNacimiento = request.json['fechaNacimiento']
            doctor.sexo = request.json['sexo']
            doctor.username = request.json['username']
            doctor.password = request.json['password']
            doctor.especialidad = request.json['especialidad']
            doctor.telefono = request.json['telefono']
            doctorr = {
                'Nombre': doctor.nombre,
                'Apellido': doctor.apellido,
                'FechaNacimiento': doctor.fechaNacimiento,
                'Sexo': doctor.sexo,
                'Username': doctor.username,
                'Passsword': doctor.password,
                'Especialidad': doctor.especialidad,
                'Telefono': doctor.telefono
            }
            Datos.append(doctorr)
            return jsonify({
                "message": "Doctor modificado",
                "doctor": Datos
            })
    if len(Datos) <= 0:
        return jsonify({
            "message": "No se encontro el doctor"
        })


@app.route('/modificarEnfermera/<int:enfermeraId>', methods=['PUT'])
def editarEnfermera(enfermeraId):
    Datos = []
    for enfermera in Enfermeras:
        if enfermera.id == enfermeraId:
            enfermera.nombre = request.json['nombre']
            enfermera.apellido = request.json['apellido']
            enfermera.fechaNacimiento = request.json['fechaNacimiento']
            enfermera.sexo = request.json['sexo']
            enfermera.username = request.json['username']
            enfermera.password = request.json['password']
            enfermera.telefono = request.json['telefono']
            enfermeraa = {
                'Nombre': enfermera.nombre,
                'Apellido': enfermera.apellido,
                'FechaNacimiento': enfermera.fechaNacimiento,
                'Sexo': enfermera.sexo,
                'Username': enfermera.username,
                'Passsword': enfermera.password,
                'Telefono': enfermera.telefono
            }
            Datos.append(enfermeraa)
            return jsonify({
                "message": "Enfermera modificada",
                "enfermera": Datos
            })
    if len(Datos) <= 0:
        return jsonify({
            "message": "No se encontro la enfermera"
        })


@app.route('/modificarMedicamento/<int:medId>', methods=['PUT'])
def editarMedicamento(medId):
    Datos = []
    for med in Medicamentos:
        if med.id == medId:
            med.nombre = request.json['nombre']
            med.precio = request.json['precio']
            med.descripcion = request.json['descripcion']
            med.cantidad = request.json['cantidad']
            medd = {
                'Nombre': med.nombre,
                'Precio': med.precio,
                'Descripcion': med.descripcion,
                'Cantidad': med.cantidad
            }
            Datos.append(medd)
            return jsonify({
                "message": "Medicamento modificado",
                "medicamento": Datos
            })
    if len(Datos) <= 0:
        return jsonify({
            "message": "No se encontro el medicamento"
        })
# ------------------------FUNCIONES-----------ELIMINAR-----------PACIENTE----------------------------------------


@app.route('/eliminarPaciente/<int:pacienteId>', methods=['DELETE'])
def eliminarPaciente(pacienteId):
    Datos = []
    for paciente in Pacientes:
        if paciente.id == pacienteId:
            pacientee = {
                'Nombre': paciente.nombre,
                'Apellido': paciente.apellido,
                'Fecha Nacimiento': paciente.fechaNacimiento,
                'Sexo': paciente.sexo,
                'Username': paciente.username,
                'Passsword': paciente.password,
                'Telefono': paciente.telefono
            }
            Pacientes.remove(paciente)
            return jsonify({
                "message": "Paciente eliminado"
            })
    if len(Datos) <= 0:
        return jsonify({
            "message": "No se encontro el paciente"
        })


@app.route('/eliminarDoctor/<int:doctorId>', methods=['DELETE'])
def eliminarDoctor(doctorId):
    Datos = []
    for doctor in Doctores:
        if doctor.id == doctorId:
            doctorr = {
                'Nombre': doctor.nombre,
                'Apellido': doctor.apellido,
                'Fecha Nacimiento': doctor.fechaNacimiento,
                'Sexo': doctor.sexo,
                'Username': doctor.username,
                'Passsword': doctor.password,
                'Especialidad': doctor.especialidad,
                'Telefono': doctor.telefono
            }
            Doctores.remove(doctor)
            return jsonify({
                "message": "Doctor eliminado"
            })
    if len(Datos) <= 0:
        return jsonify({
            "message": "No se encontro el paciente"
        })


@app.route('/eliminarEnfermera/<int:enfermeraId>', methods=['DELETE'])
def eliminarEnfermera(enfermeraId):
    Datos = []
    for enfermera in Enfermeras:
        if enfermera.id == enfermeraId:
            enfermeraa = {
                'Nombre': enfermera.nombre,
                'Apellido': enfermera.apellido,
                'Fecha Nacimiento': enfermera.fechaNacimiento,
                'Sexo': enfermera.sexo,
                'Username': enfermera.username,
                'Passsword': enfermera.password,
                'Telefono': enfermera.telefono
            }
            Enfermeras.remove(enfermera)
            return jsonify({
                "message": "Enfermera eliminada"
            })
    if len(Datos) <= 0:
        return jsonify({
            "message": "No se encontro la enfermera"
        })


@app.route('/eliminarMedicamento/<int:medId>', methods=['DELETE'])
def eliminarMedicamento(medId):
    Datos = []
    for medicamento in Medicamentos:
        if medicamento.id == medId:
            medicamentoo = {
                'Nombre': medicamento.nombre,
                'Precio': medicamento.precio,
                'Descripcion': medicamento.descripcion,
                'Cantidad': medicamento.cantidad
            }
            Medicamentos.remove(medicamento)
            return jsonify({
                "message": "Medicamento Eliminado"
            })
    if len(Datos) <= 0:
        return jsonify({
            "message": "No se encontro el medicamento"
        })

# ------------------------MODULO-----------PACIENTE---------------------------------------------------


@app.route('/moduloPaciente/solicitarCita', methods=['POST'])
def solicitarCita():
    global Citas
    contador_cita = len(Citas)
    idPaciente = request.json['idPaciente']
    fecha = request.json['fecha']
    hora = request.json['hora']
    motivo = request.json['motivo']
    estado = "Pendiente"
    doctor = ""
    for cita in Citas:
        if cita.idPaciente == idPaciente:
            if cita.estado == "Pendiente" or cita.estado == "Aceptada":
                return jsonify({
                    "message": "Repetido"
                })
    cita_agregada = {
        'IdPaciente': idPaciente,
        'Fecha': fecha,
        'Hora': hora,
        'Motivo': motivo,
        'Estado': estado,
        'Doctor': ''
    }
    contador_cita += 1
    Citas.append(Cita(contador_cita, idPaciente,
                 fecha, hora, motivo, estado, doctor))
    return jsonify({
        "message": "Cita creada exitosamente"
    })
# ----------------GET MEDICAMENTOS SOLO CON CANTIDAD DISPONIBLE-------------------------------


@app.route('/moduloPaciente/medicamentosCompra', methods=['GET'])
def getMedicamentosCompra():
    # return render_template("modAdmin.html")
    global Medicamentos
    Datos = []
    for med in Medicamentos:
        if int(med.cantidad) > 0:
            admin = {
                'Id': med.id,
                'Nombre': med.nombre,
                'Precio': med.precio,
                'Descripcion': med.descripcion,
                'Cantidad': med.cantidad,
            }
            Datos.append(admin)
    return jsonify({
        "message": "Medicamentos",
        "medicamentos": Datos
    })


@app.route('/moduloPaciente/agregarProductoPedido')
def agregarProductoPedido():
    global Productos
    nombreProducto = request.json['nombreProducto']
    precio = request.json['precio']
    cantidad = request.json['cantidad']
    subtotal = precio*cantidad
    producto_agregada = {
        'Nombre': nombreProducto,
        'Precio': precio,
        'Cantidad': cantidad,
        'Subtotal': subtotal
    }
    Productos.append(producto_agregada)
    return jsonify({
        "message": "Producto agregado al pedido"
    })


@app.route('/moduloPaciente/pedido', methods=['GET'])
def getProductosPedido():
    # return render_template("modAdmin.html")
    global Productos
    Datos = []
    for p in Productos:
        producto = {
            'Nombre': p.Nombre,
            'Precio': p.Precio,
            'Cantidad': p.Cantidad,
            'Subtotal': p.Subtotal
        }
        Datos.append(producto)
    return jsonify({
        "message": "Productos",
        "productos": Datos
    })


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        global Users
        username = request.form['username']
        password = request.form['password']
        print("hola")
        for user in Users:
            if user.username == username and user.password == password:
                if user.tipoUsuario == 0:
                    # return(jsonify(user.nombre))
                    return redirect(url_for('getAdmins'))

                if user.tipoUsuario == 3:
                    return redirect(url_for('getPacientes'))
                    # return jsonify({
                    #     "message":"HOLA USTED ES DOCTOR"
                    # })

    return render_template("login.html")


@app.route('/registroPaciente', methods=['POST'])
def registroPaciente():
    if request.method == 'POST':
        global Users, Pacientes
        contador_pacientes = len(Pacientes)
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        fechaNacimiento = request.json['fechaNacimiento']
        sexo = request.json['sexo']
        username = request.json['username']
        password = request.json['password']
        telefono = request.json['telefono']
        for user in Users:
            print(user.username)
            if username == user.username:
                return jsonify({
                    "message": "Este usuario ya existe"
                })
        if len(password) >= 8:
            contador_pacientes += 1
            Users.append(User(nombre, apellido, fechaNacimiento,
                         sexo, username, password, telefono, 3))
            Pacientes.append(Paciente(
                contador_pacientes, nombre, apellido, fechaNacimiento, sexo, username, password, telefono))
            return jsonify({
                "message": "Ok",
                "usuario": {"nombre": nombre, "apellido": apellido, "fechaNacimiento": fechaNacimiento, "sexo": sexo, "username": username, "password": password, "telefono": telefono}
            }), 200
        return jsonify({
            "message": "La contrasena debe al menos 8 caracteres"
        })


@app.route('/modificarPerfil/<string:username>', methods=['PUT'])
def modificarPerfil():
    userFound = [
        user for user in Users if user['username'] == username]
    if (len(userFound) > 0):
        userFound[0]['nombre'] = request.form['nombre']
        userFound[0]['price'] = request.json['price']
        userFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "User Updated",
            "product": userFound[0]
        })
        return jsonify({"messsage": "User not found"})

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
    # return render_template("modAdmin.html")
    global Users
    Datos = []
    for user in Users:
        admin = {
            'Nombre': user.nombre,
            'Apellido': user.appellido,
            'Telefono': user.telefono,
            'Usuario': user.username,
            'TipoUsuario': user.tipoUsuario,
            'Fecha Nacimiento': user.fechaNacimiento,
            'sexo': user.sexo
        }
        Datos.append(admin)
        # Datos.append(admin)

    return jsonify({
        "message": "Product Deleted",
        "product": Datos
    })


@app.route('/paciente')
def getPaciente():
    global Users
    Datos = []
    for user in Users:
        if user.username == username:
            paciente = {
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
