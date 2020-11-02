comment="Circular patch antenna with lumped source feed";
bitmap="patch20.bmp";

PAR("object name",oname,"patch1");
PAR("patch diameter",pd,21);
PAR("patch thickness (z-dir)",pth,0.5);
PAR("dielectric mt.",dim,"teflon");
PAR("dielectric th.(z-dir)",dth,1);
PAR("base diameter",bd,50);
PAR("base thickness (z-dir)",bth,0.5);
PAR("feed x-position (x-dir)",cxp,-3);
PAR("cell size around feed",cxr,1);
PAR("feed wire diameter",fwd,0.3);
PAR("port IOP file",inp,"NO");

ENDHEADER;

INSERTMEDIUM(dim,"ISOTROPIC");
MEDIUMPAR(dim,12.45,1,0.1433,0,12.45,1,0.1433,0,12.45,1,0.1433,0,0);
MEDIUMCOL(dim,229,229,178,0,1,229,229,178,228,243,146,99);

sec=1;
n=360;
siz=0.1*cxr;

OPENOBJECT(oname);

xof=x+cxp;

b1=0.5*bd;
ELEMENT(z-bth,bth,0,metal,base,IN);
 NEWLINE(x+b1,y,x+b1*cos(sec),y+b1*sin(sec));
 i=3;
 while i<n do
  ADDLINE(x+b1*cos(i*sec),y+b1*sin(i*sec));
  i++;
 endwhile;
 CLOSELINE;
ENDELEM;

b1=0.5*bd;
ELEMENT(z,dth,0,dim,diel,IN);
 NEWLINE(x+b1,y,x+b1*cos(sec),y+b1*sin(sec));
 i=3;
 while i<n do
  ADDLINE(x+b1*cos(i*sec),y+b1*sin(i*sec));
  i++;
 endwhile;
 CLOSELINE;
ENDELEM;

b1=0.5*pd;
ELEMENT(z+dth,pth,0,metal,patch,IN);
 NEWLINE(x+b1,y,x+b1*cos(sec),y+b1*sin(sec));
 i=3;
 while i<n do
  ADDLINE(x+b1*cos(i*sec),y+b1*sin(i*sec));
  i++;
 endwhile;
 CLOSELINE;
ENDELEM;


CLOSEOBJ;