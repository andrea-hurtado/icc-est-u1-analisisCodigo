from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento

def medir_tiempo(metodo, arreglo, benchmark):
    tarea = lambda: metodo(arreglo.copy())
    return benchmark.contar_con_current_time_miles(tarea)

if __name__ == "__main__":
    print("funciona")

    benchmark = Benchmarking()
    metodos_instancia = MetodosOrdenamiento()

    tam = 10000
    arreglo_base = benchmark.build_arreglo(tam)

    metodos = {
        "burbuja": metodos_instancia.sort_bubble,
        "seleccion": metodos_instancia.sort_seleccion,
    }

    resultados = []
    for nombre, metodo in metodos.items():
        tiempo = medir_tiempo(metodo, arreglo_base, benchmark)
        tupla_resultado = (tam, nombre, tiempo)
        resultados.append(tupla_resultado)

    for resultado in resultados:
        tam, nombre, tiempo = resultado
        print(f"Tamaño: {tam}, Método: {nombre}, Tiempo: {tiempo:.6f} segundos")
