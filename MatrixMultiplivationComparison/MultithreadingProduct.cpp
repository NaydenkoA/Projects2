#include "MultithreadingProduct.h"

void DotProductRows(vector<vector <int>> a, vector<vector <int>> b, vector<vector <int>>& v, int row) {
	int n = a.size();
	for (int i = row; i < n; i += 4) {
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < n; k++) {
				v[i][j] = v[i][j] + a[i][k] * b[k][j];
			}
		}
	}
}

vector<vector <int>> DotProductThreas(vector<vector <int>> a, vector<vector <int>> b) {
	int n = a.size();
	vector<vector <int>> v(n, vector<int>(n, 0));
	thread t1(DotProductRows, ref(a), ref(b), ref(v), 0);
	thread t2(DotProductRows, ref(a), ref(b), ref(v), 1);
	thread t3(DotProductRows, ref(a), ref(b), ref(v), 2);
	thread t4(DotProductRows, ref(a), ref(b), ref(v), 3);
	t1.join();
	t2.join();
	t3.join();
	t4.join();
	return v;
}