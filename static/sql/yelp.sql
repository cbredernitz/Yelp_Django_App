-- Combine UN Statistics Division (UNSD) standard region, sub-regions, intermediate
-- regions and countries or areas codes (M49) with UNESCO World Heritage List.
-- Source: https://unstats.un.org/unsd/methodology/m49/overview/
-- Source: https://whc.unesco.org/en/list/

--
-- Create database
--

-- CREATE DATABASE IF NOT EXISTS unesco_heritage_sites;
-- USE unesco_heritage_sites;

--
-- Drop tables
-- turn off FK checks temporarily to eliminate drop order issues
--

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS noise_level, attire, city, state, user, review, business, tmp_business, tmp_review;
SET FOREIGN_KEY_CHECKS=1;



--
-- Noise Level
--

CREATE TABLE IF NOT EXISTS noise_level
  (
    noise_level_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    noise VARCHAR(45) NOT NULL UNIQUE,
    PRIMARY KEY (noise_level_id)
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

INSERT IGNORE INTO noise_level (noise) VALUES
  ('Average'), ('Loud'), ('Quiet'), ('Very Loud');



-- --
-- -- Attire
-- --

CREATE TABLE IF NOT EXISTS attire
  (
    attire_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    attire VARCHAR(45) NOT NULL UNIQUE,
    PRIMARY KEY (attire_id)
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

INSERT IGNORE INTO attire (attire) VALUES
  ('Casual'),
  ('Dressy'),
  ('Formal');



--
-- Business Temporary
--

CREATE TABLE IF NOT EXISTS tmp_business
  (
    business_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    business_name VARCHAR(100) NOT NULL,
    yelp_business_id VARCHAR(45),
    address VARCHAR(100),
    city_name VARCHAR(45),
    state_name VARCHAR(45),
    neighborhood VARCHAR(100),
    postal_code VARCHAR(15),
    latitude DECIMAL(10,2),
    longitude DECIMAL(10,2),
    business_stars DECIMAL(10,2),
    business_review_count INTEGER,
    is_open TINYINT,
    attire_name VARCHAR(45),
    noise_name VARCHAR(45),
    categories VARCHAR(45),
    PRIMARY KEY (business_id)
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

-- LOAD DATA LOCAL INFILE './input/csv/yelp_full_businesses.csv'
LOAD DATA LOCAL INFILE './input/csv/SMALL_yelp_full_businesses.csv'
INTO TABLE tmp_business
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ','
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES
  (yelp_business_id, business_name, neighborhood, address, city_name, state_name, postal_code, latitude, longitude, business_stars, business_review_count, is_open, categories, attire_name, noise_name);

-- --
-- -- State
-- --



CREATE TABLE IF NOT EXISTS state
  (
    state_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    state_abbrev VARCHAR(45) NOT NULL UNIQUE,
    PRIMARY KEY (state_id)
   )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE './output/states.csv'
INTO TABLE state
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY '\t'
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES
  (state_abbrev);



--
-- City
--
 
CREATE TABLE IF NOT EXISTS city
  (
    city_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    city_name VARCHAR(45) NOT NULL UNIQUE,
    PRIMARY KEY (city_id)
   )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE './output/cities.csv'
INTO TABLE city
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY '\t'
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES
  (city_name);



--
-- Businesses
--

CREATE TABLE IF NOT EXISTS business
  (
    business_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    business_name VARCHAR(100) NOT NULL,
    yelp_business_id VARCHAR(45),
    address VARCHAR(100),
    neighborhood VARCHAR(100),
    city_id INTEGER,
    state_id INTEGER,
    attire_id INTEGER,
    noise_level_id INTEGER,
    postal_code VARCHAR(15),
    latitude DECIMAL(10,2),
    longitude DECIMAL(10,2),
    business_stars DECIMAL(10,2),
    business_review_count INTEGER,
    is_open TINYINT,
    PRIMARY KEY (business_id),
    FOREIGN KEY (city_id) REFERENCES city(city_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (state_id) REFERENCES state(state_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (noise_level_id) REFERENCES noise_level(noise_level_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (attire_id) REFERENCES attire(attire_id)
    ON DELETE CASCADE ON UPDATE CASCADE
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

INSERT IGNORE INTO business (
    business_name,
    yelp_business_id,
    address,
    neighborhood,
    city_id,
    state_id,
    attire_id,
    noise_level_id,
    postal_code,
    latitude,
    longitude,
    business_stars,
    business_review_count,
    is_open
)
SELECT bs.business_name, bs.yelp_business_id, bs.address, bs.neighborhood, cit.city_id, st.state_id, atr.attire_id,
       noi.noise_level_id, bs.postal_code, bs.latitude, bs.longitude, bs.business_stars, bs.business_review_count, bs.is_open
  FROM tmp_business bs
       LEFT JOIN city cit
              ON TRIM(bs.city_name) = TRIM(cit.city_name)
       LEFT JOIN state st
              ON TRIM(bs.state_name) = TRIM(st.state_abbrev)
       LEFT JOIN attire atr
              ON TRIM(bs.attire_name) = TRIM(atr.attire)
       LEFT JOIN noise_level noi
              ON TRIM(bs.noise_name) = TRIM(noi.noise)
ORDER BY bs.business_name;



--
-- Users
--

CREATE TABLE IF NOT EXISTS user
  (
    user_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    user_name VARCHAR(45) NOT NULL,
    review_count INT NOT NULL,
    yelper_since DATE,
    useful INTEGER,
    cool INTEGER,
    funny INTEGER,
    average_stars DECIMAL(10,2),
    yelp_user_id VARCHAR(45),
    PRIMARY KEY (user_id)
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

-- LOAD DATA LOCAL INFILE './input/csv/yelp_user.csv'
LOAD DATA LOCAL INFILE './input/csv/SMALL_yelp_user.csv'
INTO TABLE user
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ','
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES
  (yelp_user_id, user_name, review_count, yelper_since, @dummy, useful, funny, cool, @dummy, @dummy, average_stars, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy);



-- --
-- -- Temporary Review
-- --

CREATE TABLE IF NOT EXISTS tmp_review
  (
    review_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    yelp_review_id VARCHAR(45),
    yelp_user_id VARCHAR(45),
    yelp_business_id VARCHAR(45),
    stars DECIMAL(10,2),
    date_created DATE,
    review_text TEXT,
    PRIMARY KEY (review_id)
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

-- LOAD DATA LOCAL INFILE './input/csv/yelp_review.csv'
LOAD DATA LOCAL INFILE './input/csv/SMALL_yelp_review.csv'
INTO TABLE tmp_review
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ','
  ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES
  (yelp_review_id, yelp_user_id, yelp_business_id, stars, date_created, review_text, @dummy, @dummy, @dummy);



--
-- Review (Many-To-Many)
--

CREATE TABLE IF NOT EXISTS review
  (
    review_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    business_id INTEGER,
    user_id INTEGER,
    stars DECIMAL(10,2),
    date_created DATE,
    review_text TEXT,
    PRIMARY KEY (review_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (business_id) REFERENCES business(business_id)
    ON DELETE CASCADE ON UPDATE CASCADE
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;

INSERT IGNORE INTO review (
    business_id,
    user_id,
    stars,
    date_created,
    review_text
)
SELECT  bs.business_id, usr.user_id, trv.stars, trv.date_created, trv.review_text
  FROM tmp_review trv
       INNER JOIN business bs
              ON TRIM(trv.yelp_business_id) = TRIM(bs.yelp_business_id)
       INNER JOIN user usr
              ON TRIM(trv.yelp_user_id) = TRIM(usr.yelp_user_id)
  ORDER BY trv.stars, trv.date_created, trv.review_text;

DROP TABLE tmp_review;
DROP TABLE tmp_business;