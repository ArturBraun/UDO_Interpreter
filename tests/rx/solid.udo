comment="Cuboid";
bitmap="solid0.bmp";

PAR("name", oname, "solid");
PAR("length (x-dir)", a, 6 );
PAR("width (y-dir)", b, 5 );
PAR("height (z-dir)", h, 7 );
PAR("medium", med, air );
PAR("type (E/N)", type, E );
PAR("rotation angle", rota, 0);

ENDHEADER;

TEST( a>0, "Length should be positive" );
TEST( h>=0, "Height should be positive or equal to 0" );
TEST( b>0, "Width should be positive" );
TEST((((type=="E")||(type=="N"))&&(h>0))||((type=="E")&&(h==0)),"Type should be E for h equal to 0");


OPENOBJECT(oname);

CALL("cubic1.udo", oname, a, b, h, med, type, x, y, z, 10);

if rota != 0 do
  MARK( ELEML,ALL, SET );
  ROTATE(-rota, x, y );
  MARK( ELEML,ALL, RESET );
endif;
CLOSEOBJ;
