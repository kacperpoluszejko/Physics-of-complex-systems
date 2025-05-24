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


const int N = 10;

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
        wypisz(H);
        cout<<endl<<"Krok lawiny  , s = "<<s<<endl;

        if (H[x][y] >= 4)
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




    int s = 0;
    while (s < 8)
    {
        int i = static_cast<int>(rn.get_random() * 9);
        int j  =static_cast<int>(rn.get_random() * 9);
        cout<<endl<<"Dodajemy ziarenko do współrzędnej (x, y) = ("<<i<<", "<<j<<")"<<endl;
        s = dodaj_ziarenko(H, i, j);
    }

    cout<<endl<<"Finalna postać H: "<< endl;

    wypisz(H);






    return 0;
}


