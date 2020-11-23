comment="Double reflector antenna in V2D";
bitmap="ant2R0.bmp";

PAR("Name",name,"ant2R");
PAR("Focal length of main reflector and c of subreflector",c,451);
PAR("Half angle of main reflector ",hamr,62.745);
PAR("Half angle of subreflector",hasr,62.745);
PAR("Distance between reflectors",a,432);
PAR("Reflector  thickness",th,2);
PAR("Waveguide length",length,30);
PAR("Waveguide  radius",wgh,20);
PAR("Radius of the horn",wiwgh,30);
PAR("Angle of the horn",alpha,17);
PAR("Waveguide thickness",wgt,2);
PAR("Port position",portpos,-20);


ENDHEADER;

#Preparatory operations for drawing a hyperbolic subreflectror

bsq=(c*c)-(a*a);
b=sqrt(bsq);
k=c-a;
xtmp=a+th;
ytmp=0;
yf=(-tan(hasr))*(xtmp-c);

while ytmp<yf do
xtmp=xtmp+k/10000;
ytmp=b*sqrt(((xtmp*xtmp)/(a*a))-1);
yf=(-tan(hasr))*(xtmp-c);
endwhile;

h=ytmp;
ystep=h/100;
tmpy=ystep;

OPENOBJECT(name);

#Drawing of the hyperbolical subreflector

ELEMENT(z,1,0,metal,subref,IN);
NEWLINE(x+a,y,x+a+th,y);
while tmpy<h do
  tmpy=tmpy+ystep;
  ADDLINE(x+th+(a*sqrt(1+ ((tmpy*tmpy)/bsq))),y+tmpy);
endwhile;
ADDX(-th);
while tmpy>ystep do
  tmpy=tmpy-ystep;
  ADDLINE(x+(a*sqrt(1+ ((tmpy*tmpy)/bsq))),y+tmpy);
endwhile;
ADDLINE(x+a,y);
CLOSELINE;
ENDELEM;

#Drawing of an element describing input waveguide and the radiating horn
ELEMENT(0, 1, 0, metal, waveguide, IN);
NEWLINE(x+portpos,y+wgh,x+length+portpos,y+wgh);
ADDLINE( x+((wiwgh-wgh)/tan(alpha))+portpos+length, y+wgh+(wiwgh-wgh) );
ADDLINE( x+((wiwgh-wgh)/tan(alpha))+portpos+length, y+wgh+wgt+(wiwgh-wgh) );
ADDLINE(x+length+portpos,y+wgh+wgt);
ADDX(-length);
CLOSELINE;
ENDELEM;


# Call of the "mainR.udo" describing the shape of the main reflector
CALL("mainR.udo",parrefl,c,hamr,th,wgh+wgt,metal,x,y,z,10);

# Call of a standard library UDO for drawing a circular waveguide port
CALL("port2dv.udo", port, wgh, UP, 1, 18, port, 0.4*wgh, x+portpos, y, z, 11);

# Call of a standard library UDO for drawing absorbing box and near-to-far transformation box
rrad=0.66*c*tan(hamr);
CALL("ntf_2dv.udo", a+10*wgh, rrad+6*wgh, a+4*wgh, rrad+2*wgh, 0, x-4*wgh, y, z, 9 );







CLOSEOBJ;
