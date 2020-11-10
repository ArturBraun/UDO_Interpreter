comment="Circular waveguide for heating with linear or circular polarisation";
bitmap="cwgh0.bmp";

PAR( "Object name", onam, cwgh );
PAR( "Waveguide length (z-dir)", wl, 300);
PAR( "Waveguide radius", wr, 50);
PAR( "Load length (z-dir)", ll, 100);
PAR( "Load radius", lr, 15 );
PAR( "Load medium", med, air );
PAR( "Port-ref. distance (z-dir)",ptr,30);
PAR(" Add second source Y/N",source2, "N");
PAR(" Add second load Y/N",load2, "N");
PAR( "V-ports IOP file", piov, "NO");
PAR( "H-ports IOP file", pioh, "NO");
PAR( "Sectors", sec, 64);

ENDHEADER;

TEST( wl>0 && ll>0, "Length should be greater than 0" );
TEST( wr>0 && lr>0, "Radius should be greater than 0" );
TEST( wl>(2*ptr+ll), "Waveguide length should be greater than load plus double port-ref distance" );

OPENOBJECT(onam);

CALL( "elements/cyv.udo", onam@wg, wr, wl, sec, air, E, x, y, z, 10 );
CALL( "elements/cyv.udo", onam@ld, lr, ll, sec, med, E, x, y, z+(wl-ll)/2, 10 );
CALL( "elements/portz.udo", onam@inp1, 2*wr, 2*wr,UP, 1, ptr, piov, x, y, z, 11 ); 
CALL( "elements/portz.udo", onam@out1, 2*wr, 2*wr,DOWN, 2, ptr, piov, x, y, z+wl, 11 ); 
if source2==Y do
 CALL( "elements/portz.udo", onam@inp2, 2*wr, 2*wr,UP, 1, ptr, pioh, x, y, z, 11 ); 
endif;
if load2==Y do
 CALL( "elements/portz.udo", onam@out2, 2*wr, 2*wr,DOWN, 2, ptr, pioh, x, y, z+w1, 11 ); 
endif;

CLOSEOBJ;
