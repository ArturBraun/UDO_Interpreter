comment="Rectangular vertical taper";
bitmap="vtape0.bmp";

PAR("name", ename, vtape);
PAR("length (z-dir)", l, 30 );
PAR("bottom width (x-dir)", w1, 12 );
PAR("cover width (x-dir)", w2, 8 );
PAR("bottom height (y-dir)", h1, 6 );
PAR("cover height (y-dir)", h2, 3 );
PAR("medium", med, "air" );
PAR("type (E/N)", type, E );

ENDHEADER;

TEST( l>0, "Lenght should be positive" );
TEST( w1>0, "Width of the bottom should be positive" );
TEST( h1>0, "Height of the bottom should be positive" );
TEST((type=="E")||(type=="N"),"Type can be only E or N ");

b1=h1/2;
a1=w1/2;
b2=h2/2;
a2=w2/2;

strtype = "INe";  #electric -- default
if type == "N" do #neutral
	strtype = "INn";
endif;

	ELEMENT(z,0,5,med,ename,strtype);
	  NEWLINE(x-a1,y-b1,x+a1,y-b1); 
	  ADDY(h1); 
	  ADDX(-w1); 
	CLOSELINE;
	ENDELEM;
	ELEMENT( z+l,0,6,med,ename,strtype );
	   NEWLINE( x-a2, y-b2, x+a2, y-b2); 
	  ADDY(h2); 
	  ADDX(-w2); 
	CLOSELINE;
	ENDELEM;

