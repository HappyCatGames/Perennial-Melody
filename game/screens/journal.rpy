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

                    add 'gui/journal_empty_horizontal.png' yalign 0.5
                    add 'gui/journal_empty_vertical.png' yalign 0.5
                    add 'gui/journal_empty_horizontal.png' yalign 0.5

                # row 2
                frame:
                    has hbox
                    spacing 30

                    add 'gui/journal_empty_vertical.png' yalign 0.5
                    add 'gui/journal_empty_horizontal.png' yalign 0.5
                    add 'gui/journal_empty_vertical.png' yalign 0.5

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

                    add 'gui/journal_empty_vertical.png' yalign 0.5
                    add 'gui/journal_empty_horizontal.png' yalign 0.5
                    add 'gui/journal_empty_horizontal.png' yalign 0.5

                # row 2
                frame:
                    has hbox
                    spacing 30

                    add 'gui/journal_empty_horizontal.png' yalign 0.5
                    add 'gui/journal_empty_vertical.png' yalign 0.5
                    add 'gui/journal_empty_vertical.png' yalign 0.5

        if journal_page == 3:
            frame:
                has vbox
                spacing 50
                label "Page 3"

                # row 1 
                frame:
                    has hbox
                    spacing 30

                    add 'gui/journal_empty_horizontal.png' yalign 0.5
                    add 'gui/journal_empty_vertical.png' yalign 0.5
                    add 'gui/journal_empty_horizontal.png' yalign 0.5

                # row 2
                frame:
                    has hbox
                    spacing 30

                    add 'gui/journal_empty_vertical.png'


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