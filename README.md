# WINE RECOMMANDER PROJECT

---

![](https://images.unsplash.com/photo-1519671482749-fd09be7ccebf?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80)

Photo by [Kelsey Chance](https://unsplash.com/@kchance8)

# Context

This project is related to a kaggle's project : [Wine Reviews](https://www.kaggle.com/zynicide/wine-reviews).

The objective here is to create a **wine recommandation model** based on the oenological description of a wine by a sommelier. This algorithm should be able to bring together wines that are similar on the aromatic level.

# Content

The data was scraped from the famous wine magazine [WineEnthusiast](https://www.winemag.com/?s=&drink_type=wine) during the week of June 15th, 2017 for year 2014 and 2015. 

The dataset contains **130k wine reviews** with variety, location, winery, price, points and description.
For the sake of computing power, the model is focused on french wines, but it is scallable and reproductible.

**Columns's labels**:

- Country
- Description
- Designation
- Points
- Price
- Province
- Region_1
- Region_2
- Taster_name
- Taster_twitter_handle
- Title	
- Variety
- Winery


# Sections 

1.**Data preparation and EDA**
2.**Preprocessing** (Spacy)
3.**Modeling** (TFIDF, Cosine Similarity)
4.**Model Prediction**
5.**Deployment** (Flask & Heroku) [link](https://samewineeverywhere.herokuapp.com/wine_app)
