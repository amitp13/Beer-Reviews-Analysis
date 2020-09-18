PRAGMA foreign_keys = OFF;

ALTER TABLE beer_master RENAME TO beer_master_old; 

CREATE TABLE "beer_master" 
(   "beer_beerid"	INT NOT NULL PRIMARY KEY,
	"beer_name"	VARCHAR,
	"brewery_id"	INT,
	"brewery_name"	VARCHAR,
	"beer_style"	VARCHAR,
	"beer_abv"	INTEGER,
	"avg_review_appearance"	INTEGER,
	"avg_review_aroma"	INTEGER,
	"avg_review_palate"	INTEGER,
	"avg_review_taste"	INTEGER,
	"avg_review_overall"	INTEGER,
	CONSTRAINT fk_brewery
		FOREIGN KEY (brewery_id)
		REFERENCES brewery(brewery_id)
		);

INSERT INTO beer_master SELECT * FROM beer_master_old;

PRAGMA foreign_keys = ON;