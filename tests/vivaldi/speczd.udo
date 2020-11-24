comment="Mesh snapping plane parallel to 0xy plane with enforced cell-size below ";
bitmap="specz0.bmp";

PAR("name of element",elname,speczd);
PAR("size",size,1);
PAR("forced mesh down",me,1);

ENDHEADER;

PORT(z,0,SPECIAL,NONE,elname,NULL);
 NEWLINE(x,y,x+size,y);
 ADDLINE(x+size,y+size);
 ADDLINE(x,y+size);
 CLOSELINE;
 NEWLINE(x+size/2,y+size/2,x+size/2,y+size/2);
 PORTPAR(me,0,1,0,1,0);
ENDPORT;

