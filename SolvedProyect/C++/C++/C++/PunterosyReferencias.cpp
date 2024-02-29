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


