import sys
sys.path.append("./src_python")

import random
import time 
from metodos_ordenamiento import MetodosOrdenamiento

class Benchmarking:
    def init (self):
        print("Bench inicializado")

    def ejemplo(self): 
        self.mOrdenamiento=MetodosOrdenamiento()

        arreglo= self.build_arreglo(1000)

        tarea=lambda: self.mOrdenamiento.sortByBubble(arreglo)
        timepoMilis= self.contar_con_current_time_miles(tarea)
        tiempoNano=self.contar_con_nano_time(tarea)

        print (f"Tiempo {timepoMilis}segundos")
        print (f"Tiempo{tiempoNano}segundos")


    def build_arreglo(self, tamano):
        array = []
        for i in range(tamano):
            n = random.randint(0,99999)

            array.append(n)
        return array


    def contar_con_current_time_miles(self, tarea):
        inicio= time.time ()
        tarea()
        final=time.time()
        return (final-inicio)/1000


    def contar_con_nano_time(self, tarea):
        inicio= time.time_ns()
        tarea()
        final=time.time_ns()
        return (final-inicio)/1000000