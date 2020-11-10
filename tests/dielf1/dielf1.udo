comment="waveguide dielectric filter";
bitmap="dielf0.bmp";

PAR("object name",oname,"dif1");
PAR("wg. width ",wgw, 20);
PAR("wgheight ",wgh,10);
PAR("wg. input section length",wgil,20);
PAR("wg. resonator section length",wgrl,20);
PAR("wg. resonator section width",wgrw,12);
PAR("resonator radius",rr,5);
PAR("resonator height",rh,2);
PAR("resonator material",rm,"metal");


ENDHEADER;


OPENOBJECT(oname);

wstep=(wgw-wgrw)*0.5;
cenx=wgil+wgrl*0.5;
rpv=(wgh-rh)*0.5;

ELEMENT(z,wgh,0,air,wg,IN);
 NEWLINE(x,y,x,y-wgw*0.5);
 ADDX(wgil);
 ADDY(wstep);
 ADDX(wgrl);
 ADDY(-wstep);
 ADDX(wgil);
 ADDY(wgw);
 ADDX(-wgil);
 ADDY(-wstep);
 ADDX(-wgrl);
 ADDY(wstep);
 ADDX(-wgil);
 CLOSELINE;
ENDELEM;

CALL( "cyvo.udo", res, rr, rh, 30, rm, E, x+cenx, y, z+rpv, 10 );

# input (waveguide port);
CALL( "portoxe.udo", inp, wgh, wgw, UP, 1, wgh,inp, 0, 0, x, y-wgw*0.5, z, 13 );
CALL( "portoxe.udo", out, wgh, wgw, DOWN, 2, wgh, out, 0, 0, x+cenx*2, y-wgw*0.5, z, 13 );


#CALL("elements/portz.udo","coaxout",2*R2,2*R2,DOWN,2,CXRD,"coax",xc,yc,z+B+H,11);


CLOSEOBJ;
