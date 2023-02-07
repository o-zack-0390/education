#include <stdio.h>

void moveone(int size,char dep,char tmp);
void towerH(int num,char dep,char arv,char tmp);
/* □ □ □ */  step=1;


int main(void)
{
	int /* □ □ □ */;
	printf("n=");
	scanf("%d",/* ○ ○ ○ */n);
	towerH(n,'A','C','B');
	return 0;
}


void moveone(int size,char dep,char arv)
{
	printf("step2:%-2d size:%d %c --> %c\n",step++,size,dep,arv);
}


void towerH(int num,char dep,char arv,char tmp)
{
    printf("S\n");
	
	if(num/* ○ ○ ○ */1)
	{
		printf("M\n");
		moveone(1,/* □ □ □ */,arv);
	}
	
	else
	{
		printf("H\n");
		towerH(num/* ○ ○ ○ */1,dep,tmp,arv);
		printf("M2\n");
		moveone(num,dep,/* □ □ □ */);
		printf("H2\n");
		/* □ □ □ */(num-1,tmp,arv,dep);
	}
}