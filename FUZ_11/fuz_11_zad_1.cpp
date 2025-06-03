#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <random>
#include <climits>

using namespace std;

class RandomNumberGenerator 
{
    private:
        std::random_device rd;
        std::mt19937 gen;
        std::uniform_real_distribution<double> dist;
    
    public:
        RandomNumberGenerator()
            : gen(rd()), dist(0.0, 1.0) {}

        double get_random() { 
            return dist(gen);
        }
};


vector<double> generate(int N_max, double dx)
{
    double p = 0.5;
    double x_pos = 0;
    RandomNumberGenerator rn;
    vector<double> x_table;
    x_table.push_back(0);

    for (int i = 0; i<N_max; i++)
    {
        if (rn.get_random()<p)
        {
             x_pos += dx;
             x_table.push_back(x_pos);
        }
        else
        {
             x_pos -= dx;
             x_table.push_back(x_pos);
        }

    }

    return x_table;
}


int distance(int N_max, int dx)
{
    double p = 0.5;
    int x_pos = 0;
    RandomNumberGenerator rn;

    for (int i = 0; i<N_max; i++)
    {
        if (rn.get_random()<p)
        {
             x_pos += dx;
        }
        else
        {
             x_pos -= dx;
        }

    }

    return x_pos;
}

int main()
{


    int N_max = 200;
    double dx = 1;

    ofstream plik1("C:\\Users\\kacpe\\OneDrive\\Pulpit\\C_plus\\FUZ\\FUZ_11\\fuz11.txt");
    vector<double> table_1 = generate(N_max, dx);
    vector<double> table_2 = generate(N_max, dx);
    vector<double> table_3 = generate(N_max, dx);
    vector<double> table_4 = generate(N_max, dx);
    vector<double> table_5 = generate(N_max, dx);

    for (int i = 0; i<N_max; i++)
    {
        plik1<<i<<" "<<table_1[i]<<" "<<table_2[i]<<" "<<table_3[i]<<" "<<table_4[i]<<" "<<table_5[i]<<endl;
    }

    ofstream plik2("C:\\Users\\kacpe\\OneDrive\\Pulpit\\C_plus\\FUZ\\FUZ_11\\fuz11_zad1_1.txt");
    //ZADANIE 2
    for (int i = 0; i<1000000; i++)
    {
        plik2<<distance(20, 1)<<endl;

    }

    return 0;
}