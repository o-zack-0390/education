#include <stdio.h>
int main(void)
{
        int i,j,tmp;

        int data[12];

        int total;
        printf("蜈･蜉帙☆繧区焚蛟､縺ｮ邱乗焚 = ");
        scanf("%d",&total);
        if(12<total){
                printf("邱乗焚繧・2蛟九↓螟画鋤\n");
                total=12;
        }

        printf("%d蛟九・謨ｰ蛟､繧貞・蜉媾n",total);
        for(i=0;i<total;++i)
                scanf("%d",&data[i]);

        for(i=0;i<total;++i){
                for(j=i+1;j<total;++j){

                        if(data[j]<data[i]){
                                tmp=data[i];
                                data[i]=data[j];
                                data[j]=tmp;
                        }
                }
        }

        printf("譏・・た繝ｼ繝医＠縺滓焚蛟､\n");
        for(i=0;i<total;++i)
                printf("%d ",data[i]);
        printf("\n");
        return 0;
}