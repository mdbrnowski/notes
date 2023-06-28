#include <bits/stdc++.h>
using namespace std;

typedef complex<double> cd;
typedef vector<double> vd;
typedef vector<int> vi;
const long double PI = acos(-1.0L);

void fft(vector<cd>& a) {
    int n = a.size(), L = 31 - __builtin_clz(n);
    static vector<complex<long double>> R(2, 1);
    static vector<cd> rt(2, 1);  // (^ 10% faster if double)
    for (static int k = 2; k < n; k *= 2) {
        R.resize(n); rt.resize(n);
        auto x = polar(1.0L, PI / k);
        for (int i = k; i < 2*k; i++)
            rt[i] = R[i] = i&1 ? R[i/2] * x : R[i/2];
    }
    vi rev(n);
    for (int i = 0; i < n; i++)
        rev[i] = (rev[i / 2] | (i & 1) << L) / 2;
    for (int i = 0; i < n; i++)
        if (i < rev[i]) swap(a[i], a[rev[i]]);
    for (int k = 1; k < n; k *= 2)
        for (int i = 0; i < n; i += 2 * k)
            for (int j = 0; j < k; j++) {
                cd z = rt[j+k] * a[i+j+k];
                a[i + j + k] = a[i + j] - z;
                a[i + j] += z;
            }
}