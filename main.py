import pygame
from pygame.locals import *
from sys import exit
import pymysql

connection = pymysql.connect(
  host="localhost",
  user="root",
  passwd="",
  db="Register"
)

cursor = connection.cursor()


"""Verify if The User Exists"""
def verifyUser(user, usertype):
  if usertype == 'name':
    cursor.execute(f"SELECT * FROM users WHERE user = '{user}'")
    result = cursor.fetchall()
    if len(result) != 0:
      return True
    else:
      return False

  if usertype == 'email':
    cursor.execute(f"SELECT * FROM users WHERE email = '{user}'")
    result = cursor.fetchall()
    if len(result) != 0:
      return True
    else:
      return False


"""Verify if The Password is Correct"""
def verifyPassword(user, password, usertype):

  if usertype == "name":
    cursor.execute(f"SELECT password FROM users WHERE user = '{user}'")
    result = cursor.fetchall()
    if result[0][0] == password:
      return True
    else:
      return False
    
  if usertype == "email":
    cursor.execute(f"SELECT password FROM users WHERE email = '{user}'")
    result = cursor.fetchall()
    if result[0][0] == password:
      return True
    else:
      return False


"""Verify If The Email Already Exists"""
def verifyEmail(email):
    cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
    result = cursor.fetchall()
    if len(result) == 0:
        return True
    else:
        return False


def registeraUser(user, email, password):
    com_sql = "INSERT INTO users(user, email, password) VALUES (%s, %s, %s)"
    values = (user, email, password)
    cursor.execute(com_sql, values)
    connection.commit()


"""Essentials"""
pygame.init()
screen = pygame.display.set_mode((680, 540))
pygame.display.set_caption('Login Screen')

main = pygame.image.load('Main.png')
main = pygame.transform.scale(main, (365, 369))

login = pygame.image.load('Login Button.png')
login = pygame.transform.scale(login, (218, 36))

register = pygame.image.load('Register Button.png')
register = pygame.transform.scale(register, (140, 27))

font = pygame.font.SysFont("Arial", 16, False, False)
font2 = pygame.font.SysFont("Arial", 13, False, False)
font3 = pygame.font.SysFont("Arial", 13, False, False)
msg1 = "username"
msg2 = "password"
msg3 = "Por favor, preencha este campo."
msg4 = "Este nome de usuário não existe."
msg5 = "A senha está incorreta."
msg6 = "Este email não existe."
txt1 = font2.render(msg1, True, (166, 166, 166))
txt2 = font2.render(msg2, True, (166, 166, 166))
txt3 = font2.render(msg3, True, (219, 62, 62))
txt4 = font2.render(msg4, True, (219, 62, 62))
txt5 = font2.render(msg5, True, (219, 62, 62))
txt6 = font2.render(msg6, True, (219, 62, 62))

userwrite = False
passwordwrite = False

usererror1 = False
usererror2 = False
usererror3 = False
passworderror1 = False
passworderror2 = False
logged = False

user = ""
password = ""
fakepassword = ""

registerscreen = False

main2 = pygame.image.load('Main 2.png')
main2 = pygame.transform.scale(main2, (365, 412))

register2 = pygame.image.load('Register Button 2.png')
register2 = pygame.transform.scale(register2, (218, 39))

login2 = pygame.image.load('Login Button 2.png')
login2 = pygame.transform.scale(login2, (110, 27))

registered = pygame.image.load("Successfuly Registered.png")
registered = pygame.transform.scale(registered, (223, 120))

logged = pygame.image.load("Successfuly Logged.png")
logged = pygame.transform.scale(logged, (223, 120))

msg7 = "username"
msg8 = "e-mail"
msg9 = "password"
msg10 = "Por favor, preencha este campo."
msg11 = "Este nome é inválido."
msg12 = "Por favor, preencha este campo."
msg13 = "Este email é inválido."
msg14 = "Este email já está registrado."
msg15 = "Por favor, preencha este campo."
msg16 = "A senha deve ter no mínimo 8 digitos."
txt7 = font2.render(msg7, True, (166, 166, 166))
txt8 = font2.render(msg8, True, (166, 166, 166))
txt9 = font2.render(msg9, True, (166, 166, 166))
txt10 = font2.render(msg10, True, (219, 62, 62))
txt11 = font2.render(msg11, True, (219, 62, 62))
txt12 = font2.render(msg12, True, (219, 62, 62))
txt13 = font2.render(msg13, True, (219, 62, 62))
txt14 = font2.render(msg14, True, (219, 62, 62))
txt15 = font2.render(msg15, True, (219, 62, 62))
txt16 = font2.render(msg16, True, (219, 62, 62))

registeruserwrite = False
registeremailwrite = False
registerpasswordwrite = False

registeruser = ""
registeremail = ""
registerpassword = ""
registerfakepassword = ""

registerusererror1 = False
registerusererror2 = False
registeremailerror1 = False
registeremailerror2 = False
registeremailerror3 = False
registerpassworderror1 = False
registerpassworderror2 = False

registeredscreen = False

time = pygame.time.Clock()

loggedscreen = False
"""///"""

while True:
    """Essentials"""
    user = user.lstrip()
    password = password.lstrip()
    usertxt = font3.render(user, True, (30, 30, 30))
    passwordtxt = font3.render(fakepassword, True, (30, 30, 30))
    fakepasswordtxt = font3.render(fakepassword, True, (30, 30, 30))
    """///"""
  
    """Objects"""
    screen.fill((82, 231, 185))  #Background
    screen.blit(main, (157.5, 85.5))  #Main
    screen.blit(login, (231, 315))  #Login Button
    screen.blit(register, (270, 410))  #Register Button

    userinput = pygame.Rect(207, 188, 237, 34)  #User Input Area
    passwordinput = pygame.Rect(207, 252, 237, 34)  #Password Input Area
    loginarea = pygame.Rect(231, 315, 218, 36)  #Login Button Area
    registerarea = pygame.Rect(270, 410, 140, 27)  #Register Button Area
    """///"""
  
    """Texts"""
    if not userwrite and user.strip() == "":
        screen.blit(txt1, (214, 196))

    if not passwordwrite and password.strip() == "":
        screen.blit(txt2, (214, 260))

  
    if usererror1:  #User Empty
        screen.blit(txt3, (235, 225))
    if usererror2:  #User Doesn't Exist (Name)
        screen.blit(txt4, (235, 225))
    if usererror3: #User Doesn't Exist (Email)
        screen.blit(txt6, (265, 225))

    if passworderror1:  #Password Empty
        screen.blit(txt3, (230, 289))
    if passworderror2:  #Password Incorrect
        screen.blit(txt5, (265, 289))

    
    screen.blit(usertxt, (214, 197))  #User
    screen.blit(fakepasswordtxt, (214, 261))  #Fake Password
    """///"""

    for event in pygame.event.get():  #Functions
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if userinput.collidepoint(pos):
                userwrite = True  #Hide "username"
            else:
                userwrite = False  #Show "username"

            if passwordinput.collidepoint(pos):
                passwordwrite = True  #Hide "password"
            else:
                passwordwrite = False  #Show "password"

            """Submit With Mouse"""
            if loginarea.collidepoint(pos):

                #Clear Every Errors In The Screen
                userwrite = False
                passwordwrite = False
                usererror1 = False
                usererror2 = False
                usererror3 = False
                passworderror1 = False
                passworderror2 = False
                usertype = None

                #Remove The Don't Necessary Spaces
                user = user.strip()
                password = password.strip()

                #Verify if The User Is Email Or Name
                if '@' in user:
                    usersplit = user.split('@')
                    if ".com" in usersplit[1]:
                        usertype = 'email'
                    else:
                        usertype = 'nane'
                else:
                    usertype = 'name'

                #Errors
                if user == "":
                    usererror1 = True
                    if password == "":
                        passworderror1 = True
                    else:
                        passworderror2 = True

                else:

                    #Verify If The User Exists
                    vuser = verifyUser(user, usertype)

                    if vuser:
                        if password == "":
                            passworderror1 = True
                        else:

                            #Verify If The Password It's Correct
                            vpassword = verifyPassword(user, password, usertype)
                            if vpassword:
                                loggedscreen = True
                            else:
                                passworderror2 = True

                    #Errors
                    else:
                        if usertype == "name":
                            usererror2 = True

                            if password == "":
                                passworderror1 = True
                            else:
                                passworderror2 = True

                        elif usertype == "email":
                            usererror3 = True

                            if password == "":
                                passworderror1 = True
                            else:
                                passworderror2 = True
                    
                if password == "":
                    passworderror1 = True

                #Clean The Texts
                if not usererror1 and not usererror2 and not usererror3 and not passworderror1 and not passworderror2:
                    user = ""
                    password = ""
                    fakepassword = ""
            """///"""

            if registerarea.collidepoint(pos):  #Switch To Register
                userwrite = False
                passwordwrite = False
                usererror1 = False
                usererror2 = False
                usererror3 = False
                passworderror1 = False
                passworderror2 = False
                usertype = None
                user = ""
                password = ""
                fakepassword = ""
                registerscreen = True

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                userwrite = False
                passwordwrite = False

            """Submit With Keyboard"""
            if event.key == K_RETURN:

                #Clear Every Errors In The Screen
                userwrite = False
                passwordwrite = False
                usererror1 = False
                usererror2 = False
                usererror3 = False
                passworderror1 = False
                passworderror2 = False
                usertype = None

                #Remove The Don't Necessary Spaces
                user = user.strip()
                password = password.strip()

                #Verify if The User Is Email Or Name
                if '@' in user:
                    usersplit = user.split('@')
                    if ".com" in usersplit[1]:
                        usertype = 'email'
                    else:
                        usertype = 'nane'
                else:
                    usertype = 'name'

                #Errors
                if user == "":
                    usererror1 = True
                    if password == "":
                        passworderror1 = True
                    else:
                        passworderror2 = True

                else:

                    #Verify If The User Exists
                    vuser = verifyUser(user, usertype)

                    if vuser:
                        if password == "":
                            passworderror1 = True
                        else:

                            #Verify If The Password It's Correct
                            vpassword = verifyPassword(user, password, usertype)
                            if vpassword:
                                loggedscreen = True
                            else:
                                passworderror2 = True

                    #Errors
                    else:
                        if usertype == "name":
                            usererror2 = True

                            if password == "":
                                passworderror1 = True
                            else:
                                passworderror2 = True

                        elif usertype == "email":
                            usererror3 = True

                            if password == "":
                                passworderror1 = True
                            else:
                                passworderror2 = True
                    
                if password == "":
                    passworderror1 = True

                #Clean The Texts
                if not usererror1 and not usererror2 and not usererror3 and not passworderror1 and not passworderror2:
                    user = ""
                    password = ""
                    fakepassword = ""
            """///"""
            
            """Write"""
            if userwrite:
                if event.key == K_BACKSPACE:  #Eraese
                    user = user[:-1]

                elif usertxt.get_width() <= 210: #Only Write In This Range
                    user += event.unicode

            if passwordwrite:
                if event.key == K_BACKSPACE:  #Erase
                    password = password[:-1]
                    fakepassword = fakepassword[:-1]
                
                elif passwordtxt.get_width() <= 210: #Only Write In This Range

                    password += event.unicode
                    password = password.lstrip()

                    #Make The Fakepassword Regulate With The Password
                    if len(password) != len(fakepassword):
                        if len(password) > len(fakepassword):
                            fakepassword += "*"
                        if len(password) < len(fakepassword):
                            fakepassword = fakepassword[:-1]
            """///"""

    pygame.display.update()

    if registerscreen:
        while True:
            """Essentials"""
            registeruser = registeruser.lstrip()
            registeremail = registeremail.lstrip()
            registerpassword = registerpassword.lstrip()

            registerusertxt = font3.render(registeruser, True, (30, 30, 30))
            registeremailtxt = font3.render(registeremail, True, (30, 30, 30))
            registerpasswordtxt = font3.render(registerpassword, True, (30, 30, 30))
            registerfakepasswordtxt = font3.render(registerfakepassword, True, (30, 30, 30))
            """///"""

            """Objects"""
            screen.fill((82, 231, 185))  #Background
            screen.blit(main2, (157.5, 64))  #Main
            screen.blit(register2, (231, 336.5)) #Register Button
            screen.blit(login2, (285, 431.5)) #Login Button

            registeruserinput = pygame.Rect(201, 141, 234, 34) #User Input Area
            registeremailinput = pygame.Rect(201, 204.5, 234, 34) #Email Input Area
            registerpasswordinput = pygame.Rect(201, 268, 234, 34) #Password Input Area
            registerarea2 = pygame.Rect(235, 336.5, 211, 36) #Register Button Area
            loginarea2 = pygame.Rect(285, 431.5, 110, 27) #Login Button Area
            """///"""

            """Texts"""
            if not registeruserwrite and registeruser == "":
                screen.blit(txt7, (208, 149))

            if not registeremailwrite and registeremail == "":
                screen.blit(txt8, (208, 213.5))

            if not registerpasswordwrite and registerpassword == "":
                screen.blit(txt9, (208, 277))
            
            if registerusererror1: #User Empty
                screen.blit(txt10, (238, 178))
            if registerusererror2: #User Invalid
                screen.blit(txt11, (272, 178))        
            if registeremailerror1: #Email Empty
                screen.blit(txt12, (238, 241.5))
            if registeremailerror2: #Email Invalid
                screen.blit(txt13, (270, 241.5))
            if registeremailerror3: #Email Already Exists
                screen.blit(txt14, (248, 241.5))   
            if registerpassworderror1: #Password Empty
                screen.blit(txt15, (238, 305))
            if registerpassworderror2: #Minimun 8 Characters
                screen.blit(txt16, (222, 305))
            
            screen.blit(registerusertxt, (208, 150)) #User
            screen.blit(registeremailtxt, (208, 214.5)) #Email
            screen.blit(registerfakepasswordtxt, (208, 278)) #Fake Password
            """///"""

            for event in pygame.event.get(): #Functions
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    if registeruserinput.collidepoint(pos):
                        registeruserwrite = True #Show "username"
                    else:
                        registeruserwrite = False #Hide "username"
                    
                    if registeremailinput.collidepoint(pos):
                        registeremailwrite = True #Show "email"
                    else:
                        registeremailwrite = False #Hide "email"
                    
                    if registerpasswordinput.collidepoint(pos):
                        registerpasswordwrite = True #Show "password"
                    else:
                        registerpasswordwrite = False #Hide "password"
                    
                    """Submit With Mouse"""
                    if registerarea2.collidepoint(pos):

                        #Clear Every Errors In The Screen
                        registerusererror1 = False
                        registerusererror2 = False
                        registeremailerror1 = False
                        registeremailerror2 = False
                        registeremailerror3 = False
                        registerpassworderror1 = False
                        registerpassworderror2 = False
                        registeruserwrite = False
                        registeremailwrite = False
                        registerpasswordwrite = False
                        
                        #Remove The Don't Necessary Spaces
                        registeruser = registeruser.strip()
                        registeremail = registeremail.strip()
                        registerpassword = registerpassword.strip()

                        #Errors
                        if registeruser == "":
                            registerusererror1 = True
                        else:
                            if "@" in registeruser or "!" in registeruser or "#" in registeruser or "$" in registeruser or "%" in registeruser or "&" in registeruser or "*" in registeruser or "%" in registeruser or "{" in registeruser or "}" in registeruser or "[" in registeruser or "]" in registeruser or "(" in registeruser or ")" in registeruser or "+" in registeruser or "=" in registeruser or "'" in registeruser or '"' in registeruser or "`" in registeruser or "´" in registeruser or "|" in registeruser or "/" in registeruser or "?" in registeruser or ":" in registeruser or ";" in registeruser or "ª" in registeruser or "º" in registeruser or "^" in registeruser or "~" in registeruser or "¨" in registeruser or "¬" in registeruser or "§" in registeruser or "°" in registeruser or "₢" in registeruser or "<" in registeruser or ">" in registeruser or "," in registeruser or "." in registeruser or "²" in registeruser or "³" in registeruser or "£" in registeruser or "¢" in registeruser:
                                registerusererror2 = True
                        
                        if registeremail == "":
                            registeremailerror1 = True
                        else:
                            if "@" in registeremail:
                                registeremailsplit = registeremail.split("@")
                                if ".com" in registeremailsplit[1]:
                                    vemail = verifyEmail(registeremail)
                                    if vemail:
                                        pass
                                    else:
                                        registeremailerror3 = True
                                else:
                                    registeremailerror2 = True
                            else:
                                registeremailerror2 = True
                        
                        if registerpassword == "":
                            registerpassworderror1 = True
                        else:
                            if len(registerpassword) < 8:
                                registerpassworderror2 = True
                        
                        #Submit The Register, Clear Texts And Open Registered Screen
                        if not registerusererror1 and not registerusererror2 and not registeremailerror1 and not registeremailerror2 and not registeremailerror3 and not registerpassworderror1 and not registerpassworderror2:
                            registeraUser(registeruser, registeremail, registerpassword)
                            registeruser = ""
                            registeremail = ""
                            registerpassword = ""
                            registerfakepassword = ""
                            registeredscreen = True
                    """///"""

                    if loginarea2.collidepoint(pos): #Switch To Login
                        registerusererror1 = False
                        registerusererror2 = False
                        registeremailerror1 = False
                        registeremailerror2 = False
                        registeremailerror3 = False
                        registerpassworderror1 = False
                        registerpassworderror2 = False
                        registeruserwrite = False
                        registeremailwrite = False
                        registerpasswordwrite = False
                        registerscreen = False
                        registeruser = ""
                        registeremail = ""
                        registerpassword = ""
                        registerfakepassword = ""
                
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE: #Esc
                        registeruserwrite = False
                        registeremailwrite = False
                        registerpasswordwrite = False
                    
                    """Submit With Keyboard"""
                    if event.key == K_RETURN:

                        #Clear Every Errors In The Screen
                        registerusererror1 = False
                        registerusererror2 = False
                        registeremailerror1 = False
                        registeremailerror2 = False
                        registeremailerror3 = False
                        registerpassworderror1 = False
                        registerpassworderror2 = False
                        registeruserwrite = False
                        registeremailwrite = False
                        registerpasswordwrite = False
                        
                        #Remove The Don't Necessary Spaces
                        registeruser = registeruser.strip()
                        registeremail = registeremail.strip()
                        registerpassword = registerpassword.strip()

                        #Errors
                        if registeruser == "":
                            registerusererror1 = True
                        else:
                            if "@" in registeruser or "!" in registeruser or "#" in registeruser or "$" in registeruser or "%" in registeruser or "&" in registeruser or "*" in registeruser or "%" in registeruser or "{" in registeruser or "}" in registeruser or "[" in registeruser or "]" in registeruser or "(" in registeruser or ")" in registeruser or "+" in registeruser or "=" in registeruser or "'" in registeruser or '"' in registeruser or "`" in registeruser or "´" in registeruser or "|" in registeruser or "/" in registeruser or "?" in registeruser or ":" in registeruser or ";" in registeruser or "ª" in registeruser or "º" in registeruser or "^" in registeruser or "~" in registeruser or "¨" in registeruser or "¬" in registeruser or "§" in registeruser or "°" in registeruser or "₢" in registeruser or "<" in registeruser or ">" in registeruser or "," in registeruser or "." in registeruser or "²" in registeruser or "³" in registeruser or "£" in registeruser or "¢" in registeruser:
                                registerusererror2 = True
                        
                        if registeremail == "":
                            registeremailerror1 = True
                        else:
                            if "@" in registeremail:
                                registeremailsplit = registeremail.split("@")
                                if ".com" in registeremailsplit[1]:
                                    vemail = verifyEmail(registeremail)
                                    if vemail:
                                        pass
                                    else:
                                        registeremailerror3 = True
                                else:
                                    registeremailerror2 = True
                            else:
                                registeremailerror2 = True
                        
                        if registerpassword == "":
                            registerpassworderror1 = True
                        else:
                            if len(registerpassword) < 8:
                                registerpassworderror2 = True
                        
                        #Submit The Register, Clear Texts And Open Registered Screen
                        if not registerusererror1 and not registerusererror2 and not registeremailerror1 and not registeremailerror2 and not registeremailerror3 and not registerpassworderror1 and not registerpassworderror2:
                            registeraUser(registeruser, registeremail, registerpassword)
                            registeruser = ""
                            registeremail = ""
                            registerpassword = ""
                            registerfakepassword = ""
                            registeredscreen = True
                    """///"""

                    """Write"""
                    if registeruserwrite:
                        if event.key == K_BACKSPACE: #Erase
                            registeruser = registeruser[:-1]
                        
                        elif registerusertxt.get_width() <= 210: #Only Write In This Range
                            registeruser += event.unicode
                            registeruser = registeruser.lstrip()

                    if registeremailwrite:
                        if event.key == K_BACKSPACE: #Erase
                            registeremail = registeremail[:-1]
                        
                        elif registeremailtxt.get_width() <= 210: #Only Write In This Range
                            registeremail += event.unicode
                            registeremail = registeremail.lstrip()
                    
                    if registerpasswordwrite:
                        if event.key == K_BACKSPACE: #Erase
                            registerpassword = registerpassword[:-1]
                            registerfakepassword = registerfakepassword[:-1]
                        
                        elif registerpasswordtxt.get_width() <= 210: #Only Write In This Range
                            registerpassword += event.unicode
                            registerpassword = registerpassword.lstrip()
                        
                            #Make The Fakepassword Regulate With The Password
                            if len(registerpassword) != len(registerfakepassword):
                                if len(registerpassword) > len(registerfakepassword):
                                    registerfakepassword += "*"
                                if len(registerpassword) < len(registerfakepassword):
                                    registerfakepassword = registerfakepassword[:-1]
                    """///"""

            pygame.display.update()

            if not registerscreen:
                break
            
            if registeredscreen:
                registeredscreenlinewidth = 215
                while True:
                    """Essentials"""
                    time.tick(35)
                    """///"""

                    """Objects"""
                    screen.blit(registered, (228.5, 210)) #Main
                    pygame.draw.rect(screen, (143, 207, 227), (232.5, 276, registeredscreenlinewidth, 5)) #Line Of Time
                    confirmarea = pygame.Rect(301, 291, 75, 32) #OK Button Area
                    """///"""

                    #Make The Line Decrease
                    if registeredscreenlinewidth != 0:
                        registeredscreenlinewidth -= 1

                    if registeredscreenlinewidth == 0: #Switch To Register
                        registeredscreen = False

                    for event in pygame.event.get(): #Functions
                        if event.type == QUIT:
                            pygame.quit()
                            exit()
                        
                        if event.type == MOUSEBUTTONDOWN:
                            pos = pygame.mouse.get_pos()

                            if confirmarea.collidepoint(pos): #Switch To Register
                                registeredscreen = False
                        
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE or event.key == K_RETURN: #Switch To Register
                                registeredscreen = False

                    pygame.display.update()

                    if not registeredscreen:
                        break

    if loggedscreen:
        loggedscreenlinewidth = 215
        while True:
            """Essentials"""
            time.tick(35)
            """///"""

            """Objects"""
            screen.blit(logged, (228.5, 210)) #Main
            pygame.draw.rect(screen, (143, 207, 227), (232.5, 276, loggedscreenlinewidth, 5)) #Line Of Time
            confirmarea = pygame.Rect(301, 291, 75, 32) #OK Button Area
            """///"""

            #Make The Line Decrease
            if loggedscreenlinewidth != 0:
                loggedscreenlinewidth -= 1

            if loggedscreenlinewidth == 0: #Switch To Login
                loggedscreen = False

            for event in pygame.event.get(): #Functions
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    if confirmarea.collidepoint(pos): #Switch To Login
                        loggedscreen = False
                
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE or event.key == K_RETURN: #Switch To Login
                        loggedscreen = False

            pygame.display.update()

            if not loggedscreen:
                break