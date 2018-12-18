

# Project Name
### Yelp_Django_App

## Purpose

For this project, I aim to use the Yelp dataset found at https://www.kaggle.com/yelp-dataset/yelp-dataset/version/6. The goal of the project was to  create a Django app based off the data that will show businesses, users, and reviews. I’m primarily interested in using this dataset since it would be like a smaller scale Yelp application that I created with some of their data. I want to set out to see if I can create something that shows exactly what I want based off a company’s existing data and see if there are other views that could be utilized but are not from them. I have worked with this dataset in the past to do analytics, but I have never made a Django app or used all 5 JSON files before.

Overall, I feel like this project will be great help build my front-end experience up in my portfolio. Most of the work I have been doing has been backend and machine learning. As I work on this project, I will most likely be building other views as I see fit and adjusting proposed ones.
## Data set

The data set is comprised of 5 different JSON files. Specifically, there is a file for businesses, users, the review, check-ins, and tips. I ended up just using the json files for specific unique attributes and creating a full_business dataset. In order to fill the main database tables (business, user, and review) I used a mix of csv's found above and json talked about prior. The many-to-many relationship is a reviews table linking the business with the users since many businesses can have many different reviewers. Tables are comprised of user data, business data, business attribute data linking back to the business, and review data. All in all there are 7 tables in this database as shown below. The user's are the primary entity with businesses being the secondary.

## Data model

The Django app is comprised of 3 main views all with detail views. The views are Users, Businesses, and Reviews all with details about each when clicked on. Since the User's are the primary entity, a web form was created to add/edit/delete user's into the backend database. When creating a user, you can link them abck to a business to show they have "reviewed" this entity. Via the API, a user will be able to GET/POST/PUT businesses into the backend. In order for this, the user needs to have an access key of which they can register themselves through the Django App.


![yelp_data_model](https://user-images.githubusercontent.com/20977403/48651266-16336c80-e9c8-11e8-98ca-24848d971b5b.png)

## Package Dependencies

All package dependencies can be installed via the requirements.txt file found in the repo. Run `python install -r requirements.txt` within a virtual enviornment.