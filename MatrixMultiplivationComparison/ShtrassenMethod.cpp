#include"ShtrassenMethod.h"

vector<vector <int>> AddZeros(vector<vector <int>> a) {
	int n = a.size();
	double x = log(n) / log(2);
	int m = pow(2, floor(x) + 1);
	vector<vector <int>> v(m, vector <int>(m, 0));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			v[i][j] = a[i][j];
		}
	}
	return v;
}

vector<vector <int>> AddZerosOptimal(vector<vector <int>> a) {
	int n = a.size();
	int k = 2;
	while (n / k > 150) {
		k = 2 * k;
	}
	k = (floor(n / k) + 1) * k;
	vector<vector <int>> v(k, vector <int>(k,0));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			v[i][j] = a[i][j];
		}
	}
	return v;
}

vector<vector <int>> RemoveZeros(vector<vector <int>> a, int n) {
	if (n == a.size())
		return a;
	else {
		vector<vector <int>> v(n, vector <int>(n));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				v[i][j] = a[i][j];
			}
		}
		return v;
	}
}

vector<vector <int>> ShtrassenMethodAction(vector<vector <int>> a, vector<vector <int>> b) {
	int n = a.size();
	if (n == 2)
		return DotProduct(a, b);
	vector<vector <int>> a11(n / 2, vector <int>(n / 2));
	vector<vector <int>> a12(n / 2, vector <int>(n / 2));
	vector<vector <int>> a21(n / 2, vector <int>(n / 2));
	vector<vector <int>> a22(n / 2, vector <int>(n / 2));
	vector<vector <int>> b11(n / 2, vector <int>(n / 2));
	vector<vector <int>> b12(n / 2, vector <int>(n / 2));
	vector<vector <int>> b21(n / 2, vector <int>(n / 2));
	vector<vector <int>> b22(n / 2, vector <int>(n / 2));
	for (int i = 0; i < n/2; i++) {
		for (int j = 0; j < n/2; j++) {
			a11[i][j] = a[i][j];
			a21[i][j] = a[i + n / 2][j];
			a12[i][j] = a[i][j + n / 2];
			a22[i][j] = a[i + n / 2][j + n / 2];
			b11[i][j] = b[i][j];
			b21[i][j] = b[i + n / 2][j];
			b12[i][j] = b[i][j + n / 2];
			b22[i][j] = b[i + n / 2][j + n / 2];
		}
	}
	vector<vector <int>> d = ShtrassenMethodAction(SumMatrix(a11,a22), SumMatrix(b11,b22));
	vector<vector <int>> d1 = ShtrassenMethodAction(SubtractMatrix(a12,a22),SumMatrix(b21,b22));
	vector<vector <int>> d2 = ShtrassenMethodAction(SubtractMatrix(a21,a11),SumMatrix(b11,b12));
	vector<vector <int>> h1 = ShtrassenMethodAction(SumMatrix(a11,a12),b22);
	vector<vector <int>> h2 = ShtrassenMethodAction(SumMatrix(a21,a22),b11);
	vector<vector <int>> v1 = ShtrassenMethodAction(a22,SubtractMatrix(b21,b11));
	vector<vector <int>> v2 = ShtrassenMethodAction(a11,SubtractMatrix(b12,b22));
	vector<vector <int>> q = SumMatrix(SumMatrix(d,d1),SubtractMatrix(v1,h1));
	vector<vector <int>> p = SumMatrix(v2,h1);
	vector<vector <int>> g = SumMatrix(v1,h2);
	vector<vector <int>> l = SumMatrix(SumMatrix(d,d2),SubtractMatrix(v2,h2));
	vector<vector <int>> v(n, vector <int>(n));
	for (int i = 0; i < n / 2; i++) {
		for (int j = 0; j < n / 2; j++) {
			v[i][j] = q[i][j];
			v[i][j + n / 2] = p[i][j];
			v[i + n / 2][j] = g[i][j];
			v[i + n / 2][j + n / 2] = l[i][j];
		}
	}
	return v;
}

vector<vector <int>> ShtrassenMethodOptimalAction(vector<vector <int>> a, vector<vector <int>> b) {
	int n = a.size();
	if (n <= 256)
		return DotProduct(a, b);
	vector<vector <int>> a11(n / 2, vector <int>(n / 2));
	vector<vector <int>> a12(n / 2, vector <int>(n / 2));
	vector<vector <int>> a21(n / 2, vector <int>(n / 2));
	vector<vector <int>> a22(n / 2, vector <int>(n / 2));
	vector<vector <int>> b11(n / 2, vector <int>(n / 2));
	vector<vector <int>> b12(n / 2, vector <int>(n / 2));
	vector<vector <int>> b21(n / 2, vector <int>(n / 2));
	vector<vector <int>> b22(n / 2, vector <int>(n / 2));
	for (int i = 0; i < n / 2; i++) {
		for (int j = 0; j < n / 2; j++) {
			a11[i][j] = a[i][j];
			a21[i][j] = a[i + n / 2][j];
			a12[i][j] = a[i][j + n / 2];
			a22[i][j] = a[i + n / 2][j + n / 2];
			b11[i][j] = b[i][j];
			b21[i][j] = b[i + n / 2][j];
			b12[i][j] = b[i][j + n / 2];
			b22[i][j] = b[i + n / 2][j + n / 2];
		}
	}
	vector<vector <int>> d = ShtrassenMethodOptimalAction(SumMatrix(a11, a22), SumMatrix(b11, b22));
	vector<vector <int>> d1 = ShtrassenMethodOptimalAction(SubtractMatrix(a12, a22), SumMatrix(b21, b22));
	vector<vector <int>> d2 = ShtrassenMethodOptimalAction(SubtractMatrix(a21, a11), SumMatrix(b11, b12));
	vector<vector <int>> h1 = ShtrassenMethodOptimalAction(SumMatrix(a11, a12), b22);
	vector<vector <int>> h2 = ShtrassenMethodOptimalAction(SumMatrix(a21, a22), b11);
	vector<vector <int>> v1 = ShtrassenMethodOptimalAction(a22, SubtractMatrix(b21, b11));
	vector<vector <int>> v2 = ShtrassenMethodOptimalAction(a11, SubtractMatrix(b12, b22));
	vector<vector <int>> q = SumMatrix(SumMatrix(d, d1), SubtractMatrix(v1, h1));
	vector<vector <int>> p = SumMatrix(v2, h1);
	vector<vector <int>> g = SumMatrix(v1, h2);
	vector<vector <int>> l = SumMatrix(SumMatrix(d, d2), SubtractMatrix(v2, h2));
	vector<vector <int>> v(n, vector <int>(n));
	for (int i = 0; i < n / 2; i++) {
		for (int j = 0; j < n / 2; j++) {
			v[i][j] = q[i][j];
			v[i][j + n / 2] = p[i][j];
			v[i + n / 2][j] = g[i][j];
			v[i + n / 2][j + n / 2] = l[i][j];
		}
	}
	return v;
}

vector<vector <int>> ShtrassenMethod(vector<vector <int>> a, vector<vector <int>> b) {
	int n = a.size();
	double x = log(n) / log(2);
	if (floor(x) != x) {
		a = AddZeros(a);
		b = AddZeros(b);
		return RemoveZeros(ShtrassenMethodAction(a, b), n);
	}
	return ShtrassenMethodAction(a, b);
}

vector<vector <int>> ShtrassenMethodOptimal(vector<vector <int>> a, vector<vector <int>> b) {
	int n = a.size();
	if (n <= 256)
		return DotProduct(a, b);
	else {
		double x = log(n) / log(2);
		if (floor(x) != x) {
			a = AddZerosOptimal(a);
			b = AddZerosOptimal(b);
			return RemoveZeros(ShtrassenMethodOptimalAction(a, b), n);
		}
		else
			return ShtrassenMethodOptimalAction(a, b);
	}
}