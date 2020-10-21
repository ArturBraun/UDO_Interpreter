comment="Port for transmission in X-dir with excitation in the port center ";
bitmap="portx1.bmp";

PAR("port name",pname,portx);
PAR("port height (z-dir)",hpo,3);
PAR("port width (y-dir)",wip,3);
PAR("port-to-circuit dir. (UP or DOWN)",pdir,"UP");
PAR("1-inp.,2-outp.",kind,1);
PAR("port-ref. distance (x-dir)",ptr,3);
PAR("port IOP file",pio,NO);

ENDHEADER;

TEST((kind==1)||(kind==2),"port can be only 1-input or 2-output");
TEST((pdir==UP)||(pdir==DOWN),"energy transmission can be only UP or DOWN");

y1=0.5*wip;

portkind=INPTEMPLATE;
actref=pdir;
if (kind==2) do
	portkind=OUTTEMPLATE;
	if pdir=="UP" do 
		actref="DOWN";
	endif;
	if pdir=="DOWN" do 
		actref="UP";
	endif;
endif;

refpos=ptr;
if pdir=="DOWN" do 
	refpos=-ptr;
endif;

portkind=INPTEMPLATE;
if (kind==2) do
	portkind=OUTTEMPLATE;
endif;

PORT(z,hpo,portkind,pdir,pname,r@pname);
	NEWLINE(x,y,x,y+wip);
	NEWLINE(x,y+y1,x,y+y1);
	if pio!="NO" do 
		GETIOPAR(pio@".iop");
	endif;
ENDPORT;

PORT(z,hpo,REFERENCE,actref,r@pname,pname);
	NEWLINE(x+refpos,y,x+refpos,y+wip);
	NEWLINE(x+refpos,y+y1,x+refpos,y+y1);
ENDPORT;

