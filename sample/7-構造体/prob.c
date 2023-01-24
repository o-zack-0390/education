#include<stdio.h>
#include<stdlib.h>
#include<math.h>

/* □ □ □ */ point {
  double x;
  /* □ □ □ */ y;
};

struct rectangle{
  struct point ll;
  struct /* □ □ □ */ ur;
};

struct rectangle inputr(void);
double area(struct rectangle r);
double lengthd(struct rectangle r);
int    issquare(struct rectangle r);

int main(void){
  struct /* □ □ □ */ a;
  
  printf("A:\n");
  a = /* □ □ □ */();
  
  printf("The area of A is %f\n", area(a));
  printf("The length of the diagonal of A is %f\n", lengthd(a));
  printf("A is ");
  if (!issquare(a)) printf("NOT ");
  printf("a square");
  
  /* □ □ □ */ 0;
}

struct rectangle inputr(void){
  struct rectangle r;
  
  printf("\tInput the coordinate of the lower left  corner: ");
  scanf ("\n(%lf,%lf)", &r.ll.x, &r.ll.y);
  printf("\tInput the coordinate of the upper right corner: ");
  scanf ("\n(%lf,%lf)", &r.ur.x, &r.ur./* □ □ □ */);

  if ( (r.ll.x >= r./* □ □ □ */.x) || (r.ll.y >= r./* □ □ □ */.y) ){
    fprintf(stderr, "Inputs are invalid.\n");
    exit(1);
  }
  
  return /* □ □ □ */;
}

double area(struct rectangle r){
  return (r.ur.x /* □ □ □ */ r.ll.x) * (r.ur.y /* □ □ □ */ r.ll.y);
}

double lengthd(struct rectangle r){
  double vertical = ((r.ur.x - r./* □ □ □ */.x) * (r.ur.x - r./* □ □ □ */.x));
  double /* □ □ □ */     = ((r.ur.y - r.ll.y) * (r.ur.y - r.ll.y));
  return sqrt(/* □ □ □ */ + side);
}

int issquare(struct rectangle r){
  return r.ur./* □ □ □ */-r.ll./* □ □ □ */ == r.ur.y-r.ll.y;
}
