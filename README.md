# AlbumOfTheYearWrapper

A light weight python library that acts as an API for https://www.albumoftheyear.org/

## Description

Gets data from https://www.albumoftheyear.org/. The website doesn't currently provide API support so web parsing is required to obtain data. Because of this,
according to https://www.albumoftheyear.org/robots.txt, searching and POST requests are not allowed. 

## Installation

## Usage
```pip install album-of-the-year-api
```
or upgrade
```pip install album-of-the-year-api --upgrade
```

**Examples**

Here's a quick example of getting a specific users follower count
```from albumoftheyearapi import AOTY

client = AOTY()
print_num_of_followers('doublez')

def print_num_of_followers(user):
    print(client.user_followers(user))
```

If you don't need the full functionality, you can also import only the neccesary files
```from albumoftheyearapi.artist import ArtistMethods

client = ArtistMethods
print_all_artist_albums('183-kanye-west')

def print_all_artist_albums(artist):
    print(client.artist_albums(artist))
```
Notice artists also need their unique id along with their name

**Artist Methods**

```artist_albums(artist)```
<br>Returns all albums by an artist
<br>    Parameters:  
* artist - artist id and name


```artist_mixtapes(artist)```
<br>Returns all mixtapes by an artist
<br>Parameters:  
* artist - artist id and name

```artist_eps(artist)```
<br>Returns all eps by an artist
<br>Parameters:  
* artist - artist id and name

**User Methods**

```user_ratings(user)```
<br>Returns the number of ratings by a user
<br>Parameters:  
* user - username

```user_reviews(user)```
<br>Returns the number of reviews by a user
<br>Parameters:  
* user - username

```user_lists(user)```
<br>Returns the number of lists by a user
<br>Parameters:  
* user - username

```user_followers(user)```
<br>Returns the number of followers a user has
<br>Parameters:  
* user - username

```user_about(user)```
<br>Returns the about page of a user
<br>Parameters:  
* user - username

```user_rating_distribution(user)```
<br>Returns a list of a users rating distribution
<br>Parameters:  
* user - username