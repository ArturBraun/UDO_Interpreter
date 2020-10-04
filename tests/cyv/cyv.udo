comment="Vertical cylinder ";
bitmap="cyv0.bmp";

PAR("name", ename, "cyv");
PAR("radius", r, 2 );
PAR("height (z-dir)", h, 4 );
PAR("sectors", n, 16 );
PAR("medium", med, "air" );
PAR("type (E/N)", type, E );

ENDHEADER;

if type=="Etype" do
	type="E";
endif;
if type=="Ntype" do
	type="N";
endif;

TEST( r>0, "Length should be positive" );
TEST( h>=0, "Height should be positive or equal to 0" );
TEST( n>2, "n!");
TEST((type=="E")||(type=="N"),"Type can be only E or N ");
TEST((((type=="E")||(type=="N"))&&(h>0))||((type=="E")&&(h==0)),"Type should be E for h equal to 0");

strtype = "INe";  #electric -- default
if type == "N" do #neutral
	strtype = "INn";
endif;

# Normal element
	ELEMENT( z, h, 0, med, ename, strtype );
	 	step=360/n;
	  NEWLINE(x+r,y,x+r*cos(step),y+r*sin(step)); 
	  i=3;
	  while i<=n do
	   ADDLINE(x+r*cos((i-1)*step),y+r*sin((i-1)*step)); 
	   i++;
	  endwhile;
 		CLOSELINE;
	ENDELEM;
