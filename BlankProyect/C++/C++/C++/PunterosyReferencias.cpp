#include <iostream>

using namespace std;


int suma(int* a,int* b) {
    return (*a + *b);
}

int main() {
   
    int x = 5;
    int* px = &x;

   /* cout << "Valor de x:" << x << endl;
    cout << "Direccion de x: " << &x << endl;*/
    cout << "valor de X: " << *px << endl; 
    cout << "Direccion de X: " << px << endl;

    int a = 8, b = 5;

    int valor = suma(&a,&b);

    cout << "Valor de x después de incrementar: " << valor << endl;
    
 

    delete &valor;

    
    cout << "Valor de x después de incrementar: " << valor << endl;
    return 0;
}



