comment="Port for transmission in Z-dir with excitation in the port center";
bitmap="portz1.bmp";

PAR("port name",pname,portz);
PAR("port length (x-dir)",lep,3);
PAR("port width (y-dir)",wip,3);
PAR("port-to-circuit dir. (UP or DOWN)", pdir,"UP");
PAR("1-inp.,2-outp.",kind,1);
PAR("port-ref. distance (z-dir)",ptr,3);
PAR("port IOP file",pio,NO);

ENDHEADER;


TEST((kind==1)||(kind==2),"port can be only 1-input or 2-output");
TEST((pdir==UP)||(pdir==DOWN),"energy transmission can be only UP or DOWN");


leph=0.5*lep;
wiph=0.5*wip;

portkind=INPTEMPLATE;
actref=pdir;
if (kind==2) do
portkind=OUTTEMPLATE;
if pdir=="UP" do actref="DOWN";endif;
if pdir=="DOWN" do actref="UP";endif;
endif;

refpos=ptr;
if pdir=="DOWN" do refpos=-ptr;endif;

 PORT(z,0,portkind,pdir,pname,r@pname);
 NEWLINE(x-leph,y-wiph,x+leph,y-wiph);
 ADDY(wip);
 ADDX(-lep);
 CLOSELINE;
 NEWLINE(x,y,x,y);
 if pio!="NO" do GETIOPAR(pio@".iop");endif;
 ENDPORT;

 PORT(z+refpos,0,REFERENCE,actref,r@pname,pname);
 NEWLINE(x-leph,y-wiph,x+leph,y-wiph);
 ADDY(wip);
 ADDX(-lep);
 CLOSELINE;
 NEWLINE(x,y,x,y);
 ENDPORT;


