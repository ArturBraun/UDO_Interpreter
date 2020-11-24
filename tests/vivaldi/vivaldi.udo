comment="Vivaldi antenna considered in the Manual (Sec.2.3.5) ";
bitmap="vivaldi0.bmp";

PAR("object name",oname,"vivaldi");

ENDHEADER;
wa=40;
la=90;
wt=3;
xbox=80;
ybox=120;
hbox=40;
he=1.5748;
be=2*he;

INSERTMEDIUM("RD5870",ISOTROPIC);
MEDIUMPAR("RD5870",2.06,1,0,0,2.06,1,0,0,2.06,1,0,0,0);
THERMALPAR("RD5870",20,1,0,0,0);
MEDIUMCOL("RD5870",0,139,139,0,1,0,0,128,85,107,47,6);

OPENOBJECT(oname);
#substrate
CALL ("solid.udo",substrate,wa,la,be,RD5870,E,0,x,y+la/2,z+be/2,11);
#lower flare
CALL ("flare.udo",lflare,-1,metal,x+21.5,y+41.5,z,7);
#upper flare
CALL ("flare.udo",uflare,-1,metal,x+21.5,y+41.5,z+be,7);
#inner flare
CALL ("flare.udo",iflare,+1,metal,x-18.5,y+41.5,z+he,7);
#lower transition
CALL ("trans.udo",ltrans,metal,x,y,z,6);
#upper transition
CALL ("trans.udo",utrans,metal,x,y,z+be,6);

#stripline
ELEMENT(z+he,0.1,0,metal,strip,IN);
  NEWLINE(x+18.5,y,x+18.5+wt,y);
  ADDLINE(x+18.5+wt,y+41.5);
  ADDLINE(x+18.5,y+41.5);
  CLOSELINE;
ENDELEM;

MARKFJ(ELEM,lflare,ACTIVE);
MARKFJ(ELEM,ltrans,PASSIVE);
JOIN(GLUE);
#rename glue object name to lflare 
RENAME(OBJECT,LAST,lflare);
MARKFJ(OBJECT,ALL,RESET);

MARKFJ(ELEM,uflare,ACTIVE);
MARKFJ(ELEM,utrans,PASSIVE);
JOIN(GLUE);
#rename glue object name to uflare 
RENAME(OBJECT,LAST,uflare);
MARKFJ(OBJECT,ALL,RESET);

#MARKFJ(ELEM,iflare,ACTIVE);
#MARKFJ(ELEM,strip,PASSIVE);
#JOIN(GLUE);
##rename glue object name to iflare 
#RENAME(OBJECT,LAST,iflare);
#MARKFJ(OBJECT,ALL,RESET);


#NTF
CALL ("pmlntf.udo",xbox,ybox,hbox,wa+10,la+10,be+10,"pmlall",x-xbox/2+wa/2,y-ybox/2+la/2,z-hbox/2,11);

#mesh snapping planes
CALL( "specxu.udo", spxl1, 1, 0.25, x+14, y,   z,   7 ); 
CALL( "specxd.udo", spxp1, 1, 0.25, x+26, y,   z,   7 ); 
CALL( "speczu.udo", spzl1, 1, 0.5,  x,    y,   z-2, 7 ); 
CALL( "speczd.udo", spzp1, 1, 0.5,  x,    y,   z+5, 7 ); 
#metal near port area
CALL ("solid.udo",m1,14,0.1,be,metal,E,0,x,y-0.1/2,z+be/2,11);
CALL ("solid.udo",m2,14,0.1,be,metal,E,0,x+26,y-0.1/2,z+be/2,11);
#input port
CALL( "portoye.udo", ip, 3.1496, 12, UP, 1, 5, ip, 0, 0, x+14, y, z, 13 );

CLOSEOBJ;
