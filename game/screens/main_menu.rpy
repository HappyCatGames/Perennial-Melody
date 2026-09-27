
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

image mm_btn_hover_bg:
    Image("gui/button/mm_btn_03_hover.png")
    pause .3
    Image("gui/button/mm_btn_01_hover.png")
    pause .3
    Image("gui/button/mm_btn_05_hover.png")
    pause .3
    repeat    


screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu
    style_prefix "game_menu"
    add "gui/overlay/mainmenu_2.png"

    vbox:
        xsize 763
        yoffset 380
        spacing 25

        textbutton _('Start').upper() background Frame("gui/button/mm_btn_01.png") hover_background Frame("mm_btn_hover_bg") action Start() hovered Play('sound', randomizeAudio()) xalign 0.5 xsize 456

        textbutton _('Load').upper(): 
            background Frame("gui/button/mm_btn_02.png")
            hover_background Frame("mm_btn_hover_bg")
            xalign 0.5
            xsize 456
            action ShowMenu("load") 
            hovered Play('sound', randomizeAudio())

        textbutton _('Preferences').upper():
            background Frame("gui/button/mm_btn_03.png")
            hover_background Frame("mm_btn_hover_bg")
            xalign 0.5
            xsize 456
            action ShowMenu("preferences") 
            hovered Play('sound', randomizeAudio())

        if persistent.hasCompletedARoute:
            textbutton _('Extras').upper():
                background Frame("gui/button/mm_btn_04.png")
                hover_background Frame("mm_btn_hover_bg")
                xalign 0.5
                xsize 456
                action ShowMenu("extras")
                hovered Play('sound', randomizeAudio())

        if _in_replay:

            textbutton _('End Replay').upper(): 
                background Frame("gui/button/mm_btn_05.png")
                hover_background Frame("mm_btn_hover_bg")
                xalign 0.5
                xsize 456
                action EndReplay(confirm=True) 
                hovered Play('sound', randomizeAudio())

        textbutton _('About').upper(): 
            background Frame("gui/button/mm_btn_06.png")
            hover_background Frame("mm_btn_hover_bg")
            xalign 0.5
            xsize 456
            action ShowMenu("about") 
            hovered Play('sound', randomizeAudio())

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")): 

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _('Help').upper():
                background Frame("gui/button/mm_btn_02.png")
                hover_background Frame("mm_btn_hover_bg")
                xalign 0.5
                xsize 456
                action ShowMenu("help") 
                hovered Play('sound', randomizeAudio())

        if persistent.allRoutesUnlocked == True:

            textbutton _('Credits').upper(): 
                background Frame("gui/button/mm_btn_02.png")
                hover_background Frame("mm_btn_hover_bg")
                xalign 0.5
                xsize 456
                action Jump("credits") 
                hovered Play('sound', randomizeAudio())
        
        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _('Quit').upper(): 
                background Frame("gui/button/mm_btn_03.png")
                hover_background Frame("mm_btn_hover_bg")
                xalign 0.5
                xsize 456
                action Quit(confirm=not main_menu) 
                hovered Play('sound', randomizeAudio())
