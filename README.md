## Demographic-Analysis-of-Moviegoers-in-the-Twitter-Sphere

### Project Abstract
Understanding movie audience is important for movie production and marketing campaigns. Big data from open sources provides us with a massive amount of data about moviegoers and facilitates new approaches to deciphering the data. In this work, we analyze the audience of five primary genres, namely action, animation, comedy, drama and science fiction movies, based on the followers information of the official movie accounts from Twitter. By using a face detection software tool Face++ to analyze the Twitter profile images, we extract rich demographic information about movie followers in terms of age, gender and race. The results of text analysis on profile self-descriptions further reveal their identities and passions.

### Codes
Here are all codes for our project.
There are there python files and one r code in this folder:

- Get-follower-ids.py:
This file is for getting the first 1000 followers’ id by inputting the screen names of movies’ Twitter account. It returns a JSON file.
- Get-follower-profiles.py:
This file is to get accounts’ image urls and their self-descriptions. The input is account’s id and it returns a JSON file.
- face_detect.py
This file is linking to Face++ detection API and it detects face from images. The input is a file of lists of image urls and it returns age, gender and race information of the face detected.
- Text-analysis-word-cloud.R
This is a r code which analyze the frequency of words showing in followers’ self-descriptions.
