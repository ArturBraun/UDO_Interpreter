comment="Mesh snapping plane parallel to 0yz plane";
bitmap="specx0.bmp";

PAR("name of element",elname,specx);
PAR("size",size,1);

ENDHEADER;

PORT(z,0,SPECIAL,NONE,elname,NULL);
 NEWLINE(x,y,x,y+size);
 NEWLINE(x,y+size/2,x,y+size/2);
ENDPORT;

