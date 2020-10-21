comment="Waveguide to coaxial line transition";
bitmap="wgtocx.bmp";

PAR("object name",oname,"wgtocx");
PAR("wg. width in y-dir (A)",A,10);
PAR("wg. length in x-dir (L)",L,30);
PAR("wg. height in z-dir (B)",B,5);
PAR("coax inner radius (R1)",R1,1);
PAR("coax outer radius (R2)",R2,2.5);
PAR("coax height in z-dir (H)",H,9);
PAR("coax pos. in x-dir (OX)",OX,19.6);
PAR("coax pos. in y-dir (OY)",OY,5);
PAR("anttenna length in z-dir (E)",E,2);
PAR("sectors (N)",N,32);
PAR("inp-to-ref-dist in x-dir (WGRD)",WGRD,5.2);
PAR("out-to-ref-dist in z-dir (CXRD)",CXRD,5);

ENDHEADER;

TEST(A>0 && L>0 && B>0 && R1>0 && R2>0,"A,L,B,R1,R2>0");
TEST((R2>R1) && (R2<A/2),"outer has to be grater then inner and less then width");

xc=x+OX; 
yc=y+OY;

OPENOBJECT(oname);

ELEMENT(z,B,0,air,waveguid,IN);
 NEWLINE(x,y,x+L,y);
 ADDY(A);
 ADDX(-L);
 CLOSELINE;
ENDELEM;

#inner conductor+antenna
CALL("elements/cyv.udo","antenna",R1,E+H,N,metal,"Etype",xc,yc,z+B-E,10);

# coax aif filling

CALL("elements/cyv.udo","coaxair",R2,H,N,air,"Etype",xc,yc,z+B,10);

# input (waveguide port);

CALL("elements/portx.udo","guideinp",B,A,UP,1,WGRD,"guide",x,y,z,11);

# input (waveguide port);

CALL("elements/portz.udo","coaxout",2*R2,2*R2,DOWN,2,CXRD,"coax",xc,yc,z+B+H,11);


CLOSEOBJ;
