#include <iostream>
#include <fstream>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <conio.h>
#include <math.h>
#include <vector>
#include <ctime>

using namespace std;

int main()
{
    int N = 11;
    int tablica[N][N];

    for (int i=0; i<N; i++)
    {
        for (int j=0; j<N; j++)
        {
            if((i+j)%2 ==0)
            tablica[i][j]=0;
            else
            tablica[i][j]=1;
        }
    }


    // for (int i=0; i<5; i++)
    // {
    //     for (int j=0; j<5; j++)
    //     {
    //         tablica[3+i][3+j] = 1;
    //     }
    // }


    std::ofstream plik1;
    plik1.open("C:\\Users\\kacpe\\OneDrive\\Pulpit\\C_plus\\FUZ\\fuz0_3.txt");

    for (int i=0; i<N; i++)
    {
        for (int j=0; j<N; j++)
        {
            plik1<<tablica[i][j]<<" ";
            cout<<tablica[i][j]<<" ";
        }
        plik1<<endl;
        cout<<endl;
    }

    cout<<"Koniec";
}

