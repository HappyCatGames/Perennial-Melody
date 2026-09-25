################################################################################
## MUSIC ROOM DECLARATION
################################################################################
init python:
    #################### STEP 1: Set up the music room.
    ## You can make multiple music rooms consisting of different sets of tracks,
    ## if you so desire, or use one music room for all your music. You only need
    ## to pass in the name of the ExtendedMusicRoom object you set up here to
    ## the music room screens below.

    ## You can pass any of the following arguments to ExtendedMusicRoom:
    ## channel: The channel to play the music on. Defaults to 'music'.
    ## fadeout: The time in seconds to fade out the old song when changing
    ##          tracks. Defaults to 0.0 (no fade).
    ## fadein: The time in seconds to fade in the new song when changing tracks.
    ##         Defaults to 0.0 (no fade).
    ## loop: Whether to loop the music when reaching the end of the track list.
    ##       Defaults to True and can be toggled in the music room with a
    ##       button.
    ## single_track: If True, only a single track will loop. Defaults to False
    ##               and can be toggled in the music room with a button.
    ## shuffle: Whether to shuffle the tracks or play them in default order.
    ##          Defaults to False and can be toggled in the music room with a
    ##          button.
    ## stop_action: A screen action to run when the music stops. Defaults to
    ##              None, so no action is run.
    ## alphabetical : If True, the tracks will be sorted alphabetically.
    ##                If False, the default, they will be arranged in the order
    ##                they are added to the music room in.
    music_room = ExtendedMusicRoom(channel='music', fadeout=0.0, fadein=0.0,
        loop=True, single_track=False, shuffle=False, stop_action=None,
        alphabetical=True)

    ## This sets up a default art image for all tracks in this room which aren't
    ## given a more specific one. This default art is 600x600, but several
    ## layouts resize it. It should typically be square.
    music_room.default_art = "gui/music_room/cover_art.webp"

    music_room.add(
        name=_("Ambient Lo-Fi"),
        artist="Red Robotix",
        path="audio/Ambient Lo-Fi.wav",
    )
    music_room.add(
        name=_("Bass Groove Revival"),
        artist="Tobi Weiss",
        path="audio/Bass Groove Revival.wav",
    )
    music_room.add(
        name=_("ChildHood Memories"),
        artist="Tobi Weiss",
        path="audio/ChildHood Memories.wav",
    )
    music_room.add(
        name=_("News"),
        artist="Tobi Weiss",
        path="audio/News.wav",
    )
    music_room.add(
        name=_("Sadness"),
        artist="Tobi Weiss",
        path="audio/Sadness.wav",
    )
    music_room.add(
        name=_("Tech Ambient"),
        artist="Tobi Weiss",
        path="audio/Tech Ambient.wav",
    )
    music_room.add(
        name=_("The Future Bass"),
        artist="Tobi Weiss",
        path="audio/The Future Bass.wav",
    )
    music_room.add(
        name=_("Wistful Reflections (Distorted)"),
        artist="Tobi Weiss",
        path="audio/Wistful Reflections Distorted.wav",
    )
################################################################################
## CONFIGURATION VALUES
################################################################################
## Set this to True if you want to unlock all tracks in the music room during
## development. Set it to False to test the unlock conditions. Tracks will
## automatically obey unlock rules in a distribution regardless of the value
## of this configuration variable.
define myconfig.UNLOCK_TRACKS_FOR_DEVELOPMENT = False

################################################################################
## IMAGES & DEFINITIONS
################################################################################
## These colours are used by the colorize_button transform in the screens below
## to colorize the default music controls. You can change these if you want to
## use the provided images, or simply supply your own and remove the lines
## `at colorize_button` from the screen below.
define MUSIC_ROOM_IDLE_COLOR = "#ff8335"
define MUSIC_ROOM_HOVER_COLOR = "#f93c3e"
define MUSIC_ROOM_SELECTED_IDLE_COLOR = "#ff8335"
define MUSIC_ROOM_SELECTED_HOVER_COLOR = "#f93c3e"
define MUSIC_ROOM_INSENSITIVE_COLOR = "#888"

## Here are the default buttons used for the music controls below. You can
## update these or replace them.
image play_button = "gui/music_room/play.webp"
image pause_button = "gui/music_room/pause.webp"
image next_button = "gui/music_room/next.webp"
image prev_button = Transform("gui/music_room/next.webp", xzoom=-1.0)
image repeat_all_button = "gui/music_room/repeat all.webp"
## Note that this image is just a foreground on top of the repeat_all button!
image repeat_one_button = "gui/music_room/repeat 1.webp"
image shuffle_button = "gui/music_room/shuffle.webp"
image back_10_button = "gui/music_room/back_10.webp"
image forward_10_button = "gui/music_room/forward_10.webp"

## The "audio level" bars. These are optional to show next to the currently
## playing song. There are four bars that randomly change height.
define AUDIO_BAR_HEIGHT = 30
define AUDIO_BAR_WIDTH = 8
image audio_bar = Transform(MUSIC_ROOM_HOVER_COLOR,
    xysize=(AUDIO_BAR_WIDTH, AUDIO_BAR_HEIGHT))
transform audio_bar_move():
    yzoom renpy.random.random() ## Start at a random height
    block:
        ## Choose a random height to be
        choice:
            ease 0.2 yzoom 1.0
        choice:
            ease 0.2 yzoom 0.2
        choice:
            ease 0.2 yzoom 0.8
        choice:
            ease 0.2 yzoom 0.0
        choice:
            ease 0.2 yzoom 0.5
        repeat
## The final audio bars image, with four bars that randomly change height.
image audio_bars = HBox(
    At('audio_bar', audio_bar_move),
    At('audio_bar', audio_bar_move),
    At('audio_bar', audio_bar_move),
    At('audio_bar', audio_bar_move),
    yalign=1.0, ysize=AUDIO_BAR_HEIGHT,
)

################################################################################
## TRANSFORMS
################################################################################
## A transform that makes it easier to apply colours to the various buttons.
## The default images are black, so it uses ColorizeMatrix to colorize them.
## The colours are defined at the top of the file.
transform colorize_button(idle=MUSIC_ROOM_IDLE_COLOR,
        hover=MUSIC_ROOM_HOVER_COLOR,
        selected_idle=MUSIC_ROOM_SELECTED_IDLE_COLOR,
        selected_hover=MUSIC_ROOM_SELECTED_HOVER_COLOR,
        insensitive=MUSIC_ROOM_INSENSITIVE_COLOR):
    matrixcolor ColorizeMatrix(insensitive, "#fff")
    on idle:
        matrixcolor ColorizeMatrix(idle, "#fff")
    on hover:
        matrixcolor ColorizeMatrix(hover, "#fff")
    on insensitive:
        matrixcolor ColorizeMatrix(insensitive, "#fff")
    on selected_idle:
        matrixcolor ColorizeMatrix(selected_idle, "#fff")
    on selected_hover:
        matrixcolor ColorizeMatrix(selected_hover, "#fff")

## A simple transform to easily resize buttons. Used by some layouts.
transform zoom_button(z):
    zoom z


################################################################################
## Styles for the track list, shared generally by the other rooms.
################################################################################
style track_list_frame:
    background "#21212d"
    yalign 0.0 xalign 0.0
    padding (25, 25)
style track_list_viewport:
    xfill False yfill False ymaximum config.screen_height-200
style track_list_side:
    spacing 20
style track_list_vbox:
    spacing 0
style track_list_button:
    right_padding 45
    background Transform("#ff8335", ysize=2, yalign=1.0)
    hover_foreground "#fff1"
    ypadding 15 xfill True
style track_list_hbox:
    xalign 0.0 spacing 18
style track_list_fixed:
    xsize 45 ysize 45 yalign 0.5
style track_list_text:
    color "#bfbfb9"
    insensitive_color "#666"
style track_list_label:
    background None padding (2, 0)
style track_list_label_text:
    color "#f7f7ed" hover_color "#f93c3e" selected_color "#ff8335"
    insensitive_color "#666"
style track_list_vscrollbar:
    thumb "#fc5f39" base_bar "#292835"

################################################################################
## SCREENS - VERSION 3
################################################################################
screen music_room3(mr):

    tag menu

    ## Needed to have easy access to information on the currently playing song.
    ## Required for ALL music rooms!
    default current_track = mr.get_current_song()

    style_prefix "music_room3"

    add HBox(Transform("#292835", xsize=350), "#21212db2") # Background

    ############################################################################
    ## If you have a standard Ren'Py UI sidebar, you can use this:
    ##
    # use game_menu(_("Music Room")):
    ##
    ## Otherwise, if you're using my Easy Ren'Py GUI (https://feniksdev.itch.io/easy-renpy-gui)
    ## you can use this:
    ##
    use game_menu(_("Music Room"))
    fixed:
        yfill True
        xsize config.screen_width-420
        align (1.0, 0.5)
    ##
    ############################################################################

        frame:
            style_prefix 'track_list'
            xfill True top_margin 25 yfill True bottom_margin 220
            viewport:
                mousewheel True scrollbars "vertical" draggable True
                has vbox
                label _("Track List") style "music_room_title"
                ## get_tracklist takes one argument, all_tracks. If all_tracks is
                ## True, it shows all tracks, including locked ones (which will be
                ## shown grayed out). If all_tracks is False, it only shows unlocked
                ## tracks.
                for num, song in enumerate(mr.get_tracklist(all_tracks=True)):
                    button:
                        action mr.Play(song.path)
                        has hbox
                        fixed:
                            if song is current_track:
                                ## If the song is currently playing, add a bit of
                                ## flair with some audio bars.
                                add Transform('audio_bars', ysize=30, xalign=0.5,
                                    yzoom=-1.0, yalign=0.55)
                            else:
                                ## The track number. +1 is because enumerate starts
                                ## at 0 instead of 1.
                                text str(num+1) align (0.5, 0.55)
                        add song.art ysize 100 fit "contain"
                        vbox:
                            spacing 4
                            ## Track info
                            label song.name
                            text song.artist

        ## This holds the album art, song title, artist, music bar, and music
        ## controls. You may adjust this however you wish! The important part
        ## is generally the actions on the buttons, and the music bar is special
        ## so you can click it to seek in the song.
        frame:
            style_prefix 'musicroom3'
            has hbox
            xalign 0.5 yalign 0.5
            if current_track:
                add current_track.art ysize 150 fit "contain"
            else:
                add mr.default_art ysize 150 fit "contain"
            vbox:
                xsize 250
                if current_track:
                    text current_track.name
                    text current_track.artist color "#bfbfb9"
                else:
                    text _("No song playing")

            null width 10

            vbox:
                yalign 0.5 spacing 15
                hbox:
                    xalign 0.5 spacing 30
                    ################## Shuffle button ##################
                    imagebutton:
                        idle "shuffle_button"
                        at colorize_button(MUSIC_ROOM_INSENSITIVE_COLOR,
                            MUSIC_ROOM_IDLE_COLOR), zoom_button(0.6)
                        action mr.ToggleShuffle()
                    ############ Previous, play/pause, next buttons ############
                    imagebutton:
                        idle "prev_button"
                        at colorize_button(), zoom_button(0.4)
                        action mr.Previous()
                    imagebutton:
                        at colorize_button(), zoom_button(0.25)
                        idle "pause_button" hover "pause_button"
                        selected_idle "play_button" selected_hover "play_button"
                        action mr.PlayAction()
                    imagebutton:
                        idle "next_button"
                        at colorize_button(), zoom_button(0.4)
                        action mr.Next()
                    ################## Repeat all, repeat one buttons ##################
                    imagebutton:
                        at colorize_button(idle=MUSIC_ROOM_INSENSITIVE_COLOR,
                            hover=MUSIC_ROOM_IDLE_COLOR), zoom_button(0.6)
                        idle "repeat_all_button"
                        if mr.single_track:
                            foreground "repeat_one_button"
                        action mr.CycleLoop()

                ################## Music Bar ##################
                hbox:
                    spacing 8
                    fixed:
                        yfit True xsize 100
                        add mr.get_pos(style="music_room_pos")
                    music_bar room mr
                    fixed:
                        yfit True xsize 100
                        add mr.get_duration(style="music_room_duration")

            add "gui/music_room/volume.webp" zoom 0.45 yalign 0.5:
                matrixcolor ColorizeMatrix(MUSIC_ROOM_HOVER_COLOR, "#fff")

            bar value MixerValue(mr.channel) xysize (150, 25):
                xalign 0.5 right_bar "#21212d" thumb None yalign 0.5
                left_bar "#fc5f39"

style musicroom3_frame:
    yalign 1.0 xalign 0.5 xfill True ysize 200
    background Frame(
        Fixed(
            Transform("#f93c3e", xysize=(100, 100)),
            Transform("#292835", xysize=(90, 90), align=(0.5, 0.5)),
            xysize=(100, 100)
        ), 10, 10
    )
style music_room_text:
    color "#fff"
    xalign 0.5
style music_room_title:
    background None xalign 0.5 bottom_padding 15
style music_room_title_text:
    font gui.name_text_font
    size 50 color "#ff8335" xalign 0.5
style musicroom3_hbox:
    spacing 20
style musicroom3_image_button:
    yalign 0.5
style musicroom3_bar:
    ysize 25 xsize 480
    yalign 0.5
    right_bar "#21212d" thumb None
    left_bar "#fc5f39"
style musicroom3_text:
    yalign 0.5 size 25 color "#f7f7ed"
style musicroom3_vbox:
    yalign 0.5
style music_room_image_button:
    align (0.5, 0.5)
style music_room_bar:
    xsize 700 xalign 0.5 ysize 38
    right_bar "#21212d"
    left_bar "#fc5f39"
style music_room_pos:
    color "#fff" xalign 0.5 adjust_spacing False
style music_room_duration:
    color "#fff" xalign 0.5 adjust_spacing False