
## Say screen ##################################################################
##

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    ## If there's a side image, display it in front of the text.
    add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

# Style for the dialogue window
style window:
    xalign 0.5
    yalign 1.0
    xfill True
    ysize 278
    padding (40, 10, 40, 40)
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

# Style for the dialogue
style say_dialogue:
    adjust_spacing False
    xsize 1116
    xpos 355
    ypos 43

# The style for dialogue said by the narrator
style say_thought:
    is say_dialogue

# Style for the box containing the speaker's name
style namebox:
    ypos -149
    xpos 200
    xysize (470, 135)
    background Frame("gui/namebox.png", 5, 5, 5, 5, tile=False, xalign=0.0)
    padding (5, 5, 5, 45)

# Style for the text with the speaker's name
style say_label:
    xalign 0.5
    yalign 0.5
    size gui.name_text_size
    font gui.name_text_font


## Iteration Counter #########################################################
##

screen iteration_counter(item):
    style_prefix "iteration"
    zorder 99

    frame:
        background Frame("gui/side_tag.png", 10, 10, 10, 10)
        hbox:
            text "[item.currentIterationCount]\n/\n[item.maxIterationCount]":
                size 33 
                font gui.label_text_font 
                color gui.light_text_color
                xoffset 50
                yoffset 10
                line_spacing -5


style iteration_frame:
    xsize 97
    ysize 150
    yalign 1.0
    yoffset -125
    xalign 1.0
    xoffset -123

## Quick Menu screen #########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick" 
            xalign 0.5
            yalign 1.0               

            imagebutton auto "gui/button/qm_back_%s.png":  
                hovered Play('sound', randomizeAudio())
                action Rollback()
            imagebutton auto "gui/button/qm_history_%s.png": 
                hovered Play('sound', randomizeAudio()) 
                action ShowMenu('history')
            imagebutton auto "gui/button/qm_skip_%s.png" action Skip() alternate Skip(fast=True, confirm=True) hovered Play('sound', randomizeAudio())
            imagebutton auto "gui/button/qm_auto_%s.png" action Preference("auto-forward", "toggle") hovered Play('sound', randomizeAudio())
            imagebutton auto "gui/button/qm_save_%s.png" action ShowMenu('save') hovered Play('sound', randomizeAudio())
            imagebutton auto "gui/button/qm_qsave_%s.png" action QuickSave() hovered Play('sound', randomizeAudio())
            imagebutton auto "gui/button/qm_qload_%s.png" action QuickLoad() hovered Play('sound', randomizeAudio())
            imagebutton auto "gui/button/qm_prefs_%s.png" action ShowMenu('preferences') hovered Play('sound', randomizeAudio())


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_frame:
    background "gui/quickmenu_bg.png"
    xalign 0.5
    yalign 1.0

style quick_button is default
style quick_button_text is button_text
