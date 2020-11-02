comment="Rectangular waveguide horn (vertical) ";
bitmap="horn10.bmp";

PAR("object name",oname,"horn1");
PAR("waveguide width in x-dir (ww)",ww,10);
PAR("waveguide height in y-dir (wh)",wh,5);
PAR("waveguide length in z-dir (wl)",wl,20);
PAR("horn width in x-dir (hw)",hw,20);
PAR("horn height in y-dir (hh)",hh,15);
PAR("horn length in z-dir (hl)",hl,30);
PAR("wall thickness (wt)",wt,2);
PAR("inp-to-ref-dist in z-dir (inrd)",inrd,5);
PAR("port IOP file",pio,NO);

ENDHEADER;

TEST( ww > 0, "Width should be positive");
TEST( hw > 0, "Width should be positive");
TEST( wh > 0, "Height should be positive");
TEST( hh > 0, "Height should be positive");
TEST( wl > 0, "Length should be positive");
TEST( hl > 0, "Length should be positive");
TEST( wt > 0, "Thickness should be positive");

wwh=0.5*ww;
whh=0.5*wh;
hwh=0.5*hw;
hhh=0.5*hh;

OPENOBJECT(oname);

ELEMENT(z-wl,wl,0,metal,wgu,IN);
 NEWLINE(x-wwh-wt,y-whh-wt,x+wwh+wt,y-whh-wt);
 ADDY(wh+2*wt);
 ADDX(-ww-2*wt);
 ADDY(-wh-2*wt);
 ADDLINE(x-wwh,y-whh);
 ADDY(wh);
 ADDX(ww);
 ADDY(-wh);
 ADDX(-ww);
 CLOSELINE;
ENDELEM;

ELEMENT(z,0,5,metal,horn,IN);
 NEWLINE(x-wwh-wt,y-whh-wt,x+wwh+wt,y-whh-wt);
 ADDY(wh+2*wt);
 ADDX(-ww-2*wt);
 ADDY(-wh-2*wt);
 ADDLINE(x-wwh,y-whh);
 ADDY(wh);
 ADDX(ww);
 ADDY(-wh);
 ADDX(-ww);
 CLOSELINE;
ENDELEM;

ELEMENT(z+hl,0,6,metal,horn,IN);
 NEWLINE(x-hwh-wt,y-hhh-wt,x+hwh+wt,y-hhh-wt);
 ADDY(hh+2*wt);
 ADDX(-hw-2*wt);
 ADDY(-hh-2*wt);
 ADDLINE(x-hwh,y-hhh);
 ADDY(hh);
 ADDX(hw);
 ADDY(-hh);
 ADDX(-hw);
 CLOSELINE;
ENDELEM;

# input (waveguide port);
CALL("elements/specx.udo",spx1,0.01*ww,x-hwh,y,z,6);
CALL("elements/specx.udo",spx2,0.01*ww,x+hwh,y,z,6);
CALL("elements/specy.udo",spy1,0.01*ww,x,y-hhh,z,6);
CALL("elements/specy.udo",spy2,0.01*ww,x,y+hhh,z,6);

if inrd>0 do
  CALL("elements/portz.udo",inp,ww,wh,UP,1,inrd,pio,x,y,z-wl,11);
endif;

CLOSEOBJ;
