comment="NTF surrounded by PML box";
bitmap="pmlntf0.bmp";

PAR("length (x-dir)",l,20);
PAR("width (y-dir)",w,20);
PAR("height (z-dir)",h,20);
PAR("NTFlength (x-dir)",lntf,16);
PAR("NTFwidth (y-dir)",wntf,16);
PAR("NTFheight (z-dir)",hntf,16);
PAR("port IOP file",pio,NO);

ENDHEADER;

TEST( l>0, "Lenght should be positive" );
TEST( w>0, "Width should be positive" );
TEST( h>0, "Height should be positive" );
TEST( lntf>0 && lntf<l, "NTFlenght should be positive and less than lenght." );
TEST( wntf>0 && wntf<w, "NTFwidth should be positive and less than width." );
TEST( hntf>0 && hntf<h, "NTFheight should be positive and less than height." );

CIRTYPE(1,air);
OPENOBJECT(pmlntf);


PORT(z, 0, PML, UP, pml_bot, NULL);
   NEWLINE(x,y,x+l,y);
   ADDLINE(x+l,y+w);
   ADDLINE(x,y+w);
   CLOSELINE;
   NEWLINE(x+l/2, y+w/2, x+l/2, y+w/2);
   if pio!="NO" do GETIOPAR(pio@".iop"); endif;
ENDPORT;


PORT(z+h, 0, PML, DOWN, pml_top, NULL);
   NEWLINE(x,y,x+l,y);
   ADDLINE(x+l,y+w);
   ADDLINE(x,y+w);
   CLOSELINE;
   NEWLINE(x+l/2, y+w/2, x+l/2, y+w/2);
   if pio!="NO" do GETIOPAR(pio@".iop"); endif;
ENDPORT;


PORT(z, h, PML, UP, pml_left, NULL);
   NEWLINE(x,y,x,y+w);
   NEWLINE(x, y+w/2, x, y+w/2);
   if pio!="NO" do GETIOPAR(pio@".iop"); endif;
ENDPORT;

PORT(z, h, PML, DOWN, pml_right, NULL);
   NEWLINE(x+l,y,x+l,y+w);
   NEWLINE(x+l, y+w/2, x+l, y+w/2);
   if pio!="NO" do GETIOPAR(pio@".iop"); endif;
ENDPORT;

PORT(z, h, PML, UP, pml_down, NULL);
   NEWLINE(x,y,x+l,y);
   NEWLINE(x+l/2, y, x+l/2, y);
   if pio!="NO" do GETIOPAR(pio@".iop"); endif;
ENDPORT;

PORT(z, h, PML, DOWN, pml_up, NULL);
   NEWLINE(x,y+w,x+l,y+w);
   NEWLINE(x+l/2, y+w, x+l/2, y+w);
   if pio!="NO" do GETIOPAR(pio@".iop"); endif;	

ENDPORT;

xdist=(l-lntf)/2;
ydist=(w-wntf)/2;
zdist=(h-hntf)/2;

PORT(z+zdist, hntf, NEAR2FAR, NONE, ntfbox, NULL);
   NEWLINE(x+xdist, y+ydist, x+lntf+xdist, y+ydist);
   ADDY(wntf);
   ADDX(-lntf);
   CLOSELINE;
   NEWLINE(x+lntf/2+xdist, y+wntf/2+ydist, x+lntf/2+xdist, y+wntf/2+ydist);
ENDPORT;

CLOSEOBJ;