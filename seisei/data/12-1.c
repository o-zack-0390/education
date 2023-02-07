#include <stdio.h>
#include <stdlib.h>

struct node
{
	int    type;
	int    val; 
	struct node *left;
	struct node *right; 
};
typedef struct node* EXP;


EXP new_node(int t,int v,EXP l,EXP r)
{
	EXP x = (EXP)malloc(sizeof(EXP));
	
	if(x==NULL)
	{
	   printf("malloc filed");
	   exit(-1);
	}
	
   x->type  = t;
   x->val   = v;
   x->left  = l;
   x->right = r;
   
   return x;
}


EXP v_node(int v)
{
   return new_node('v',v,NULL,NULL);
}


EXP o_node(int o, EXP l, EXP r)
{
   return new_node('o',o,l,r);
}


int calc(EXP e)
{
	if(e->type=='v')
		return e->val;
	
	else if(e->type=='o')
	{
		if(e->val=='+')
			return calc(e->left)+calc(e->right);
		
		if(e->val=='*')
			return (calc(e->left)*calc(e->right));
	}
}


int main(void)
{
   EXP n1,n2,n3,n4,n5,n6,n7;

   n1 = v_node(1);
   n2 = v_node(2);
   n3 = v_node(3);
   n4 = v_node(4);
   n5 = o_node('+',n1,n3);
   n6 = o_node('*',n2,n4);
   n7 = o_node('+',n5,n6);
   
   printf("value=%d\n", calc(n5));
   printf("value=%d\n", calc(n6));
   printf("value=%d\n", calc(n7));

   return 0;
}