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

// Jeśli po obu stronach mamy różne spiny to dE = 0, więc P = 100%
// Jeśli mamy te same spiny i środkowy zmieniamy na inny to dE = 4, więc P zależy od 1/T
// Jeśli mamy te same siny i środkowy zmieniamy  z różnego na ten sam to P = 100%


int zero_one ()
{
    int a = (std::rand()) % 2;
    if (a==0) a= -1;
    return a;
}

double uniform()
{
    return static_cast<double>(std::rand())/RAND_MAX;
}

double count_energy (const vector<int> &spintab, int N)
{
    double ene = 0;
    for (int i=0; i<N; i++)
    {   
        ene += (-1) * spintab[i] * spintab[(i+1)%N];
    }
    return ene/N;
}

double count_mag (const vector<int> &spintab, int N)
{
    double mag =0;
    for (int i=0; i<N; i++)
    {   
        mag += spintab[i]; 
    }
    return mag/N;
}


int main ()
{
    std::srand(std::time(nullptr));
    int N = 1000;
    int MC = 10000;
    vector<int> spintab(N);
    for (int i=0; i<N; i++)
    {
        spintab[i] = zero_one();
    }
    
    double start = 0.5, end = 4.0, step = 0.1;
    std::vector<double> Ttab;

    for (double i = start; i <= end; i += step) {
        Ttab.push_back(i);
    }


    std::ofstream plik1("C:\\Users\\kacpe\\OneDrive\\Pulpit\\C_plus\\FUZ\\FUZ_5\\fuz_zad3.txt");

    for (int i = 0; i<Ttab.size(); i++)
    {
        double ene = 0, ene2 = 0, Mag = 0;
        for (int k = 0; k<MC; k++)
        {   

            for (int j=0; j<N; j++)
            {
                // int j = (std::rand()) % N;
                int sum_neighbors = spintab[(j - 1 + N) % N] + spintab[(j + 1) % N];
                int dE = 2 * spintab[j] * sum_neighbors;


                if (uniform()<exp((-1)*Ttab[i]*dE))
                    spintab[j] *= (-1);
                
            }
            if (k>9000)
            {   
                double a = count_energy(spintab, N);
                ene += a;
                ene2 += a*a;
            }

         }
     double E = ene;
     double E2 = ene2;
     cout<<i<<" ";
     plik1<<Ttab[i]<<" "<<E<<" "<<E2<<endl;

     }



    return 0;

}