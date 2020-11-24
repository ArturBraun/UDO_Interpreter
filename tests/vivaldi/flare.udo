name="flare";
comment="Flare structure prepared to be used from vivaldi.udo";
bitmap="flare0.bmp";

PAR("name",name,"flare");
PAR("orient",orient,-1);
PAR("medium",med,"metal");

ENDHEADER;

OPENOBJECT(name);
r=18.5;
a=9;
b=30;
h=0.1;
n=32;
dg=90;
ELEMENT(z,h,0,med,name,IN);
 step=dg/n;
 NEWLINE(x,y,x,y+r); 
# NEWLINE(x,y,x+a*cos(step)-a,y+b*sin(step)); 
 i=2;
#elipse
 while i<=(n+1) do
  ADDLINE(x+a*cos((i-1)*step)-a,y+b*sin((i-1)*step)+r); 
  i++;
 endwhile;
 ADDLINE(x-a-12.5,y+b+r); 
 ADDLINE(x-a-12.5,y+r); 
#circle
 i=2;
 while i<=(n+1) do
  ADDLINE(x+r*sin((i-1)*step)-21.5,y+r*cos((i-1)*step)); 
  i++;
 endwhile;
 CLOSELINE;
ENDELEM;

if orient>0 do
 MARK(ELEM,name,SET);
 MIRROR(0,0,1);
 MARK(ELEM,name,RESET);
endif;

CLOSEOBJ;
