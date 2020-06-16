comment="Cubicoidal structure - type E";
bitmap="cubic0.bmp";

PAR("name", ename, "cubic");
PAR("length (x-dir)", a, 10 );
PAR("width (y-dir)", b, 10 );
PAR("height (z-dir)", h, 10 );
PAR("medium", med, air );

ENDHEADER;

CALL("cubeNested1.udo", ename, a, b, h, med, x+15, y+15, z+15, 9);



