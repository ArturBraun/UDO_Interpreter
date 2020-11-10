comment="Vertical cylinder ";
bitmap="cyv0.bmp";

PAR("name", oname, "cyvo");
PAR("radius", r, 2 );
PAR("height (z-dir)", h, 4 );
PAR("sectors", n, 16 );
PAR("medium", med, "air" );
PAR("type (E/N)", type, E );

ENDHEADER;

TEST( r>0, "Length should be positive" );
TEST( h>=0, "Height should be positive or equal to 0" );
TEST( n>2, "n!");
TEST((((type=="E")||(type=="N"))&&(h>0))||((type=="E")&&(h==0)),"Type should be E for h equal to 0");

OPENOBJECT(oname);

CALL("cyv.udo",oname,r,h,n,med,type,x,y,z,10);
CLOSEOBJ;
