#include <iostream>
#include <cmath>
#include <cstdio>
#include <array>
#include <vector>

class Foo
{
public:
  int i=0;
  int j=0;
};

int main() {

  std::vector<int> intVector = {1,2,3,4,5,6};
  auto it = std::begin(intVector);

  std::cout << *it << std::endl;

  it += 5;
  std::cout << *it << std::endl;

  --it;
  std::cout << *it << std::endl;

  *it = 3;
  std::cout << *it << std::endl;
};
