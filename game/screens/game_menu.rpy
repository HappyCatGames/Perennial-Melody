## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the title and navigation.
##
## This screen no longer includes a background, and it no longer transcludes
## its contents. It is intended to be easily removable from any given menu
## screen and thus you are required to do some of the heavy lifting for
## setting up containers for the contents of your menu screens.
##

screen game_menu(title):

    style_prefix "game_menu"

    add "gui/overlay/game_menu.png"

    vbox:
        xpos 45 yalign 0.5
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
    
    imagebutton auto "gui/button/mm_return_%s.png":
        style "return_button"
        hovered Play('sound', randomizeAudio())
        action Return()

    ## Remove this line if you don't want to show the screen
    ## title text as a label (for example, if it's baked into
    ## the background image.)
    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style return_button:
    xpos 60
    yalign 1.0
    yoffset -45

style game_menu_viewport:
    xsize config.screen_width-500
    ysize config.screen_height-200
    align (0.5, 1.0)
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_side:
    yfill True
    align (1.0, 0.5)

style game_menu_vscrollbar:
    unscrollable "hide"

style game_menu_label:
    padding (10, 10)
    ysize 165
    xsize 525
    xpos 0

style game_menu_label_text:
    size 100
    align (0.5, 0.5)
