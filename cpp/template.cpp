#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define vi vector<int>
#define vl vector<long long>
#define pii pair<int, int>
#define pll pair<long long, long long>
#define elif else if
#define rep(i, n) for (int i = 0; i < (n); i++)
#define all(v) (v).begin(), (v).end()
#define rall(x) x.rbegin(), x.rend()
#define el '\n'
#define Yes cout << "Yes" << el
#define No cout << "No" << el
#define YES cout << "YES" << el
#define NO cout << "NO" << el
const double pi = 3.141592653589793238;
const int inf = 1073741823;
const ll infl = 1LL << 60;
const string ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const string abc = "abcdefghijklmnopqrstuvwxyz";
const int MOD = 998244353;
const array<int, 8> dx = {0, 0, -1, 1, -1, -1, 1, 1};
const array<int, 8> dy = {-1, 1, 0, 0, -1, 1, -1, 1};
template <typename T1, typename T2> inline bool chmax(T1 &a, T2 b) {
    bool compare = a < b;
    if (compare)
        a = b;
    return compare;
}
template <typename T1, typename T2> inline bool chmin(T1 &a, T2 b) {
    bool compare = a > b;
    if (compare)
        a = b;
    return compare;
}
template <typename T1, typename T2>
std::ostream &operator<<(std::ostream &os, std::pair<T1, T2> p) {
    os << "{" << p.first << "," << p.second << "}";
    return os;
}
template <typename T>
inline void print_vec(const vector<T> &v, bool split_line = false) {
    if (v.empty()) {
        cout << "This vector is empty." << el;
        return;
    }
    constexpr bool isValue = is_integral<T>::value;
    for (int i = 0; i < (int)v.size(); i++) {
        if constexpr (isValue) {
            if ((v[i] == inf) || (v[i] == infl))
                cout << 'x' << " \n"[split_line || i + 1 == (int)v.size()];
            else
                cout << v[i] << " \n"[split_line || i + 1 == (int)v.size()];
        } else
            cout << v[i] << " \n"[split_line || i + 1 == (int)v.size()];
    }
}
template <typename T> void vin(vector<T> &v) {
    for (auto &element : v) {
        cin >> element;
    }
}
template <typename T> T mod_pow(T x, T n, const T &p) {
    T ret = 1;
    while (n > 0) {
        if (n & 1)
            (ret *= x) %= p;
        (x *= x) %= p;
        n >>= 1;
    }
    return ret;
}
template <typename T> T ipow(T x, T n) {
    T ret = 1;
    while (n > 0) {
        if (n & 1)
            ret *= x;
        x *= x;
        n >>= 1;
    }
    return ret;
}

int main() {
    // to do
}