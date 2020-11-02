comment="Cube NxNxN";
bitmap="nobitmap.bmp";
PAR("name",oname,"cubeNNN");
PAR("N",N,4);
PAR("a",a,2);
ENDHEADER;

OPENOBJECT(oname);
ax=0; ay=0; az=0;
while az<N*a do
  ax=0; ay=0;
  while ay<N*a do
    ax=0;
    while ax < N*a do
	ELEMENT(az,a,0,air,"p","E");
  	  NEWLINE(ax, ay, ax+a, ay);
  	  ADDY(a);
	 ADDX(-a);
	 CLOSELINE;
	ENDELEM;
      ax=ax+a;
    endwhile;
    ay=ay+a;
  endwhile;
  az=az+a;
endwhile;


CLOSEOBJ;
