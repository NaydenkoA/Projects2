#include"AditionalFunctions.h"

void ShowMatrix(vector<vector <int>> v) {
	int m, n = v.size();
	for (int i = 0; i < n; i++) {
		m = v[i].size();
		for (int j = 0; j < m; j++) {
			cout << v[i][j] << " ";
		}
		cout << endl;
	}
}

vector<vector <int>> DotProduct(vector<vector <int>> a, vector<vector <int>> b) {
	int n = a.size();
	vector<vector <int>> v(n, vector<int>(n,0));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < n; k++) {
				v[i][j] = v[i][j] + a[i][k] * b[k][j];
			}
		}
	}
	return v;
}

vector<vector <int>> SumMatrix(vector<vector <int>> a, vector<vector <int>> b) {
	int n = a.size();
	vector<vector <int>> v(n, vector<int>(n));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			v[i][j] = a[i][j] + b[i][j];
		}
	}
	return v;
}

vector<vector <int>> SubtractMatrix(vector<vector <int>> a, vector<vector <int>> b) {
	int n = a.size();
	vector<vector <int>> v(n, vector<int>(n));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			v[i][j] = a[i][j] - b[i][j];
		}
	}
	return v;
}