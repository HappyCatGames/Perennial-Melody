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
                        style 'journal_horizontal'
                        if bed.isInteracted:
                            add 'journal_bed.png' xalign 0.5 ypos -5 
                    frame:
                        style 'journal_horizontal'
                        if oatmeal.isInteracted:
                            add 'journal_oatmeal.png' xalign 0.5 ypos -5 

                # row 2
                frame:
                    has hbox
                    spacing 30

                    frame:
                        style 'journal_vertical'
                        if mirror.isInteracted:
                            add 'journal_mirror.png' xalign 0.5 ypos -3 
                    frame:
                        style 'journal_horizontal'
                        if books.isInteracted:
                            add 'journal_books.png' xalign 0.5 ypos -5
                    frame:
                        style 'journal_vertical'
                        if keys.isInteracted:
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
                        if laundry.isInteracted:
                            add 'journal_laundry.png' xalign 0.5 ypos -3 
                    frame:
                        style 'journal_horizontal'
                        if phone.isInteracted:
                            add 'journal_phone.png' xalign 0.5 ypos -5
                    frame:
                        style 'journal_horizontal'
                        if meds.isInteracted:
                            add 'journal_meds.png' xalign 0.5 ypos -5

                # row 2
                frame:
                    has hbox
                    spacing 30

                    frame:
                        style 'journal_horizontal'
                        if idCard.isInteracted:
                            add 'journal_id_card.png' xalign 0.5 ypos -5
                    frame:
                        style 'journal_vertical'
                        if camellia.isInteracted:
                            add 'journal_camellia.png' xalign 0.5 ypos -3 
                    frame:
                        style 'journal_vertical'
                        if plant_2.isInteracted:
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
                        if picture.isInteracted:
                            add 'journal_picture.png' xalign 0.5 ypos -5
                    frame:
                        style 'journal_vertical'
                        if guitar.isInteracted:
                            add 'journal_guitar.png' xalign 0.5 ypos -3 
                    frame:
                        style 'journal_horizontal'
                        if pc.isInteracted:
                            add 'journal_computer.png' xalign 0.5 ypos -5

                # row 2
                frame:
                    has hbox
                    spacing 30

                    frame:
                        style 'journal_vertical'
                        if alyssum.isInteracted:
                            add 'journal_alyssum.png' xalign 0.5 ypos -3 
                    frame:
                        style 'journal_horizontal'
                        if plant_1.isInteracted:
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