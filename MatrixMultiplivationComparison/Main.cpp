#include"AditionalFunctions.h"
#include"MatrixGenerator.h"
#include"MultithreadingProduct.h"
#include"ShtrassenMethod.h"

int main() {
	vector<vector <int>> a = GenerateMatrix(1000,0.1);
	vector<vector <int>> b = GenerateMatrix(1000,0.1);
	vector<vector <int>> x;
	int t;
	t = time(0);
	x = DotProduct(a, b);
	cout << time(0) - t << endl;
	t = time(0);
	x = ShtrassenMethodOptimal(a,b);
	cout << time(0) - t << endl;
	t = time(0);
	x = DotProductThreas(a, b);
	cout << time(0) - t << endl;
	return 0;
}