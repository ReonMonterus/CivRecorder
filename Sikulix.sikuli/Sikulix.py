import shutil
import os
import glob
load("C:\\Users\\weath\\Downloads\\sqlite-jdbc-3.23.1.jar")
from com.ziclix.python.sql import zxJDBC

def turn_processing(civgame, OBS):
    #Civ V popup handing
    if exists("1536089769203.png"):
        click("1536089769203.png")
    elif exists("1536090373974.png"):
        click("1536090373974.png")
    elif exists("1536090913714.png"):
        click("1536090913714.png")
    elif exists("1551291437192.png"):
        click("1551291437192.png")
    else:
        turn = turn_getter() #get the turn
        print "turn processing"
        map_screen_shotter() #take some screenshots
        if turn % 10 == 0 and turn > 20:
            addl_info_shotter() #every 10 turns screenshot religion and cities info
        recording_stopper(OBS)
        wait(10)
        file_processor()
        OBS = recording_initializer() #start recording again after taking screenshots after turn 30
        #try to find the next turn button. sometimes fails so we kick out of the loop and try again if it does
        try:
            print "next turn"
            click("1536087253968.png")
            #hover(civgame.window().getBottomRight().offset(-30,-30))
            hover(Region(0,0,1780,1100).getBottomRight())
        except:
            return

def test_processing(civgame):
    #Civ V popup handing
    if exists("1536089769203.png"):
        click("1536089769203.png")
    elif exists("1536090373974.png"):
        click("1536090373974.png")
    elif exists("1536090913714.png"):
        click("1536090913714.png")
    elif exists("1551291437192.png"):
        click("1551291437192.png")
    else:
        turn = turn_getter() #get the turn
        print "turn processing"
        #map_screen_shotter() #take some screenshots
#        if turn % 10 == 0 and turn > 20:
#            addl_info_shotter() #every 10 turns screenshot religion and cities info
        wait(10)
#        file_processor()
        #try to find the next turn button. sometimes fails so we kick out of the loop and try again if it does
        try:
            print "next turn"
            click("1536087253968.png")
            #hover(civgame.window().getBottomRight().offset(-30,-30))
            hover(Region(0,0,1780,1100).getBottomRight())
        except:
            return


def turn_waiter(civgame, OBS):
    while appActive("CivilizationV_DX11.exe"):
        #wait while the turn processes
        buttonRegion = Region(1574,894,336,54) 
        wait(30)
        if not appActive("CivilizationV_DX11.exe"):
            print "Game crashed in while loop"
            return None
        while not exists("1536087253968.png") and appActive("CivilizationV_DX11.exe"):
            wait(10)
            if exists("1550604767883.png"):
                click("1550604767883.png")
                wait(2)
                while not exists("1550604816256.png") and appActive("CivilizationV_DX11.exe"):
                    wait(5)
                click("1550604816256.png")
                wait(1)
                click("1550604837734.png")    
        else:
            try:
                if appActive("CivilizationV_DX11.exe"):
                    turn_processing(civgame,OBS) #after next turn appears, call the turn processing
                    print "turn processed"
                    #hover(civgame.window().getBottomRight().offset(-30,-30))
                    hover(Region(0,0,1780,1100).getBottomRight())
            except:
                print "turn failed, return None"
                return None
            try:
                hover(Region(0,0,1780,1100).getBottomRight())
            except:
                print "hover failed"
            print "Waiter While loop end"
    print "while failed" 
    return None

def test_waiter(civgame):
    while appActive("CivilizationV_DX11.exe"):
        #wait while the turn processes
        buttonRegion = Region(1574,894,336,54) 
        wait(30)
        if not appActive("CivilizationV_DX11.exe"):
            print "Game crashed in while loop"
            return None
        while not exists("1536087253968.png") and appActive("CivilizationV_DX11.exe"):
            wait(10)
            if exists("1550604767883.png"):
                click("1550604767883.png")
                wait(2)
                while not exists("1550604816256.png") and appActive("CivilizationV_DX11.exe"):
                    wait(5)
                click("1550604816256.png")
                wait(1)
                click("1550604837734.png")    
        else:
            try:
                if appActive("CivilizationV_DX11.exe"):
                    test_processing(civgame) #after next turn appears, call the turn processing
                    print "turn processed"
                    #hover(civgame.window().getBottomRight().offset(-30,-30))
                    hover(Region(0,0,1780,1100).getBottomRight())
            except:
                print "turn failed, return None"
                return None
            try:
                hover(Region(0,0,1780,1100).getBottomRight())
            except:
                print "hover failed"
            print "Waiter While loop end"
    print "while failed" 
    return None

def map_screen_shotter():
    minimapRegion = Region(1580,901,329,210)
    ssoffsetx = -150 #starting offsets
    ssoffsety = 60
    turn = turn_getter()
    print "taking screenshots"
    #take screenshots with steams F12 keybind. loop through the map
    while ssoffsety < 195:
        ssoffsetx = -150
        while ssoffsetx < 190:
            click(minimapRegion.find("1536087253968.png").offset(ssoffsetx,ssoffsety))
            wait(2)
#            type(Key.F12)
            ssoffsetx += 15
        ssoffsety += 24        
    
    
def recording_initializer():
    OBS = App("OBS")
    try:
        if not OBS.window():
            OBS.open("C:\\Users\\weath\\OneDrive\\Documents\\obs.bat")
            wait(5)
            print "OBS Opened"
        else:
            print "OBS already open"
        OBS.focus() #focus on OBS
        click(find("1569046487219.png"))
        click(find("1569046525675.png"))
        return OBS
    except:
        print "Recording init error"
        return #if the above fails, abandon ship

def recording_stopper(OBS):
    #Processing the stopping of recording
    try:
        #if OBS.window():
#           OBS.focus()
#           click(find("1539302248946.png"))
        OBS.close()            
        print "stopped recording"
        return OBS
    except:
        print "recording stop error"
        return "recording stop error"

def recording_starter(OBS):
    #independent processing of the starting of recording
    try:
        if OBS.window():
            OBS.focus()
            click(find("1541843460948.png").offset(0,40))
            print "started recording"
            return OBS
    except:
        print "recording start error"
        return "recording start error"
                    
        
def game_restarter(started):
    CivV = App("CivilizationV")
    turn = turn_getter()
    try:
        if not started:
            CivV.open("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Sid Meier's Civilization V\\CivilizationV_DX11.exe")
            wait(30)
            click("1589037799223.png")
            wait(10)
            while not exists("1537682070546.png") and appActive("CivilizationV_DX11.exe"):
                wait(10)
            else:
                if exists("1537682070546.png"):
                    wait(10)
                    click("1537682070546.png") #initial prompt
                else:
                    print "Game crash, restart"
                    return None
            wait(1)
            click("1537682089185.png") #mods menu
            wait(1)
            click("1537682120561.png") #accept terms
            wait(1)
            click("1537682143489.png") #mod selection
            wait(60)
            click("1537682222024.png") #single player menu
            wait(1)
            click("1537682237784.png") #load menu
            wait(1)
            click("1537682252680.png") #select autosaves
            wait(1)
            click(find("1537690445225.png").offset(0,90)) #choose the top save
            click("1537682336599.png") #load it
            while not exists("1538435041037.png") and appActive("CivilizationV_DX11.exe"):
                wait(10)
            else:
                if exists("1538435041037.png"):
                    click("1538435041037.png") #DoM prompt
                else:
                    print "Game crash, restart"
                    return None
#            wait(1) 
#            click("1569902718242.png")
#            wait(30)
#            type("-")             #zoom out all the way, then back in one
#            wait(30)
#            type("-")
#            wait(30)
#            type("-")
#            wait(30)
#            type("-")
#            wait(30)
#            type("+")
#            wait(30)
        else:
            print "Civ V already open"
            return CivV
        return CivV
    except:
        print "app open failed"
        return None

def game_starter():
    CivV = App("CivilizationV")
    try:
        if not CivV.window():
            CivV.open("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Sid Meier's Civilization V\\CivilizationV_DX11.exe")
            wait(10)
            while not exists("1537682070546.png") and appActive("CivilizationV_DX11.exe"):
                wait(10)
            else:
                if exists("1537682070546.png"):
                    wait(30)
                    click("1537682070546.png") #initial prompt
                else:
                    print "Game crash, restart"
                    return None
            wait(1)
            click("1537682089185.png") #mods menu
            wait(1)
            click("1537682120561.png") #accept terms
            wait(1)
            click("1537682143489.png") #mod selection
            wait(60)
            click("1537682222024.png") #single player menu
            wait(1)
            click("1540774074657.png") #new game
            wait(1)
            click("1540774098776.png") #advanced menu
            wait(1)
            click("1540774117681.png") #Start er up
            while not exists("1538435041037.png") and appActive("CivilizationV_DX11.exe"):
                wait(10)
            else:
                if exists("1538435041037.png"):
                    click("1538435041037.png") #DoM prompt
                else:
                    print "Game crash, restart"
                    return None
#            wait(1) 
#            click("1569902718242.png")
#            wait(30)
#            type("-")             #zoom out all the way, then back in one
#            wait(30)
#            type("-")
#            wait(30)
#            type("-")
#            wait(30)
#            type("-")
#            wait(30)
#            type("+")
#            wait(30)
        return CivV
    except:
        return CivV

def file_processor():
    print "processing files"
    turn = turn_getter() #get the current turn
    try:
        os.mkdir("D:\\CBRXS1 Processed Turns\\Turn %d" %(turn)) #make a directory to store stuff in
        os.mkdir("D:\\CBRXS1 Processed Turns\\Turn %d\\images" %(turn))
        os.mkdir("D:\\CBRXS1 Processed Turns\\Turn %d\\video" %(turn))
        os.mkdir("D:\\CBRXS1 Processed Turns\\Turn %d\\save" %(turn))
        os.mkdir("D:\\CBRXS1 Processed Turns\\Turn %d\\db" %(turn))
    except:
        print "Directory already made"
    savesource = max(glob.glob("C:\\Users\\weath\\OneDrive\\Documents\\my games\\Sid Meier's Civilization 5\\ModdedSaves\\single\\auto\*"), key = os.path.getctime)
    savedest = "D:\\CBRXS1 Processed Turns\\Turn %d\\save" %(turn)
    dbdest = "D:\\CBRXS1 Processed Turns\\Turn %d\\db" %(turn)
    try:
        if turn >= 1:
            vidsource = os.listdir("D:\\Recordings")
            viddest = "D:\\CBRXS1 Processed Turns\\Turn %d\\video" %(turn)
            for vidfiles in vidsource:
                if vidfiles.endswith(".mkv"):
                    shutil.move("D:\\Recordings"+"\\"+vidfiles, viddest) #move video recording
        else:
            print "too soon to move videos"
        try:
            shutil.copy(savesource, savedest) #copy the save
        except:
            print "Save move failed"
        try:
            if turn % 10 == 0 and turn > 20:
                shutil.copy("C:\\Users\\weath\\OneDrive\\Documents\\my games\\Sid Meier's Civilization 5\\cache\\Civ5SavedGameDatabase.db", dbdest) #copy the DB file
        except:
            print "DB move failed"
        try:
            shutil.copy("C:\\Users\\weath\\OneDrive\\Documents\\my games\\Sid Meier's Civilization 5\\Logs\\Lua.log", dbdest) #copy the Lua log
        except:
            print "Lua log move failed"
    except:
        print "files move failed"
        
    
def turn_getter():
    #set db connection info
    url = "jdbc:sqlite:C:\\Users\\weath\\OneDrive\\Documents\\my games\\Sid Meier's Civilization 5\\cache\\Civ5SavedGameDatabase.db"
    dbuser = ""
    dbpassword = ""
    driver = "org.sqlite.JDBC"
    #connect to the db
    dbconn = zxJDBC.connect(url, dbuser, dbpassword, driver)
    dbcur = dbconn.cursor()
    #grab the current turn
    turn = [0]
    try:
        dbcur.execute("select max(Turn) from InfoAddictHistoricalData")
        turn = dbcur.fetchone()
    except:
        print "turn error"
        return -1 #return -1 if it fails
    finally:
        dbcur.close()
        dbconn.close()
        print turn[0]
        return turn[0]

def addl_info_shotter():
    print "taking additional screenshots"
    try:
        click_offset = 300
        click("1579217182046.png")
        click("1539555772349.png")
        wait(10)
        click("1539555846035.png")
        click("1579217182046.png")
        click("1539555887396.png")
        wait(1)
        try:
            click(find("1539556837966.png").offset(0,click_offset))
        except:
            print "too few religions"
        click_offset = 75
        click("1539555922251.png")
        while not exists("1539556977333.png") and click_offset < 600:
            click(find("1539556837966.png").offset(0,click_offset))
            click_offset += 75
            wait(1)
        click(find("1539556837966.png").offset(0,50))
        click("1539556230809.png")
        click("1539556745086.png")
        click("1539556264290.png")
    except:
        return

def appActive(appName):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % appName
    # Get the tasklist result
    proc = subprocess.Popen(call, shell=True, stdout=subprocess.PIPE)
    # Trimming lines with information
    output = proc.communicate()[0].strip().split('\r\n')
    # If TASKLIST returns multiple lines, it is running. 
    if len(output) > 1 and appName in output[-1]:
#        print('Result: "%s" is running!' % appName)
        return True
    else:
        print('Result: "%s" is NOT running!' % appName)
        return False
      
def CBRX_loader(started):
    civgame = game_restarter(started)
    if appActive("CivilizationV_DX11.exe"):
        click("1541199351624.png")
    else:
        civgame = game_restarter(False)
    wait(10)
    while True:
        while appActive("CivilizationV_DX11.exe"):
            print "load sucessful"
            return
        else:
            print "Game crashed"
            try:
                civgame.close()
            except:
                print "game close failed"
            wait(300)
            civgame = game_restarter(False)
            
def CBRX_processor(started):
    civgame = game_restarter(started)
    OBS = App("OBS")
    if not appActive("obs64.exe"):
        recorder = recording_initializer()
    else:
        OBS.close()
        recorder = recording_initializer()
    if appActive("CivilizationV_DX11.exe"):
        click("1541199351624.png")
    else:
        civgame = game_restarter(False)
    wait(10)
    while True:
        while appActive("CivilizationV_DX11.exe"):
            try:
                if exists("1550604767883.png"):
                    click("1550604767883.png")
                    wait(2)
                    click("1550604816256.png")
                    wait(2)
                    click("1550604837734.png")
            except:
                print "Not WC turn"
            try:
                click("1536087253968.png")
                #hover(civgame.window().getBottomRight().offset(-30,-30))
                hover(Region(0,0,1780,1100).getBottomRight())
            except:
                print "first click error"
            print "going to turn waiter"            
            turn_waiter(civgame,recorder)
        else:
            print "Game crashed"
            try:
                civgame.close()
            except:
                print "game close failed"
            recording_stopper(recorder)
            wait(300)
            civgame = game_restarter(False)
            recording_initializer()

def test_processor(started):
    civgame = game_restarter(started)
    if appActive("CivilizationV_DX11.exe"):
        click("1541199351624.png")
    else:
        civgame = game_restarter(False)
    wait(10)
    while True:
        while appActive("CivilizationV_DX11.exe"):
            try:
                if exists("1550604767883.png"):
                    click("1550604767883.png")
                    wait(2)
                    click("1550604816256.png")
                    wait(2)
                    click("1550604837734.png")
            except:
                print "Not WC turn"
            try:
                click("1536087253968.png")
                #hover(civgame.window().getBottomRight().offset(-30,-30))
                hover(Region(0,0,1780,1100).getBottomRight())
            except:
                print "first click error"
            print "going to turn waiter"            
            test_waiter(civgame)
        else:
            print "Game crashed"
            try:
                civgame.close()
            except:
                print "game close failed"
            wait(300)
            civgame = game_restarter(False)


def early_processor():
    OBS = App("OBS")
    civv = App("CivilizationV")
    turn = turn_getter()
    while turn < 6:
        turn_waiter(civv,OBS)

def restart_processor():
    OBS = App("OBS")
    civv = App("CivilizationV")
    turn = turn_getter()
    while True:
        turn_waiter(civv,OBS)

#test_processor(False)
CBRX_processor(True)
#CBRX_loader(False)
#game_starter()
#map_screen_shotter()
#file_processor()
#turn_getter()

