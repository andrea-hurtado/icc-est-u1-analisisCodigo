import java.util.Random;

public class Benchmarking {
    public Benchmarking(){
        long inicioMillis = System.currentTimeMillis(); //Fecha de referencia 
        //long inicioNano = System.nanoTime();

        //System.out.println(inicioMillis);
       // System.out.println(inicioNano);

        metodosOrdenamiento = new MetodosOrdenamiento();
        int [] arreglo = generarArregloAleatorio(tamano:100000);
        Runnable tarea = () metodosOrdenamiento.burbujaTradicional(arreglo);

        double tiempoNano = medirConNanoTime(tarea);
        double tiempoMillis = medirConCurrentTime(tarea);

        System.out.println("Tiempo con nanoTime: " + tiempoNano + "se");
        System.out.println("Tiempo")

    }

    private int[] generarArregloAleatorio(int tamaño){
        int [] arreglo = new int [tamaño];
        Random random  = new Random();
        for (int i = 0; i < tamaño; i++){
            arreglo [i] = random.nextInt(100_000);
        }
        //valores entre 0 y 99,999
        return new int[] {};

    }

    //Tiempo usando nanoTime (en segundos)
    public double medirNanoTime(Runnable tarea){
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin - inicio) / 1_000_000_000.0;

    }
    //Tiempos usando currentTimeMillis (en segundos)
    public double medirConCurrentTime(Runnable tarea){
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        return (fin - inicio) / 1000.0;

    }

}
