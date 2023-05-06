# AlbumOfTheYearWrapper

A light weight python library that acts as an API for https://www.albumoftheyear.org/
<br>
![Tests](https://github.com/JahsiasWhite/AlbumOfTheYearAPI/workflows/Tests/badge.svg?branch=master)
<img alt="PyPI" src="https://img.shields.io/pypi/v/album-of-the-year-api">

## Description

Gets data from https://www.albumoftheyear.org/. The website doesn't currently provide API support so web parsing is required to obtain data. Because of this,
and according to https://www.albumoftheyear.org/robots.txt, searching and POST requests are not allowed. 

## Installation

```
pip install album-of-the-year-api
```
or upgrade
```
pip install album-of-the-year-api --upgrade
```

## Usage

**Examples**

Here's a quick example of getting a specific users follower count
```
from albumoftheyearapi import AOTY

client = AOTY()
print(client.user_follower_count('jahsias'))

>> 0
```

If you don't need the full functionality, you can also import only the neccesary files
```
from albumoftheyearapi.artist import ArtistMethods

client = ArtistMethods()
print(client.artist_albums('183-kanye-west'))

>> ['Donda 2', 'Donda', 'JESUS IS KING', 'ye', 'The Life of Pablo', 'Yeezus', 'Watch the Throne', 'My Beautiful Dark Twisted Fantasy', '808s & Heartbreak', 'Graduation', 'Late Registration', 'The College Dropout']
```
Notice artists also need their unique id along with their name

Each function also is able to return the data in JSON format
```
from albumoftheyearapi import AOTY

client = AOTY()
print(client.artist_critic_score_json('183-kanye-west'))

>> {"critic_score": "73"}
```

## Methods

**Artist Methods**

```artist_albums(artist)```
<br>Returns a list of all albums by an artist
<br>    Parameters:  
* artist - artist id and name

```artist_mixtapes(artist)```
<br>Returns a list of all mixtapes by an artist
<br>Parameters:  
* artist - artist id and name

```artist_eps(artist)```
<br>Returns a list of all eps by an artist
<br>Parameters:  
* artist - artist id and name

```artist_singles(artist)```
<br>Returns a list of all singles by an artist
<br>Parameters:  
* artist - artist id and name

```artist_name(artist)```
<br>Returns the name of the artist
<br>Parameters:  
* artist - artist id and name

```artist_critic_score(artist)```
<br>Returns the critic score of the artist
<br>Parameters:  
* artist - artist id and name

```artist_user_score(artist)```
<br>Returns the user score of the artist
<br>Parameters:  
* artist - artist id and name

```artist_total_score(artist)```
<br>Returns the average of the critic and users score of the artist
<br>Parameters:  
* artist - artist id and name

```artist_follower_count(artist)```
<br>Returns the follower count of the artist
<br>Parameters:  
* artist - artist id and name

```artist_details(artist)```
<br>Returns the detials of the artist
<br>Parameters:  
* artist - artist id and name

```artist_top_songs(artist)```
<br>Returns a list of the top songs of the artist
<br>Parameters:  
* artist - artist id and name

```similar_artists(artist)```
<br>Returns a list of similar artists to the given artist
<br>Parameters:  
* artist - artist id and name

**User Methods**

```user_rating_count(user)```
<br>Returns the number of ratings by a user
<br>Parameters:  
* user - username

```user_review_count(user)```
<br>Returns the number of reviews by a user
<br>Parameters:  
* user - username

```user_list_count(user)```
<br>Returns the number of lists by a user
<br>Parameters:  
* user - username

```user_follower_count(user)```
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

```user_ratings(user)```
<br>Returns a list of the users ratings
<br>Parameters:  
* user - username

```user_perfect_scores(user)```
<br>Returns a list of the users perfect scores
<br>Parameters:  
* user - username

```user_liked_music(user)```
<br>Returns a list of the users liked music
<br>Parameters:  
* user - username
