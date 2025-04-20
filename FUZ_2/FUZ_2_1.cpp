#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main()
{
double r=2;
int t=50;
double xn, xn1;

ofstream plik1("C:\\Users\\kacpe\\OneDrive\\Pulpit\\C_plus\\FUZ\\fuz2_1.txt");

double x0[9] = {0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9};

for (int j = 0; j<9; j++)
{
    xn = x0[j];
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