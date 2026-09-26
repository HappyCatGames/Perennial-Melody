screen extras():

    tag menu

    style_prefix "game_menu"
    add "gui/overlay/game_menu.png"

    vbox:
        xpos 45 yalign 0.5 yoffset 25
        spacing 25

        if main_menu and persistent.hasCompletedARoute:
            textbutton _('Journal').upper():
                background Frame(button_bg_list[0][0])
                hover_background Frame("button_hover_bg")
                action [ShowMenu("journal", 1), Function(open_journal_achievement.grant)]
                hovered Play('sound', randomizeAudio())
            textbutton _('Credits').upper():
                background Frame(button_bg_list[2][0])
                hover_background Frame("button_hover_bg")
                action Jump("credits")
                hovered Play('sound', randomizeAudio())
            textbutton _('Music Room').upper():
                background Frame(button_bg_list[3][0])
                hover_background Frame("button_hover_bg")
                action ShowMenu("music_room3", mr=music_room)
                hovered Play('sound', randomizeAudio())
        elif not main_menu:
            textbutton _('Journal').upper():
                background Frame(button_bg_list[0][0])
                hover_background Frame("button_hover_bg")
                action [ShowMenu("journal", 1), Function(open_journal_achievement.grant)]
                hovered Play('sound', randomizeAudio())
        if main_menu:
            textbutton _('Achievements').upper(): 
                background Frame(button_bg_list[1][0])
                hover_background Frame("button_hover_bg")
                action ShowMenu("achievement_gallery")
                hovered Play('sound', randomizeAudio())
    
    imagebutton auto "gui/button/mm_return_%s.png":
        style "return_button"
        hovered Play('sound', randomizeAudio())
        action Return()

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

    label __("Extras")

style return_button:
    xpos 45
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
    hover_background Frame("button_hover_bg")

style game_menu_button_text:
    idle_color '#fff'
    size 26
    xalign 0.5
