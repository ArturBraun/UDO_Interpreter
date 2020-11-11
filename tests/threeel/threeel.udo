comment="Example of three elemens";
bitmap="threeel0.bmp";

PAR("name", oname, "3el");
PAR("length (x-dir)", a, 6 );
PAR("width (y-dir)", b, 5 );
PAR("height of first elem.(z-dir)", h1, 5 );
PAR("height of second elem.(z-dir)", h2, 7 );
PAR("height of third elem.(z-dir)", h3, 3 );
PAR("shape ratio top/bottom", sr, 0.5);
PAR("medium", med, air );


ENDHEADER;

TEST( (a>0)&&(b>0)&&(h1>0)&&(h2>0)&&(h3>0), "Dimensions should be positive" );

OPENOBJECT(oname);

ELEMENT( z, h1, 0, med, cubic1,IN);
 NEWLINE(x-a/2, y-b/2, x+a/2, y-b/2);
 ADDLINE(x+a/2,y+b/2);
 ADDLINE(x-a/2,y+b/2);
 CLOSELINE;
ENDELEM;

ELEMENT( z+h1,0, 5, med, prismb,INe);
 NEWLINE(x-a/2, y-b/2, x+a/2, y-b/2);
 ADDLINE(x+a/2,y+b/2);
 ADDLINE(x-a/2,y+b/2);
 CLOSELINE;
ENDELEM;

ELEMENT( z+h1+h2,0, 6, med, prismt,INe);
 NEWLINE(x-sr*a/2, y-sr*b/2, x+sr*a/2, y-sr*b/2);
 ADDLINE(x+sr*a/2,y+sr*b/2);
 ADDLINE(x-sr*a/2,y+sr*b/2);
 CLOSELINE;
ENDELEM;

ELEMENT( z+h1+h2, h3, 0, med, cubic3,INn);
 NEWLINE(x-sr*a/2, y-sr*b/2, x+sr*a/2, y-sr*b/2);
 ADDY(sr*b);
 ADDX(-sr*a);
 CLOSELINE;
ENDELEM;

CLOSEOBJ;
