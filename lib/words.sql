BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "words" (
	"alphabet"	TEXT,
	"word_name"	TEXT,
	"level"	INTEGER,
	"char_count"	INTEGER,
	"image_loc"	TEXT,
	"audio_loc"	TEXT,
	"alphabet_order"	INTEGER
);
INSERT INTO "words" VALUES ('A','Ant',1,3,'images/A/ant.png','audio/A/ant.mp3',0);
INSERT INTO "words" VALUES ('A','Apple',2,5,'images/A/apple.png','audio/A/apple.mp3',0);
INSERT INTO "words" VALUES ('A','Aeroplane',3,9,'images/A/aeroplane.png','audio/A/aeroplane.mp3',0);

INSERT INTO "words" VALUES ('B','Bag',1,3,'images/B/bag.png','audio/B/bag.mp3',1);
INSERT INTO "words" VALUES ('B','Ball',2,4,'images/B/ball.png','audio/B/ball.mp3',1);
INSERT INTO "words" VALUES ('B','Birds',3,5,'images/B/birds.png','audio/B/birds.mp3',1);


INSERT INTO "words" VALUES ('C','Cat',1,3,'images/C/bag.png','audio/C/bag.mp3',2);
INSERT INTO "words" VALUES ('C','Ball',2,4,'images/C/ball.png','audio/C/ball.mp3',2);
INSERT INTO "words" VALUES ('C','Birds',3,5,'images/C/birds.png','audio/C/birds.mp3',2);


INSERT INTO "words" VALUES ('D','Dog',1,3,'images/D/dog.png','audio/D/dog.mp3',3);
INSERT INTO "words" VALUES ('D','Dress',2,5,'images/D/dress.png','audio/D/dress.mp3',3);
INSERT INTO "words" VALUES ('D','Doctor',3,6,'images/D/doctor.png','audio/D/doctor.mp3',3);


INSERT INTO "words" VALUES ('E','Eyes',1,4,'images/E/eyes.png','audio/E/eyes.mp3',4);
INSERT INTO "words" VALUES ('E','Earth',2,5,'images/E/earth.png','audio/E/earth.mp3',4);
INSERT INTO "words" VALUES ('E','Engine',3,5,'images/E/engine.png','audio/E/engine.mp3',4);


INSERT INTO "words" VALUES ('F','Fan',1,3,'images/F/fan.png','audio/F/fan.mp3',5);
INSERT INTO "words" VALUES ('F','Fish',2,4,'images/F/fish.png','audio/F/fish.mp3',5);
INSERT INTO "words" VALUES ('F','Flowers',3,7,'images/F/flowers.png','audio/F/flowers.mp3',5);


INSERT INTO "words" VALUES ('G','Gift',1,4,'images/G/gift.png','audio/G/gift.mp3',6);
INSERT INTO "words" VALUES ('G','Grass',2,5,'images/G/grass.png','audio/G/grass.mp3',6);
INSERT INTO "words" VALUES ('G','Garden',3,6,'images/G/garden.png','audio/G/garden.mp3',6);


INSERT INTO "words" VALUES ('H','Home',1,4,'images/H/home.png','audio/H/home.mp3',7);
INSERT INTO "words" VALUES ('H','Horse',2,5,'images/H/horse.png','audio/H/horse.mp3',7);
INSERT INTO "words" VALUES ('H','Hammer',3,6,'images/H/hammer.png','audio/H/hammer.mp3',7);


INSERT INTO "words" VALUES ('I','Ink',1,3,'images/I/ink.png','audio/I/ink.mp3',8);
INSERT INTO "words" VALUES ('I','Island',2,6,'images/I/island.png','audio/I/island.mp3',8);
INSERT INTO "words" VALUES ('I','Icecream',3,8,'images/I/icecream.png','audio/I/icecream.mp3',8);


INSERT INTO "words" VALUES ('J','Jar',1,3,'images/J/jar.png','audio/J/jar.mp3',9);
INSERT INTO "words" VALUES ('J','Jeep',2,4,'images/J/jeep.png','audio/J/jeep.mp3',9);
INSERT INTO "words" VALUES ('J','Jacket',3,5,'images/J/jacket.png','audio/J/jacket.mp3',9);


INSERT INTO "words" VALUES ('K','Key',1,3,'images/K/key.png','audio/K/key.mp3',10);
INSERT INTO "words" VALUES ('K','Kite',2,4,'images/K/kite.png','audio/K/kite.mp3',10);
INSERT INTO "words" VALUES ('K','Keyboard',3,8,'images/K/keyboard.png','audio/K/keyboard.mp3',10);


INSERT INTO "words" VALUES ('L','Leaf',1,4,'images/L/leaf.png','audio/L/leaf.mp3',11);
INSERT INTO "words" VALUES ('L','Light',2,5,'images/L/light.png','audio/L/light.mp3',11);
INSERT INTO "words" VALUES ('L','Letter',3,6,'images/L/letter.png','audio/L/letter.mp3',11);


INSERT INTO "words" VALUES ('M','Milk',1,4,'images/M/milk.png','audio/M/milk.mp3',12);
INSERT INTO "words" VALUES ('M','Monkey',2,6,'images/M/monkey.png','audio/M/milk.mp3',12);
INSERT INTO "words" VALUES ('M','Mother',3,6,'images/M/mother.png','audio/M/milk.mp3',12);

COMMIT;
