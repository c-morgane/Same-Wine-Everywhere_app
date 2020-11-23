{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# WINE RECOMMANDER PROJECT\n",
    "\n",
    "# Context\n",
    "\n",
    "This project is related to a kaggle's project : [Wine Reviews](https://www.kaggle.com/zynicide/wine-reviews).\n",
    "\n",
    "The objective here is to create a **wine recommandation model** based on the oenological description of a wine by a sommelier. This algorithm should be able to bring together wines that are similar on the aromatic level.\n",
    "\n",
    "# Content\n",
    "\n",
    "The data was scraped from the famous wine magazine [WineEnthusiast](https://www.winemag.com/?s=&drink_type=wine) during the week of June 15th, 2017 for year 2014 and 2015. \n",
    "\n",
    "The dataset contains **130k wine reviews** with variety, location, winery, price, points and description.\n",
    "For the sake of computing power, the model is focused on french wines, but it is scallable and reproductible.\n",
    "\n",
    "# Sections \n",
    "\n",
    "1. **Data preparation and EDA**\n",
    "2. **Preprocessing** (Spacy)\n",
    "3. **Modeling** (TFIDF, Cosine Similarity)\n",
    "4. **Model Prediction**\n",
    "5. **Deployment** (Flask & Heroku) [link](https://samewineeverywhere.herokuapp.com/wine_app)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
