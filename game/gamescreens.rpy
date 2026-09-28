#######################################################################################################
#                                                                                                     #
#                                             IMAGEMAPS                                               #
#                                                                                                     #
#######################################################################################################

image dust_background = CreateFlutterParticles(
    ## The background fireflies are the smallest and most plentiful!
    image=firefly_blink("dust1"), particle_size=25, fast=False,
    ## For these fireflies, we'll only make them move by fluttering, so
    ## they aren't moving in straight lines.
    amount=20, xspeed=-5, yspeed=10,
    ## distribute_fast_start helps so particles aren't all starting at the
    ## same time blinking in sync
    distribute_fast_start=0.5,
    ## Our flutter motion! The backmost fireflies move the least, so they
    ## have the longest times and the smallest width/height.
    flutter_xtime=(10, 17), flutter_width=(40, 90),
    flutter_ytime=(10, 17), flutter_height=(40, 60),
    ## These two properties are key for the effect. They'll start anywhere,
    ## and disappear after the animation is done.
    start_anywhere=True, lifetime=1.0,
    ## This means that if a particle goes offscreen from the fluttering motion,
    ## it is immediately removed and a new one spawned.
    strict_offscreen=True,
    ## frame_time_range means the frozen version of this animation will always
    ## show actual fireflies rather than the fade in/out period
    animation=False, frame_time_range=(0.2, 0.8))
image dust_midground = CreateFlutterParticles(
    image=firefly_blink("dust2", zoom=1.5), particle_size=50, fast=False,
    ## Not quite as many fireflies in the midground
    amount=10, xspeed=-5, yspeed=10, distribute_fast_start=0.5,
    ## These fireflies have a bigger flutter width and height
    flutter_xtime=(4, 7), flutter_ytime=(4, 7),
    flutter_width=(40, 200), flutter_height=(40, 90),
    start_anywhere=True, lifetime=1.0, strict_offscreen=True,
    animation=False, frame_time_range=(0.2, 0.8))
image dust_foreground = CreateFlutterParticles(
    image=firefly_blink("dust1", zoom=2.0), particle_size=90, fast=False,
    ## These are the biggest fireflies, closest to the camera. There's only two
    ## of them, so there's a delay for when they reappear.
    amount=2, xspeed=-5, yspeed=10, distribute_fast_start=0.5,
    delay=(0.0, 0.5),
    ## They also have the largest flutter distance
    flutter_xtime=(4, 7), flutter_ytime=(4, 7),
    flutter_width=(120, 300), flutter_height=(120, 150),
    start_anywhere=True, lifetime=1.0, strict_offscreen=True,
    animation=False, frame_time_range=(0.2, 0.8))

screen bedmap:

    imagemap: 
        auto "images/bg_bed_%s.png"

        hotspot(321,204,50,84) action Jump("keys")
        hotspot(12,471,225,305) action Jump("planttwo")
        hotspot(408,127,238,447) action Jump("mirror")
        hotspot(819,485,151,83) action Jump("oatmeal")
        hotspot(1521,509,93,45) action Jump("phone") 
        hotspot(1340,653,556,266) action Jump("books")
        hotspot(1633,325,223,223) action Jump("plantone")          

    imagebutton auto "images/couch_%s.png" focus_mask True action Jump("bed")
    imagebutton auto "images/id_%s.png" focus_mask True action Jump("id")
    imagebutton auto "images/turn_%s.png" focus_mask True action Jump("pcmapScene")

    add "dust_background"
    add "dust_midground"
    add "dust_foreground"

screen pcmap:

    imagemap: 
        auto "images/bg_pc_%s.png"

        hotspot(713,360,387,261) action Jump("pc")
        hotspot(1206,699,264,345) action Jump("laundry")
        hotspot(1102,520,83,94) action Jump("meds")
 
        #only accessible in scenario 3
        if persistent.playthroughNumber >= 3:
            hotspot(30,309,322,671) focus_mask True action Jump("guitar") 
            hotspot(1378,221,214,187) action Jump("picture")
            imagebutton auto "images/camellia_%s.png" focus_mask True action Jump("camellia")
            imagebutton auto "images/alyssum_%s.png" focus_mask True action Jump("alyssum")

    imagebutton auto "images/turn_%s.png" focus_mask True action Jump("bedmapScene")

    add "dust_background"
    add "dust_midground"
    add "dust_foreground"

screen scen3pcmap:

    imagemap: 
        auto "images/bg_pc_%s.png"

        #only accessible in scenario 3, in order
        if itemsInteracted == 0:
            hotspot(1378,221,214,187) action Jump("picture")
        if itemsInteracted == 1:
            imagebutton auto "images/camellia_%s.png" focus_mask True action Jump("camellia")
        if itemsInteracted == 2:
            hotspot(30,309,322,671) focus_mask True action Jump("guitar") 
        if itemsInteracted == 3:            
            imagebutton auto "images/alyssum_%s.png" focus_mask True action Jump("alyssum")