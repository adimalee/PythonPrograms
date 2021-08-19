# CS 460 Project
# Iceland Project
# By: Aditya Maleeswaran

import pygame
from pygame.locals import *

# Intialize a few basic colors
# These values are 255 because there are 256 (0 - 255) bits for a byte of color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (250, 0, 0)
GREEN = (0, 250, 0)
BLUE = (0, 0, 250)
 
# Include some libraries
# Initializing pygame library
pygame.init()
 
# Create a window with the same size of the actual map
# The size of the map is 1152x900 
screen = pygame.display.set_mode((1152,900),HWSURFACE|DOUBLEBUF|RESIZABLE)

# This sets the name of the window
pygame.display.set_caption('Iceland Battle with Ships')

# Set a digital clock to the window
clock = pygame.time.Clock()

# Set positions of graphics
background_position = [0, 0]

# Load and set up background
background_image = pygame.image.load("sea.jpg").convert()

 
# Bismark Function
def bismark(location):
    # Load and set up ships
    bismarkRightDown = pygame.image.load('bis1.jpg').convert()
    bismarkDown = pygame.image.load('bis2.jpg').convert()
    bismarkLeftDown = pygame.image.load('bis3.jpg').convert()
    bismarkLeftDownFire = pygame.image.load('bis3f.jpg').convert()
    bismarkLeft = pygame.image.load('bis4.jpg').convert()
    bismarkLeftFire = pygame.image.load('bis4f.jpg').convert()
    bismarkLeftHit = pygame.image.load('bis4fh.jpg').convert()
    bismarkLeftSplash = pygame.image.load('bis4s.jpg').convert()
    bismarkPort = pygame.image.load('bis5.jpg').convert()

    # Array of coordinates for ships
    bismarkPosition = [(605,21),(609,27),(613,34),(617,38),(621,44),(625,49),(629,55),(633,60),(638,66),(642,71),(646,76),
                        (650,82),(654,87),(658,93),(663,98),(667,103),(671,108),(675,113),(678,118),(682,122),(685,126),
                        (684,130),(683,134),(680,137),(676,141),(672,145),(669,148),(665,152),(661,156),(656,161),(652,165),
                        (647,170),(643,175),(638,180),(634,184),(629,189),(625,193),(620,198),(615,202),(610,207),(606,211),
                        (601,216),(597,220),(592,225),(588,230),(583,235),(579,239),(574,244),(569,249),(564,254),(559,259),
                        (554,264),(548,270),(542,276),(537,281),(531,287),(526,292),(520,298),(514,303),(508,309),(503,314),
                        (497,320),(492,325),(486,331),(480,337),(474,343),(469,348),(463,354),(458,359),(452,365),(446,371),
                        (440,377),(433,384),(426,391),(419,398),(412,405),(405,412),(398,419),(391,426),(384,433),(377,440),
                        (370,447),(363,454),(356,461),(349,466),(342,468),(333,468),(324,468),(315,468),(305,468),(295,468),
                        (285,472),(280,480),(279,489),(278,498),(278,505),(277,512),(266,529),(262,533),(257,536),(251,539),
                        (241,541),(231,542),(223,542),(215,543),(207,543),(199,544),(191,544),(183,544),(175,545),(167,545),
                        (159,546),(151,546),(143,547),(135,547),(128,548),(120,548),(113,549),(105,549),(98,550)]


    if(location < 20 ):
        screen.blit(bismarkRightDown,bismarkPosition[location])
    elif(location >= 20 and location <= 21 ):
        screen.blit(bismarkDown,(bismarkPosition[location]))
    elif (location > 21 and location <= 84): 
        if(location == 79 or location == 83):
            screen.blit(bismarkLeftDownFire,(bismarkPosition[location]))    
        else:
            screen.blit(bismarkLeftDown,(bismarkPosition[location]))
    elif(location > 84  and location < 92):
        if(location == 85):
            screen.blit(bismarkLeftFire,(bismarkPosition[location]))
        elif(location == 90):
            screen.blit(bismarkLeftSplash,(bismarkPosition[location]))
        else:
            screen.blit(bismarkLeft,(bismarkPosition[location]))
    elif(location >= 92 and location < 96): 
        screen.blit(bismarkDown,(bismarkPosition[location]))
    elif(location >= 96 and location <= 98):
        screen.blit(bismarkLeftDown,(bismarkPosition[location]))
    elif(location > 98 ):
        screen.blit(bismarkLeft,(bismarkPosition[location]))
    
# Prince of Eugen Function
def PofE(location):
    # Load and set up ships
    princeEugenDownRight = pygame.image.load('pe1.ppm').convert()
    princeEugenDownLeft = pygame.image.load('pe2.ppm').convert()
    princeEugenDownLeftFire = pygame.image.load('pe2f.ppm').convert()
    princeEugenDownLeftSplash = pygame.image.load('pe2s.ppm').convert()
    princeEugenLeftUp  = pygame.image.load('pe3.ppm').convert()
    princeEugenDown  = pygame.image.load('pe4.ppm').convert()
    princeEugenLeft = pygame.image.load('pe5.gif').convert()
    princeEugenLeftSplash = pygame.image.load('pe5s.ppm').convert()
    princeEugenLeftFire = pygame.image.load('pe5f.ppm').convert()
    
    # Array of coordinates for ships
    princeEugenPosition = [(620,41),(624,47),(628,54),(632,58),(636,64),(640,69),(644,75),(648,80),(652,86),(657,91),(661,96),
                        (665,102),(670,107),(674,113),(680,118),(684,123),(684,129),(683,134),(679,138),(675,141),(672,145),
                        (667,150),(663,154),(660,157),(656,161),(652,165),(649,168),(645,172),(641,176),(636,181),(632,185),
                        (627,190),(623,195),(618,200),(614,204),(609,209),(605,213),(600,218),(595,222),(590,227),(586,231),
                        (581,236),(577,240),(572,245),(568,250),(563,255),(559,259),(554,264),(549,269),(544,274),(539,279),
                        (534,284),(528,290),(522,296),(517,301),(511,307),(506,312),(500,318),(494,323),(488,329),(483,334),
                        (477,340),(472,345),(466,351),(460,357),(454,363),(449,368),(443,374),(438,379),(432,385),(426,391),
                        (420,397),(413,404),(406,411),(399,418),(392,425),(385,432),(378,439),(371,446),(364,453),(357,460),
                        (350,467),(343,474),(337,478),(332,482),(323,484),(314,485),(307,485),(300,485),(293,486),(285,488),
                        (278,490),(271,492),(264,494),(258,494),(249,495),(240,497),(222,505),(217,510),(212,515),(206,521),
                        (201,526),(196,531),(190,537),(184,543),(179,548),(174,550),(168,552),(162,550),(156,548),(151,543),
                        (145,537),(140,532),(134,526),(128,520),(122,518),(116,516),(110,518),(104,520),(98,534)]

    # Put Prince Eugen to screen
    if location < 17:
        screen.blit(princeEugenDownRight,(princeEugenPosition[location]))
    elif location >= 17 and location < 85:
        if(location == 70):
            screen.blit(princeEugenDownLeftFire,(princeEugenPosition[location]))
        elif(location == 68):
            screen.blit(princeEugenDownLeftSplash,(princeEugenPosition[location]))
        elif(location == 79):
            screen.blit(princeEugenDownLeftFire,(princeEugenPosition[location]))
        else:    
            screen.blit(princeEugenDownLeft,(princeEugenPosition[location]))
    elif location >= 85 and location <= 95:
        screen.blit(princeEugenLeft,(princeEugenPosition[location]))  
    elif location > 95 and location <106:
         screen.blit(princeEugenDownLeft,(princeEugenPosition[location]))   
    elif location >= 106  and location < 108:
        screen.blit(princeEugenLeft,(princeEugenPosition[location]))
    elif location >= 108  and location < 116:
        screen.blit(princeEugenLeftUp,(princeEugenPosition[location]))
    elif location >= 116:
        screen.blit(princeEugenDownLeft,(princeEugenPosition[location]))
# Hood
def Hood(location):
    # Load and set up ships
    HoodDownLeft = pygame.image.load('hood1.ppm').convert()
    HoodLeft = pygame.image.load('hood2.ppm').convert()
    HoodLeftBlast = pygame.image.load('hood2b.ppm').convert()
    HoodLeftFire = pygame.image.load('hood2f.ppm').convert()
    HoodLeftHit = pygame.image.load('hood2h.ppm').convert()
    HoodLeftExplode = pygame.image.load('hood2l.ppm').convert()
    HoodLeftSink = pygame.image.load('hood2r.ppm').convert()
    HoodUpRight = pygame.image.load('hood3.ppm').convert()
    HoodUpRightBurn = pygame.image.load('hood3b.ppm').convert()
    HoodUpRightFire = pygame.image.load('hood3f.ppm').convert()
    HoodUpRightHit = pygame.image.load('hood3h.ppm').convert()
    HoodUpRightSplash = pygame.image.load('hood3s.ppm').convert()
    HoodUpRightSplashBurn = pygame.image.load('hood3sb.ppm').convert()

    # Array of coordinates for ships
    HoodPosition = [(0,0),(0,0),(0,0),( 0,0),(1142,702),(1134,706),(1126,710),(1118,714),(1110,718),(1102,722),(1094,726),
                    (1086,730),(1078,734),(1070,736),(1062,742),(1054,746),(1046,750),(1038,754),(1030,758),(1022,762),(1014,766),
                    (1006,770),(998,774),(990,778),(982,782),(974,786),(966,790),(958,794),(950,798),(942,802),(934,806),
                    (926,810),(918,814),(910,818),(902,822),(896,821),(889,819),(883,818),(876,816),(870,815),(863,814),
                    (857,813),(850,811),(844,810),(837,809),(831,808),(824,806),(818,805),(811,803),(805,802),(798,800),
                    (792,799),(785,798),(779,797),(772,795),(766,794),(759,792),(753,790),(746,787),(739,785),(732,782),
                    (725,780),(718,777),(711,775),(704,772),(697,769),(690,766),(683,763),(676,760),(669,758),(662,756),
                    (655,755),(648,754),(641,752),(634,751),(627,750),(620,748),(613,747),(606,746),(599,745),(592,744),
                    (585,743),(578,742),(578,742),(578,742),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                    (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                    (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                    (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]

    # Put hood to screen
    
    if(HoodPosition[location] != (0,0)):
        if(location < 34):
            screen.blit(HoodDownLeft,HoodPosition[location]) 
            
        elif(location == 34):
            screen.blit(HoodLeft,HoodPosition[location]) 
        elif(location > 34 and location < 67):
            screen.blit(HoodUpRight,HoodPosition[location])  
        elif(location >= 67 and location < 74 ):
            if(location == 67):
                screen.blit(HoodUpRightFire,HoodPosition[location])
            elif(location == 71):
                screen.blit(HoodUpRightSplash,HoodPosition[location])
            else:    
                screen.blit(HoodUpRight,HoodPosition[location])
        elif(location >= 74):
            if(location == 80):
                screen.blit(HoodUpRightSplashBurn,HoodPosition[location])
            elif(location == 81):
                screen.blit(HoodUpRightHit,HoodPosition[location])
            elif(location == 82):
                screen.blit(HoodLeftExplode,HoodPosition[location])
            elif(location > 82):
                screen.blit(HoodLeftSink,HoodPosition[location])
            else:
                screen.blit(HoodUpRightBurn,HoodPosition[location])

                
# PrinceOfWales Function
def princeOfWales(location):
    # Load and set up ships
    princeOfWalesDownLeft = pygame.image.load('pw1.ppm').convert()
    princeOfWalesLeft = pygame.image.load('pw2.ppm').convert()
    princeOfWalesLeftFire = pygame.image.load('pw2f.ppm').convert()
    princeOfWalesLeftHit = pygame.image.load('pw2h.ppm').convert()
    princeOfWalesUpLeft = pygame.image.load('pw3.ppm').convert()
    princeOfWalesUpLeftBlast = pygame.image.load('pw3b.ppm').convert()
    princeOfWalesUpLeftFire = pygame.image.load('pw3f.ppm').convert()
    princeOfWalesUpLeftHit = pygame.image.load('pw3h.ppm').convert()
    princeOfWalesUpLeftHitFire = pygame.image.load('pw3hf.ppm').convert()
    princeOfWalesDownRight = pygame.image.load('pw4.ppm').convert()
    princeOfWalesDownRightFire = pygame.image.load('pw4f.ppm').convert()
    princeOfWalesRight = pygame.image.load('pw5.ppm').convert()
    princeOfWalesRightSplash = pygame.image.load('pw5s.ppm').convert()
    princeOfWalesDown = pygame.image.load('pw6.ppm').convert()
    princeOfWalesDownFire = pygame.image.load('pw6f.ppm').convert()
    princeOfWalesDownHit = pygame.image.load('pw6h.ppm').convert()
    # Array of coordinates for ships
    princeOfWalesPosition = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),( 0,0),(1138,704),(1130,708),(1122,712),(1114,716),
                        (1106,720),(1098,724),(1090,726),(1082,732),(1074,736),(1066,740),(1058,744),(1050,748),(1042,752),(1034,756),
                        (1026,760),(1018,764),(1010,768),(1002,772),(994,776),(986,780),(978,784),(970,788),(962,790),(954,796),
                        (946,800),(938,804),(930,808),(922,812),(916,811),(909,809),(903,808),(896,806),(890,805),(883,804),
                        (877,803),(870,801),(864,800),(857,799),(851,798),(844,796),(838,795),(831,793),(825,792),(818,790),
                        (812,789),(805,788),(799,787),(792,785),(786,784),(779,782),(773,780),(766,777),(759,775),(752,772),
                        (745,770),(738,767),(731,765),(724,762),(717,759),(710,756),(703,753),(696,750),(689,748),(682,746),
                        (675,745),(668,744),(661,742),(654,741),(647,740),(640,738),(633,737),(626,736),(619,735),(612,734),
                        (605,733),(598,732),(592,725),(587,717),(577,714),(567,712),(561,717),(560,725),(560,733),(560,741),
                        (561,749),(561,757),(562,764),(563,770),(567,776),(571,782),(579,794),(583,802),(591,804),(600,805),
                        (609,805),(618,805),(627,806),(636,808),(638,813),(640,818),(642,824),(644,829),(646,835),(648,840),
                        (650,846),(652,851),(654,857),(656,862),(658,868),(660,873),(662,879),(664,884),(666,890)]
    # Put hood to screen
    if(princeOfWalesPosition[location] != (0,0)):
        if(location < 33):
            screen.blit(princeOfWalesDownLeft,princeOfWalesPosition[location])
        elif(location >= 33 and location <= 35):
            screen.blit(princeOfWalesLeft,princeOfWalesPosition[location])
        elif(location > 35 and location < 67):
            if(location == 66):
                screen.blit(princeOfWalesUpLeftFire,princeOfWalesPosition[location]) 
            else:
                screen.blit(princeOfWalesUpLeft,princeOfWalesPosition[location])   
            
        elif(location >= 67 and location < 83):
              screen.blit(princeOfWalesUpLeft,princeOfWalesPosition[location])

        elif(location >=83  and location < 86):
            if location == 84:
                screen.blit(princeOfWalesUpLeftHitFire,princeOfWalesPosition[location]) 
            else:  
                screen.blit(princeOfWalesUpLeftFire,princeOfWalesPosition[location])      
        elif(location >= 86 and location < 88):
            if location == 86:
                screen.blit(princeOfWalesUpLeftHitFire,princeOfWalesPosition[location]) 
            else:  
                screen.blit(princeOfWalesDownLeft,princeOfWalesPosition[location]) 
        elif(location >= 88 and location < 95):
            if(location == 89):
                screen.blit(princeOfWalesDownFire,princeOfWalesPosition[location])
            else:    
                screen.blit(princeOfWalesDown,princeOfWalesPosition[location])
        elif(location >= 95 and location < 100):
            screen.blit(princeOfWalesDownRight,princeOfWalesPosition[location])
        elif(location >= 100 and location < 105):
            screen.blit(princeOfWalesRight,princeOfWalesPosition[location])
        elif(location >= 105 ):
            screen.blit(princeOfWalesDownRight,princeOfWalesPosition[location])

# Norfolk Function
def Norfolk(location):
    # Load and set up ships
    nor1 = pygame.image.load('nor.ppm').convert()
    nor2 = pygame.image.load('nor1.ppm').convert()
    # Array of coordinates for ships
    NorfolkPosition = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(978,10),(972,16),(966,22),(960,28),(954,34),(948,40),(942,46),
                        (936,52),(930,58),(924,64),(918,70),(912,76),(906,82),(894,94),(888,100),(882,106),(876,112),
                        (870,118),(864,124),(858,130),(852,136),(846,142),(840,148),(834,154),(828,160),(822,166),(816,172),
                        (810,178),(804,184),(798,190),(792,196),(786,202),(780,208),(774,214),(768,220),(762,226)]
    # Put norfolk to screen
    if(NorfolkPosition[location] != (0,0)):
        screen.blit(nor1, (NorfolkPosition[location]))


# Suffolk Function
def Suffolk(location):
    # Load and set up ships
    suf1 = pygame.image.load('suf.ppm').convert()
    suf2 = pygame.image.load('suf1.ppm').convert()

    # Array of coordinates for ships
    SuffolkPosition = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(628,10),(622,16),(616,22),(610,28),(604,34)]
                        # Put ship to screen
    if(SuffolkPosition[location] != (0,0)):
        screen.blit(suf1, SuffolkPosition[location])

# Clock Function

def timeKeeper(location):
    time = ["05:20:00","05:20:30","05:21:00","05:21:30","05:22:00","05:22:30","05:23:00","05:23:30","05:24:00","05:24:30","05:25:00","05:25:30","05:26:00","05:26:30","05:27:00","05:27:30","05:28:00","05:28:30","05:29:00","05:29:30"
            ,"05:30:00","05:30:30","05:31:00","05:31:30","05:32:00","05:32:30","05:33:00","05:33:30","05:34:00","05:34:30","05:35:00","05:35:30","05:36:00","05:36:30","05:37:00","05:37:30","05:38:00","05:38:30","05:39:00","05:39:30"
            ,"05:40:00","05:40:30","05:41:00","05:41:30","05:42:00","05:42:30","05:43:00","05:43:30","05:44:00","05:44:30","05:45:00","05:45:30","05:46:00","05:46:30","05:47:00","05:47:30","05:48:00","05:48:30","05:49:00","05:49:30"
            ,"05:50:00","05:50:30","05:51:00","05:51:30","05:52:00","05:52:30","05:53:00","05:53:30","05:54:00","05:54:30","05:55:00","05:55:30","05:56:00","05:56:30","05:57:00","05:57:30","05:58:00","05:58:30","05:59:00","05:59:30"
            ,"06:00:00","06:00:30","06:01:00","06:01:30","06:02:00","06:02:30","06:03:00","06:03:30","06:04:00","06:04:30","06:05:00","06:05:30","06:06:00","06:06:30","06:07:00","06:07:30","06:08:00","06:08:30","06:09:00","06:09:30"
            ,"06:10:00","06:10:30","06:11:00","06:11:30","06:12:00","06:12:30","06:13:00","06:13:30","06:14:00","06:14:30","06:15:00","06:15:30","06:16:00","06:16:30","06:17:00","06:17:30","06:18:00","06:18:30","06:19:00","06:19:30"
            ,"06:20:00"]
    thisPhase = str(location)
    font = pygame.font.Font(None, 50)
    block = font.render(thisPhase, True, BLACK)
    text = font.render(time[location], True, WHITE)
    rect = block.get_rect()
    screen.blit(text, (950,250))


# Main Function

def main():
    done = False
    
    # Initialize the Iterator to 0 for the mouse click
    phase = 0
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or(event.type is KEYDOWN and event.key == K_ESCAPE):
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                phase+=1
            elif event.type is KEYDOWN and event.key == K_z:
                phase-=1    

        # Print the background image to the window
        screen.blit(background_image,background_position)
        
        # Outputs the clock
        timeKeeper(phase)

        # Calling the function to prints the images of the ship to the screen:
        bismark(phase)
        PofE(phase)
        Hood(phase)
        Norfolk(phase)
        Suffolk(phase)
        princeOfWales(phase)

        # Flips to display
        pygame.display.flip()
        clock.tick(60)

 
main() 
pygame.quit()
