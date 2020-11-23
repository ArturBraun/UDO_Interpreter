comment="Near-To-Far box with absorbing boundaries for 2DV projects";
bitmap="ntf2dv0.bmp";

PAR("AbsLength (x-dir)",L,30);
PAR("AbsRadius",R,10.5);
PAR("NTFLength (x-dir)",dntf,20);
PAR("NTFRadius",sntf,5.5);
PAR("NTFxshift (x-dir)",ntfxs,0);

ENDHEADER;

CIRTYPE(4,air);
OPENOBJECT(Ntf2dv);

w=1; wntf=0.5;

PORT(z, w, MUR, UP, abs_left, NULL);
   NEWLINE(x,y,x,y+R);
   NEWLINE(x, y+R/2, x, y+R/2);
ENDPORT;

PORT(z, w, MUR, DOWN, abs_right, NULL);
   NEWLINE(x+L,y,x+L,y+R);
   NEWLINE(x+L, y+R/2, x+L, y+R/2);
ENDPORT;

PORT(z, w, OPEN, UP, open_y, NULL);
   NEWLINE(x,y,x+L,y);
   NEWLINE(x+L/2, y, x+L/2, y);
ENDPORT;

PORT(z, w, MUR, DOWN, abs_up, NULL);
   NEWLINE(x,y+R,x+L,y+R);
   NEWLINE(x+L/2, y+R, x+L/2, y+R);
ENDPORT;

   xdist=(L-dntf)/2+ntfxs;

   ydist=0;

   zdist=(w-wntf)/2;

PORT(z+zdist, wntf, NEAR2FAR, NONE, ntfbox, NULL);
   NEWLINE(x+xdist, y+ydist, x+dntf+xdist, y+ydist);
   ADDLINE(x+dntf+xdist, y+sntf+ydist);
   ADDLINE(x+xdist, y+sntf+ydist);
   CLOSELINE;
   NEWLINE(x+dntf/2+xdist, y+sntf/2+ydist, x+dntf/2+xdist, y+sntf/2+ydist);
ENDPORT;

CLOSEOBJ;
