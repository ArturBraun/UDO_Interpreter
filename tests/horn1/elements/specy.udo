comment="Mesh snapping plane parallel to 0xz plane";
bitmap="specy0.bmp";

PAR("name of element",elname,specy);
PAR("size",size,1);

ENDHEADER;

PORT(z,0,SPECIAL,NONE,elname,NULL);
 NEWLINE(x,y,x+size,y);
 NEWLINE(x+size/2,y,x+size/2,y);
ENDPORT;

