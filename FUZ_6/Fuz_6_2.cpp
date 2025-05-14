#include <iostream>
#include <fstream>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <ctime>
#include <random>


using namespace std;


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
        return mag;
    }
    

int main ()
{
    RandomNumberGenerator rng;
    // cout<<rng.get_random();
    int N = 32;
    int MC = 10000;
    double T = 4;

    vector<vector<int>> spintab(N, vector<int>(N));
    double T_table[4] = {1, 2,  2.5, 4};
    double P_table[5][2];
    double otoczenie[5] = {4, 2, 0, -2, -4};


    for (int i=0; i<N; i++)
    {
        for (int j=0; j<N; j++)
        {
            spintab[i][j] = 1;
        }
    }

      
    double start = 0.25, end = 4.0, step = 0.25;
    std::vector<double> Ttab;

    for (double i = start; i <= end; i += step) {
        Ttab.push_back(i);
    }

    ofstream plik1("C:\\Users\\kacpe\\OneDrive\\Pulpit\\C_plus\\FUZ\\FUZ_6\\fuz6_zad4.txt");

    for (int t = 0; t<Ttab.size(); t++)
    {
        double mag=0, mag2 = 0;

        for (int k = 0; k<MC; k++)
        {

            double M = count_mag(spintab, N);


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
                else if (rng.get_random()<exp((-2.0)*dE/Ttab[t]))
                    spintab[i][j] *= (-1); 
            }

            if (k>9000)
            {   
                double a = count_mag(spintab, N);
                mag += a;
                mag2 += a*a;
            }
    
        }

        double mag_bar = mag/1000;
        double mag2_bar = mag2/1000;
        double magnet = mag_bar/(N*N);
        double magnet2 = (mag2_bar - mag_bar*mag_bar)/(T*N*N);
        cout<<t<<" ";
        plik1<<Ttab[t]<<" "<<magnet<<" "<<magnet2<<endl;
    }

    return 0;
}


//2.269