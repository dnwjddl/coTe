#include <bits/stdc++.h>

using namespace std;

int n, k;
int result;

int main(void){
  cin >> n >> k;
  while(true){
    int target = (n/k) * k;
    result += (n-target);
    n = target;
    if(n<k) break;
    result++;
    n /= k;
  }
  result += (n-1);
  cout << result << '\n';
}
