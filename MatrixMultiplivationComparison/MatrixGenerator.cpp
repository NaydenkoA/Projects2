#include"MatrixGenerator.h"

double GetRandom(double min, double max) {
	srand(time(0) + rand());
	double x = rand();
	return x / RAND_MAX * (max - min) + min;
}

int GetRandomInt(int min, int max) {
	double x = GetRandom(min, max + 1);
	return floor(x);
}

vector<vector <int>> GenerateMatrix(int n, double p) {
	vector<vector <int>> v(n, vector<int>(n, 0));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (GetRandom(0, 1) > p) {
				v[i][j] = GetRandomInt(-1000, 1000);
			}
		}
	}
	return v;
}