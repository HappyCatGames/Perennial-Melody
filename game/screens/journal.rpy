init python:
    def nextJournalPage(currentPage):
        if currentPage == 3:
            return 3
        elif currentPage < 3:
            return currentPage + 1

    def previousJournalPage(currentPage):
        if currentPage == 1:
            return 1
        elif currentPage > 1:
            return currentPage - 1

transform rotated:
    rotate rotation()
    rotate_pad False

screen journal(page):
    tag menu
    default journal_page = page
    use game_menu('Journal')

    fixed:
        xsize 1500 xalign 1.0


        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True
        style_prefix 'journal'

        # page 1
        if journal_page == 1:
            frame:
                has vbox
                spacing 50
                label "Page 1"

                # row 1 
                frame:
                    has hbox
                    spacing 30

                    ## Add To Do: Grab keys, grab phone here
                    frame:
                        style_prefix 'to_do'
                        at rotated
                        yoffset 25
                        has vbox
                        spacing 45
                        xalign 0.5
                        label "To do:" xalign 0.5:
                            background Frame('gui/button/button_bg_01_idle.png')
                            xsize 250
                            text_color '#fff'
                            text_xalign 0.5
                            yoffset 25
                
                        vbox:

                            spacing 15
                            hbox:
                                spacing 10
                                if hasKeys:
                                    add "gui/hover_background.png"
                                else:
                                    add 'gui/idle_background.png'
                                text "Get keys"
                            hbox:
                                spacing 10
                                if hasPhone:
                                    add "gui/hover_background.png"
                                else:
                                    add 'gui/idle_background.png'
                                text "Grab phone"

                    frame:
                        style 'journal_horizontal'
                        if persistent.bedUnlocked:
                            add 'journal_bed.png' xalign 0.5 ypos -5 
                    frame:
                        style 'journal_horizontal'
                        if persistent.oatmealUnlocked:
                            add 'journal_oatmeal.png' xalign 0.5 ypos -5 

                # row 2
                frame:
                    has hbox
                    spacing 30

                    frame:
                        style 'journal_vertical'
                        if persistent.mirrorUnlocked:
                            add 'journal_mirror.png' xalign 0.5 ypos -3 
                    frame:
                        style 'journal_horizontal'
                        if persistent.booksUnlocked:
                            add 'journal_books.png' xalign 0.5 ypos -5
                    frame:
                        style 'journal_vertical'
                        if persistent.keysUnlocked:
                            add 'journal_keys.png' xalign 0.5 ypos -3

        # page 2
        if journal_page == 2:
            frame:
                has vbox
                spacing 50
                label "Page 2"

                # row 1 
                frame:
                    has hbox
                    spacing 30

                    frame:
                        style 'journal_vertical'
                        if persistent.laundryUnlocked:
                            add 'journal_laundry.png' xalign 0.5 ypos -3 
                    frame:
                        style 'journal_horizontal'
                        if persistent.phoneUnlocked:
                            add 'journal_phone.png' xalign 0.5 ypos -5
                    frame:
                        style 'journal_horizontal'
                        if persistent.medsUnlocked:
                            add 'journal_meds.png' xalign 0.5 ypos -5

                # row 2
                frame:
                    has hbox
                    spacing 30

                    frame:
                        style 'journal_horizontal'
                        if persistent.idCardUnlocked:
                            add 'journal_id_card.png' xalign 0.5 ypos -5
                    frame:
                        style 'journal_vertical'
                        if persistent.camelliaUnlocked:
                            add 'journal_camellia.png' xalign 0.5 ypos -3 
                    frame:
                        style 'journal_vertical'
                        if persistent.plant_2Unlocked:
                            add 'journal_plant2.png' xalign 0.5 ypos -3 

        if journal_page == 3:
            frame:
                has vbox
                spacing 50
                label "Page 3"

                # row 1 
                frame:
                    has hbox
                    spacing 30

                    frame:
                        style 'journal_horizontal'
                        if persistent.pictureUnlocked:
                            add 'journal_picture.png' xalign 0.5 ypos -5
                    frame:
                        style 'journal_vertical'
                        if persistent.guitarUnlocked:
                            add 'journal_guitar.png' xalign 0.5 ypos -3 
                    frame:
                        style 'journal_horizontal'
                        if persistent.pcUnlocked:
                            add 'journal_computer.png' xalign 0.5 ypos -5

                # row 2
                frame:
                    has hbox
                    spacing 30

                    frame:
                        style 'journal_vertical'
                        if persistent.alyssumUnlocked:
                            add 'journal_alyssum.png' xalign 0.5 ypos -3 
                    frame:
                        style 'journal_horizontal'
                        if persistent.plant_1Unlocked:
                            add 'journal_plant1.png' xalign 0.5 ypos -5


        ## Buttons to access other pages.
        vbox:
            style_prefix "page"

            xalign 0.5
            yalign 0.9
            yoffset 50

            hbox:
                
                textbutton _("<") action ShowMenu('journal', previousJournalPage(journal_page)) hovered Play('sound', randomizeAudio())

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 4):
                    textbutton "[page]": 
                        if journal_page == page:
                            background Frame('gui/hover_background.png') 
                            text_color '#fff'
                        action ShowMenu('journal', page) 
                        hovered Play('sound', randomizeAudio())

                textbutton _(">") action ShowMenu('journal', nextJournalPage(journal_page)) hovered Play('sound', randomizeAudio())

style journal_frame is empty:
    xalign 0.5

style journal_label:
    xalign 0.5
    yoffset 25

style journal_horizontal:
    background Frame('gui/journal_empty_horizontal.png')
    xsize 398
    ysize 324 
    yalign 0.5

style journal_vertical:
    background Frame('gui/journal_empty_vertical.png')
    xsize 324
    ysize 398 
    yalign 0.5

style to_do_frame:
    padding (50, 60, 50, 60)
    background Frame("gui/frame.png", 50, 50, 50, 50, tile=False)

style to_do_text is gui_text