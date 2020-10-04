comment="Rotated vertical cylinder";
bitmap="cyv0.bmp";

PAR("name",ename,"cyvr");
PAR("radius",r,2);
PAR("height (z-dir)",h,4);
PAR("sectors",n,16);
PAR("medium",med,"air");
PAR("start angle",stang,0);
PAR("type (E/N)", type, E );

ENDHEADER;

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
		ang=stang+step;
		NEWLINE(x+r*cos(stang),y+r*sin(stang),x+r*cos(ang),y+r*sin(ang)); 
		i=2;
		while i<n do
			ang=stang+i*step;
			ADDLINE(x+r*cos(ang),y+r*sin(ang)); 
			i++;
		endwhile;
		CLOSELINE;
	ENDELEM;
