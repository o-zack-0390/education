#include <stdio.h>
int kaijou(int n){
        int r;
        printf(" 髢句ｧ九n=%d\n",n);
        if(n==1)
                r=1;
        else{
                r=n*kaijou(n-1);
        }
        printf("邨ゆｺ・=%d,r=%d\n",n,r);
        return r;
}
int main(void){
        int x,k;
        printf("n繧貞・蜉幢ｼ・");
        scanf("%d",&x);
        k=kaijou(x );
        printf("%d 縺ｮ髫惹ｹ励・%d\n",x,k);
        return 0;
}