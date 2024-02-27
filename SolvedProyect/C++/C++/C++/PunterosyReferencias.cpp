#include <iostream>

int suma(int& a, int& b) {
    return a + b;
}

int main() {
    int x = 5;
    int* px = &x; // creamos un puntero que apunta a la variable x //& esto se usa para hacer referencia a una direccion de memoria que apunta a una variable


    std::cout << "Valor de x: " << x << std::endl;
    std::cout << "Dirección de x: " << &x << std::endl;
    std::cout << "Valor de px: " << *px << std::endl;

    int a, b = 5;
    int resultado = suma(a, b);
    std::cout << "Valor de suma en direccion de memoria: " << suma(a, b) << std::endl;
    std::cout << "Valor de suma en entero: " << resultado << std::endl;

    
    return 0;
}

int examplePointer()
{
    int* p; // p es un puntero a un entero
    int x = 5;
    int* p = &x; // p es un puntero que apunta a la dirección de memoria de x
        
    int x = 5;
    int* p = &x;
    std::cout << *p; // imprime el valor de x (5)

    int valor = *p; // copia el valor a la direccion *p

    int x = 5;
    int* p = &x;
    *p = 10; // cambia el valor de x a 10

    int arr[5];
    int* p = arr; // p es un puntero que apunta al primer elemento de arr
    int* p = &arr[0]; // p es un puntero que apunta al array completo, para recorrerlo

    int i = 0;
    int valor = *(p + i); // valor es igual al i-esimo elemento de arr
   

    int x_2 = 5;
    int& r = x_2; // r es una referencia a x

    int r_2 = x_2;
    int* valor_2 = &r_2; // valor es igual a 5

    int arr[5];
    int& r = arr[0]; // r es una referencia al primer elemento de arr

    
    int x = 5;
    const int& r_3 = x; // r es una referencia constante a x
    int** p; // p es un puntero a un puntero a un entero

    void funcion(int x);
    void (*p)(int) = funcion; // p apunta a la función funcion

}

struct Persona {
    int edad;
    char nombre[20];
};
Persona persona;
Persona* p = &persona; // p apunta a la estructura persona


class Clase {
public:
    void metodo();
};
Clase obj;
Clase* p = &obj; // p apunta al objeto obj