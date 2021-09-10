class Usuario:

    def __init__(self,nombre,apellidos,genero,tipo,cedula,correo,contrasenia):
        self._nombre = nombre
        self._apellidos = apellidos
        self._genero = genero
        self._tipo = tipo
        self._cedula = cedula
        self._correo = correo
        self._contrasenia = contrasenia

    def getCorreo(self):
        return self._correo

    def getContrasenia(self):
        return self._contrasenia
    
    def toString(self):
        return self._nombre+' : '+self._apellidos+' : '+self._genero+' : '+self._cedula+' : '+self._correo+' : '+self._contrasenia+' : '+self._tipo

    def toString2(self):
        return self._correo+' : '+self._contrasenia
    """

    
    def __str__(self):
        return self.nombre +" : "+self.apellidos +" : "+self.genero +" : "+self.cedula +" : "+self.correo +" : "+self.contrasenia
    """