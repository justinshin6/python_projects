###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)

"""
Steps to installing colorgram: 
1.) Navigate to PyCharm at the very top navbar.
2.) Click on Preferences 
3.) Navigate to Project:
4.) Click on Python Interpreter and then click on the + button 
5.) Type in cologram and then press install and then the red line underneath should go away 
"""