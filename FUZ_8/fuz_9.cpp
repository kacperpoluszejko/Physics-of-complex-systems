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

const int N = 100;

// Zadanie 1 - generujemy graf
void generate_graph(int G[N][N], int alfa)
{
    RandomNumberGenerator rn;
    double p = static_cast<double>(alfa) / N;

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            G[i][j] = 0;

    for (int i = 0; i < N; i++) 
    {
        for (int j = i + 1; j < N; j++) 
        {   
            if (rn.get_random() < p)
            {
                G[i][j] = 1;
                G[j][i] = 1;
            }
        }
    }
}

//Liczenie wiązań
int count_bindings(int G[N][N])
{
    int count = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = i + 1; j < N; j++) 
        {   
            if (G[i][j] == 1) count++;
        }
    }
    return count;
}

// Liczenie stopni
int count_rank(int G[N][N], int i)
{
    int count = 0;
    for(int j = 0; j<N; j++)
    {
        if(G[i][j] == 1) count ++; 
    }

    return count;
}

//Zadanie 5 - do liczenia dystansu i tworzenia macierzy dystansu
double distance(int alfa)
{
    int G[N][N];
    generate_graph(G, alfa);
    int D[N][N];

    for (int i = 0; i<N; i++)
    {
        for(int j = 0; j<N; j++)
        {
            if(i == j) D[i][j] = 0;
            else if(G[i][j] == 1) D[i][j] = 1;
            else D[i][j] = 100000;
        }
    }

    for (int k = 0; k<N; k++)
    {
        for(int i = 0; i<N; i++)
        {
            for (int j = 0; j<N; j++)
            {
                D[i][j] = min(D[i][j], D[i][k] + D[k][j]);
            }
        }
    }

    double sum_distances = 0;
    int count = 0;

    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j < N; j++) 
        {
            if (i != j && D[i][j] < 100000)  
            {
                sum_distances += D[i][j];  
                count++;
            }
        }
    }

    return sum_distances/count;
}

// Zadanie 6 - trójkąty
int count_triangles(int G[N][N]) 
{
    int triangle_count = 0;

    for (int i = 0; i < N; i++) 
    {
        for (int j = i + 1; j < N; j++) 
        {
            for (int k = j + 1; k < N; k++) 
            {
                if (G[i][j] == 1 && G[j][k] == 1 && G[k][i] == 1) 
                {
                    triangle_count++;
                }
            }
        }
    }
    return triangle_count;
}


int main()
{
    int repeats = 100;   // Liczba powtórzeń
    int alfa[2] = {4,10};        // Parametr prawdopodobieństwa - aby zmienić alfe wystarczy zmienić alfa[0] --> alfa[1] w kodzie poniżej
    double average_bindings = 0;
    double average_rank = 0;


    // ZADANIE 2
    cout<<endl<<"Zadanie 2: "<<endl;
    for (int t = 0; t < repeats; t++)
    {
        int G[N][N];
        generate_graph(G, alfa[0]);
        average_bindings += count_bindings(G);
    }
    average_bindings /= repeats;  // Obliczenie średniej liczby krawędzi

    double expected_bindings = (static_cast<double>(alfa[0]) * (N - 1)) / 2;
    cout << "Średnia liczba krawędzi: " << average_bindings << endl;
    cout << "Wartość oczekiwana: " << expected_bindings << endl;


    //ZADANIE 3
    cout<<endl<<"Zadanie 3: "<<endl;
    double sum_average_rank = 0;
    for (int t = 0; t<repeats; t++)
    {
        int G[N][N];
        generate_graph(G, alfa[0]);
        for (int i = 0; i<N; i++)
        {
            average_rank += count_rank(G, i);
        }
        average_rank /= N;
        sum_average_rank += average_rank;
    }
    sum_average_rank /= repeats;
    double expected_rank = (static_cast<double>(alfa[0]) * (N - 1)) / N;
    cout << "Średni stopień wierzchołka: " << average_rank << endl;
    cout << "Wartość oczekiwana: " << expected_rank << endl;



    //Zadanie 4
    ofstream plik1("C:\\Users\\kacpe\\OneDrive\\Pulpit\\C_plus\\FUZ\\FUZ_9\\fuz9_1.txt");
    cout<<endl<<"Zadanie 4: "<<endl;
    double sum_rank_dist[N] = {0};
    for (int t = 0; t<repeats; t++)
    {
        double rank_dist[N] = {0};
        int G[N][N];
        generate_graph(G, alfa[0]);
        for (int i = 0; i<N; i++)
        {
            int rank = 0;
            rank = count_rank(G, i);
            rank_dist[rank] += 1;
        }
        
        for (int r = 0; r < N; r++) 
        {
            sum_rank_dist[r] += rank_dist[r]/(N-1);
        }
    }
    cout << "Rozkład stopni wierzchołków:\n";
    for (int r = 0; r < N; r++) 
    {
        if(sum_rank_dist[r] != 0)
        {
            cout << "Stopień " << r << ": " << sum_rank_dist[r]/repeats<< " wierzchołków\n";
            plik1<<r<<" "<<sum_rank_dist[r]/repeats<<endl;
        }
    }
   

    //Zadanie 5
    cout<<endl<<"Zadanie 5: "<<endl;
    double sum_average_distance = 0;
    for (int t = 0; t<repeats; t++)
    {
        sum_average_distance += distance(alfa[0]);

    }
        double expected_distance = (static_cast<double>(log(N))/(log(alfa[0]*(N-1)/N)));
        cout<<"Średnia odległość między wierzchołkami: "<<sum_average_distance/repeats<<endl;
        cout<< "Wartość oczekiwana: "<<expected_distance<<endl;
    
        //Obliczona wartość odbiega od wartości oczekiwanej. Trzeba by wyeliminować grafy niespójne, ale nie zdążyłem tego zrobić


    //Zadanie 6
    cout<<endl<<"Zadanie 6: "<<endl;
    double sum_triangle_count = 0;
    for (int t = 0; t<repeats; t++)
    {
        int G[N][N];
        generate_graph(G, alfa[0]);
        sum_triangle_count += count_triangles(G);
    }

    double expected_triangles = (N * (N - 1) * (N - 2) / 6.0) * pow(static_cast<double>(alfa[0]) / N, 3);

    cout << "Średnia liczba trójkątów w grafie: " << sum_triangle_count/repeats << endl;
    cout << "Wartość oczekiwana: " << expected_triangles << endl;

    return 0;
}
