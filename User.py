class User:
    def __init__(self,nombre,apellido,fechaNacimiento,sexo,username,password,telefono,tipoUsuario):
        self.nombre=nombre
        self.appellido=apellido
        self.fechaNacimiento=fechaNacimiento
        self.sexo=sexo
        self.username=username
        self.password=password
        self.telefono=telefono
        self.tipoUsuario=tipoUsuario

##TIPOS DE USUARIO
## -----------0-------admin
##------------1-------doctor
##------------2-------enfermera
##------------3-------paciente
        