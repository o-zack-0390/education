#include <stdio.h>
void moveone(int size, char dep, char tmp);
void towerH(int num, char dep, char arv, char tmp);
int  step = 1;

int main(void){
	int n;
	printf("n=");
	scanf("%d",/* ○ ○ ○ */n);
	towerH(/* □ □ □ */,'A','C','B');
	return 0;
}

void moveone(int size, char dep, char arv){
	printf("step2:%-2d size:%d %c --> %c\n",step++, size, dep, arv);
}

void towerH(int num, char dep, char arv, char tmp){
    printf("S\n");
		if(/* □ □ □ */ == 1){
			printf("M\n");
			/* □ □ □ */(1, dep, arv);
		}
	
		else{
			printf("H\n");
			towerH(num-1, dep, tmp, arv);
			
			printf("M2\n");
			moveone(num, /* □ □ □ */, arv);
			
			printf("H2\n");
			towerH(num-1, /* □ □ □ */, arv, dep);
		}
}

/*
空欄の行 : 計6行

空欄一覧

(行番号,置換文字) : (9,&)

(行番号,置換文字) : (30,dep)

(行番号,置換文字) : (33,tmp)

(行番号,置換文字) : (22,moveone)

(行番号,置換文字) : (20,num)

(行番号,置換文字) : (10,n)
*/
