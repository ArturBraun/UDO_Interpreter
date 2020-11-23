comment="Paraboloidal reflector in V2D";
bitmap="mainR0.bmp";

PAR("Name",name,"mainR");
PAR("Focal length (fl)",fl,100);
PAR("Half angle (ha)",ha,39.2);
PAR("Thickness (th)",th,2);
PAR("Radius of the opening",r,0);
PAR("Medium",med,metal);

ENDHEADER;

hac=cos(ha);
hp=sqrt((1-hac)/(1+hac))*2*fl;
dhp=hp/100;
flq=4*fl;

hpp=dhp;

OPENOBJECT(name);
ELEMENT(z,1,0,metal,reflectpar,IN);
 NEWLINE(x,y,x+th,y); 
 while hpp<hp do
 hpp=hpp+dhp;
 ADDLINE(x+hpp*hpp/flq+th,y+hpp);
 endwhile;

ADDX(-th);

while hpp>dhp do 
 hpp=hpp-dhp;
 ADDLINE(x+hpp*hpp/flq,y+hpp);
 endwhile;
 CLOSELINE;

ENDELEM;

ELEMENT(z,1,0,air,airopening,IN);
NEWLINE(x,y,x+2*th,y);
ADDLINE(x+2*th,y+r);
ADDLINE(x,y+r);
CLOSELINE;
ENDELEM;

MARKFJ(ELEM,airopening,ACTIVE);
MARKFJ(ELEM,reflectpar,PASSIVE);
JOIN(CUT);
MARKFJ(ELEM,reflectpar,RESET);
MARKFJ(ELEM,airopening,RESET);

DELETE(ELEM,airopening);

CLOSEOBJ;
