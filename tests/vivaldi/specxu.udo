comment="Mesh snapping plane parallel to 0yz plane with enforced cell-size above";
bitmap="specx0.bmp";

PAR("name of element",elname,specxu);
PAR("size",size,1);
PAR("forced mesh up",me,1);

ENDHEADER;

PORT(z,0,SPECIAL,NONE,elname,NULL);
 NEWLINE(x,y,x,y+size);
 NEWLINE(x,y+size/2,x,y+size/2);
PORTPAR(0,me,0,1,1,0);
ENDPORT;

