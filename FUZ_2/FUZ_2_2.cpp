#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main()
{
double x0=0.5;
int t=100;
double xn, xn1, r;

ofstream plik1("C:\\Users\\kacpe\\OneDrive\\Pulpit\\Programming\\FUZ\\FUZ_2\\fuz2_2.txt");
if(!plik1.is_open()) {
    cout << "Nie mozna otworzyc pliku!\n";
    return 1;
}


double r_table[6] = {1, 2, 3, 3.5, 3.55, 3.6};


for (int j = 0; j<6; j++)
{
    xn=x0;
    r = r_table[j];
    for (int i=0; i<t; i++)
    {
        plik1<<i<<" "<<xn<<endl;
        xn1 = r*xn*(1-xn);
        xn=xn1;

    }
    plik1<<endl;
}
cout<<"Koniec";

return 0;
}