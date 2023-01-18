import pygame
import os #importing the operating system library which will help us define the path to the folders.
    
#initializing 
pygame.init() # Required by most pygame applications


#defining colours
WHITE=(255,255,255)
RED=(255,0,0)
YELLOW=(255,255,0)
LINE_COLOR=(50,200,220)

#dimensions
WIDTH, HEIGHT= 900, 600
SHIP_WIDTH, SHIP_HEIGHT= WIDTH//18, HEIGHT//20

VEL=WIDTH/180 #the speed of the spaceships
    

    
BULLET_VEL=WIDTH/180 #the speed of the bullets
BULLET_DIM=WIDTH/180 #dimension of the bullets
MAX_BULLETS=3 #maximum number of bullets allowed


FPS=60 # we do not want the game to run with different speeds on different computers so we define a frame per second constant
text=""


#draw_first_window #main surface drawing
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')#this does not need updating.
BG=pygame.image.load("Assets/space.png")
BG=pygame.transform.scale(BG, (WIDTH,HEIGHT))
SURFACE.blit(BG,(0,0))
# BG_COLOR=(60,160,155)
# SURFACE.fill(BG_COLOR)
pygame.draw.line(SURFACE, LINE_COLOR, (WIDTH//2, 0), (WIDTH//2, HEIGHT), WIDTH//90)

#draw the spaceships
#YELLOW_SPACESHIP=pygame.image.load("Assets/spaceship_yellow.png")
#RED_SPACESHIP=pygame.image.load("Assets/spaceship_red.png")
YELLOW_SPACESHIP=pygame.image.load(os.path.join("Assets","spaceship_yellow.png")) #image.load allows the pygame to load the image for it to be used on the surface.
RED_SPACESHIP=pygame.image.load(os.path.join("Assets","spaceship_red.png"))
#depending on what operating system we are on the directory separator might be different so OS will handle that for us.
#when the image or text is loaded to pygame they are known as surfaces so we have to use blit command.




YELLOW_SPACESHIP=pygame.transform.scale(YELLOW_SPACESHIP,(SHIP_WIDTH,SHIP_HEIGHT))#rescaling our image 
RED_SPACESHIP=pygame.transform.scale(RED_SPACESHIP,(SHIP_WIDTH,SHIP_HEIGHT))

YELLOW_SPACESHIP=pygame.transform.rotate(YELLOW_SPACESHIP,90)#rotating the image counter clock wise by 90 degrees.
RED_SPACESHIP=pygame.transform.rotate(RED_SPACESHIP,270)


SURFACE.blit (YELLOW_SPACESHIP, (WIDTH//5,HEIGHT//2)) #whenever you want to put surfaces that is text or images on your screen use this command.
#argument one is the image, argument two is the tuple containing the coordinates. surface.blit (the surface is the variable of the display we defined)
SURFACE.blit (RED_SPACESHIP, ((4*WIDTH)//5,HEIGHT//2))

#defining rectangles for changing the position of our scpaceship. the reason we use rectangles is that pygame has methods that can be used to modify the rectangle position. thus modify the position of the object.
yellow_rect=pygame.Rect(WIDTH//5,HEIGHT//2,SHIP_WIDTH,SHIP_HEIGHT) #ship_width and ship_height do not matter for movement but matter for collision. for only movement purpose they can be defined as 1,1 or any random numbers.
red_rect=pygame.Rect((4*WIDTH)//5,HEIGHT//2, SHIP_WIDTH, SHIP_HEIGHT)

#creating the fonts
text_font = pygame.font.Font('freesansbold.ttf', 20) 
win_font=pygame.font.Font('freesansbold.ttf', 40) 

pygame.display.update()


def draw_update_window(SURFACE, YH, RH, YELLOW_LIST_BULLET, RED_LIST_BULLET, YELLOW_HEALTH,RED_HEALTH):
    
    
    SURFACE.blit(BG,(0,0))
    pygame.draw.line(SURFACE, LINE_COLOR, (WIDTH//2, 0), (WIDTH//2, HEIGHT), WIDTH//90)
    #pygame.draw.rect(SURFACE, COLOUR, REC). where REC=pygame.RECT(....) draws a rectangle on top of the surface. 
    #changing yellow_ract.x to ++100 only changes the starting point. 
    SURFACE.blit (YELLOW_SPACESHIP, (yellow_rect.x,yellow_rect.y)) #whenever you want to put surfaces that is text or images on your screen use this command.
    #argument one is the image, argument two is the tuple containing the coordinates. surface.blit (the surface is the variable of the display we defined)
    SURFACE.blit (RED_SPACESHIP, (red_rect.x,red_rect.y))
    
    #in one frame all the bullets need to be shown.
    for bullets in YELLOW_LIST_BULLET:
        pygame.draw.rect(SURFACE,YELLOW,bullets)
        
    for bullets in RED_LIST_BULLET:
        pygame.draw.rect(SURFACE,RED,bullets)
    
    YH = text_font.render("YELLOW HEALTH: " + str(YELLOW_HEALTH), True, WHITE)
    RH = text_font.render("RED HEALTH: "+ str(RED_HEALTH), True, WHITE)
    SURFACE.blit (YH, (10,10))
    SURFACE.blit (RH, (WIDTH-160,10))

        
    pygame.display.update()
    
        
    
    
def key(keys_pressed, yellow_rect, red_rect): #if I want to change a parameter inside a function even if the parameter is global I have to put it as an argument. If I want to just print it I do not need to put it as an argument. 
    if keys_pressed[pygame.K_w]:
        if 0<=yellow_rect.y-VEL:
            yellow_rect.y-=VEL
                
    if keys_pressed[pygame.K_s]:
        if yellow_rect.y+SHIP_HEIGHT+VEL+30<=HEIGHT:
            yellow_rect.y+=VEL
        
    if keys_pressed[pygame.K_d]:
        if yellow_rect.x+SHIP_WIDTH+VEL-20<=WIDTH//2:
            yellow_rect.x+=VEL
                
    if keys_pressed[pygame.K_a]:
        if 0<=yellow_rect.x-VEL:
            yellow_rect.x-=VEL
        
    if keys_pressed[pygame.K_UP]:
        if 0<=red_rect.y-VEL:
            red_rect.y-=VEL
                
    if keys_pressed[pygame.K_DOWN]:
        if red_rect.y+SHIP_HEIGHT+VEL+30<=HEIGHT:
            red_rect.y+=VEL
        
    if keys_pressed[pygame.K_RIGHT]:
        if red_rect.x+SHIP_WIDTH+VEL-20<=WIDTH:
            red_rect.x+=VEL
                
    if keys_pressed[pygame.K_LEFT]:
        if WIDTH//2<=red_rect.x-VEL:
            red_rect.x-=VEL

def game():

    
    #because the below are changed in the lopp I have defined them inside the main function so that I do not need to put them as arguments.
    RED_LIST_BULLET=[]
    YELLOW_LIST_BULLET=[]
    #defining the healths
    RED_HEALTH=5
    YELLOW_HEALTH=5
    
    #creating a new even in pygame is like below:(pygame.USEREVENT is like a number and because we have multiple users we need to create multiple distinctive events)
    YELLOW_HIT=pygame.USEREVENT+1
    RED_HIT=pygame.USEREVENT+2
    #default events are defined above.
    
    #last part of initializing
    YH = text_font.render("YELLOW HEALTH: " + str(YELLOW_HEALTH), True, WHITE)
    RH = text_font.render("RED HEALTH: "+ str(RED_HEALTH), True, WHITE)

    SURFACE.blit (YH, (10,10))
    SURFACE.blit (RH, (WIDTH-70,10))
    pygame.display.update()
    
    clock=pygame.time.Clock() #creating clock object (instance)

    #main loop which runs the events of the game. 
    running = True
    while running:
        
        clock.tick(FPS) # this makes our main event loop of the computer run 60 times per second. it is controllable consistent and in all computers the game speed will be similar unless the computer cannot keep up with the speed and it will go on the maximum speed. it can. but 60 FPS is a good rate.
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #every program needs a termination event defined. the x 
                print('ReceivedQuitEvent:', event)
                #running=False
                pygame.quit()
            
              #the problem with the below is that it gets keys pressed one at a time that is multiple keys pressed at time will not be carried out simultaneously but rather in a queu and in order.
              #another problem it has we cannot apply that as long as the key is pressed down move up. Here each time we want to move up we have to press w again.
            
#             if event.type==pygame.KEYDOWN:
#                 if event.key==pygame.K_w:
                    
#                     yellow_rect.y-=1 #this indicates a movement of 60 pixels per second because FPS is 60 that is the loop is running 60 times a second. 
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f and len(YELLOW_LIST_BULLET)<MAX_BULLETS:
                    yellow_bullet_rect=pygame.Rect(yellow_rect.x+SHIP_WIDTH-3,yellow_rect.y+SHIP_HEIGHT//2, BULLET_DIM,BULLET_DIM)
                    YELLOW_LIST_BULLET.append(yellow_bullet_rect)

                if event.key == pygame.K_SPACE and len(RED_LIST_BULLET)<MAX_BULLETS:
                    red_bullet_rect=pygame.Rect(red_rect.x,red_rect.y+SHIP_HEIGHT//2, BULLET_DIM,BULLET_DIM)
                    RED_LIST_BULLET.append(red_bullet_rect)
                    
            if event.type==RED_HIT:
                RED_HEALTH-=1
                if RED_HEALTH==0:
                    text="YELLOW WON"
                    draw_update_window(SURFACE, YH, RH, YELLOW_LIST_BULLET, RED_LIST_BULLET, YELLOW_HEALTH,RED_HEALTH)
                    WINNER = win_font.render(text, True, WHITE)
                    SURFACE.blit (WINNER, (WIDTH//2-WINNER.get_width()//2, HEIGHT//2-WINNER.get_height()//2))
                    pygame.display.update()
                    pygame.time.delay(5000)
                    running=False

                
            if event.type==YELLOW_HIT:
                YELLOW_HEALTH-=1
                if YELLOW_HEALTH==0:
                    text="RED_WON"
                    draw_update_window(SURFACE, YH, RH, YELLOW_LIST_BULLET, RED_LIST_BULLET, YELLOW_HEALTH,RED_HEALTH)
                    WINNER = win_font.render(text, True, WHITE)
                    SURFACE.blit (WINNER, (WIDTH//2-WINNER.get_width()//2, HEIGHT//2-WINNER.get_height()//2))
                    pygame.display.update()
                    pygame.time.delay(5000)
                    running=False
                    


        
    
    
        keys_pressed=pygame.key.get_pressed()#this allows us to click multiple keys simultaneously and as long as the key is pressed it moves so we dont have to click again
        key(keys_pressed, yellow_rect, red_rect)
                
        #taqirat inja sabt mishan hamananad bala dar loop running
        for bullets in YELLOW_LIST_BULLET:
            bullets.x+=BULLET_VEL
            if red_rect.colliderect(bullets):
                pygame.event.post(pygame.event.Event(RED_HIT))#posting the new event. when posting the event it goes into the event list: pygame.event.get(): so if you use if statement and call your posted event for an action it can carry it out.
                YELLOW_LIST_BULLET.remove(bullets)
            elif yellow_bullet_rect.x>WIDTH:
                YELLOW_LIST_BULLET.remove(bullets)
            
        for bullets in RED_LIST_BULLET:
            bullets.x-=BULLET_VEL
            if yellow_rect.colliderect(bullets):
                pygame.event.post(pygame.event.Event(YELLOW_HIT))#posting the new event
                RED_LIST_BULLET.remove(bullets)
            elif red_bullet_rect.x<0:
                RED_LIST_BULLET.remove(bullets)
 
        
        draw_update_window(SURFACE, YH, RH, YELLOW_LIST_BULLET, RED_LIST_BULLET, YELLOW_HEALTH,RED_HEALTH)
        
        
    #restart automatically but be aware you need to put the pygame.quit somewhere for termination. 
    game()
    #pygame.quit()
    




    
#this line says that if this file has been imported to another python module do not run the game.
#in other words only run the game if the file was run under the "main" file that is the file that the code was written in. 
if __name__=="__main__":
    game()