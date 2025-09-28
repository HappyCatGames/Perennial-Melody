init python:

    def setPlaythroughNumber():
        return 1
    
    class InteractibleItem:
        def __init__(self, name, currentIterationCount, maxIterationCount, isActive, isInteracted, canBeInteracted, itemLocation):
            self.name = name
            self.currentIterationCount = currentIterationCount
            self.maxIterationCount = maxIterationCount
            self.isActive = isActive
            self.isInteracted = isInteracted
            self.canBeInteracted = canBeInteracted
            self.itemLocation = itemLocation

    keys = InteractibleItem("keys", 0, 3, False, False, True, "bedmap")
    bed = InteractibleItem("bed", 0, 3, False, False, True, "bedmap")
    idCard = InteractibleItem("idCard", 0, 3, False, False, True, "bedmap")
    books = InteractibleItem("books", 0, 3, False, False, True, "bedmap")
    plant_1 = InteractibleItem("plant_1", 0, 3, False, False, True, "bedmap")
    plant_2 = InteractibleItem("plant_2", 0, 3, False, False, True, "bedmap")
    oatmeal = InteractibleItem("oatmeal", 0, 3, False, False, True, "bedmap")
    mirror = InteractibleItem("mirror", 0, 3, False, False, True, "bedmap")
    phone = InteractibleItem("phone", 0, 3, False, False, True, "bedmap")

    laundry = InteractibleItem("laundry", 0, 3, False, False, True, "pcmap")
    meds = InteractibleItem("meds", 0, 3, False, False, True, "pcmap")
    pc = InteractibleItem("pc", 0, 3, False, False, True, "pcmap")

    picture = InteractibleItem("picture", 0, 3, False, False, True, "pcmap")
    camellia = InteractibleItem("camellia", 0, 4, False, False, True, "pcmap")
    guitar = InteractibleItem("guitar", 0, 8, False, False, True, "pcmap")
    alyssum = InteractibleItem("keys", 0, 5, False, False, True, "pcmap")

    button_sfx_list = ["audio/pageflip_01.wav", "audio/pageflip_02.wav", "audio/pageflip_03.wav", "audio/pageflip_04.wav"]
    button_bg_list = [["gui/button/button_bg_01_idle.png", "gui/button/button_bg_01_hover.png"], ["gui/button/button_bg_02_idle.png", "gui/button/button_bg_02_hover.png"], ["gui/button/button_bg_03_idle.png", "gui/button/button_bg_03_hover.png"], ["gui/button/button_bg_04_idle.png", "gui/button/button_bg_04_hover.png"], ["gui/button/button_bg_05_idle.png", "gui/button/button_bg_05_hover.png"], ["gui/button/button_bg_06_idle.png", "gui/button/button_bg_06_hover.png"],]
    
    def assessRequirements(interactibleItem):
        if itemsInteracted <= 5 and interactibleItem.isActive == False:
            if hasKeys == False or hasPhone == False:
                return False
            if hasKeys == True and hasPhone == True:
                return True

    def setCurrentLocation(interactibleItem):
        return interactibleItem.itemLocation

    def resetItemInteractedStatus(interactibleItem):
        return False

    def randomizeAudio():
        return renpy.random.choice(button_sfx_list)

    def randomizeButton():
        return renpy.random.choice(button_bg_list)

    def rotation():
        return renpy.random.randint(-5, 5)

                   
