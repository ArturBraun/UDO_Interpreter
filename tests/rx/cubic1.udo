comment="Cubicoidal structure";
bitmap="cubic10.bmp";

PAR("name", ename, "cubic1");
PAR("length (x-dir)", a, 6 );
PAR("width (y-dir)", b, 5 );
PAR("height (z-dir)", h, 7 );
PAR("medium", med, air );
PAR("type (E/N)", type, E );

ENDHEADER;

TEST( a>0, "Length should be positive" );
TEST( h>=0, "Height should be positive or equal to 0" );
TEST( b>0, "Width should be positive" );
TEST((type=="E")||(type=="N"),"Type can be only E or N ");
TEST((((type=="E")||(type=="N"))&&(h>0))||((type=="E")&&(h==0)),"Type should be E for h equal to 0");

strtype = "INe";  #electric -- default
if type == "N" do #neutral
	strtype = "INn";
endif;

# Normal element
if (type ==  "E") || (type == "N") do
	ELEMENT( z-h/2, h, 0, med, ename, strtype);
		NEWLINE(x, y-b/2, x+a, y-b/2 );
		ADDY(b);
		ADDX(-a);
		CLOSELINE;
	ENDELEM;
endif;
