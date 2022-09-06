#include<bits/stdc++.h>
using namespace std;
void change(int &a, int &b){
	int t=0;
	t=a;
	a=b;
	b=t;
}
int main(){
    int a=1;
    int b=2;
    change(a, b);
    printf("%d %d", a, b);
    return 0;
} 
