comment="Mesh snapping plane paralell to 0xy plane with enforced cell-size above ";
bitmap="specz0.bmp";

PAR("name of element",elname,speczu);
PAR("size",size,1);
PAR("forced mesh up",me,1);

ENDHEADER;

PORT(z,0,SPECIAL,NONE,elname,NULL);
 NEWLINE(x,y,x+size,y);
 ADDLINE(x+size,y+size);
 ADDLINE(x,y+size);
 CLOSELINE;
 NEWLINE(x+size/2,y+size/2,x+size/2,y+size/2);
 PORTPAR(0,me,0,1,1,0);
ENDPORT;

