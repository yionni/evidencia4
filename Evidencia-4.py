class MaquinaInyeccionCera:
    def __init__(self, marca, modelo, capacidad_cera):
        self._marca = marca
        self._modelo = modelo
        self._capacidad_cera = capacidad_cera
        self._cera_actual = 0
    
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, nueva_marca):
        if isinstance(nueva_marca, str):
            self._marca = nueva_marca
        else:
            raise ValueError("La marca debe ser una cadena de texto.")
    
    @property
    def capacidad_cera(self):
        return self._capacidad_cera

    @capacidad_cera.setter
    def capacidad_cera(self, nueva_capacidad):
        if nueva_capacidad > 0:
            self._capacidad_cera = nueva_capacidad
        else:
            raise ValueError("La capacidad debe ser un valor positivo.")
    
    @property
    def cera_actual(self):
        return self._cera_actual

    def cargar_cera(self, cantidad):
        if cantidad + self._cera_actual > self._capacidad_cera:
            return f"No se puede cargar {cantidad}g de cera. Excede la capacidad máxima de {self._capacidad_cera}g."
        else:
            self._cera_actual += cantidad
            return f"{cantidad}g de cera cargados. Cera actual: {self._cera_actual}g."
    
    def inyectar_cera(self, cantidad):
        if cantidad > self._cera_actual:
            return f"No hay suficiente cera para inyectar. Cera disponible: {self._cera_actual}g."
        else:
            self._cera_actual -= cantidad
            return f"Inyectando {cantidad}g de cera. Cera restante: {self._cera_actual}g."
        
maquina_cera = MaquinaInyeccionCera("Kaya Cast", "2.0", 300)

# Cargar cera
resultado_carga = maquina_cera.cargar_cera(300)
print(resultado_carga)  

# Inyectar cera
resultado_inyeccion = maquina_cera.inyectar_cera(100)
print(resultado_inyeccion)  

