name="trans";
comment="Trans structure prepared to be used from vivaldi.udo";
bitmap="trans0.bmp";

PAR("name",name,"trans");
PAR("medium",med,"metal");

ENDHEADER;

OPENOBJECT(name);
a=18.5;
b=31.5;
h=0.1;
n=32;
dg=90;
w=40;
d1=10;
we=3;
ELEMENT(z,h,0,med,name,IN);
 step=dg/n;
 NEWLINE(x,y,x+w,y); 
 ADDLINE(x+w,y+d1); 
 i=2;
#elipse 1
 while i<=(n+1) do
  ADDLINE(x+w-a*sin((i-1)*step),y+d1-b*cos((i-1)*step)+b); 
  i++;
 endwhile;
 ADDLINE(x+a,y+d1+b); 
#elipse 2
 i=2;
 while i<=(n+1) do
  ADDLINE(x+a*cos((i-1)*step),y+d1-b*sin((i-1)*step)+b); 
  i++;
 endwhile;
 CLOSELINE;
ENDELEM;

CLOSEOBJ;
