#include <iostream>
#include <fstream>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <ctime>
#include <random>


using namespace std;

// 1. Jeśli dwa +, dwa - to dE zawsze 0
// 2. Jeśli 4 + to jeśli z +1 na -1 to dE = 8, jeśli z -1 na +1 to dE = -8
// 3. Jeśli 4 - to odwrotnie jak w punkcie 2.
// 4. Jeśli 3+, 1-, to jeśli z +1 na -1 to dE = 4, jeśli z -1 na +1 to dE = -4
// 5. Jeśli 3-, 1+ to odwrotnie niż w punkcie 4.

class RandomNumberGenerator {
    private:
        std::random_device rd;
        std::mt19937 gen;
        std::uniform_real_distribution<double> dist;
    
    public:
        // Konstruktor bezargumentowy
        RandomNumberGenerator()
            : gen(rd()), dist(0.0, 1.0) {}

        double get_random() { 
            return dist(gen);
        }
        
        int get_random_index(int min, int max) {
            std::uniform_int_distribution<int> dynamic_dist(min, max);
            return dynamic_dist(gen);
        }
    };

    double count_mag (const vector<vector<int>> &spintab, int N)
    {
        double mag = 0;
        for (int i=0; i<N; i++)
        {   
            for (int j = 0; j<N; j++)
            {
                mag += spintab[i][j]; 
            }
        }
        return mag/(N*N);
    }
    

int main ()
{
    RandomNumberGenerator rng;
    // cout<<rng.get_random();
    int N = 32;
    int MC = 100000;
    double T = 4;

    vector<vector<int>> spintab(N, vector<int>(N));
    double T_table[4] = {1, 2,  2.5, 4};
    double P_table[5][2];
    double otoczenie[5] = {4, 2, 0, -2, -4};

    // Tablice prawdopodobienstwa (zad 1)

    // //Spin up
    // for (int i = 0; i<5; i++)
    // {
    //     P_table[i][0] = exp(-otoczenie[i]*1/T);
    // }
    // //Spin down
    // for (int i = 0; i<5; i++)
    // {
    //     P_table[i][1] = exp(-otoczenie[i]*(-1)/T);
    // }
    // //Wypisz
    // for (int i = 0; i<5; i++)
    // {
    //     for (int j = 0; j<2; j++)
    //     {   
    //         if (P_table[i][j] >= 1) cout<<1<<" ";
    //         else cout<<P_table[i][j]<<" ";
    //     }
    //     cout<<endl;
    // }



    for (int i=0; i<N; i++)
    {
        for (int j=0; j<N; j++)
        {
            spintab[i][j] = 1;
        }
    }

    ofstream plik1("C:\\Users\\kacpe\\OneDrive\\Pulpit\\C_plus\\FUZ\\FUZ_6\\fuz6_3.txt");

    for (int k = 0; k<MC; k++)
    {

        double M = count_mag(spintab, N);
        plik1<<k<<" "<<M<<endl;
        cout<<k<<endl;

        for (int s = 0; s < N * N; ++s) 
        {
            int i = rng.get_random_index(0, N - 1);
            int j = rng.get_random_index(0, N - 1);

            int sum_neighbors = spintab[(i-1+N)%N][(j+N)%N] + spintab[(i+1+N)%N][(j+N)%N] + spintab[(i+N)%N][(j+1+N)%N] + spintab[(i+N)%N][(j-1+N)%N];
            int dE =  spintab[i][j] * sum_neighbors;

            if (dE <= 0)
            {
                spintab[i][j] *= (-1);
            }
            else if (rng.get_random()<exp((-2.0)*dE/T_table[2]))
                spintab[i][j] *= (-1); 
        }
 
    }

    ofstream plik2("C:\\Users\\kacpe\\OneDrive\\Pulpit\\C_plus\\FUZ\\FUZ_6\\fuz6_6.txt");
    for (int i=0; i<N; i++)
    {
        for (int j=0; j<N; j++)
        {
            plik2<<spintab[i][j]<<" ";
        }
        plik2<<endl;
    }

    return 0;
}

