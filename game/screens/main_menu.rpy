
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

define config.main_menu_music = "audio/Tech Ambient.wav"

## Replace this with your background image, if you like
image main_menu_background = HBox(
    Solid("#292835", xsize=350),
    Solid("#21212d")
)

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add "gui/overlay/main_menu.png"

    vbox:
        xpos 45
        yalign 0.7
        spacing 25

        if main_menu:
            imagebutton auto "gui/button/mm_start_%s.png" action Start() hovered Play('sound', randomizeAudio())

        else: 
            imagebutton auto "gui/button/mm_history_%s.png" action ShowMenu("history") hovered Play('sound', randomizeAudio())

            imagebutton auto "gui/button/mm_save_%s.png" action ShowMenu("save") hovered Play('sound', randomizeAudio())

        imagebutton auto "gui/button/mm_load_%s.png" action ShowMenu("load") hovered Play('sound', randomizeAudio())

        imagebutton auto "gui/button/mm_prefs_%s.png" action ShowMenu("preferences") hovered Play('sound', randomizeAudio())

        if _in_replay:

            imagebutton auto "gui/button/mm_endreplay_%s.png" action EndReplay(confirm=True) hovered Play('sound', randomizeAudio())

        elif not main_menu:

            imagebutton auto "gui/button/mm_mainmenu_%s.png" action MainMenu() hovered Play('sound', randomizeAudio())

        imagebutton auto "gui/button/mm_about_%s.png" action ShowMenu("about") hovered Play('sound', randomizeAudio())

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")): 

            ## Help isn't necessary or relevant to mobile devices.
            imagebutton auto "gui/button/mm_help_%s.png" action ShowMenu("help") hovered Play('sound', randomizeAudio())

        if persistent.allRoutesUnlocked == True:

            imagebutton auto "gui/button/credits_%s.png" action Jump("credits") hovered Play('sound', randomizeAudio())
        
        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            imagebutton auto "gui/button/mm_quit_%s.png" action Quit(confirm=not main_menu) hovered Play('sound', randomizeAudio())

