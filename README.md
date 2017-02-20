## Demographic-Analysis-of-Moviegoers-in-the-Twitter-Sphere


This folder contains all codes for our final project “Audience Analysis based on Twitter and IMDb”
There are there python files and one r code in this folder:

1. <b>Get-follower-ids.py<b>

This file is for getting the first 1000 followers’ id by inputting the screen names of movies’ Twitter account. It returns a JSON file.
2. Get-follower-profiles.py
This file is to get accounts’ image urls and their self-descriptions. The input is account’s id and it returns a JSON file.
3. face_detect.py
This file is linking to Face++ detection API and it detects face from images. The input is a file of lists of image urls and it returns age, gender and race information of the face detected.
4. Text-analysis-word-cloud.R
This is a r code which analyze the frequency of words showing in followers’ self-descriptions.
