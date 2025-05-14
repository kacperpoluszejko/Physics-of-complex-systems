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

double uniform ()
{
    return static_cast<double>(std::rand()) / RAND_MAX;
}


int main ()
{


    std::srand(static_cast<unsigned>(std::time(0)));

    double U1 = uniform();
    cout<<U1;

    return 0;

}