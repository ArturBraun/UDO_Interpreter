comment="Tee junction of 2 rect. wg. of different dimensions";
bitmap="rt2w0.bmp";

PAR("Name", oname, rt2w);
PAR("Mainstream width (y-dir)", mw,  6);
PAR("Mainstream height (z-dir)", mh, 4);
PAR("Sidestream width (x-dir)", sw,  4);
PAR("Sidestream height (z-dir)", sh, 3);
PAR("Length of one arm (x-dir&y-dir)", lh, 10);
PAR("Medium", med, air );
PAR("Type (E/N)", type, E );
PAR("Rotation angle", rota, 0);

ENDHEADER;

TEST( lh > 0, "Length must be positive" );
TEST( mw > 0, "Width must be positive" );
TEST( sw > 0, "Width must be positive" );
TEST( mh > 0, "Height must be positive" );
TEST( sh > 0, "Height must be positive" );

OPENOBJECT( oname );

CALL( "solid.udo", oname@one, 2*lh, mw, mh, med, type, 0, x-lh, y, z, 11 );
CALL( "solid.udo", oname@sec, lh,   sw, sh, med, type, 90, x, y, z, 11 );

MARKFJ( OBJECTL, oname@one, PASSIVE );
MARKFJ( OBJECTL, oname@sec, ACTIVE );
JOIN( GLUE );

# Name the resulting objects
RENAME( OBJECTL, LAST, oname );

if rota != 0 do
	MARK( OBJECTL,ALL, SET );
	ROTATE(-rota, x, y );
	MARK( OBJECTL,ALL, RESET );
endif;

CLOSEOBJ;