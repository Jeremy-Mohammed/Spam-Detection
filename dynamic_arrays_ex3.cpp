#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef int* IntPtr;

//int[] createRandomArray(int size); //illegal
IntPtr createRandomArray(int size);

int main() {
  int s = 1;
  cout << "Enter array size: ";
  cin >> s;

  IntPtr p1 = createRandomArray(s);

  for (int i=0; i < s; i++) {
    cout << "p1[" << i << "] = " << p1[i] << endl;
  }

  delete[] p1;

  return 0;
}

IntPtr createRandomArray(int size) {
  IntPtr x = new int[size];

  //seed random number generator
  srand(time(NULL));

  //generate random numbers (0-99) and store in array
  for (int i=0; i < size; i++) {
    x[i] = rand()%100;
  }
  return x;
}