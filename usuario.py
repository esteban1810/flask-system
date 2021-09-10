class Usuario:
    
    def __init__(self,nombre,apellidos,genero,cedula,correo,contrasenia):
        self.nombre = nombre
        self.apellidos = apellidos
        self.genero = genero
        self.cedula = cedula
        self.correo = correo
        self.contrasenia = contrasenia

    
    def toString(self):
        return self.nombre+' : '+self.apellidos+' : '+self.genero+' : '+self.cedula+' : '+self.correo+' : '+self.contrasenia
        
    """

    
    def __str__(self):
        return self.nombre +" : "+self.apellidos +" : "+self.genero +" : "+self.cedula +" : "+self.correo +" : "+self.contrasenia
    """