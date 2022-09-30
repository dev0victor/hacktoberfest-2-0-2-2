/*-----------------CODED BY ROCKHOPPER130-----------------*/
#include <bits/stdc++.h>
#include <numeric>
#define INF (int)1e9
#define EPS 1e-9
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007
#define int long long int
#define FOR(i, j, k, in) for (int i=j ; i<k ; i+=in)
#define RFOR(i, j, k, in) for (int i=j ; i>=k ; i-=in)
#define REP(i, j, k) FOR(i, j, k, 1)
#define RREP(i, j, k) RFOR(i, k, j, 1)
typedef std::pair<int, int> PII;
typedef std::vector<int> VI;
typedef std::vector<std::string> VS;
typedef std::vector<PII> VII;
typedef std::vector<VI> VVI;
typedef std::map<int,int> MPII;
typedef std::set<int> SETI;
typedef std::multiset<int> MSETI;
using namespace std;

///*------------------------FUNCTIONS-----------------------*///
int gcd(int a, int b) { 
if (b == 0) { 
return a; 
} 
return gcd(b, a % b); 
}
///*--------------------CODE BEGINS HERE--------------------*///

int32_t main() {
ios::sync_with_stdio(0);
cin.tie(0);

VI v;

v.push_back(2);
v.push_back(3);
v.push_back(6);
v.push_back(4);
v.push_back(9);
v.push_back(5);
v.push_back(1);
v.push_back(2);
v.push_back(7);
v.push_back(4);

int l=v.size();
REP(i,0,l){
    cout << v[i] << " ";
}
cout<<"\n";

REP(i,1,l){
    REP(j,0,l-i){
        if (v[j] > v[j + 1]) {
            swap(v[j],v[j+1]);
        }
    }
}

REP(i,0,l){
    cout << v[i] << " ";
}
cout<<"\n";

return 0;
}