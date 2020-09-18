CREATE TABLE beer_master AS 
SELECT beer_beerid, beer_name, brewery_id, brewery_name, beer_style, beer_abv, ROUND(AVG(review_appearance),2) AS avg_review_appearance, 
ROUND(AVG(review_aroma),2) AS avg_review_aroma, ROUND(AVG(review_palate),2) AS avg_review_palate, 
ROUND(AVG(review_taste),2) AS avg_review_taste, ROUND(AVG(review_overall),2) AS avg_review_overall 
FROM beer_reviews 
GROUP BY beer_beerid

CREATE TABLE brewery AS
SELECT brewery_id, brewery_name, count(DISTINCT beer_beerid) AS no_of_beers, count(DISTINCT beer_style) AS no_of_beerstyles 
FROM beer_reviews 
GROUP BY brewery_id

