#-------------------------------------------------------------------------------
# Name:        Stick Figure Animation
# Purpose:     To show a figure walking across the screen as naturally as
#              possible.
#
# Author:      Jeremy Mohammed
#
# Created:     01/06/2017
# Copyright:   (c) s201016279 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Importing Pygame
import pygame
import sys
from pygame.locals import *
pygame.init()

#Window Features
Window = pygame.display.set_mode((1150,720))
pygame.display.set_caption("Stick Figure Animation")

#Setting Colours
White = (255,255,255)
DarkWhite = (250,250,250)
Black = (0,0,0)
Red = (237,3,16)
Green = (65,163,23)
Brown = (126,56,23)
LightBlue = (130,202,250)
DarkBlue = (0,32,194)
Yellow = (255,255,0)
DarkYellow = (215,215,0)
Peach = (255,229,180)
BrownRed = (149,69,53)
DarkGrey = (98,93,93)
LightGrey = (182,182,180)
LightOrange = (255,166,47)
GrassGreen = (161,201,53)
DarkGGreen = (101,141,0)
LDGGreen = (121,161,20)
DarkBrown = (89,9,0)
MediumGrey = (130,130,130)
VLightGrey = (220,220,220)
DarkPeach = (195,169,120)

#Setting Coordinates
x = 0
y = 0
#Sun
SunS = -30
#Sun flares
SunF11S = -85
SunF12S = -55
SunF21S = -30
SunF22S = -25
SunF23S = -35
SunF31S = 25
SunF32S = -5
SunF41S = -30
SunF42S = -25
SunF43S = -35
#Clouds
Cloud11 = -30
Cloud12 = 40
Cloud13 = 100
Cloud21 = 30
Cloud22 = 110
Cloud23 = 170
Cloud31 = 200
Cloud32 = 310
Cloud33 = 250
Cloud41 = 350
Cloud42 = 430
Cloud43 = 490
Cloud51 = 450
Cloud52 = 570
Cloud53 = 510
Cloud61 = 600
Cloud62 = 680
Cloud63 = 740
Cloud71 = 720
Cloud72 = 790
Cloud73 = 850
Cloud81 = 850
Cloud82 = 970
Cloud83 = 910
Cloud91 = 980
Cloud92 = 1050
Cloud93 = 1110

#FPS
FPS = 30
fpsClock = pygame.time.Clock()

#Running Event
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #Background Colours
    Window.fill(LightBlue)
    pygame.draw.rect(Window, GrassGreen, (0,360,1280,720),0)

    #Building grounds
    pygame.draw.rect(Window, DarkGrey, (0,370,1280,70),0)
    pygame.draw.polygon(Window, GrassGreen, ((-20,440), (20,440), (75,370), (-20,370),0))
    pygame.draw.polygon(Window, GrassGreen, ((180,440), (220,440), (275,370), (235,370),0))
    pygame.draw.polygon(Window, GrassGreen, ((380,440), (420,440), (475,370), (435,370),0))
    pygame.draw.polygon(Window, GrassGreen, ((830,440), (870,440), (925,370), (885,370),0))
    pygame.draw.polygon(Window, GrassGreen, ((1080,440), (1300,440), (1310,370), (1135,370),0))

    #Sun
    pygame.draw.circle(Window, Yellow, (int(SunS),50),20,0)
    pygame.draw.polygon(Window, DarkBrown, ((150,150), (150,440), (200,380), (200,100),0))
    pygame.draw.polygon(Window, DarkBrown, ((350,250), (350,440), (400,380), (400,200),0))
    pygame.draw.polygon(Window, DarkBrown, ((800,200), (800,440), (850,380), (850, 150),0))
    pygame.draw.polygon(Window, DarkBrown, ((1050,150), (1050,440), (1100,380), (1100,100),0))

    #Sun flares
    pygame.draw.polygon(Window, LightOrange, ((int(SunF11S),50), (int(SunF12S),45), (int(SunF12S),55)),0)
    pygame.draw.polygon(Window, LightOrange, ((int(SunF21S),5), (int(SunF22S),25), (int(SunF23S),25)),0)
    pygame.draw.polygon(Window, LightOrange, ((int(SunF31S),50), (int(SunF32S),45), (int(SunF32S),55)),0)
    pygame.draw.polygon(Window, LightOrange, ((int(SunF41S),95), (int(SunF42S),75), (int(SunF43S),75)),0)

    #Clouds
    #Cloud 1
    pygame.draw.ellipse(Window, White, (int(Cloud11),220,200,50),0)
    pygame.draw.circle(Window, White, (int(Cloud12),230),50,0)
    pygame.draw.circle(Window, White, (int(Cloud13),225),30,0)

    #Cloud 2
    pygame.draw.ellipse(Window, White, (Cloud21,40,200,50),0)
    pygame.draw.circle(Window, White, (Cloud22,50),50,0)
    pygame.draw.circle(Window, White, (Cloud23,45),30,0)

    #Cloud 3
    pygame.draw.ellipse(Window, White, (Cloud31,160,200,50),0)
    pygame.draw.circle(Window, White, (Cloud32,170),50,0)
    pygame.draw.circle(Window, White, (Cloud33,165),30,0)

    #Cloud 4
    pygame.draw.ellipse(Window, White, (int(Cloud41),50,200,50),0)
    pygame.draw.circle(Window, White, (int(Cloud42),60),50,0)
    pygame.draw.circle(Window, White, (int(Cloud43),55),30,0)

    #Cloud 5
    pygame.draw.ellipse(Window, White, (Cloud51,250,200,50),0)
    pygame.draw.circle(Window, White, (Cloud52,260),50,0)
    pygame.draw.circle(Window, White, (Cloud53,255),30,0)

    #Cloud 6
    pygame.draw.ellipse(Window, White, (int(Cloud61),140,200,50),0)
    pygame.draw.circle(Window, White, (int(Cloud62),150),50,0)
    pygame.draw.circle(Window, White, (int(Cloud63),145),30,0)

    #Cloud 7
    pygame.draw.ellipse(Window, White, (Cloud71,60,200,50),0)
    pygame.draw.circle(Window, White, (Cloud72,70),50,0)
    pygame.draw.circle(Window, White, (Cloud73,65),30,0)

    #Cloud 8
    pygame.draw.ellipse(Window, White, (Cloud81,230,200,50),0)
    pygame.draw.circle(Window, White, (Cloud82,240),50,0)
    pygame.draw.circle(Window, White, (Cloud83,235),30,0)

    #Cloud 9
    pygame.draw.ellipse(Window, White, (Cloud91,30,200,50),0)
    pygame.draw.circle(Window, White, (Cloud92,40),50,0)
    pygame.draw.circle(Window, White, (Cloud93,35),30,0)

    #Top sidewalk
    pygame.draw.rect(Window, VLightGrey, (0,435,1200,25),0)
    pygame.draw.rect(Window, DarkGrey, (0,435,1200,5),0)
    pygame.draw.rect(Window, DarkGrey, (0,440,1200,5),0)
    pygame.draw.rect(Window, DarkGrey, (0,460,1200,3),0)
    pygame.draw.rect(Window, Black, (0,463,1200,2),0)
    pygame.draw.rect(Window, LightGrey, (0,464,1200,3),0)
    pygame.draw.line(Window, DarkGrey, (0,460),(15,440),3)
    pygame.draw.line(Window, DarkGrey, (40,460),(55,440),3)
    pygame.draw.line(Window, DarkGrey, (80,460),(95,440),3)
    pygame.draw.line(Window, DarkGrey, (120,460),(135,440),3)
    pygame.draw.line(Window, DarkGrey, (160,460),(175,440),3)
    pygame.draw.line(Window, DarkGrey, (200,460),(215,440),3)
    pygame.draw.line(Window, DarkGrey, (240,460),(255,440),3)
    pygame.draw.line(Window, DarkGrey, (280,460),(295,440),3)
    pygame.draw.line(Window, DarkGrey, (320,460),(335,440),3)
    pygame.draw.line(Window, DarkGrey, (360,460),(375,440),3)
    pygame.draw.line(Window, DarkGrey, (400,460),(415,440),3)
    pygame.draw.line(Window, DarkGrey, (440,460),(455,440),3)
    pygame.draw.line(Window, DarkGrey, (480,460),(495,440),3)
    pygame.draw.line(Window, DarkGrey, (520,460),(535,440),3)
    pygame.draw.line(Window, DarkGrey, (560,460),(575,440),3)
    pygame.draw.line(Window, DarkGrey, (600,460),(615,440),3)
    pygame.draw.line(Window, DarkGrey, (640,460),(655,440),3)
    pygame.draw.line(Window, DarkGrey, (680,460),(695,440),3)
    pygame.draw.line(Window, DarkGrey, (720,460),(735,440),3)
    pygame.draw.line(Window, DarkGrey, (760,460),(775,440),3)
    pygame.draw.line(Window, DarkGrey, (800,460),(815,440),3)
    pygame.draw.line(Window, DarkGrey, (840,460),(855,440),3)
    pygame.draw.line(Window, DarkGrey, (880,460),(895,440),3)
    pygame.draw.line(Window, DarkGrey, (920,460),(935,440),3)
    pygame.draw.line(Window, DarkGrey, (960,460),(975,440),3)
    pygame.draw.line(Window, DarkGrey, (1000,460),(1015,440),3)
    pygame.draw.line(Window, DarkGrey, (1040,460),(1055,440),3)
    pygame.draw.line(Window, DarkGrey, (1080,460),(1095,440),3)
    pygame.draw.line(Window, DarkGrey, (1120,460),(1135,440),3)

    #Road
    pygame.draw.rect(Window, Black, (0,467,1200,220),0)
    pygame.draw.rect(Window, DarkYellow, (0,515,1200,4),0)
    pygame.draw.rect(Window, DarkYellow, (0,525,1200,5),0)

    #Top street lines
    pygame.draw.rect(Window, DarkWhite, (0,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (40,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (80,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (120,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (160,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (200,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (240,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (280,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (320,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (360,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (400,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (440,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (480,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (520,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (560,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (600,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (640,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (680,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (720,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (760,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (800,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (840,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (880,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (920,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (960,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (1000,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (1040,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (1080,480,30,3),0)
    pygame.draw.rect(Window, DarkWhite, (1120,480,30,3),0)

    #Bottom street lines
    pygame.draw.rect(Window, DarkWhite, (0,560,80,7),0)
    pygame.draw.rect(Window, DarkWhite, (100,560,80,7),0)
    pygame.draw.rect(Window, DarkWhite, (200,560,80,7),0)
    pygame.draw.rect(Window, DarkWhite, (300,560,80,7),0)
    pygame.draw.rect(Window, DarkWhite, (400,560,80,7),0)
    pygame.draw.rect(Window, DarkWhite, (500,560,80,7),0)
    pygame.draw.rect(Window, DarkWhite, (600,560,80,7),0)
    pygame.draw.rect(Window, DarkWhite, (700,560,80,7),0)
    pygame.draw.rect(Window, DarkWhite, (800,560,80,7),0)
    pygame.draw.rect(Window, DarkWhite, (900,560,80,7),0)
    pygame.draw.rect(Window, DarkWhite, (1000,560,80,7),0)
    pygame.draw.rect(Window, DarkWhite, (1100,560,80,7),0)

    #Bottom sidewalk
    pygame.draw.rect(Window, VLightGrey, (0,630,1200,55),0)
    pygame.draw.rect(Window, DarkGrey, (0,630,1200,5),0)
    pygame.draw.rect(Window, DarkGrey, (0,680,1200,4),0)
    pygame.draw.rect(Window, Black, (0,683,1200,3),0)
    pygame.draw.rect(Window, LightGrey, (0,684,1200,6),0)
    pygame.draw.rect(Window, Black, (0,690,1200,3),0)
    pygame.draw.rect(Window, DarkGGreen, (0,693,1200,6),0)
    pygame.draw.rect(Window, LDGGreen, (0,699,1200,3),0)
    pygame.draw.line(Window, DarkGrey, (40,680),(75,630),3)
    pygame.draw.line(Window, DarkGrey, (120,680),(155,630),3)
    pygame.draw.line(Window, DarkGrey, (200,680),(235,630),3)
    pygame.draw.line(Window, DarkGrey, (280,680),(315,630),3)
    pygame.draw.line(Window, DarkGrey, (360,680),(395,630),3)
    pygame.draw.line(Window, DarkGrey, (440,680),(475,630),3)
    pygame.draw.line(Window, DarkGrey, (520,680),(555,630),3)
    pygame.draw.line(Window, DarkGrey, (600,680),(635,630),3)
    pygame.draw.line(Window, DarkGrey, (680,680),(715,630),3)
    pygame.draw.line(Window, DarkGrey, (760,680),(795,630),3)
    pygame.draw.line(Window, DarkGrey, (840,680),(875,630),3)
    pygame.draw.line(Window, DarkGrey, (920,680),(955,630),3)
    pygame.draw.line(Window, DarkGrey, (1000,680),(1035,630),3)
    pygame.draw.line(Window, DarkGrey, (1080,680),(1115,630),3)

    #Side of buldings
    pygame.draw.polygon(Window, DarkBrown, ((150,150), (150,440), (200,380), (200,100),0))
    pygame.draw.polygon(Window, DarkBrown, ((350,250), (350,440), (400,380), (400,200),0))
    pygame.draw.polygon(Window, DarkBrown, ((800,200), (800,440), (850,380), (850, 150),0))
    pygame.draw.polygon(Window, DarkBrown, ((1050,150), (1050,440), (1100,380), (1100,100),0))

    #Top of buildings
    pygame.draw.polygon(Window, MediumGrey, ((150,150), (50,150), (100,100), (200,100),0))
    pygame.draw.polygon(Window, MediumGrey, ((350,250), (250,250), (300,200), (400,200),0))
    pygame.draw.polygon(Window, MediumGrey, ((800,200), (650,200), (700,150), (850,150),0))
    pygame.draw.polygon(Window, MediumGrey, ((450,350), (650,350), (650,300), (500,300),0))
    pygame.draw.polygon(Window, MediumGrey, ((1050,150), (900,150), (950,100), (1100,100),0))

    #Front of back ledge of buildings
    pygame.draw.polygon(Window, DarkGrey, ((195,105), (95,105), (90,115), (190,115),0))
    pygame.draw.polygon(Window, DarkGrey, ((395,205), (295,205), (290,215), (390,215),0))
    pygame.draw.polygon(Window, DarkGrey, ((650,305), (505,305), (495,315), (650,315),0))
    pygame.draw.polygon(Window, DarkGrey, ((845,155), (695,155), (690,165), (840,165),0))
    pygame.draw.polygon(Window, DarkGrey, ((1095,105), (945,105), (940,115), (1090,115),0))

    #Front of left side ledge of buildings
    pygame.draw.polygon(Window, DarkGrey, ((70,150), (50,150), (100,100), (120,100),0))
    pygame.draw.polygon(Window, DarkGrey, ((270,250), (250,250), (300,200), (320,200),0))
    pygame.draw.polygon(Window, DarkGrey, ((470,350), (460,350), (510,300), (520,300),0))
    pygame.draw.polygon(Window, DarkGrey, ((670,200), (650,200), (700,150), (720,150),0))
    pygame.draw.polygon(Window, DarkGrey, ((920,150), (900,150), (950,100), (970,100),0))

    #Side ledge of buildings
    pygame.draw.polygon(Window, MediumGrey, ((150,150), (150,170), (200,120), (200,100),0))
    pygame.draw.polygon(Window, MediumGrey, ((350,250), (350,270), (400,220), (400,200),0))
    pygame.draw.polygon(Window, MediumGrey, ((800,200), (800,220), (850,170), (850, 150),0))
    pygame.draw.polygon(Window, MediumGrey, ((1050,150), (1050,170), (1100,120), (1100,100),0))

    #Top of front ledge of buildings
    pygame.draw.polygon(Window, VLightGrey, ((150,150), (50,150), (60,140), (160,140),0))
    pygame.draw.polygon(Window, VLightGrey, ((350,250), (250,250), (260,240), (360,240),0))
    pygame.draw.polygon(Window, VLightGrey, ((800,200), (650,200), (660,190), (810,190),0))
    pygame.draw.polygon(Window, VLightGrey, ((450,350), (650,350), (650,340), (460,340),0))
    pygame.draw.polygon(Window, VLightGrey, ((1050,150), (900,150), (910,140), (1060,140),0))

    #Top of right side ledge of buildings
    pygame.draw.polygon(Window, VLightGrey, ((150,150), (140,150), (190,100), (200,100),0))
    pygame.draw.polygon(Window, VLightGrey, ((350,250), (340,250), (390,200), (400,200),0))
    pygame.draw.polygon(Window, VLightGrey, ((800,200), (790,200), (840,150), (850,150),0))
    pygame.draw.polygon(Window, VLightGrey, ((1050,150), (1040,150), (1090,100), (1100,100),0))

    #Top of left side ledge of buildings
    pygame.draw.polygon(Window, VLightGrey, ((60,150), (50,150), (100,100), (110,100),0))
    pygame.draw.polygon(Window, VLightGrey, ((260,250), (250,250), (300,200), (310,200),0))
    pygame.draw.polygon(Window, VLightGrey, ((450,350), (460,350), (510,300), (500,300),0))
    pygame.draw.polygon(Window, VLightGrey, ((660,200), (650,200), (700,150), (710,150),0))
    pygame.draw.polygon(Window, VLightGrey, ((910,150), (900,150), (950,100), (960,100),0))

    #Top of back ledge of buildings
    pygame.draw.polygon(Window, VLightGrey, ((195,105), (95,105), (100,100), (200,100),0))
    pygame.draw.polygon(Window, VLightGrey, ((395,205), (295,205), (300,200), (400,200),0))
    pygame.draw.polygon(Window, VLightGrey, ((650,305), (505,305), (510,300), (650,300),0))
    pygame.draw.polygon(Window, VLightGrey, ((845,155), (695,155), (700,150), (850,150),0))
    pygame.draw.polygon(Window, VLightGrey, ((1095,105), (945,105), (950,100), (1100,100),0))

    #Front of buildings
    pygame.draw.rect(Window, BrownRed, (50,150,100,290),0)
    pygame.draw.rect(Window, BrownRed, (250,250,100,190),0)
    pygame.draw.rect(Window, BrownRed, (450,350,350,90),0)
    pygame.draw.rect(Window, BrownRed, (650,200,150,220),0)
    pygame.draw.rect(Window, BrownRed, (900,150,150,290),0)

    #Front ledge of buildings
    pygame.draw.rect(Window, LightGrey, (50,150,100,20),0)
    pygame.draw.rect(Window, LightGrey, (250,250,100,20),0)
    pygame.draw.rect(Window, LightGrey, (450,350,200,20),0)
    pygame.draw.rect(Window, LightGrey, (650,200,150,20),0)
    pygame.draw.rect(Window, LightGrey, (900,150,150,20),0)

    #Front windows on buildings (left to right)
    #Building 1
    pygame.draw.rect(Window, Peach, (60,180,10,30),0)
    pygame.draw.rect(Window, Peach, (80,180,10,30),0)
    pygame.draw.rect(Window, Peach, (100,180,10,30),0)
    pygame.draw.rect(Window, Peach, (120,180,20,30),0)
    pygame.draw.rect(Window, Peach, (60,220,10,10),0)
    pygame.draw.rect(Window, Peach, (80,220,10,10),0)
    pygame.draw.rect(Window, Peach, (100,220,10,10),0)
    pygame.draw.rect(Window, Peach, (120,220,20,10),0)
    pygame.draw.rect(Window, Peach, (60,240,10,10),0)
    pygame.draw.rect(Window, Peach, (80,240,10,10),0)
    pygame.draw.rect(Window, Peach, (100,240,10,10),0)
    pygame.draw.rect(Window, Peach, (120,240,20,10),0)
    pygame.draw.rect(Window, Peach, (60,260,10,10),0)
    pygame.draw.rect(Window, Peach, (80,260,10,10),0)
    pygame.draw.rect(Window, Peach, (100,260,10,10),0)
    pygame.draw.rect(Window, Peach, (120,260,20,10),0)
    pygame.draw.rect(Window, Peach, (60,280,10,10),0)
    pygame.draw.rect(Window, Peach, (80,280,10,10),0)
    pygame.draw.rect(Window, Peach, (100,280,10,10),0)
    pygame.draw.rect(Window, Peach, (120,280,20,10),0)
    pygame.draw.rect(Window, Peach, (60,300,10,10),0)
    pygame.draw.rect(Window, Peach, (80,300,10,10),0)
    pygame.draw.rect(Window, Peach, (100,300,10,10),0)
    pygame.draw.rect(Window, Peach, (120,300,20,10),0)
    pygame.draw.rect(Window, Peach, (60,320,10,10),0)
    pygame.draw.rect(Window, Peach, (80,320,10,10),0)
    pygame.draw.rect(Window, Peach, (100,320,10,10),0)
    pygame.draw.rect(Window, Peach, (120,320,20,10),0)
    pygame.draw.rect(Window, Peach, (60,340,10,10),0)
    pygame.draw.rect(Window, Peach, (80,340,10,10),0)
    pygame.draw.rect(Window, Peach, (100,340,10,10),0)
    pygame.draw.rect(Window, Peach, (120,340,20,10),0)
    pygame.draw.rect(Window, Peach, (60,360,10,10),0)
    pygame.draw.rect(Window, Peach, (80,360,10,10),0)
    pygame.draw.rect(Window, Peach, (100,360,10,10),0)
    pygame.draw.rect(Window, Peach, (120,360,20,10),0)
    pygame.draw.rect(Window, Peach, (60,380,80,10),0)
    pygame.draw.rect(Window, Peach, (60,400,10,30),0)
    pygame.draw.rect(Window, Peach, (80,400,15,10),0)
    pygame.draw.rect(Window, Peach, (105,400,15,10),0)
    pygame.draw.rect(Window, Peach, (130,400,10,30),0)

    #Building 2
    pygame.draw.rect(Window, Peach, (260,280,20,10),0)
    pygame.draw.rect(Window, Peach, (290,280,20,10),0)
    pygame.draw.rect(Window, Peach, (320,280,20,10),0)
    pygame.draw.rect(Window, Peach, (260,300,20,10),0)
    pygame.draw.rect(Window, Peach, (290,300,20,10),0)
    pygame.draw.rect(Window, Peach, (320,300,20,10),0)
    pygame.draw.rect(Window, Peach, (260,320,20,10),0)
    pygame.draw.rect(Window, Peach, (290,320,20,10),0)
    pygame.draw.rect(Window, Peach, (320,320,20,10),0)
    pygame.draw.rect(Window, Peach, (260,340,20,10),0)
    pygame.draw.rect(Window, Peach, (290,340,20,10),0)
    pygame.draw.rect(Window, Peach, (320,340,20,10),0)
    pygame.draw.rect(Window, Peach, (260,360,20,10),0)
    pygame.draw.rect(Window, Peach, (290,360,20,10),0)
    pygame.draw.rect(Window, Peach, (320,360,20,10),0)
    pygame.draw.rect(Window, Peach, (260,380,80,10),0)
    pygame.draw.rect(Window, Peach, (260,400,10,30),0)
    pygame.draw.rect(Window, Peach, (280,400,15,10),0)
    pygame.draw.rect(Window, Peach, (305,400,15,10),0)
    pygame.draw.rect(Window, Peach, (330,400,10,30),0)

    #Building 3
    pygame.draw.rect(Window, Peach, (660,230,40,40),0)
    pygame.draw.rect(Window, Peach, (660,280,40,40),0)
    pygame.draw.rect(Window, Peach, (660,330,40,40),0)
    pygame.draw.rect(Window, Peach, (705,230,40,40),0)
    pygame.draw.rect(Window, Peach, (705,280,40,40),0)
    pygame.draw.rect(Window, Peach, (705,330,40,40),0)
    pygame.draw.rect(Window, Peach, (750,230,40,40),0)
    pygame.draw.rect(Window, Peach, (750,280,40,40),0)
    pygame.draw.rect(Window, Peach, (750,330,40,40),0)
    pygame.draw.rect(Window, Peach, (460,380,100,10),0)
    pygame.draw.rect(Window, Peach, (575,380,100,10),0)
    pygame.draw.rect(Window, Peach, (690,380,100,10),0)
    pygame.draw.rect(Window, Peach, (460,400,100,10),0)
    pygame.draw.rect(Window, Peach, (690,400,100,10),0)
    pygame.draw.rect(Window, Peach, (460,420,100,10),0)
    pygame.draw.rect(Window, Peach, (690,420,100,10),0)
    pygame.draw.rect(Window, Peach, (590,400,10,30),0)
    pygame.draw.rect(Window, Peach, (650,400,10,30),0)

    #Building 4
    pygame.draw.rect(Window, Peach, (920,190,20,230),0)
    pygame.draw.rect(Window, Peach, (965,190,20,205),0)
    pygame.draw.rect(Window, Peach, (1010,190,20,230),0)

    #Side windows on buildings (Left to right)
    #Building 1
    pygame.draw.polygon(Window, DarkPeach, ((160,195), (160,215), (190,180), (190,160),0))
    pygame.draw.polygon(Window, DarkPeach, ((160,235), (160,255), (190,220), (190,200),0))
    pygame.draw.polygon(Window, DarkPeach, ((160,275), (160,295), (190,260), (190,240),0))
    pygame.draw.polygon(Window, DarkPeach, ((160,315), (160,335), (190,300), (190,280),0))
    pygame.draw.polygon(Window, DarkPeach, ((160,355), (160,375), (190,340), (190,320),0))

    #Building 2
    pygame.draw.polygon(Window, DarkPeach, ((360,295), (360,315), (390,280), (390,260),0))
    pygame.draw.polygon(Window, DarkPeach, ((360,335), (360,355), (390,320), (390,300),0))

    #Building 3
    pygame.draw.polygon(Window, DarkPeach, ((810,245), (810,305), (840,270), (840,210),0))
    pygame.draw.polygon(Window, DarkPeach, ((810,325), (810,385), (840,350), (840,290),0))

    #Building 4
    pygame.draw.polygon(Window, DarkPeach, ((1070,180), (1070,390), (1080,370), (1080,165),0))

    #Door on buildings (Left to right)
    #Building 1
    pygame.draw.rect(Window, LightGrey, (85,415,30,25),0)
    pygame.draw.rect(Window, DarkGrey, (85,415,2,25),0)
    pygame.draw.rect(Window, DarkGrey, (113,415,2,25),0)
    pygame.draw.rect(Window, DarkGrey, (85,415,30,2),0)
    pygame.draw.rect(Window, DarkGrey, (98,415,2,25),0)
    pygame.draw.rect(Window, DarkGrey, (100,415,2,25),0)
    pygame.draw.circle(Window, DarkGrey, (95,432),1,0)
    pygame.draw.circle(Window, DarkGrey, (104,432),1,0)

    #Building 2
    pygame.draw.rect(Window, LightGrey, (285,415,30,25),0)
    pygame.draw.rect(Window, DarkGrey, (285,415,2,25),0)
    pygame.draw.rect(Window, DarkGrey, (313,415,2,25),0)
    pygame.draw.rect(Window, DarkGrey, (285,415,30,2),0)
    pygame.draw.rect(Window, DarkGrey, (298,415,2,25),0)
    pygame.draw.rect(Window, DarkGrey, (300,415,2,25),0)
    pygame.draw.circle(Window, DarkGrey, (295,432),1,0)
    pygame.draw.circle(Window, DarkGrey, (304,432),1,0)

    #Building 3
    pygame.draw.rect(Window, LightGrey, (610,415,30,25),0)
    pygame.draw.rect(Window, DarkGrey, (610,415,2,25),0)
    pygame.draw.rect(Window, DarkGrey, (638,415,2,25),0)
    pygame.draw.rect(Window, DarkGrey, (610,415,30,2),0)
    pygame.draw.rect(Window, DarkGrey, (623,415,2,25),0)
    pygame.draw.rect(Window, DarkGrey, (625,415,2,25),0)
    pygame.draw.circle(Window, DarkGrey, (620,432),1,0)
    pygame.draw.circle(Window, DarkGrey, (629,432),1,0)

    #Building 4
    pygame.draw.rect(Window, LightGrey, (960,415,30,25),0)
    pygame.draw.rect(Window, DarkGrey, (960,415,2,25),0)
    pygame.draw.rect(Window, DarkGrey, (988,415,2,25),0)
    pygame.draw.rect(Window, DarkGrey, (960,415,30,2),0)
    pygame.draw.rect(Window, DarkGrey, (973,415,2,25),0)
    pygame.draw.rect(Window, DarkGrey, (975,415,2,25),0)
    pygame.draw.circle(Window, DarkGrey, (970,432),1,0)
    pygame.draw.circle(Window, DarkGrey, (979,432),1,0)


    #Moving Coordinates
    #Sun
    SunS = SunS + 0.25
    #Sun flares
    SunF11S = SunF11S + 0.25
    SunF12S = SunF12S + 0.25
    SunF21S = SunF21S + 0.25
    SunF22S = SunF22S + 0.25
    SunF23S = SunF23S + 0.25
    SunF31S = SunF31S + 0.25
    SunF32S = SunF32S + 0.25
    SunF41S = SunF41S + 0.25
    SunF42S = SunF42S + 0.25
    SunF43S = SunF43S + 0.25
    #Clouds
    #Move forward
    if x == 0:
        Cloud11 = Cloud11 + 0.5
        Cloud12 = Cloud12 + 0.5
        Cloud13 = Cloud13 + 0.5
        Cloud21 = Cloud21 + 1
        Cloud22 = Cloud22 + 1
        Cloud23 = Cloud23 + 1
        Cloud31 = Cloud31 + 2
        Cloud32 = Cloud32 + 2
        Cloud33 = Cloud33 + 2
        Cloud41 = Cloud41 + 0.5
        Cloud42 = Cloud42 + 0.5
        Cloud43 = Cloud43 + 0.5
        Cloud51 = Cloud51 + 1
        Cloud52 = Cloud52 + 1
        Cloud53 = Cloud53 + 1
        Cloud61 = Cloud61 + 0.5
        Cloud62 = Cloud62 + 0.5
        Cloud63 = Cloud63 + 0.5
        Cloud71 = Cloud71 + 2
        Cloud72 = Cloud72 + 2
        Cloud73 = Cloud73 + 2
        Cloud81 = Cloud81 + 1
        Cloud82 = Cloud82 + 1
        Cloud83 = Cloud83 + 1
        Cloud91 = Cloud91 + 1
        Cloud92 = Cloud92 + 1
        Cloud93 = Cloud93 + 1
    #Move backwards
    elif x == 1:
        Cloud11 = Cloud11 - 0.5
        Cloud12 = Cloud12 - 0.5
        Cloud13 = Cloud13 - 0.5
        Cloud21 = Cloud21 - 1
        Cloud22 = Cloud22 - 1
        Cloud23 = Cloud23 - 1
        Cloud31 = Cloud31 - 2
        Cloud32 = Cloud32 - 2
        Cloud33 = Cloud33 - 2
        Cloud41 = Cloud41 - 0.5
        Cloud42 = Cloud42 - 0.5
        Cloud43 = Cloud43 - 0.5
        Cloud51 = Cloud51 - 1
        Cloud52 = Cloud52 - 1
        Cloud53 = Cloud53 - 1
        Cloud61 = Cloud61 - 0.5
        Cloud62 = Cloud62 - 0.5
        Cloud63 = Cloud63 - 0.5
        Cloud71 = Cloud71 - 2
        Cloud72 = Cloud72 - 2
        Cloud73 = Cloud73 - 2
        Cloud81 = Cloud81 - 1
        Cloud82 = Cloud82 - 1
        Cloud83 = Cloud83 - 1
        Cloud91 = Cloud91 - 1
        Cloud92 = Cloud92 - 1
        Cloud93 = Cloud93 - 1
    #Make move backwards
    if Cloud71 == 1000:
        x = 1
    #Make move forwards
    elif Cloud31 == -100:
        x = 0

    #Refresh
    pygame.display.update()
    fpsClock.tick(FPS)