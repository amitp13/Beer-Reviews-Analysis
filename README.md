# Beer-Reviews-Analysis

Beer has been around which has been around ancient Egypt is the oldest reciepie in the world. Beer eventually made its way from the Middle East across the Mediterranean to Europe, where it became an integral part of life. In the Middle Ages German monks began commonly using wild hops in beer and introduced to the world more mordern beers. Beer arrived in the New World with the first European colonists in the 1800's. As of 2007, the brewing industry is a global business, consisting of several dominant multinational companies and many thousands of smaller producers ranging from brewpubs to regional breweries.As of 2006, more than 133 billion litres (35 billion US gallons), the equivalent of a cube 510 metres on a side, of beer are sold per year, producing total global revenues of US$294.5 billion. 

Since beer is such an integral part of our world and one of my favorite things heres a quick analysis on reviews on different types of breweries. With the data we have we can probably find the best beer and best brewery among the bunch. Another interesting insight I hope to find is if there is a correlation between the overall rating of the product and its various properties like aroma, abv, taste, appearance and so on. If a strong correlation does exist we can probably build a predictive model around it.  

# About The Dataset

This dataset consists of beer reviews from Beeradvocate. The data span a period of more than 10 years, including all ~1.5 million reviews up to November 2011. Each review includes ratings in terms of five "aspects": appearance, aroma, palate, taste, and overall impression. Reviews include product and user information, followed by each of these five ratings, and a plaintext review. We also have reviews from ratebeer. The Dataset can be found on this link https://www.kaggle.com/rdoume/beerreviews.

# Dataset Format
The dataset was downloaded in a CSV format but transformed in SQLite Database for ease of use. It was transformed into 3 tables by using simple queries. 

1. Beer Reviews : This table is the raw csv file without any changes in a table format.
2. Beer Master : This contains the average of all the rating combined for each beer along with the brewery information where the beer was produced
3. Brewery : The Brewery table consists of information on all the breweries in the database.
