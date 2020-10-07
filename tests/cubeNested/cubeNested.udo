comment="Cubicoidal structure - type E";
bitmap="cubic0.bmp";

PAR("name", ename, "cubic");
PAR("length (x-dir)", a, 10 );
PAR("width (y-dir)", b, 10 );
PAR("height (z-dir)", h, 10 );
PAR("medium", med, air );

ENDHEADER;

TEST( a>0, "Length should be positive" );
TEST( b>0, "Width should be positive" ); 
TEST( h>=0, "Height should be positive or equal to 0" );

ELEMENT(z,h,0,med,ename,IN);
  NEWLINE(x-a/2, y-b/2, x+a/2, y-b/2 );
  ADDY(b);
  ADDX(-a);
  CLOSELINE;
ENDELEM;

CALL("cubeNested2.udo", ename, a, b, h, med, x, y, z, 9);