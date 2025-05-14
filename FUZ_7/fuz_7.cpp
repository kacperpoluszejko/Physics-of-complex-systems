#include <iostream>
#include <vector>
#include <random>
#include <iomanip>
#include <fstream>

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


int perkol (int L, double p)
{
    int label_counter = 1;
    vector<vector<int>> grid(L, vector<int>(L, 0));
    vector<int> label_map(L * L + 1);
    for (int i = 0; i < label_map.size(); ++i)
        label_map[i] = i;

    RandomNumberGenerator rng;

    auto get_label = [&](int label) {
        while (label_map[label] != label) {
            label = label_map[label];
        }
        return label;
    };

    for (int i = 0; i < L; ++i) {
        for (int j = 0; j < L; ++j) {
            if (rng.get_random() < p) {
                bool top = (i > 0 && grid[i - 1][j] != 0);
                bool left = (j > 0 && grid[i][j - 1] != 0);

                if (top && left) {
                    int top_label = get_label(grid[i - 1][j]);
                    int left_label = get_label(grid[i][j - 1]);
                    int min_label = min(top_label, left_label);
                    int max_label = max(top_label, left_label);

                    grid[i][j] = min_label;
                    if (min_label != max_label) {
                        label_map[max_label] = min_label; 
                }
                else if (top) {
                    grid[i][j] = get_label(grid[i - 1][j]);
                }
                else if (left) {
                    grid[i][j] = get_label(grid[i][j - 1]);
                }
                else {
                    grid[i][j] = label_counter++;
                }
            }
        }
    }

    for (int i = 0; i < L; ++i) {
        for (int j = 0; j < L; ++j) {
            if (grid[i][j] != 0) {
                grid[i][j] = get_label(grid[i][j]);
            }
        }
    }

    int perkolacja, max = 0, min = 1000;

    for (int j = 0; j<L; j++)
    {
        if(grid[0][j]>max  && grid[0][j] != 0) max = grid[0][j];
        if(grid[L-1][j]<min && grid[L-1][j] != 0) min = grid[L-1][j];
    }

    if (max >= min) perkolacja = 1;
    else perkolacja = 0;


    // Wyświetlanie
    // for (const auto& row : grid) {
    //     for (int val : row) {
    //         cout << setw(3) << val << " ";
    //     }
    //     cout << '\n';
    // }

    return perkolacja;
};


int main(); {
    const int L = 16;
    double p = 0.4;
    int R = 1000;
    double suma = 0;

    vector<double> p_values;
    for (double p = 0.4; p <= 0.8 + 1e-9; p += 0.01) // Wektor wartości p
    {
        p_values.push_back(p);
    }


    ofstream plik1("C:\\Users\\kacpe\\OneDrive\\Pulpit\\C_plus\\FUZ\\FUZ_7\\fuz7_2.txt");
    
    for (int j = 0; j<p_values.size(); j++)
    {
        suma = 0;
        for (int i=0; i<R; i++)
        {
            suma += perkol(L,p_values[j]);
        }
        double W = suma/R;
        cout<<W<<endl;
        plik1<<p_values[j]<<" "<<W<<endl;
    }
    


    return 0;
}
