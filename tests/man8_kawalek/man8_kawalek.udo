PAR("Fat",Fat,"Fat");
PAR("BoneCortical",BoneCortical,"BoneCortical");
PAR("SkinDry",SkinDry,"SkinDry");
PAR("Muscle",Muscle,"Muscle");
PAR("BoneMarrow",BoneMarrow,"BoneMarrow");
PAR("Tendon",Tendon,"Tendon");
PAR("ZeroAir",ZeroAir,"ZeroAir");
PAR("e_1",e_1,"e_1");
PAR("e_2",e_2,"e_2");
PAR("e_3",e_3,"e_3");
PAR("e_4",e_4,"e_4");
PAR("e_5",e_5,"e_5");
PAR("e_6",e_6,"e_6");
PAR("e_7",e_7,"e_7");
PAR("e_8",e_8,"e_8");
PAR("e_9",e_9,"e_9");
PAR("e_10",e_10,"e_10");
PAR("e_11",e_11,"e_11");
PAR("e_12",e_12,"e_12");
PAR("e_13",e_13,"e_13");
PAR("e_14",e_14,"e_14");
PAR("e_15",e_15,"e_15");
PAR("e_16",e_16,"e_16");
PAR("e_17",e_17,"e_17");
PAR("e_18",e_18,"e_18");
PAR("e_19",e_19,"e_19");
PAR("e_20",e_20,"e_20");
PAR("e_21",e_21,"e_21");
PAR("e_22",e_22,"e_22");
PAR("e_23",e_23,"e_23");
PAR("e_24",e_24,"e_24");
PAR("e_25",e_25,"e_25");
PAR("e_26",e_26,"e_26");
PAR("e_27",e_27,"e_27");
PAR("e_28",e_28,"e_28");
PAR("e_29",e_29,"e_29");
PAR("e_30",e_30,"e_30");
PAR("e_31",e_31,"e_31");
PAR("e_32",e_32,"e_32");
PAR("e_33",e_33,"e_33");
PAR("e_34",e_34,"e_34");
PAR("e_35",e_35,"e_35");
PAR("e_36",e_36,"e_36");
PAR("e_37",e_37,"e_37");
PAR("e_38",e_38,"e_38");
PAR("e_39",e_39,"e_39");
PAR("e_40",e_40,"e_40");
PAR("e_41",e_41,"e_41");
PAR("e_42",e_42,"e_42");
PAR("e_43",e_43,"e_43");
PAR("e_44",e_44,"e_44");
PAR("e_45",e_45,"e_45");
PAR("e_46",e_46,"e_46");
PAR("e_47",e_47,"e_47");
PAR("e_48",e_48,"e_48");
PAR("e_49",e_49,"e_49");
PAR("e_50",e_50,"e_50");

ENDHEADER;

OPENOBJECT(test224);
INSERTMEDIUM(Fat,"ISOTROPIC");
MEDIUMPAR(Fat,5.462,1,0.051,0,5.462,1,0.051,0,5.462,1,0.051,0,0);
MEDIUMCOL(Fat,159,255,95,0,1,159,255,95,60,217,132,99);
ELEMENT(z+(16),8,0,Fat,e_1,IN);
NEWLINE(x+(192),y+(552),x+(192),y+(544));
ADDLINE(x+(184),y+(544));
ADDLINE(x+(184),y+(536));
ADDLINE(x+(192),y+(536));
ADDLINE(x+(192),y+(520));
ADDLINE(x+(200),y+(520));
ADDLINE(x+(200),y+(512));
ADDLINE(x+(208),y+(512));
ADDLINE(x+(208),y+(504));
ADDLINE(x+(224),y+(504));
ADDLINE(x+(224),y+(496));
ADDLINE(x+(232),y+(496));
ADDLINE(x+(232),y+(488));
ADDLINE(x+(248),y+(488));
ADDLINE(x+(248),y+(512));
ADDLINE(x+(264),y+(512));
ADDLINE(x+(264),y+(520));
ADDLINE(x+(240),y+(520));
ADDLINE(x+(240),y+(528));
ADDLINE(x+(248),y+(528));
ADDLINE(x+(248),y+(536));
ADDLINE(x+(224),y+(536));
ADDLINE(x+(224),y+(544));
ADDLINE(x+(232),y+(544));
ADDLINE(x+(232),y+(552));
CLOSELINE;
ENDELEM;
INSERTMEDIUM(BoneCortical,"ISOTROPIC");
MEDIUMPAR(BoneCortical,12.45,1,0.1433,0,12.45,1,0.1433,0,12.45,1,0.1433,0,0);
MEDIUMCOL(BoneCortical,229,229,178,0,1,229,229,178,228,243,146,99);
ELEMENT(z+(16),8,0,BoneCortical,e_2,IN);
NEWLINE(x+(232),y+(552),x+(232),y+(544));
ADDLINE(x+(240),y+(544));
ADDLINE(x+(240),y+(552));
CLOSELINE;
ENDELEM;
INSERTMEDIUM(SkinDry,"ISOTROPIC");
MEDIUMPAR(SkinDry,41.41,1,0.8667,0,41.41,1,0.8667,0,41.41,1,0.8667,0,0);
MEDIUMCOL(SkinDry,255,242,127,0,1,255,242,127,29,231,148,99);
ELEMENT(z+(16),8,0,SkinDry,e_3,IN);
NEWLINE(x+(240),y+(552),x+(240),y+(536));
ADDLINE(x+(248),y+(536));
ADDLINE(x+(248),y+(552));
CLOSELINE;
ENDELEM;
ELEMENT(z+(16),8,0,SkinDry,e_4,IN);
NEWLINE(x+(224),y+(544),x+(224),y+(536));
ADDLINE(x+(232),y+(536));
ADDLINE(x+(232),y+(544));
CLOSELINE;
ENDELEM;
ELEMENT(z+(16),8,0,Fat,e_5,IN);
NEWLINE(x+(232),y+(544),x+(232),y+(536));
ADDLINE(x+(240),y+(536));
ADDLINE(x+(240),y+(544));
CLOSELINE;
ENDELEM;
ELEMENT(z+(16),8,0,BoneCortical,e_6,IN);
NEWLINE(x+(248),y+(536),x+(248),y+(528));
ADDLINE(x+(256),y+(528));
ADDLINE(x+(256),y+(536));
CLOSELINE;
ENDELEM;
ELEMENT(z+(16),8,0,SkinDry,e_7,IN);
NEWLINE(x+(240),y+(528),x+(240),y+(520));
ADDLINE(x+(264),y+(520));
ADDLINE(x+(264),y+(528));
CLOSELINE;
ENDELEM;
ELEMENT(z+(16),8,0,BoneCortical,e_8,IN);
NEWLINE(x+(264),y+(520),x+(264),y+(512));
ADDLINE(x+(272),y+(512));
ADDLINE(x+(272),y+(520));
CLOSELINE;
ENDELEM;
ELEMENT(z+(16),8,0,SkinDry,e_9,IN);
NEWLINE(x+(256),y+(512),x+(256),y+(504));
ADDLINE(x+(272),y+(504));
ADDLINE(x+(272),y+(512));
CLOSELINE;
ENDELEM;
ELEMENT(z+(16),8,0,Fat,e_10,IN);
NEWLINE(x+(272),y+(512),x+(272),y+(504));
ADDLINE(x+(280),y+(504));
ADDLINE(x+(280),y+(512));
CLOSELINE;
ENDELEM;
ELEMENT(z+(16),8,0,BoneCortical,e_11,IN);
NEWLINE(x+(280),y+(512),x+(280),y+(504));
ADDLINE(x+(288),y+(504));
ADDLINE(x+(288),y+(512));
CLOSELINE;
ENDELEM;
ELEMENT(z+(16),8,0,SkinDry,e_12,IN);
NEWLINE(x+(272),y+(504),x+(272),y+(496));
ADDLINE(x+(288),y+(496));
ADDLINE(x+(288),y+(504));
CLOSELINE;
ENDELEM;
ELEMENT(z+(16),8,0,Fat,e_13,IN);
NEWLINE(x+(272),y+(496),x+(272),y+(480));
ADDLINE(x+(288),y+(480));
ADDLINE(x+(288),y+(488));
ADDLINE(x+(296),y+(488));
ADDLINE(x+(296),y+(496));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,Fat,e_14,IN);
NEWLINE(x+(176),y+(552),x+(176),y+(520));
ADDLINE(x+(192),y+(520));
ADDLINE(x+(192),y+(512));
ADDLINE(x+(200),y+(512));
ADDLINE(x+(200),y+(504));
ADDLINE(x+(208),y+(504));
ADDLINE(x+(208),y+(496));
ADDLINE(x+(216),y+(496));
ADDLINE(x+(216),y+(480));
ADDLINE(x+(224),y+(480));
ADDLINE(x+(224),y+(472));
ADDLINE(x+(248),y+(472));
ADDLINE(x+(248),y+(480));
ADDLINE(x+(296),y+(480));
ADDLINE(x+(296),y+(488));
ADDLINE(x+(256),y+(488));
ADDLINE(x+(256),y+(496));
ADDLINE(x+(272),y+(496));
ADDLINE(x+(272),y+(504));
ADDLINE(x+(216),y+(504));
ADDLINE(x+(216),y+(520));
ADDLINE(x+(208),y+(520));
ADDLINE(x+(208),y+(528));
ADDLINE(x+(216),y+(528));
ADDLINE(x+(216),y+(536));
ADDLINE(x+(192),y+(536));
ADDLINE(x+(192),y+(544));
ADDLINE(x+(232),y+(544));
ADDLINE(x+(232),y+(552));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,SkinDry,e_15,IN);
NEWLINE(x+(232),y+(552),x+(232),y+(544));
ADDLINE(x+(224),y+(544));
ADDLINE(x+(224),y+(536));
ADDLINE(x+(240),y+(536));
ADDLINE(x+(240),y+(552));
CLOSELINE;
ENDELEM;
INSERTMEDIUM(Muscle,"ISOTROPIC");
MEDIUMPAR(Muscle,55.03,1,0.9429,0,55.03,1,0.9429,0,55.03,1,0.9429,0,0);
MEDIUMCOL(Muscle,255,95,0,0,1,255,95,0,220,106,151,99);
ELEMENT(z+(24),8,0,Muscle,e_16,IN);
NEWLINE(x+(192),y+(544),x+(192),y+(536));
ADDLINE(x+(200),y+(536));
ADDLINE(x+(200),y+(544));
CLOSELINE;
ENDELEM;
INSERTMEDIUM(BoneMarrow,"ISOTROPIC");
MEDIUMPAR(BoneMarrow,5.504,1,0.0402,0,5.504,1,0.0402,0,5.504,1,0.0402,0,0);
MEDIUMCOL(BoneMarrow,229,229,178,0,1,229,229,178,17,231,160,99);
ELEMENT(z+(24),8,0,BoneMarrow,e_17,IN);
NEWLINE(x+(200),y+(544),x+(200),y+(536));
ADDLINE(x+(208),y+(536));
ADDLINE(x+(208),y+(544));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,BoneCortical,e_18,IN);
NEWLINE(x+(208),y+(544),x+(208),y+(536));
ADDLINE(x+(216),y+(536));
ADDLINE(x+(216),y+(544));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,Fat,e_19,IN);
NEWLINE(x+(216),y+(544),x+(216),y+(536));
ADDLINE(x+(224),y+(536));
ADDLINE(x+(224),y+(544));
CLOSELINE;
ENDELEM;
INSERTMEDIUM(Tendon,"ISOTROPIC");
MEDIUMPAR(Tendon,45.83,1,0.7184,0,45.83,1,0.7184,0,45.83,1,0.7184,0,0);
MEDIUMCOL(Tendon,198,198,86,0,1,198,198,86,26,175,98,99);
ELEMENT(z+(24),8,0,Tendon,e_20,IN);
NEWLINE(x+(216),y+(536),x+(216),y+(528));
ADDLINE(x+(224),y+(528));
ADDLINE(x+(224),y+(536));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,BoneCortical,e_21,IN);
NEWLINE(x+(224),y+(536),x+(224),y+(528));
ADDLINE(x+(232),y+(528));
ADDLINE(x+(232),y+(536));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,Fat,e_22,IN);
NEWLINE(x+(232),y+(536),x+(232),y+(520));
ADDLINE(x+(240),y+(520));
ADDLINE(x+(240),y+(504));
ADDLINE(x+(264),y+(504));
ADDLINE(x+(264),y+(512));
ADDLINE(x+(256),y+(512));
ADDLINE(x+(256),y+(520));
ADDLINE(x+(248),y+(520));
ADDLINE(x+(248),y+(528));
ADDLINE(x+(240),y+(528));
ADDLINE(x+(240),y+(536));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,BoneCortical,e_23,IN);
NEWLINE(x+(240),y+(536),x+(240),y+(528));
ADDLINE(x+(248),y+(528));
ADDLINE(x+(248),y+(536));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,SkinDry,e_24,IN);
NEWLINE(x+(248),y+(536),x+(248),y+(520));
ADDLINE(x+(256),y+(520));
ADDLINE(x+(256),y+(536));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,Tendon,e_25,IN);
NEWLINE(x+(208),y+(528),x+(208),y+(520));
ADDLINE(x+(216),y+(520));
ADDLINE(x+(216),y+(528));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,BoneMarrow,e_26,IN);
NEWLINE(x+(216),y+(528),x+(216),y+(520));
ADDLINE(x+(224),y+(520));
ADDLINE(x+(224),y+(528));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,Tendon,e_27,IN);
NEWLINE(x+(224),y+(528),x+(224),y+(520));
ADDLINE(x+(216),y+(520));
ADDLINE(x+(216),y+(504));
ADDLINE(x+(240),y+(504));
ADDLINE(x+(240),y+(512));
ADDLINE(x+(232),y+(512));
ADDLINE(x+(232),y+(528));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,BoneCortical,e_28,IN);
NEWLINE(x+(232),y+(520),x+(232),y+(512));
ADDLINE(x+(240),y+(512));
ADDLINE(x+(240),y+(520));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,BoneCortical,e_29,IN);
NEWLINE(x+(256),y+(520),x+(256),y+(512));
ADDLINE(x+(264),y+(512));
ADDLINE(x+(264),y+(520));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,SkinDry,e_30,IN);
NEWLINE(x+(264),y+(520),x+(264),y+(512));
ADDLINE(x+(272),y+(512));
ADDLINE(x+(272),y+(520));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,BoneCortical,e_31,IN);
NEWLINE(x+(264),y+(512),x+(264),y+(504));
ADDLINE(x+(272),y+(504));
ADDLINE(x+(272),y+(512));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,SkinDry,e_32,IN);
NEWLINE(x+(272),y+(512),x+(272),y+(496));
ADDLINE(x+(288),y+(496));
ADDLINE(x+(288),y+(504));
ADDLINE(x+(280),y+(504));
ADDLINE(x+(280),y+(512));
CLOSELINE;
ENDELEM;
INSERTMEDIUM(ZeroAir,"ISOTROPIC");
MEDIUMPAR(ZeroAir,1,1,0,0,1,1,0,0,1,1,0,0,0);
MEDIUMCOL(ZeroAir,0,255,255,0,1,0,255,255,21,53,62,99);
ELEMENT(z+(24),8,0,ZeroAir,e_33,IN);
NEWLINE(x+(256),y+(496),x+(256),y+(488));
ADDLINE(x+(264),y+(488));
ADDLINE(x+(264),y+(496));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,Fat,e_34,IN);
NEWLINE(x+(264),y+(496),x+(264),y+(488));
ADDLINE(x+(296),y+(488));
ADDLINE(x+(296),y+(496));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,ZeroAir,e_35,IN);
NEWLINE(x+(248),y+(480),x+(248),y+(472));
ADDLINE(x+(256),y+(472));
ADDLINE(x+(256),y+(480));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,Fat,e_36,IN);
NEWLINE(x+(256),y+(480),x+(256),y+(472));
ADDLINE(x+(288),y+(472));
ADDLINE(x+(288),y+(480));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,Fat,e_37,IN);
NEWLINE(x+(248),y+(192),x+(248),y+(184));
ADDLINE(x+(232),y+(184));
ADDLINE(x+(232),y+(176));
ADDLINE(x+(216),y+(176));
ADDLINE(x+(216),y+(168));
ADDLINE(x+(208),y+(168));
ADDLINE(x+(208),y+(160));
ADDLINE(x+(200),y+(160));
ADDLINE(x+(200),y+(136));
ADDLINE(x+(232),y+(136));
ADDLINE(x+(232),y+(144));
ADDLINE(x+(240),y+(144));
ADDLINE(x+(240),y+(152));
ADDLINE(x+(256),y+(152));
ADDLINE(x+(256),y+(160));
ADDLINE(x+(264),y+(160));
ADDLINE(x+(264),y+(184));
ADDLINE(x+(256),y+(184));
ADDLINE(x+(256),y+(192));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,ZeroAir,e_38,IN);
NEWLINE(x+(264),y+(168),x+(264),y+(160));
ADDLINE(x+(272),y+(160));
ADDLINE(x+(272),y+(168));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,Fat,e_39,IN);
NEWLINE(x+(272),y+(168),x+(272),y+(160));
ADDLINE(x+(288),y+(160));
ADDLINE(x+(288),y+(168));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,ZeroAir,e_40,IN);
NEWLINE(x+(256),y+(160),x+(256),y+(152));
ADDLINE(x+(264),y+(152));
ADDLINE(x+(264),y+(160));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,SkinDry,e_41,IN);
NEWLINE(x+(264),y+(160),x+(264),y+(152));
ADDLINE(x+(272),y+(152));
ADDLINE(x+(272),y+(144));
ADDLINE(x+(280),y+(144));
ADDLINE(x+(280),y+(152));
ADDLINE(x+(288),y+(152));
ADDLINE(x+(288),y+(160));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,ZeroAir,e_42,IN);
NEWLINE(x+(240),y+(152),x+(240),y+(144));
ADDLINE(x+(248),y+(144));
ADDLINE(x+(248),y+(152));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,SkinDry,e_43,IN);
NEWLINE(x+(248),y+(152),x+(248),y+(144));
ADDLINE(x+(256),y+(144));
ADDLINE(x+(256),y+(136));
ADDLINE(x+(264),y+(136));
ADDLINE(x+(264),y+(152));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,Fat,e_44,IN);
NEWLINE(x+(264),y+(152),x+(264),y+(144));
ADDLINE(x+(272),y+(144));
ADDLINE(x+(272),y+(152));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,SkinDry,e_45,IN);
NEWLINE(x+(232),y+(144),x+(232),y+(136));
ADDLINE(x+(240),y+(136));
ADDLINE(x+(240),y+(144));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,Fat,e_46,IN);
NEWLINE(x+(240),y+(144),x+(240),y+(136));
ADDLINE(x+(256),y+(136));
ADDLINE(x+(256),y+(144));
CLOSELINE;
ENDELEM;
ELEMENT(z+(24),8,0,SkinDry,e_47,IN);
NEWLINE(x+(248),y+(136),x+(248),y+(128));
ADDLINE(x+(256),y+(128));
ADDLINE(x+(256),y+(136));
CLOSELINE;
ENDELEM;
ELEMENT(z+(32),8,0,Fat,e_48,IN);
NEWLINE(x+(168),y+(552),x+(168),y+(544));
ADDLINE(x+(160),y+(544));
ADDLINE(x+(160),y+(528));
ADDLINE(x+(168),y+(528));
ADDLINE(x+(168),y+(520));
ADDLINE(x+(176),y+(520));
ADDLINE(x+(176),y+(512));
ADDLINE(x+(184),y+(512));
ADDLINE(x+(184),y+(504));
ADDLINE(x+(192),y+(504));
ADDLINE(x+(192),y+(496));
ADDLINE(x+(200),y+(496));
ADDLINE(x+(200),y+(488));
ADDLINE(x+(208),y+(488));
ADDLINE(x+(208),y+(480));
ADDLINE(x+(216),y+(480));
ADDLINE(x+(216),y+(472));
ADDLINE(x+(224),y+(472));
ADDLINE(x+(224),y+(464));
ADDLINE(x+(256),y+(464));
ADDLINE(x+(256),y+(472));
ADDLINE(x+(280),y+(472));
ADDLINE(x+(280),y+(480));
ADDLINE(x+(264),y+(480));
ADDLINE(x+(264),y+(488));
ADDLINE(x+(232),y+(488));
ADDLINE(x+(232),y+(496));
ADDLINE(x+(216),y+(496));
ADDLINE(x+(216),y+(504));
ADDLINE(x+(208),y+(504));
ADDLINE(x+(208),y+(512));
ADDLINE(x+(192),y+(512));
ADDLINE(x+(192),y+(528));
ADDLINE(x+(176),y+(528));
ADDLINE(x+(176),y+(552));
CLOSELINE;
ENDELEM;
ELEMENT(z+(32),8,0,Muscle,e_49,IN);
NEWLINE(x+(176),y+(552),x+(176),y+(528));
ADDLINE(x+(192),y+(528));
ADDLINE(x+(192),y+(512));
ADDLINE(x+(208),y+(512));
ADDLINE(x+(208),y+(504));
ADDLINE(x+(216),y+(504));
ADDLINE(x+(216),y+(496));
ADDLINE(x+(224),y+(496));
ADDLINE(x+(224),y+(528));
ADDLINE(x+(216),y+(528));
ADDLINE(x+(216),y+(536));
ADDLINE(x+(200),y+(536));
ADDLINE(x+(200),y+(544));
ADDLINE(x+(192),y+(544));
ADDLINE(x+(192),y+(552));
CLOSELINE;
ENDELEM;
ELEMENT(z+(32),8,0,Fat,e_50,IN);
NEWLINE(x+(192),y+(552),x+(192),y+(544));
ADDLINE(x+(208),y+(544));
ADDLINE(x+(208),y+(552));
CLOSELINE;
ENDELEM;
CLOSEOBJ;