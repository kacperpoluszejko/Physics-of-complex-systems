
#include <iostream>
#include <fstream>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <conio.h>
#include <math.h>
#include <vector>



int main ()
{
    int N;
    N = 5;
    int tablica[N][N];

    for (int i = 0; i < N ; i++)
    {
        for (int j = 0; j< N; j++)
        {
            if (i!=j)
                tablica[i][j] = 1;
            else
                tablica[i][j] = 0;
        }
    }

    std::ofstream plik1;
    plik1.open("C:\\Users\\kacpe\\OneDrive\\Pulpit\\fuz0.txt");

    for (int i = 0; i < N; i++)
    {
        for (int j =0; j < N; j++)
        {
           // std::cout<<tablica[i][j]<<'\n';
            plik1<<tablica[i][j]<<" ";
        }
    }

    int suma;
    double rozklad[N] = {0};

    for (int i = 0; i < N; i++)
    {
        suma = 0;
        for (int j = 0; j < N; j++ )
        {
            if (tablica[i][j] != 0)
            {
                suma += 1;
            }
        }
        rozklad[suma] += 1;
    }

    std::ofstream plik2;
    plik2.open("C:\\Users\\kacpe\\OneDrive\\Pulpit\\fuz0_0.txt");

    for (int  i = 0; i<(N); i++)
    {
        std::cout<<rozklad[i]/N<<" "<<i<<'\n';
        plik2<<rozklad[i]/N<<" "<<i<<'\n';

    }
}
