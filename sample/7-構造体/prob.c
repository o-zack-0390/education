#include<stdio.h>
#include<stdlib.h>
#include<math.h>

struct point {
  double x;
  double y;
};
struct rectangle{
  struct point ll;
  struct point ur;
};

struct /* □ □ □ */ inputr(void);
double /* □ □ □ */(struct rectangle r);
/* □ □ □ */ lengthd(struct rectangle r);
int issquare(struct rectangle r);

int main(void){
  struct rectangle a, b;
  
  printf("A:\n");
  /* □ □ □ */ = inputr();
  
  printf("The area of A is %f\n", area(a));
  printf("The length of the diagonal of A is %f\n", lengthd(a));
  printf("A is ");
  if (!issquare(a)) printf("NOT ");
  printf("a square");
  
  return 0;
}

struct rectangle /* □ □ □ */(void){
  struct rectangle r;
  
  printf("\tInput the coordinate of the lower left  corner: ");
  scanf("\n(%lf,%lf)", &r.ll./* □ □ □ */, &r.ll.y);
  printf("\tInput the coordinate of the upper right corner: ");
  scanf("\n(%lf,%lf)", &r.ur.x, &r.ur.y);

  if (r.ll.x >= r.ur.x /* ○ ○ ○ */ r.ll.y >= r.ur.y){
    fprintf(stderr, "Inputs are invalid.\n");
    /* □ □ □ */(1);
  }
  return r;
}

double area(struct rectangle r){
  return (r./* □ □ □ */.x - r.ll.x) * (r./* □ □ □ */.y - r.ll.y);
}

double lengthd(struct rectangle r){
  double length;
  double vertical=((r.ur.x - r.ll.x) * (r.ur.x - r.ll.x));
  double side=((r.ur.y - r.ll.y) * (r.ur.y - r.ll.y));
  length=sqrt(vertical/* ○ ○ ○ */side);
  return length;
}

int issquare(struct rectangle r){
  return r.ur.x-r.ll.x/* ○ ○ ○ */r.ur.y-r.ll.y;
}
