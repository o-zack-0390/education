#include <stdio.h>
#define N 3

int main(void){
	int /* □ □ □ */[1000];
	/* □ □ □ */ count = 0;
	for(int i=0; ; i/* ○ ○ ○ */){
		scanf("%d",&num_list[/* □ □ □ */]);
		/* □ □ □ */++;
		if(num_list[i] /* ○ ○ ○ */ 0)
			break;
	}
	
	if(count /* ○ ○ ○ */ N)
		printf("0\n");
	
	int /* □ □ □ */;
	for(int i=0; i<count-1; i++){
		for(int j=i+1; j<count; j++){
			/* □ □ □ */(num_list[i] < num_list[j]){
				tmp         = num_list[/* □ □ □ */];
				/* □ □ □ */[i] = /* □ □ □ */[j];
				num_list[/* □ □ □ */] = tmp;
			}
		}
	}
	
	for(int i=0; i<count; i++)
		printf("%d ",num_list[i]);
	
	int target = /* □ □ □ */[0];
	/* □ □ □ */ pos    = 0;
	for(int i=0; i<count; i++){
		if(num_list[i] != num_list[i/* ○ ○ ○ */1]){
			/* □ □ □ */ = num_list[i];
			/* □ □ □ */++;
		}
		if(pos == /* □ □ □ */)
			break;
	}
	
	printf("number%d=%d\n",N,target);
	return 0;
}
#include <stdio.h>
#define N 3

int main(void){
	int num_list[1000];
	int /* □ □ □ */ = 0;
	for(int i=0; ; i/* ○ ○ ○ */){
		scanf("%d",&num_list[i]);
		count/* ○ ○ ○ */;
		if(num_list[i] /* ○ ○ ○ */ 0)
			break;
	}
	
	if(count /* ○ ○ ○ */ N)
		printf("0\n");
	
	int tmp;
	for(int i=0; i<count-1; i++){
		for(int j=i+1; j<count; j++){
			if(num_list[i] /* ○ ○ ○ */ num_list[j]){
				/* □ □ □ */         = num_list[i];
				num_list[/* □ □ □ */] = num_list[j];
				num_list[/* □ □ □ */] = tmp;
			}
		}
	}
	
	for(int i=0; i<count; i++)
		printf("%d ",num_list[i]);
	
	int /* □ □ □ */ = num_list[0];
	int /* □ □ □ */    = 0;
	for(int i=0; i<count; i++){
		if(num_list[i] /* ○ ○ ○ */ num_list[i+1]){
			target = num_list[i];
			pos/* ○ ○ ○ */;
		}
		if(pos == /* □ □ □ */)
			break;
	}
	
	printf("number%d=%d\n",N,target);
	return 0;
}
