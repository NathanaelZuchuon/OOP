#include <iostream>
using namespace std;

void fact(int n) {

    int fact=1;

    for(int i=1;i<=n;i++){
        fact*=i;
    }

    cout << "Le factoriel de " << n << " est " << fact << endl;

}

int getInput() {

    cout << "Entrer un nombre: ";

    return cin >>;
}

int main() {

    int n;

    while(true) {
        n = getInput();
        fact(n);
    }

    return 0;
}