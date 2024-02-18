from jes4py import *


def mirror(pic):



def makeHomePage (name1, name2, interest, pic1, pic2):
  file=open("homepage.html","wt")
  file.write("""<!DOCTYPE html>
<html>
<head>
<title>""" + name1 + """'s Home Page</title>
</head>
<body>
<img src= '""" + pic1 + """' alt="Nawaf" width="200" height="200">
<h1>Welcome to """ + name1 + """'s Home Page</h1>
<p>Hi!  I am <b>""" + name1 + """</b>.  This is my home page!
I am interested in <i><b>""" + interest + """</b></i></p>
"""+projetTeamHtml(pic1,pic2,name1,name2)+"""
</body>
</html>""")
  file.close()

def projetTeamHtml(pic1,pic2, name1, name2):
    return"""
    <br>
    <h2>My Project Team in CPIT380</h2>
    <img src= '""" + pic1 + """' alt="Nawaf" width="100" height="100">
    <h4>1-""" + name1 +"""</h4>
    <hr>
    <img src= '""" + pic2 + """' alt="Mohammed" width="100" height="100">
    <h4>2-""" + name2 +"""</h4>
    <hr>"""

makeHomePage("Nawaf Abdulaziz AlGhamdi","Mohammed hamdan alsafari",
             "Software Engineering",getMediaPath('nawaf.jpg'),getMediaPath('moh.jpeg'))