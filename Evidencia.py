class MaquinaInyeccionCera:
    def __init__(self, marca, modelo, capacidad_cera):
        self._marca = marca
        self._modelo = modelo
        self._capacidad_cera = capacidad_cera
        self._cera_actual = 0
        self._temperatura = 1
    
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

    @property
    def temperatura(self):
        return self._temperatura
    
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
        
    def calentar_cera(self, incremento):
        if incremento < 0:
            return "El incremento de la temperatura debe ser positivo"
        if self._temperatura + incremento > 100:
            self._temperatura = 100
            return f"No se puede calentar más. La temperatura máxima es de 100°C. Temperatura actual: {self._temperatura}°C."
        else:
            self._temperatura += incremento
            return f"Calentando cera a {self._temperatura}°C."

    def __str__(self):
        return (f"Maquina de Inyección de Cera\n"
                f"Marca: {self._marca}\n"
                f"Modelo: {self._modelo}\n"
                f"Capacidad de Cera: {self._capacidad_cera}g\n"
                f"Cera Actual: {self._cera_actual}g\n"
                f"Temperatura: {self._temperatura}°C")

# Ejemplo de uso
maquina_cera = MaquinaInyeccionCera("Kaya Cast", "2.0", 300)
print(maquina_cera)

maquina_cera = MaquinaInyeccionCera('Memco','3.0', 250)
print(maquina_cera)


#Formas manuelas de de ver los comportamientos por separado:

""" # Cargar cera
resultado_carga = maquina_cera.cargar_cera(300)
print(resultado_carga)  

# Inyectar cera
resultado_inyeccion = maquina_cera.inyectar_cera(100)
print(resultado_inyeccion) 

# Calentar cera dentro del límite
resultado_calentar = maquina_cera.calentar_cera(70)
print(resultado_calentar)

# Intentar calentar más allá del límite
resultado_calentar_exceso = maquina_cera.calentar_cera(50)
print(resultado_calentar_exceso)
 """