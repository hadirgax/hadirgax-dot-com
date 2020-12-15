#include <iostream>
#include <cmath>
#include <cstdio>
#include <array>
#include <vector>

void addOne1(int i)
{
  i++;
}

void addOne2(int& i)
{
  i++;
}

void addOne3(int &i)
{
  i++;
}

int main() {

int myInt1 = 31;
addOne1(myInt1);
std::cout << "addOne1: " << myInt1 << std::endl;

int myInt2 = 31;
addOne2(myInt2);
std::cout << "addOne2: " << myInt2 << std::endl;

int myInt3 = 31;
addOne3(myInt3);
std::cout << "addOne3: " << myInt3 << std::endl;

}
