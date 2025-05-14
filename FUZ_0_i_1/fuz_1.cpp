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



const int N = 60;



double losuj()
{
    return static_cast<double>(std::rand())/RAND_MAX;
}

vector<vector<int>> create() // tworzenie początkowej siatki
{
    double a;
    vector<vector<int>> grid(N, vector<int>(N, 0));
    for (int i=0; i<N; i++)
    {
        for (int j=0; j<N; j++)
        {
            a = losuj();
            if(a<=0.5)  // losowanie wartości, prawd. że żywa równe 50%
            grid[i][j]=0;
            else
            grid[i][j]=1;
        }
    }

    return grid;
}


int count_neighbours(const vector<vector<int>>& grid, int x, int y) // liczenie sąsiadów
{
    int count =0;
    for (int i=-1; i<=1; i++)
    {
        for (int j=-1; j<=1; j++)
        {
            if (i==0 && j==0) continue; //komórka nie jest sąsiadem dla samej siebie

            int nx = (x+i+N)%N;
            int ny = (y+j+N)%N;

            if (grid[nx][ny]==1) count+=1;
        }
    }
    return count;

}
          

    void update(vector<vector<int>>& grid)  //aktualizacja siatki
    {   
      vector<vector<int>> newgrid = grid;
      for (int i=0; i<N; i++)
      {
        for (int j=0; j<N; j++)
        {
        int neighbours = count_neighbours(grid, i, j);
            if (grid[i][j]==1)                          // B4678/S35678`
            {
                if (neighbours == 3 || neighbours >=5) newgrid[i][j]=1;
                else newgrid[i][j]=0;

            }
            else
            {
                if (neighbours == 4 || neighbours >=6) newgrid[i][j]=1;
                else newgrid[i][j]=0;
            }
        }
      }
      grid = newgrid;
    }       



    void savetofile(const vector<vector<int>>& grid, int t) // zapis do pliku
    {
        if(t==0)
        {
            std::ofstream plik1("C:\\Users\\kacpe\\OneDrive\\Pulpit\\C_plus\\FUZ\\fuz1.txt", std::ios::trunc);
            if (!plik1) cout << "Błąd otwierania pliku!\n";

            plik1.close();
        }

        ofstream plik1("C:\\Users\\kacpe\\OneDrive\\Pulpit\\C_plus\\FUZ\\fuz1.txt", ios::app);
        if (!plik1) cout<<"Nie otwarto pliku";
        for (int i=0; i<N; i++)
        {
            for (int j=0; j<N; j++)
            {
                plik1<<grid[i][j]<<" ";
            }
            plik1<<endl;
        }
        plik1<<endl;
        plik1.close();
    }



int main()
{
    std::srand(std::time(0)); 
    vector<vector<int>> grid = create();

    int t = 100;

    // for (int i=0; i<N; i++)
    // {
    //     for (int j=0; j<N; j++)
    //     {
    //         cout<<grid[i][j]<<" ";
    //     }
    //     cout<<endl;
    // }

    for (int i=0; i<=t; i++)
    {
        if(i==0 || i==1 || i==2 || i==5 || i==10 || i==50 || i==100)
        {
            cout<<i;
            savetofile(grid, i);
        }
        update(grid);

    }
    
    return 0;

}