in pytube in path C:\Users\HP\PycharmProjects\projectShalakaGif\venv\Lib\site-packages\pytube\cipher.py in line 411 from this "find_object_from_startpoint(raw_code, match.span()[1] - 1)" 
to this "js"


DOWNLODEYT.PY
downlodeyt.py downloads the yt video using pytube and it takes two parameters that is link and 
folder path for saving the video in the path given for more detail read the comments in the code 
and it returns the video path(s)

LINKFEEDER.PY
linkfeeder returns link(s) one by one and takes one paremeter that is filename in which the 
links are saved
!!!!!!note:- the txt file of links should be in this format:-!!!!!!!
link1
link2
link3
.
.
.
linkn
!!!!!no punctuation between two links!!!!!


MAIN.PY
in main.py call all the files to download youtube from the links.txt

INDEX.PY
index.py is the sample front end for now it makes links.txt in the folder input in the format as 
given above

WORK TO DO
1.to join main.py with index.py  
[link the file(./input/links.txt) to back end (main.py)]
2.to create different folder for input and output (it is made but plz look in to it, it is 
giving some error)
3.if u can make some improvements(plzzz)



if u download the pytube lib with the pip requirements.txt don't run the full code there is 
test.py in this folder run that first if it gives some error like "AttributeError: 'NoneType' object has no attribute 'span'" then do this 
in pytube in path C:\PycharmProjects\projectShalakaGif\venv\Lib\site-packages\pytube\cipher.py in line 411 from this [ transform_plan_raw = find_object_from_startpoint(raw_code, match.span()[1] - 1) ]
to this ( transform_plan_raw = js )
