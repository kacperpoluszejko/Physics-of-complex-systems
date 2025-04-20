#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main()
{
double x0=0.5;
int t=10000;
double xn, xn1, r;

ofstream plik1("C:\\Users\\kacpe\\OneDrive\\Pulpit\\C_plus\\FUZ\\fuz2_3.txt");

double r_table[601];

for (int i =0; i<601; i++)
{
    r_table[i] = 0.005*i+1;
}


for (int j = 0; j<601; j++)
{
    xn=x0;
    r = r_table[j];
    // cout<<j;
    for (int i=0; i<=t; i++)
    {
        if (i>9000) plik1<<r<<" "<<xn<<endl;

        xn1 = r*xn*(1-xn);
        xn=xn1;

    }
    plik1<<endl;
}
cout<<"Koniec";

return 0;
}