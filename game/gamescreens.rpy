#######################################################################################################
#                                                                                                     #
#                                             IMAGEMAPS                                               #
#                                                                                                     #
#######################################################################################################


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