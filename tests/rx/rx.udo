comment="Jct. of 2 horizontal rectangular wg. of equal dim.";
bitmap="rx0.bmp";

PAR("Name", oname, rx);
PAR("Width", w, 6);
PAR("Height (z-dir)", h, 5);
PAR("Length of one arm", lh, 10);
PAR("Medium", med, air);
PAR("Type (E/N)", type, E );
PAR("Rotation angle", rota,0);

ENDHEADER;

TEST( lh > 0, "Length must be positive" );
TEST( w > 0, "Diameter must be positive" );
TEST( h > 0, "Height must be positive" );

OPENOBJECT( oname );
  
  CALL( "solid.udo", oname@one, lh*2, w, h, med, type, 90, x, y-lh, z, 11 );
  CALL( "solid.udo", oname@sec, lh*2, w, h, med, type, 0, x-lh, y, z, 11 );
  
  MARKFJ( OBJECTL, oname@one, PASSIVE );
  MARKFJ( OBJECTL, oname@sec, ACTIVE );
  JOIN( GLUE );
  
  # Name the resulting objects
  RENAME( OBJECTL, LAST, oname@all );
    
  # Remove the two original objects
  DELETE( OBJECTL, oname@one );
  DELETE( OBJECTL, oname@sec );

  MARKFJ( OBJECTL, ALL, RESET );
  
  if rota != 0 do
    MARK( OBJECTL,ALL, SET );
    ROTATE(-rota, x, y );
    MARK( OBJECTL,ALL, RESET );
  endif;
CLOSEOBJ;
