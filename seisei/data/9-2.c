#include <stdio.h>
#include <string.h>
#define NLEN 14
struct town {
    int area, pop;
    char name[NLEN + 1];
};
struct town newTown(struct town s,struct town t){
    struct town rt;

    rt.area=s.area+t.area;
    rt.pop=s.pop+t.pop;
    strcat(s.name,t.name);
    strcpy(rt.name,s.name);

    int moji=strlen(rt.name);
    if(NLEN<moji)
      strcpy(rt.name,"too long");
    return rt;
}
double getDens(struct town t) {

 double x;
  x=(double)t.pop/(double)t.area;
  return x;
}
void printTown(struct town t) {
 printf("area=%d pop=%d dens=%.2f name=\"%s\"\n",t.area,t.pop,(double)t.pop/(double)t.area,t.name);

}
#define Lsize (sizeof(list)/sizeof(struct town))
int main(void) {
    struct town rt; int t1,t2,i;
    struct town list[] = {
      {33,22,"Honmachi"}, {30,17,"Kishine"}, {40,18,"Kosugi"},
      {12,11,"Kouen"}, {27,35,"Fujisawa"}, {50,11,"Kouza"},
      {17,90,"Musashi"}, {36,13,"Oono"}, {40,53,"Ootsuka"},
      {15,86,"Sagami"}, {20,67,"Shibuya"}, {34,15,"Uehara"},
      {18,60,"Yoyogi"}, {38,10,"Dai"}
    };
    printf("逕ｺ縺ｮ繝ｪ繧ｹ繝・n");
    for (i = 0; i < Lsize; i++){
        printf("%-2d ",i);
        printTown(list[i]);
    }
    while(1){
        printf("蜷井ｽｵ蟇ｾ雎｡(謨ｴ謨ｰ繧抵ｼ偵▽蜈･蜉・: ");
        scanf("%d",&t1); scanf("%d",&t2);
        if(t1<0||t2<0||t1>=Lsize||t2>=Lsize||t1==t2)
            break;
        rt = newTown(list[t1],list[t2]);
        printf("譁・ｭ玲焚%d   ",strlen(rt.name));
        printTown(rt);
    }
    return 0;
}