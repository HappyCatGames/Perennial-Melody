
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

define config.main_menu_music = "audio/Tech Ambient.wav"
image button_hover_bg:
    Image("gui/button/button_bg_03_hover.png")
    pause .3
    Image("gui/button/button_bg_04_hover.png")
    pause .3
    Image("gui/button/button_bg_01_hover.png")
    pause .3
    repeat

## Replace this with your background image, if you like
image main_menu_background = HBox(
    Solid("#292835", xsize=350),
    Solid("#21212d")
)

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu
    style_prefix "game_menu"
    add "gui/overlay/main_menu.png"

    vbox:
        xpos 45
        yoffset 325
        spacing 25

        textbutton _('Start').upper() background Frame(button_bg_list[5][0]) hover_background Frame("button_hover_bg") action Start() hovered Play('sound', randomizeAudio())

        textbutton _('Load').upper(): 
            background Frame(button_bg_list[3][0])
            hover_background Frame("button_hover_bg")
            action ShowMenu("load") 
            hovered Play('sound', randomizeAudio())

        textbutton _('Preferences').upper():
            background Frame(button_bg_list[4][0])
            hover_background Frame("button_hover_bg")
            action ShowMenu("preferences") 
            hovered Play('sound', randomizeAudio())

        if persistent.hasCompletedARoute:
            textbutton _('Extras').upper():
                background Frame(button_bg_list[0][0])
                hover_background Frame("button_hover_bg")
                action ShowMenu("extras")
                hovered Play('sound', randomizeAudio())

        if _in_replay:

            textbutton _('End Replay').upper(): 
                background Frame(button_bg_list[5][0])
                hover_background Frame("button_hover_bg")
                action EndReplay(confirm=True) 
                hovered Play('sound', randomizeAudio())

        textbutton _('About').upper(): 
            background Frame(button_bg_list[1][0])
            hover_background Frame("button_hover_bg")
            action ShowMenu("about") 
            hovered Play('sound', randomizeAudio())

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")): 

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _('Help').upper():
                background Frame(button_bg_list[2][0])
                hover_background Frame("button_hover_bg")
                action ShowMenu("help") 
                hovered Play('sound', randomizeAudio())

        if persistent.allRoutesUnlocked == True:

            textbutton _('Credits').upper(): 
                background Frame(button_bg_list[3][0])
                hover_background Frame("button_hover_bg")
                action Jump("credits") 
                hovered Play('sound', randomizeAudio())
        
        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _('Quit').upper(): 
                background Frame(button_bg_list[4][0])
                hover_background Frame("button_hover_bg")
                action Quit(confirm=not main_menu) 
                hovered Play('sound', randomizeAudio())
