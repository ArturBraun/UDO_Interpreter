comment="Port for transmission in X-dir with excitation OFF the port center";
bitmap="portxe1.bmp";

PAR("port name",pname,portoxe);
PAR("port height (z-dir)",hpo,3);
PAR("port width (y-dir)",wip,3);
PAR("port-to-circuit dir. (UP or DOWN)",pdir,"UP");
PAR("1-inp.,2-outp.",kind,1);
PAR("port-ref. distance (x-dir)",ptr,3);
PAR("port IOP file",pio,NO);
PAR("exc. point hor. shift (in y-dir from the port center)",eshxy,0);
PAR("exc. point level shift (in z-dir above port's center)",eshz,0);

ENDHEADER;

TEST((kind==1)||(kind==2),"port can be only 1-input or 2-output");
TEST((pdir==UP)||(pdir==DOWN),"energy transmission can be only UP or DOWN");

y1=0.5*wip;

OPENOBJECT(pname);

portkind=INPTEMPLATE;
actref=pdir;
if (kind==2) do
portkind=OUTTEMPLATE;
if pdir=="UP" do actref="DOWN";endif;
if pdir=="DOWN" do actref="UP";endif;
endif;

refpos=ptr;
if pdir=="DOWN" do refpos=-ptr;endif;
portkind=INPTEMPLATE;
if (kind==2) do
portkind=OUTTEMPLATE;
endif;

 PORT(z,hpo,portkind,pdir,pname,r@pname);
 NEWLINE(x,y,x,y+wip);
 NEWLINE(x,y+y1+eshxy,x,y+y1+eshxy);
 PORTEXC(z+0.5*hpo+eshz,z+0.5*hpo+eshz);
 if pio!="NO" do GETIOPAR(pio@".iop");endif;
 ENDPORT;

 PORT(z,hpo,REFERENCE,actref,r@pname,pname);
 NEWLINE(x+refpos,y,x+refpos,y+wip);
 NEWLINE(x+refpos,y+y1,x+refpos,y+y1);
 ENDPORT;

CLOSEOBJ;
