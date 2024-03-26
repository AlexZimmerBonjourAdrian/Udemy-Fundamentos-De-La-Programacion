#include <iostream>

using namespace std;

void sumar(int*);

int main() {
 
     int x = 4;
	cout << " " << endl;
    //valor
	cout << "Valor de x:" << x << endl;
	//direccion de memoria
	cout << "Direccion de memoria de x:" << &x << endl;
	cout << " " << endl;

    //Crea un puntero apuntando a la direccion del 4
    
    // asignar un punter 
    int* px = &x;
	 cout << " " << endl;
    cout << "Valor de x:" << x << endl;
    cout << "Valor de x:" << *px << endl;
    cout << " " << endl;
    
    //un puntero que apunta a una referencia
    int** ppx = &px;
   cout << " " << endl;
    cout << "Valor de x:" << x << endl;
    cout << "Valor de x: " << *px << endl;
    cout << "Valor de x: " << **ppx << endl;
   cout << " " << endl;
    int n = 4;
    sumar(&n);
    std::cout << n << std::endl;
    std::cout << n << std::endl;
    std::cout << n << std::endl;
    system("pause");
    
    int n = 4;
    sumar(&n);
    cout << n << endl;
    sumar(&n);
    cout << n << endl;
    sumar(&n);
    cout << n << endl;
    system("Pause");


    return 0;
}

void sumar(int* x)
{
    *x = *x + 1;
    cout << *x << endl;
}



