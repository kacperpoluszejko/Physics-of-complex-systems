#include <iostream>
#include <fstream>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <conio.h>
#include <math.h>
#include <vector>
#include <ctime>


int main ()
{
    int N;
    N = 50;
    double propability = 1.0/3.0;

    std::srand(static_cast<unsigned>(std::time(0)));
    double a = static_cast<double>(std::rand()) / RAND_MAX;

    std::vector<std::vector<int>> lista(N);


    for (int i = 0; i<N; i++)
    {
        for (int j = i+1; j<N; j++)
        {
            double a = static_cast<double>(std::rand()) / RAND_MAX;
            if(a<propability)
            {
                lista[i].push_back(j);
                lista[j].push_back(i);
            }
        }
    }

    for (int i=0; i<N; i++)
    {
        std::cout<<"Wierzcholek: "<<i<<" Krawedzie: ";
        for(int j = 0; j<lista[i].size(); j++)
        {
            std::cout<<lista[i][j]<<" ";
        }
        std::cout<<std::endl;
    }

    int rozklad[N] = {0};

    for (int i=0; i<N; i++)
    {
        int elementy;
        elementy = lista[i].size();
        rozklad[elementy] += 1;
    }

    std::ofstream plik2;
    plik2.open("C:\\Users\\kacpe\\OneDrive\\Pulpit\\fuz0_0.txt");

        for (int i=0; i<N; i++)
    {
        std::cout<<"Rozklad: "<<i<<" - "<<rozklad[i]<<std::endl;
        plik2<<"Rozklad: "<<i<<" - "<<rozklad[i]<<std::endl;
    }



    return 0;


}
