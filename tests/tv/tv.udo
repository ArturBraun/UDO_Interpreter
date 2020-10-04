comment="Vertical taper";
bitmap="tv0.bmp";

PAR("name", ename, tv);
PAR("bottom radius", rb, 4 );
PAR("cover radius", rc, 2 );
PAR("height (z-dir)", h, 4 );
PAR("sectors", n, 16 );
PAR("medium", med, "air" );
PAR("type (E/N)", type, E );

ENDHEADER;

TEST( rc>0, "Radius should be positive" );
TEST( rb>0, "Radius should be positive" );
TEST( h>0, "Height should be positive" );
TEST( n>2, "n!");
TEST((type=="E")||(type=="N"),"Type can be only E or N ");


strtype = "INe";  #electric -- default
if type == "N" do #neutral
	strtype = "INn";
endif;


# Normal element
	ELEMENT( z, 0, 5, med, ename, strtype );
	 	step=360/n;
	  NEWLINE( x+rb, y, x+rb*cos(step), y+rb*sin(step) ); 
	  i=3;
	  while i<=n do
	   ADDLINE( x+rb*cos((i-1)*step), y+rb*sin((i-1)*step) ); 
	   i++;
	  endwhile;
 		CLOSELINE;
	ENDELEM;
	ELEMENT( z+h, 0, 6, med, ename, strtype );
		step=360/n;
		NEWLINE( x+rc, y, x+rc*cos(step), y+rc*sin(step) ); 
		i=3;
		while i<=n do
		 ADDLINE( x+rc*cos((i-1)*step), y+rc*sin((i-1)*step) ); 
		 i++;
		endwhile;
		CLOSELINE;
	ENDELEM;

