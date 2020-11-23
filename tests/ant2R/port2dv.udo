comment="Port for V2D projects with possible excitation OFF the port center";
bitmap="port2dv0.bmp";

PAR("port name",pname,portv2d);
PAR("port width (y(R)-dir)",wip,3);
PAR("port-to-circuit dir. (UP or DOWN)",pdir,"UP");
PAR("1-inp.,2-outp.",kind,1);
PAR("port-ref. distance (x-dir)",ptr,3);
PAR("port IOP file",pio,NO);
PAR("exc. point shift (in y(R)-dir from the port center)",esr,0);

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

 PORT(z,1,portkind,pdir,pname,r@pname);
 NEWLINE(x,y,x,y+wip);
 NEWLINE(x,y+y1+esr,x,y+y1+esr);
 if pio!="NO" do GETIOPAR(pio@".iop");endif;
 ENDPORT;

 PORT(z,1,REFERENCE,actref,r@pname,pname);
 NEWLINE(x+refpos,y,x+refpos,y+wip);
 NEWLINE(x+refpos,y+y1,x+refpos,y+y1);
 ENDPORT;

CLOSEOBJ;
