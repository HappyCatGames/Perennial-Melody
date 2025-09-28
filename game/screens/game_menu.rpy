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
        xpos 45 yalign 0.5 yoffset 25
        spacing 25

        if main_menu:
            textbutton _('Start').upper() background Frame(randomizeButton()[0]) hover_background Frame(randomizeButton()[1]) action Start() hovered Play('sound', randomizeAudio())

        else: 
            textbutton _('Journal').upper():
                background Frame(button_bg_list[0][0])
                hover_background Frame(randomizeButton()[1])
                action ShowMenu("journal", 1) 
                hovered Play('sound', randomizeAudio())

            textbutton _('History').upper(): 
                background Frame(button_bg_list[1][0])
                hover_background Frame(randomizeButton()[1])
                action ShowMenu("history") 
                hovered Play('sound', randomizeAudio())

            textbutton _('Save').upper(): 
                background Frame(button_bg_list[2][0])
                hover_background Frame(randomizeButton()[1])
                action ShowMenu("save") 
                hovered Play('sound', randomizeAudio())

        textbutton _('Load').upper(): 
            background Frame(button_bg_list[3][0])
            hover_background Frame(randomizeButton()[1])
            action ShowMenu("load") 
            hovered Play('sound', randomizeAudio())

        textbutton _('Preferences').upper():
            background Frame(button_bg_list[4][0])
            hover_background Frame(randomizeButton()[1]) 
            action ShowMenu("preferences") 
            hovered Play('sound', randomizeAudio())

        if _in_replay:

            textbutton _('End Replay').upper(): 
                background Frame(button_bg_list[5][0])
                hover_background Frame(randomizeButton()[1])
                action EndReplay(confirm=True) 
                hovered Play('sound', randomizeAudio())

        elif not main_menu:

            textbutton _('Main Menu').upper(): 
                background Frame(button_bg_list[0][0])
                hover_background Frame(randomizeButton()[1])
                action MainMenu() 
                hovered Play('sound', randomizeAudio())

        textbutton _('About').upper(): 
            background Frame(button_bg_list[1][0])
            hover_background Frame(randomizeButton()[1])
            action ShowMenu("about") 
            hovered Play('sound', randomizeAudio())

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")): 

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _('Help').upper():
                background Frame(button_bg_list[2][0])
                hover_background Frame(randomizeButton()[1]) 
                action ShowMenu("help") 
                hovered Play('sound', randomizeAudio())

        if persistent.allRoutesUnlocked == True:

            textbutton _('Credits').upper(): 
                background Frame(button_bg_list[3][0])
                hover_background Frame(randomizeButton()[1])
                action Jump("credits") 
                hovered Play('sound', randomizeAudio())
        
        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _('Quit').upper(): 
                background Frame(button_bg_list[4][0])
                hover_background Frame(randomizeButton()[1])
                action Quit(confirm=not main_menu) 
                hovered Play('sound', randomizeAudio())
    
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

style game_menu_button:
    padding (10, 10)
    xsize 270

style game_menu_button_text:
    idle_color '#fff'
    size 24
    xalign 0.5


