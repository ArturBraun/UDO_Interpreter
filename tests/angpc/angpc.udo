comment="Angular profile -combined elements";
bitmap="angpc0.bmp";

PAR("name",ename,"angpc");
PAR("inner radius b",rib,2);
PAR("outer radius b",rob,4);
PAR("inner radius c",ric,3);
PAR("outer radius c",roc,5);
PAR("height (z-dir)",h,4);
PAR("medium",med,"teflon");
PAR("start angle",stang,0);
PAR("end angle",eang,90);
PAR("step angle",step,10);

ENDHEADER;

ELEMENT(z,0,15,med,ename,INn);
 ang=stang;
 NEWLINE(x+rib*cos(ang),y+rib*sin(ang),x+rob*cos(ang),y+rob*sin(ang));
 ang=ang+step;
 while ang<eang do
  ADDLINE(x+rob*cos(ang),y+rob*sin(ang)); 
  ang=ang+step;
 endwhile;
 ADDLINE(x+rob*cos(eang),y+rob*sin(eang)); 
 ang=eang;
 while ang>stang do
  ADDLINE(x+rib*cos(ang),y+rib*sin(ang)); 
  ang=ang-step;
 endwhile;
 CLOSELINE;
ENDELEM;

ELEMENT(z+h,0,16,med,ename,INn);
 ang=stang;
 NEWLINE(x+ric*cos(ang),y+ric*sin(ang),x+roc*cos(ang),y+roc*sin(ang));
 ang=ang+step;
 while ang<eang do
  ADDLINE(x+roc*cos(ang),y+roc*sin(ang)); 
  ang=ang+step;
 endwhile;
 ADDLINE(x+roc*cos(eang),y+roc*sin(eang)); 
 ang=eang;
 while ang>stang do
  ADDLINE(x+ric*cos(ang),y+ric*sin(ang)); 
  ang=ang-step;
 endwhile;
 CLOSELINE;
ENDELEM;

