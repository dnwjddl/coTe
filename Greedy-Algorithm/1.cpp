#include <bits/stdc++.h>

using namespace std;

int n = 1260;
int cnt;

int coinTypes[4] = {500, 100, 50, 10};

int main(void){
  for(int i=0; i<4; i++){
    cnt += n/coinTypes[i];
    n %= coinTypes[i];
  }
  cout << cnt << '\n';
}

// namespace : namespace란 클래스나 구조체 그리고 함수나 변수를 식별하는 사용하는 논리적인 공간
// c++ 화면 출력 방법:  cout << "Hello World" << end;
