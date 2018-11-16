

# Project Name
### Yelp_Django_App

## Purpose

For this project, I aim to use the Yelp dataset found at https://www.kaggle.com/yelpdataset/yelpdataset. The goal of the project will be to create a Django app based off the data that will show businesses and their offerings, reviewers, and places people are checking in at, just to name a few. I’m primarily interested in using this dataset since it would be like a smaller scale Yelp application that I created with some of their data. I want to set out to see if I can create something that shows exactly what I want based off a company’s existing data and see if there are other views that could be utilized but are not from them. I have worked with this dataset in the past to do analytics, but I have never made a Django app or used all 5 JSON files before.

Overall, I feel like this project will be great help build my front-end experience up in my portfolio. Most of the work I have been doing has been backend and machine learning. As I work on this project, I will most likely be building other views as I see fit and adjusting proposed ones.
## Data set

The data set is comprised of 5 different JSON files. Specifically, there is a file for businesses, users, the review, check-ins, and tips. The many-to-many relationship would be a temp table linking the business with the reviewer since many businesses can have many different reviewers. Tables will be comprised of user data, check-ins to businesses, business data, attribute data linking back to the business, review data, tmp table to link reviewers to businesses, to name a few. These might change once I get into the data closer, but I feel as though this should require 7-8 tables all in all to contain each data element required. Also, I want to add some filtering component in the front end so that a user can say “Show me businesses with Bike Parking.” or,” Show me restaurants that have a bar”. This data has a lot of filtering potential and hooking that up into a Django app will be a great challenge as it would need to dynamically filter based off the button or selection input into the front-end view.

## Data model

As of right now, the views I can think of would be businesses, business details, business attributes (filtered on location), businesses reviews, business tips, user profile, user reviewers, and possibly a map. I want to somehow leverage the geo-coordinates in the data to somehow pull a locations pin of what places would be around, but that piece could be out of scope. Mainly, I want to be able to see if I can create a “Yelp like” version using my knowledge of Django that I can bring to a company in an interview. App development is a place I see myself going after graduation and like the challenge of trying to create something for an app company that could show my front-end and backend skills.

![yelp_data_model](https://user-images.githubusercontent.com/20977403/48651266-16336c80-e9c8-11e8-98ca-24848d971b5b.png)

## Package Dependencies

To be added soon.