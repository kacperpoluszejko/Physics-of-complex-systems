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

int main()
{
    RandomNumberGenerator rn;
    int M = 10;
    double lat[M][M] = {0};
    int N = 1000000;
    int x_pos = 5, y_pos = 5;

    for (int i = 0; i<N; i++)
    {   
        double U = rn.get_random();

        if (U < 0.25) x_pos = (x_pos + 1)%M;
        else if (U < 0.5)
        {
            x_pos = (x_pos - 1);
            if (x_pos == -1) x_pos = 9;
        }
        else if (U < 0.75) y_pos = (y_pos + 1)%M;
        else 
        {
            y_pos = (y_pos - 1);
            if (y_pos == -1) y_pos = 9;  
        }
        lat[x_pos][y_pos] += 1;
    }

    for (int i = 0; i<M; i++)
    {
        for (int j = 0; j<M; j++)
        {   
            lat[i][j] = lat[i][j]/N;
            cout<<lat[i][j]<<" ";
        }
        cout<<endl;
    }

    //Liczymy średnią
    double sum = 0;

    for (int i = 0; i<M; i++)
    {
        for (int j = 0; j<M; j++)
        {
            sum += lat[i][j];
        }
    }
    double srednia  = sum/(M*M);
    cout<<endl<<"Srednia = "<<srednia<<endl;

    double sum2 = 0;
    for (int i = 0; i<M; i++)
    {
        for (int j = 0; j<M; j++)
        {
            sum2 += (lat[i][j] - srednia)*(lat[i][j] - srednia);
        }
    }
    double odch  = sqrt(sum2/(M*M));
    cout<<endl<<"Odchylenie standardowe = "<<odch<<endl;
    return 0;
}