import json
from User import User
from Doctor import Doctor
from Medicamento import Medicamento
from Paciente import Paciente
from Enfermera import Enfermera
from Cita import Cita
from Pedido import Pedido
from Factura import Factura
from Receta import Receta
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
Facturas = []
Recetas = []


# CREANDO USUARIO ADMINISTRADO
Users.append(User(0,"Cesar", "Reyes", "01-01-01",
             "M", "admin", "1234", "12345678", 0))
Users.append(User(1,"Ariel", "Bautista", "01-01-01",
             "M", "admin2", "1234", "12345678", 0))

# ----------------------------CARGAS--------MASIVAS-----------------------------------------------------------------


@app.route('/cargarPacientes', methods=['POST'])
def cargaMasiva():
    global Pacientes
    contador_pacientes = len(Pacientes)
    usuariosCM = request.json["usuarios"]
    # print (usuariosCM)
    for paciente in usuariosCM:
        contador_pacientes += 1
        nombre = paciente['nombre']
        apellido = paciente['apellido']
        fechaNacimiento = paciente['fecha']
        sexo = paciente['genero']
        username = paciente['usuario']
        password = paciente['password']
        telefono = paciente['telefono']
        Users.append(User(contador_pacientes,nombre, apellido, fechaNacimiento,
                          sexo, username, password, telefono, 3))
        Pacientes.append(Paciente(
            contador_pacientes, nombre, apellido, fechaNacimiento, sexo, username, password, telefono))
    return jsonify({
        "mensaje": "OK"
    })


@app.route('/cargarDoctores', methods=['POST'])
def cargaMasivaDoctores():
    global Doctores
    contador_doctores = len(Doctores)
    docs = request.json["doctores"]
    # print (usuariosCM)
    for doctor in docs:
        contador_doctores += 1
        nombre = doctor['nombre']
        apellido = doctor['apellido']
        fechaNacimiento = doctor['fecha']
        sexo = doctor['genero']
        username = doctor['usuario']
        password = doctor['password']
        especialidad = doctor['especialidad']
        telefono = doctor['telefono']
        Users.append(User(contador_doctores,nombre, apellido, fechaNacimiento,
                          sexo, username, password, telefono, 1))
        Doctores.append(Doctor(contador_doctores, nombre, apellido, fechaNacimiento,
                               sexo, username, password, especialidad, telefono))
    return jsonify({
        "mensaje": "OK"
    })


@app.route('/cargarEnfermeras', methods=['POST'])
def cargaMasivaEnfermeras():
    global Enfermeras
    contador_enfermeras = len(Enfermeras)
    enfers = request.json["enfermeras"]
    # print (usuariosCM)
    for enfermera in enfers:
        contador_enfermeras += 1
        nombre = enfermera['nombre']
        apellido = enfermera['apellido']
        fechaNacimiento = enfermera['fecha']
        sexo = enfermera['genero']
        username = enfermera['usuario']
        password = enfermera['password']
        telefono = enfermera['telefono']
        Users.append(User(contador_enfermeras,nombre, apellido, fechaNacimiento,
                          sexo, username, password, telefono, 2))
        Enfermeras.append(Enfermera(
            contador_enfermeras, nombre, apellido, fechaNacimiento, sexo, username, password, telefono))
    return jsonify({
        "mensaje": "OK"
    })


@app.route('/cargarMedicamentos', methods=['POST'])
def cargaMasivaMedicamentos():
    global Medicamentos
    contador_med = len(Medicamentos)
    meds = request.json["medicamentos"]
    # print (usuariosCM)
    for med in meds:
        contador_med += 1
        nombre = med['nombre']
        precio = med['precio']
        descripcion = med['descripcion']
        cantidad = med['cantidad']
        Medicamentos.append(Medicamento(
            contador_med, nombre, precio, descripcion, cantidad))
    return jsonify({
        "mensaje": "OK"
    })
# ---------------------------------------------------------------------------------------------------------------------


@app.route('/users')
def getUsuarios():
    global Users
    Datos = []
    for user in Users:
        userr = {
            'Id':user.id,
            'Nombre': user.nombre,
            'Apellido': user.apellido,
            'FechaNacimiento': user.fechaNacimiento,
            'Sexo': user.sexo,
            'Username': user.username,
            'Password': user.password,
            'Telefono': user.telefono,
            'TipoUsuario': user.tipoUsuario
        }
        Datos.append(userr)

    return jsonify({
        "message": "Usuarios",
        "usuarios": Datos
    })


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
            'Estado': cita.estado,
            'Doctor': cita.doctor
        }
        Datos.append(citaa)
        # Datos.append(admin)
    return jsonify({
        "message": "Citas",
        "product": Datos
    })

@app.route('/pedidos', methods=['GET'])
def getPedidos():
    # return render_template("modAdmin.html")
    global Pedidos
    Datos = []
    for pedido in Pedidos:
        ped = {
            'Id': pedido.id,
            'IdProducto': pedido.idProducto,
            'Nombre': pedido.nombreProducto,
            'Cantidad': pedido.cantidad,
            'Total': pedido.total
        }
        Datos.append(ped)
        # Datos.append(admin)
    return jsonify({
        "message": "Pedidos",
        "pedidos": Datos
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
                'Password': doctor.password,
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
                'Id':enfermera.id,
                'Nombre': enfermera.nombre,
                'Apellido': enfermera.apellido,
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
                'Estado': cita.estado,
                'Doctor': cita.doctor
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


@app.route('/modificarCita/<int:citaId>', methods=['PUT'])
def editarCita(citaId):
    Datos = []
    for cita in Citas:
        if cita.id == citaId:
            cita.estado = "Aceptada"
            cita.doctor = request.json['doctor']
            est = {
                'Estado': cita.estado,
                'Doctor': cita.doctor
            }
            Datos.append(est)
            return jsonify({
                "message": "Cita modificada"
            })
    if len(Datos) <= 0:
        return jsonify({
            "message": "No se encontro la cita"
        })


@app.route('/rechazarCita/<int:citaId>', methods=['PUT'])
def rechazarCita(citaId):
    Datos = []
    for cita in Citas:
        if cita.id == citaId:
            cita.estado = "Rechazada"
            est = {
                'Estado': cita.estado,
            }
            Datos.append(est)
            return jsonify({
                "message": "Cita modificada"
            })
    if len(Datos) <= 0:
        return jsonify({
            "message": "No se encontro la cita"
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


@app.route('/moduloPaciente/agregarProductoPedido', methods=['POST'])
def agregarProductoPedido():
    global Pedidos
    contador = len(Pedidos)
    idProducto = request.json['idProducto']
    nombreProducto = request.json['nombreProducto']
    cantidad = request.json['cantidad']
    # subtotal = request.json['subtotal']
    total = request.json['total']
    contador += 1
    pedido = {
        'Id': contador,
        'IdProducto': idProducto,
        'Nombre': nombreProducto,
        'Cantidad': cantidad,
        'Total': total
    }
    Pedidos.append(Pedido(contador, idProducto,
                          nombreProducto, cantidad, total))
    return jsonify({
        "message": "Producto agregado al pedido"
    })


@app.route('/moduloPaciente/pedido', methods=['GET'])
def getProductosPedido():
    # return render_template("modAdmin.html")
    global Pedidos
    Datos = []
    for p in Pedidos:
        pedido = {
            'Id': p.idProducto,
            'Nombre': p.nombreProducto,
            'Cantidad': p.cantidad,
            'Total': p.total
        }
        Datos.append(pedido)
    return jsonify({
        "message": "Productos",
        "pedidos": Datos
    })

    # -----------------------------------------MODULO------------ENFERMERA--------------------------------------------


@app.route('/moduloEnfermera/citasPendientes', methods=['GET'])
def getCitasEnfermera():
    global Citas
    Datos = []
    for cita in Citas:
        if cita.estado == "Pendiente":
            citaa = {
                'Id': cita.id,
                'IdPaciente': cita.idPaciente,
                'Fecha': cita.fecha,
                'Hora': cita.hora,
                'Motivo': cita.motivo,
                'Estado': cita.estado,
                'Doctor': cita.doctor
            }
            Datos.append(citaa)
        # Datos.append(admin)
    return jsonify({
        "message": "Citas",
        "citas": Datos
    })


@app.route('/moduloEnfermera/citasAceptadas', methods=['GET'])
def getCitasAceptadasEnfermera():
    global Citas
    Datos = []
    for cita in Citas:
        if cita.estado == "Aceptada":
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
        "citas": Datos
    })


@app.route('/moduloEnfermera/crearFactura', methods=['POST'])
def agregarFactura():
    global Facturas
    contador_fac = len(Facturas)
    Datos = []
    fecha = request.json['fecha']
    nombre = request.json['nombre']
    doctor = request.json['doctor']
    precioConsulta = request.json['precioConsulta']
    costoOperacion = request.json['costoOperacion']
    costoInter = request.json['costoInter']
    total = request.json['total']
    contador_fac += 1
    facturaa = {
        'Id': contador_fac,
        'Fecha': fecha,
        'Nombre': nombre,
        'Doctor': doctor,
        'PrecioConsulta': precioConsulta,
        'CostoOperacion': costoOperacion,
        'CostoInter': costoInter,
        'Total': total
    }
    Datos.append(facturaa)
    Facturas.append(Factura(contador_fac, fecha, nombre,
                    doctor, costoOperacion, costoInter, total))
    return jsonify({
        "message": "Factura agregada",
        "factura": Datos
    })


@app.route('/moduloEnfermera/facturas', methods=['GET'])
def getfacturas():
    global Facturas
    Datos = []
    for factura in Facturas:
        facturaa = {
            'Id': factura.id,
            'Fecha': factura.fecha,
            'Nombre': factura.nombre,
            'Doctor': factura.doctor,
            'CostoOperacion': factura.costoOperacion,
            'CostoInternado': factura.costoInter,
            'Total': factura.total
        }
        Datos.append(facturaa)
        # Datos.append(admin)
    return jsonify({
        "message": "Facturas",
        "facturas": Datos
    })

    # -------------------------------------------------------------------------------------------------------------

    # --------------------------MODULO-----------------DOCTOR------------------------------------------------------------------


@app.route('/moduloDoctor/crearReceta', methods=['POST'])
def crearReceta():
    global Recetas
    contador_rec = len(Recetas)
    Datos = []
    fecha = request.json['fecha']
    nombre = request.json['nombre']
    padecimiento = request.json['padecimiento']
    descripcion = request.json['descripcion']
    contador_rec += 1
    recetaa = {
        'Id': contador_rec,
        'Fecha': fecha,
        'Nombre': nombre,
        'Padecimiento': padecimiento,
        'Descripcion': descripcion
    }
    Datos.append(recetaa)
    Recetas.append(Receta(contador_rec, fecha,
                   nombre, padecimiento, descripcion))
    return jsonify({
        "message": "Receta agregada",
        "receta": Datos
    })


@app.route('/moduloDoctor/recetas', methods=['GET'])
def getRecetas():
    global Recetas
    Datos = []
    for receta in Recetas:
        recetaa = {
            'Id': receta.id,
            'Fecha': receta.fecha,
            'Nombre': receta.nombre,
            'Padecimiento': receta.padecimiento,
            'Descripcion': receta.descripcion
        }
        Datos.append(recetaa)
        # Datos.append(admin)
    return jsonify({
        "message": "Recetas",
        "recetas": Datos
    })


@app.route('/moduloDoctor/citas/<string:doctor>', methods=['GET'])
def getCitasDoctor(doctor):
    global Citas
    Datos = []
    for cita in Citas:
        if cita.doctor == doctor:
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
        "citas": Datos
    })


@app.route('/modificarCitaDoctor/<int:citaId>', methods=['PUT'])
def editarCitaDoc(citaId):
    Datos = []
    for cita in Citas:
        if cita.id == citaId:
            cita.estado = "Completada"
            est = {
                'Estado': cita.estado
            }
            Datos.append(est)
            return jsonify({
                "message": "Cita modificada"
            })
    if len(Datos) <= 0:
        return jsonify({
            "message": "No se encontro la cita"
        })


@app.route('/noModificarCitaDoctor/<int:citaId>', methods=['PUT'])
def noEditarCitaDoc(citaId):
    Datos = []
    for cita in Citas:
        if cita.id == citaId:
            cita.estado = "Aceptada"
            est = {
                'Estado': cita.estado
            }
            Datos.append(est)
            return jsonify({
                "message": "Cita modificada"
            })
    if len(Datos) <= 0:
        return jsonify({
            "message": "No se encontro la cita"
        })

    # -------------------------------------------------------------------------------------------------------------


@app.route('/login', methods=['POST'])
def login():
    Datos = []
    if request.method == 'POST':
        global Users
        username = request.json['username']
        password = request.json['password']
        print(username)
        print(password)
        for user in Users:
            if user.username == username and user.password == password:
                userr = {
                    'Id':user.id,
                    'Nombre': user.nombre,
                    'Apellido': user.apellido,
                    'FechaNacimiento': user.fechaNacimiento,
                    'Sexo': user.sexo,
                    'Username': user.username,
                    'Password': user.password,
                    'Telefono': user.telefono,
                    'TipoUsuario': user.tipoUsuario
                }
                Datos.append(userr)
        if len(Datos) > 0:
            return jsonify({
                "message": "Correcto",
                "usuario": Datos
            })
        if len(Datos) <= 0:
            return jsonify({
                "message": "Incorrecto"
            })

        # return jsonify({
        #     "message":"HOLA USTED ES DOCTOR"
        # })


@app.route('/registroPaciente', methods=['POST'])
def registroPaciente():
    if request.method == 'POST':
        global Users, Pacientes
        contador_pacientes = len(Pacientes)
        contador_usuarios = len(Users)
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
            contador_usuarios+=1
            Users.append(User(contador_usuarios,nombre, apellido, fechaNacimiento,
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
