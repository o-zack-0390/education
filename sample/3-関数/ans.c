#include <stdio.h>
int  cal_sum(int num, int sum);
void print_sum(int sum);

int main(void){
	int num = 1;
	int max = 10;
	int sum = cal_sum(num, max);
	print_sum(sum);
	return 0;
}


int cal_sum(int num, int max){
	int sum = 0;
	
	for(int i=num; i<max; i++)
		sum += i;
	
	return sum;
}


void print_sum(int sum){
	printf("%d",sum);
}
