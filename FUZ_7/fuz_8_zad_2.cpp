#include <iostream>
#include <vector>
#include <random>
#include <iomanip>
#include <fstream>
#include <queue>
#include <utility>

using namespace std;

class RandomNumberGenerator {
private:
    random_device rd;
    mt19937 gen;
    uniform_real_distribution<double> dist;

public:
    RandomNumberGenerator() : gen(rd()), dist(0.0, 1.0) {}

    double get_random() {
        return dist(gen);
    }
};


const int N = 20;

void wypisz(int H[N][N])
{

    for (int i = 0; i< N; i++)
    {
        for (int j = 0; j<N; j++)
        {
            cout<<H[i][j]<<" ";
        }
        cout<<endl;
    }
}


int dodaj_ziarenko(int H[N][N], int i, int j)
{
    int s = 0;

    queue<pair<int, int>> q;
    q.push({i, j});

    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();

        if (x < 0 || x >= N || y < 0 || y >= N)
        continue;

        H[x][y] += 1;

        if (H[x][y] == 4)
        {
            H[x][y] = 0;

           q.push({x - 1, y});
           q.push({x + 1, y});
           q.push({x, y - 1});
           q.push({x, y + 1});
            s += 4;
        
        }
    }

    return s;
}



int main()
{
    RandomNumberGenerator rn;
    int H[N][N];

    for (int i = 0; i<N; i++)
    {
        for (int j = 0; j<N; j++)
        {
            H[i][j] = static_cast<int>(rn.get_random() * 4);
        }
    }

    ofstream plik1("C:\\Users\\kacpe\\OneDrive\\Pulpit\\C_plus\\FUZ\\FUZ_8\\fuz8_zad3.txt");

    int s = 0;
    for (int k = 0; k<100000; k++)
    {
        int i = static_cast<int>(rn.get_random() * 9);
        int j  =static_cast<int>(rn.get_random() * 9);
        s = dodaj_ziarenko(H, i, j);
        if (s != 0) plik1 << s <<endl;

        // if (s != 0)  plik1<<"Krok: "<<k<<" Rozmiar lawiny: "<< s<< endl;
    }



    wypisz(H);



    return 0;
}


