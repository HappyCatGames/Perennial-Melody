#######################################################################################################
#                                                                                                     #
#                                          INIT VARIABLES                                             #
#                                                                                                     #
#######################################################################################################

define KANADE = Character(_("KANADE"), color="f9f3ea")
define HISAE = Character(_("HISAE"), color="043349", namebox_background="gui/namebox_hisae.png")
define NATSUME = Character(_("NATSUME"), color="f9f3ea", namebox_background="gui/namebox_natsume.png")
define KANA = Character(_("KANA"), color="f9f3ea")
define SAE = Character(_("SAE"), color="043349", namebox_background="gui/namebox_hisae.png")
define UNKNOWN = Character(_("????"), color="f9f3ea")
define n = nvl_narrator

default itemsInteracted = 0
default hasKeys = False
default hasPhone = False

default areEndingRequirementsMet = False

default currentLocation = ""

default necessaryForEnding = ""
default trueEnd = False

default persistent.playthroughNumber = 1
default persistent.allRoutesUnlocked = False

#######################################################################################################
#                                                                                                     #
#                                           GAME START                                                #
#                                                                                                     #
#######################################################################################################

label start:

    python:
        keys.isInteracted = False
        bed.isInteracted = False
        idCard.isInteracted = False
        books.isInteracted = False
        plant_1.isInteracted = False
        plant_2.isInteracted = False
        oatmeal.isInteracted = False
        mirror.isInteracted = False
        laundry.isInteracted = False
        meds.isInteracted = False
        phone.isInteracted = False
        pc.isInteracted = False
        picture.isInteracted = False
        camellia.isInteracted = False
        guitar.isInteracted = False
        alyssum.isInteracted = False

        keys.isActive = False
        bed.isActive = False
        idCard.isActive = False
        books.isActive = False
        plant_1.isActive = False
        plant_2.isActive = False
        oatmeal.isActive = False
        mirror.isActive = False
        laundry.isActive = False
        meds.isActive = False
        phone.isActive = False
        pc.isActive = False
        picture.isActive = False
        camellia.isActive = False
        guitar.isActive = False
        alyssum.isActive = False

        keys.currentIterationCount = 0
        bed.currentIterationCount = 0
        idCard.currentIterationCount = 0
        books.currentIterationCount = 0
        plant_1.currentIterationCount = 0
        plant_2.currentIterationCount = 0
        oatmeal.currentIterationCount = 0
        mirror.currentIterationCount = 0
        laundry.currentIterationCount = 0
        meds.currentIterationCount = 0
        phone.currentIterationCount = 0
        pc.currentIterationCount = 0
        picture.currentIterationCount = 0
        camellia.currentIterationCount = 0
        guitar.currentIterationCount = 0
        alyssum.currentIterationCount = 0


    label route_choice:

        $ quick_menu = True

        stop music fadeout 0.5

        if persistent.allRoutesUnlocked == True:
            
            scene black

            menu:
                "Would you like to start from a specific route?"

                "ROUTE 1: childhood dreams":
                    $ persistent.playthroughNumber = 1
                "ROUTE 2: points of intersection":
                    $ persistent.playthroughNumber = 2
                "ROUTE 3: the me that you know":
                    $ persistent.playthroughNumber = 3

    label beginning:                
    
        if persistent.playthroughNumber < 3:

            scene bg bed dark with fade
            play music "audio/News.wav"

            "You hate music. You said that with your whole heart, hands curled into tiny fists." with moveinbottom
            "It's a shame that you work in the music industry now, a shitty cog in a shitty machine. It's fine, it's just a first step toward a fulfilling and stable job career."
            "Your boss was general counsel for the biggest entertainment company to come out of Japan." 
            "If you did well enough here, surely, you'd be promoted to associate, then to partner, and then you could kick your feet up and relax for the rest of your working existence."
            "Not to say it'd be easy. It'd probably be the most miserable years of your adult life, but at least at the end of the day, you'd be rich."
            "But."
            "You hate it, really. Music."
            "Hisae Shimozaki looked at you like you said you like to eat babies. She raised her messy eyebrows, and her dead gaze was a little deader."
            "{i}\"Then what do you expect to do with that?\"{/i}"
            "She pointed at your guitar. You held it close to your chest."
            "That's right. What did you expect to do with that?"
            "It didn't matter, anyway. She moved to a different prefecture the following year and any dream of becoming a rockstar shattered with her. Fifteen years later, the two of you had the misfortune of meeting again."
            KANADE "In the end, the thing I hate more is you, after all."
        
        if persistent.playthroughNumber >= 3:

            scene bg train bw with fade
            play music "audio/ChildHood Memories.wav"

            UNKNOWN "Kana-chan... do you think that music can change people?"
            UNKNOWN "I know that sounds pretty stupid but, seriously–!! Don't laugh."
            UNKNOWN "It's just. I've seen the way you get with Shimozaki-san."
            UNKNOWN "I think it's good, what the two of you have." 
            UNKNOWN "I hope you can always cherish each other's friendship."
            KANA  "Jeez, way to make it sound so serious." 
            KANA "I hope we can always play together." 
            KANA "Playing with Sae-kun is like a dream to me." 
            UNKNOWN "What are you, a maiden in love?" 
            UNKNOWN "Leave a bit for the rest of us!"
            KANA "Don't be ridiculous ▮▮▮▮▮▮-chan!" 
            KANA "Come on, we'll be late for the bus."

            "The two of you hold hands as you run towards the stop."
            "On the other side of the road, underneath the flickering street lights–"

            UNKNOWN "Oh, there's Shimozaki-san!" 
            KANA "Sae-kun looks kind of busy... "
            UNKNOWN "It'd be rude to not say hi!"
            UNKNOWN "H—eeey!! Shimozaki-san!"
            KANA "▮▮▮▮▮▮-chan! Quiet down!" 

            "Sae-kun struck a particularly sharp image that afternoon. It was raining. Her hair was short, jaw length. She had pieces that stuck out like fox ears, much to her annoyance, Kana knows." 
            "She wears her gakuran over her shoulders. Her sailor style blouse is black and missing a tie. She's waiting for the train." 

            UNKNOWN "Aww... you're no fun, Kana-chan."
            UNKNOWN "But it's nice to see this side of Shimozaki-san! The jacket looks so good! It's a shame we go to different schools."
            UNKNOWN "You're so lucky–"
            KANA "Yeah, yeah..."
            KANA "Come on, let's go."

            "You feel her gaze. You look back."
            "She's gone. The train conductor does one final call for passengers."
            "You think about running after her." 

            UNKNOWN "Kana-chan?"
            KANA "Sorry, I was spacing out. Let's go."

            show bg pc bw with dissolve

            KANADE "Shit. Did I oversleep?" 

            "You wipe the saliva from the corner of your mouth with the back of your hand. It wouldn't be the first time you fell asleep editing something but..."

            "That was different."

            "You haven't thought about Hisae Shimozaki like that for a long time."

            "It's usually the annoying and grating laugh or the bone white bass." 

            "You sit straight up on your office chair and stretch your arms out."

            KANADE "Ugh."

            "You take your journal out and check your agenda. You have an hour before you need to leave, or else traffic will be a real nightmare."



        $ _window_hide()

        play sound "audio/pageflip_01.wav"

        if persistent.playthroughNumber < 3:
            show first todo with moveinbottom
        elif persistent.playthroughNumber >= 3:
            show second todo with moveinbottom

        pause
        
        play sound "audio/pageflip_02.wav"

        if persistent.playthroughNumber < 3:
            hide first todo with moveoutbottom
        elif persistent.playthroughNumber >= 3:
            hide second todo with moveoutbottom

        

        scene bg bed bw with dissolve
        play music "audio/Bass Groove Revival.wav"

        if persistent.playthroughNumber < 3:
            KANADE "I really need to get going." with moveinbottom
            "You open your journal. It's a combination bullet journal, planner, organizer, keeper of all secrets and crimes. It's easier to keep things organized this way. It's practical." 
            "A phone can bug out. A notebook cannot."

        if persistent.playthroughNumber >= 3:
            menu:
                "I need to focus.":
                    "It's just a dream. A memory from a long time ago. Hisae Shimozaki said it herself. You were young back then. Any sort of attachment to that time was silly."
                    "You needed to focus on getting out the door."
                    $ trueEnd = False

                "I have some time.":
                    "The dream has you feeling a little nostalgic. Your gaze flickers to the other side of the room." 
                    $ trueEnd = True

        if trueEnd == False:
            KANADE "I have about fifteen minutes... am I missing anything?"
            call screen bedmap

        #this doesn't work :-/
        hide window with moveoutbottom

        if trueEnd:
            play music "audio/Sadness.wav"
            hide screen iteration_counter
            call screen scen3pcmap with dissolve

    
    #######################################################################################################
    #                                                                                                     #
    #                                         BED SCENE ITEMS                                             #
    #                                                                                                     #
    #######################################################################################################


    label keys:
        $ keys.isInteracted = True
        $ keys.currentIterationCount += 1
        $ currentLocation = setCurrentLocation(keys)

        show screen iteration_counter(keys)

        if keys.currentIterationCount == 1:
            "Your keys. You have a mascot charm for Setsugekka on the carabiner that keeps your life together." 
            "It's a white bunny in a kimono with a snowflake, flower, and moon charm bracelet."

        if keys.currentIterationCount == 2:
            "Your keys. You're the only one who drives on a regular basis." 
            "You got your license in the States. When you came back, you decided it was the most important part of your transition to adult life." 
            "A car gives you wings, after all."

        if keys.currentIterationCount == 3:

            "Your keys. You absolutely cannot leave the house without them."
            $ hasKeys = True
            $ keys.currentIterationCount = 0

            $ areEndingRequirementsMet = assessRequirements(keys)

            if areEndingRequirementsMet == False:
                jump hurryUp
            if areEndingRequirementsMet == True:
                jump endingDecisionBlock

        jump bedmapScene

    label planttwo:
        $ currentLocation = setCurrentLocation(plant_2)
        if plant_2.isInteracted == False and itemsInteracted == 5:
            jump hurryUp  

        if plant_2.isInteracted == False and itemsInteracted < 5:
            $ itemsInteracted += 1  
           
        $ plant_2.isInteracted = True
        $ plant_2.isActive = True
        $ plant_2.currentIterationCount += 1 

        show screen iteration_counter(plant_2)
        
        if plant_2.currentIterationCount == 1:
            "Rosemary. It's part of your leafy green section. After your azalea, these little ones were the next to join your journey into making full use of your green thumb." 
            "You actually had to study quite a bit to accommodate all of these plants and make sure they were all taken care of properly." 
            "Sometimes you think that's why Mr. Shimozaki made you Setsugekka's manager. You're good at taking care of people."

            HISAE "Gross. You're such a busybody, Manager-chan."

        if plant_2.currentIterationCount == 2:
            "Hyacinth. This is one of your favorites. You have one in purple, one in pink, and one in white." 
            "You're hoping to crossbreed for a softer color, but any time you've made the attempt, it's been a bit of a disappointment."

        if plant_2.currentIterationCount == 3:
            "Wisteria. Shit. When was the last time you watered this?"
            $ plant_2.isActive = False
            $ plant_2.currentIterationCount = 0

            $ areEndingRequirementsMet = assessRequirements(plant_2)

            if itemsInteracted == 5 and areEndingRequirementsMet == False and plant_2.isActive == False:
                jump hurryUp

        jump bedmapScene

    label mirror:
        $ currentLocation = setCurrentLocation(mirror) 

        if mirror.isInteracted == False and itemsInteracted == 5:

            jump hurryUp

        if mirror.isInteracted == False:
            $ itemsInteracted += 1
           
        $ mirror.isInteracted = True
        $ mirror.isActive = True
        $ mirror.currentIterationCount += 1     

        show screen iteration_counter(mirror)     

        if mirror.currentIterationCount == 1:
            "That's you!"

        if mirror.currentIterationCount == 2:
            "That's your mirror. It's in front of your bed because you need to be able to look at yourself first thing in the morning."

        if mirror.currentIterationCount == 3:
            "That's your mirror. It's a feng shui practitioner's nightmare." 
            "Everyone knows that keeping it next to your bed the way that you do is bad for everything ever. Except you, of course." 
            "You need it for efficiency."

        if mirror.currentIterationCount == mirror.maxIterationCount:
            $ mirror.isActive = False 
            $ mirror.currentIterationCount = 0

            $ areEndingRequirementsMet = assessRequirements(mirror)

            if itemsInteracted == 5 and areEndingRequirementsMet == False and mirror.isActive == False:
                jump hurryUp

        jump bedmapScene

    label oatmeal:
        $ currentLocation = setCurrentLocation(oatmeal)
        if oatmeal.isInteracted == False and itemsInteracted == 5:
            jump hurryUp 

        if oatmeal.isInteracted == False:
            $ itemsInteracted += 1
           
        $ oatmeal.isInteracted = True
        $ oatmeal.isActive = True
        $ oatmeal.currentIterationCount += 1 

        show screen iteration_counter(oatmeal)
        

        if oatmeal.currentIterationCount == 1:
            "A bowl of oatmeal. You forgot to finish it earlier and haven't had a chance to put it away." 
            "It's brown sugar and cinnamon. A practical and delicious treat."

        if oatmeal.currentIterationCount == 2:
            "A bowl of oatmeal. You think about the latest Ti*ktok interview that you edited. Setsugekka's \"Firsts and Flops.\"" 
            "Everyone took their part of the interview seriously but when it came to food items, Hisae Shimozaki wouldn't shut up."
            HISAE "My first goes French fries. Perfect potato existence. What isn't there to enjoy." 
            HISAE "My flop? Ugh, oatmeal. Porridge. Anything in between. Gruel has no place in my palate. It should be solid, or it should be soup."
            "The clip went viral. She's the 21st century Marie Antoinette. Let them eat over-processed garbage."

        if oatmeal.currentIterationCount == 3:
            "A bowl of oatmeal. There's a gnat on the edge of the bowl. Your stomach hurts to see it."
            $ oatmeal.isActive = False
            $ oatmeal.currentIterationCount = 0

            $ areEndingRequirementsMet = assessRequirements(oatmeal)

            if itemsInteracted == 5 and areEndingRequirementsMet == False and oatmeal.isActive == False:
                jump hurryUp

        jump bedmapScene

    label bed:
        $ currentLocation = setCurrentLocation(bed)
        if bed.isInteracted == False and itemsInteracted == 5:
            jump hurryUp 

        if bed.isInteracted == False:
            $ itemsInteracted += 1
           
        $ bed.isInteracted = True
        $ bed.isActive = True
        $ bed.currentIterationCount += 1 

        show screen iteration_counter(bed)
        

        if bed.currentIterationCount == 1:
            "It's your bed." 
            "It's a pull-out couch, your parents weren't really ready to accommodate your return after your graduation." 
            "You graduated top of your class from a prestigious law school. It's unfortunate, they said, that you couldn't get a high paying job straight out of your government externship but that was fine, so don't sweat it, dear." 
            "But you have a job now, a really good job! So, maybe, start thinking about an upgrade. It'd be good for you, Kanade."

        if bed.currentIterationCount == 2:
            "It's your bed." 
            "There's the fitted sheet, the flat sheet, both matching and a boring shade of gray. There's a comfortable warm blanket, microfiber. You got it from C*ostco. Your comforter. It's from Muji. It's a nice set piece." 
            "It goes well with the perfect number of pillows (two) and the perfect amount of space (a little more than no space). You always make your bed before you head out for the day. It's important!" 
            "It keeps you from crawling back in after a particularly bad day at the studio."

        if bed.currentIterationCount == 3:
            "It's your bed. The last time you had a proper night's rest was at least four days ago. You had your little nightcap on and nightgown on and everything. Feather in the air, and phone on do not disturb."
            $ bed.isActive = False
            $ bed.currentIterationCount = 0

            $ areEndingRequirementsMet = assessRequirements(bed)

            if itemsInteracted == 5 and areEndingRequirementsMet == False and bed.isActive == False:
                jump hurryUp

        jump bedmapScene    

    label books:
        $ currentLocation = setCurrentLocation(books)
        if books.isInteracted == False and itemsInteracted == 5:
            jump hurryUp 

        if books.isInteracted == False:
            $ itemsInteracted += 1
           
        $ books.isInteracted = True
        $ books.isActive = True
        $ books.currentIterationCount += 1 

        show screen iteration_counter(books)
        

        if books.currentIterationCount == 1:
            "You really need to put these away." 
            "You were doing some research for Mr. Shimozaki. He wants to make sure that the venues Setsugekka was using for their upcoming tour were up to par."

        if books.currentIterationCount == 2:
            "You really need to put these away." 
            "It's a full set of statutes and codes relevant to contracts law for both Japan and the United States."

        if books.currentIterationCount == 3:
            "You really need to put these away. It's just, you've been so busy." 
            "And you keep needing to refer back to them. Mr. Shimozaki, please consider getting an online database subscription, all this teeny tiny text was doing a nice job of ruining your already so-so eyesight."
            $ books.isActive = False
            $ books.currentIterationCount = 0

            $ areEndingRequirementsMet=assessRequirements(books)

            if itemsInteracted == 5 and areEndingRequirementsMet == False and books.isActive == False:
                jump hurryUp

        jump bedmapScene    

    label plantone:
        $ currentLocation = setCurrentLocation(plant_1)
        if plant_1.isInteracted == False and itemsInteracted == 5:
            jump hurryUp 

        if plant_1.isInteracted == False:
            $ itemsInteracted += 1
           
        $ plant_1.isInteracted = True
        $ plant_1.isActive = True
        $ plant_1.currentIterationCount += 1 

        show screen iteration_counter(plant_1)
        

        if plant_1.currentIterationCount == 1:
            "Azalea. This one is special." 
            "When you decided you were going to get another hobby, something that wasn't micromanaging your job or searching Hisae Shimozaki on Xtwitter (advanced search: \"cancelled\" \"girlfriend\'), your parents bought you this azalea plant." 
            "It sits on your nightstand, next to your bed. It's your strongest soldier, despite being a bit of a crybaby. The last time you moved it (you needed to make sure it was getting enough sunlight), several flowers lost their petals." 
            "They'll grow back. They always do."

        if plant_1.currentIterationCount == 2:
            "Poinsettia. {i}Christmas star{/i}." 
            "You got these at a garage sale. They're fake. Your family doesn't celebrate Christmas, at least, not to the point where you would need this sort of decoration." 
            "But it was all alone, at a garage sale. Next to a wrought iron planter and a chipped bookshelf. How could you possibly resist. So now it lives here." 
            "It's kind of ugly."

        if plant_1.currentIterationCount == 3:
            "Foxglove. {i}Dead men's bells.{/i}"
            "You don't remember how you got this plant. It was probably a gift from Natsume. She's good at returning favors."

            scene bg tunnel bw with dissolve
            "You drove her around Shinjuku after a Setsugekka meet and greet, the sprawling city lights threatening to swallow the two of you whole." 
            "She pressed her hand against the window, lovely hand splayed against the glass. Her lilac hair was in a perfect plait, worn over her shoulder."
            NATSUME "I could have taken the train."
            KANADE "It's late. I don't think management would be okay with that."
            NATSUME "Funny. Did you forget you're the final say on that sort of thing?"
            "She tears her gaze from the streetlights, eyes narrowed, but not unkind."
            KANADE "And I say it's late. We needed to bring the keyboard back to the studio, anyways."
            "When you got to the studio, she fumbled for her keys in your coat pocket." 
            "You thought about kissing her under the moonlight, but the moment passed when she unlocked the door without missing a beat. That's Setsugekka's invincible pianist for you."
            $ plant_1.isActive = False
            $ plant_1.currentIterationCount = 0

            $ areEndingRequirementsMet=assessRequirements(plant_1)

            if itemsInteracted == 5 and areEndingRequirementsMet == False and plant_1.isActive == False:
                jump hurryUp

        jump bedmapScene  

    label picture:
        $ currentLocation = setCurrentLocation(picture)
        if trueEnd == False:
            if picture.isInteracted == False and itemsInteracted == 5:
                jump pcmapScene 

        if picture.isInteracted == False and trueEnd == False:
            $ itemsInteracted += 1
           
        $ picture.isInteracted = True
        $ picture.isActive = True
        $ picture.currentIterationCount += 1 

        show screen iteration_counter(picture)
        

        if trueEnd == True:
            show bg pc bw

        if picture.currentIterationCount == 1:
            "A polaroid with the members of Setsugekka."  
            "Natsume on the far left, Hisae Shimozaki after her, Akito, a head shorter than the rest of the girls, and Haruhi in her trademarked and patented boobs and ass pose."

        if picture.currentIterationCount == 2:
            "A polaroid with the members of Setsugekka." 
            "You took this picture. The girls were on their way back from practice, each of them hauling their relevant instrument. Except Akito. She had her drumsticks in Natsume's case." 
            "Natsume had smiled with such an icy intensity that it made the resulting group shot feel a little haunted."

        if picture.currentIterationCount == 3:
            "A polaroid with the members of Setsugekka. You think about Hisae Shimozaki's expression, perfect cat like grin and sharp teeth. Her eyes are empty. There's nothing there."
            $ picture.isActive = False
            $ picture.currentIterationCount = 0
            if trueEnd:
                $ itemsInteracted += 1

        if trueEnd == False:
            jump bedmapScene 
        if trueEnd == True:
            hide screen iteration_counter
            call screen scen3pcmap 
    
    label id:
        $ currentLocation = setCurrentLocation(idCard)
        if idCard.isInteracted == False and itemsInteracted == 5:
            jump hurryUp 

        if idCard.isInteracted == False:
            $ itemsInteracted += 1
           
        $ idCard.isInteracted = True
        $ idCard.isActive = True
        $ idCard.currentIterationCount += 1 

        show screen iteration_counter(idCard)
        

        if idCard.currentIterationCount == 1:
            "It's your identification card. You need it for all Setsugekka related activities."

        if idCard.currentIterationCount == 2:
            "It's your identification card. You had a very bad stomachache on the day they took the picture." 
            "Mr. Shimozaki, general counsel of the very big music production company they all worked at, said something like, you'll be managing a very important band, despite your understanding that you were going to work as an associate attorney."

        if idCard.currentIterationCount == 3:
            "It's your identification card. Maybe you should ask for a retake. Your hair's gotten longer."
            $ idCard.isActive = False
            $ idCard.currentIterationCount = 0

            $ areEndingRequirementsMet=assessRequirements(idCard)

            if itemsInteracted == 5 and areEndingRequirementsMet == False and idCard.isActive == False:
                jump hurryUp

        if trueEnd == False:
            jump bedmapScene 
        if trueEnd == True:
            hide screen iteration_counter
            call screen scen3pcmap 


    #######################################################################################################
    #                                                                                                     #
    #                                          PC SCENE ITEMS                                             #
    #                                                                                                     #
    #######################################################################################################

    label phone:
        $ currentLocation = setCurrentLocation(phone)
        $ phone.isInteracted = True
        $ phone.isActive = True
        $ phone.currentIterationCount += 1

        show screen iteration_counter(phone)
        

        if phone.currentIterationCount == 1:
            "That's your phone. You never leave home without it."

        if phone.currentIterationCount == 2:
            "That's your phone. It's a S*amsung. You're the only one in Setsugekka without an iP*hone. Except for Akito, but you're not sure what she's using. It looks more like a Nokia than anything." 
            "Sometimes she uses it to bang out some tunes when she's tired of drumming."

        if phone.currentIterationCount == 3:

            "That's your phone. You have threads of emails to review before going into the office. You have a dozen unread messages. You have a couple of voicemails."
            "You want to leave your phone on your desk and say you left it at home, but everyone knows that you never leave home without it so it's a fool's errand to pretend."
            $ hasPhone = True
            $ phone.isActive = False
            $ phone.currentIterationCount = 0

            $ areEndingRequirementsMet=assessRequirements(phone)

            if areEndingRequirementsMet == False:
                jump hurryUp
            if areEndingRequirementsMet == True:
                jump endingDecisionBlock

        jump bedmapScene 

    label laundry:
        $ currentLocation = setCurrentLocation(laundry)
        if laundry.isInteracted == False and itemsInteracted == 5:
            jump hurryUp 

        if laundry.isInteracted == False:
            $ itemsInteracted += 1
           
        $ laundry.isInteracted = True
        $ laundry.isActive = True
        $ laundry.currentIterationCount += 1 

        show screen iteration_counter(laundry)
        

        if laundry.currentIterationCount == 1:
            "It's your laundry hamper."

        if laundry.currentIterationCount == 2:
            "It's your laundry hamper. It's empty, save for yesterday's outfit. You usually have it inside your closet, but you left something in one of the pockets."

        if laundry.currentIterationCount == 3:
            "It's your laundry hamper. It's empty, save for yesterday's outfit. You left Hisae Shimozaki's bass guitar pick in your jacket pocket, hoping for the opportunity to return it. It's a piece of plastic that looks like sea glass."
            $ laundry.isActive = False
            $ laundry.currentIterationCount = 0

            $ areEndingRequirementsMet=assessRequirements(laundry)

            if itemsInteracted == 5 and areEndingRequirementsMet == False and laundry.isActive == False:
                jump hurryUp

        jump pcmapScene 

    label pc:
        $ currentLocation = setCurrentLocation(pc) 
        if pc.isInteracted == False and itemsInteracted == 5:
            jump hurryUp

        if pc.isInteracted == False:
            $ itemsInteracted += 1
           
        $ pc.isInteracted = True
        $ pc.isActive = True
        $ pc.currentIterationCount += 1

        show screen iteration_counter(pc)
        

        if pc.currentIterationCount == 1:
            "It's your computer. You bought it off a friend who built it and decided to go full send monk meditation mode with their life. Apparently, playing Va*lorant was doing numbers on her health."

        if pc.currentIterationCount == 2:
            "It's your computer. You use it to play Minesweeper and Solitaire."

        if pc.currentIterationCount == 3:
            "It's your computer. Sometimes you make music on it. Most of the time you edit the material for Setsugekka's online presence. Today, you're supposed to get a blog post out about Haruhi's latest fashion finds in Harajuku, but it's been a really busy morning."
            $ pc.isActive = False
            $ pc.currentIterationCount = 0

            $ areEndingRequirementsMet=assessRequirements(pc)

            if itemsInteracted == 5 and areEndingRequirementsMet == False and pc.isActive == False:
                jump hurryUp

        jump pcmapScene 

    label meds:
        $ currentLocation = setCurrentLocation(meds) 
        if meds.isInteracted == False and itemsInteracted == 5:
            jump hurryUp

        if meds.isInteracted == False:
            $ itemsInteracted += 1
           
        $ meds.isInteracted = True
        $ meds.isActive = True
        $ meds.currentIterationCount += 1
        
        show screen iteration_counter(meds)

        if meds.currentIterationCount == 1:
            "It's your anti-inflammatory medication."

        if meds.currentIterationCount == 2:
            "It's your allergy medication."

        if meds.currentIterationCount == 3:
            "It's your muscle relaxant."
            $ meds.isActive = False
            $ meds.currentIterationCount = 0

            $ areEndingRequirementsMet=assessRequirements(meds)

            if itemsInteracted == 5 and areEndingRequirementsMet == False and meds.isActive == False:
                jump hurryUp

        jump pcmapScene    

    label guitar:
        $ currentLocation = setCurrentLocation(guitar)
        if guitar.isInteracted == False and itemsInteracted == 5:
            jump hurryUp

        if guitar.isInteracted == False and trueEnd == False:
            $ itemsInteracted += 1
           
        $ guitar.isInteracted = True
        $ guitar.isActive = True
        $ guitar.currentIterationCount += 1 

        show screen iteration_counter(guitar)
        

        if guitar.currentIterationCount == 1:
            "That's a guitar. You don't play."

        if guitar.currentIterationCount == 2:
            "That's a guitar. You don't play."

        if guitar.currentIterationCount == 3:
            "That's your guitar."

        if guitar.currentIterationCount == 4:
            "That's your guitar. It's been sitting in its old, dusty case for at least ten years. You left it at your parents' house when you went to another city for high school, and when you went out of the country for university and law school."

        if guitar.currentIterationCount == 5:
            "That's your guitar. You take it out of the case. You pick it up. And you feel the overwhelming urge to smash it against the floor. The wall. Your bed. Anything."

        if guitar.currentIterationCount == 6:
            "That's your guitar. Hisae Shimozaki's chicken scratch signature is still there. She thought she was so sneaky, carving away at your most prized possession. When you told her to give it back, what the hell!, she didn't even blink."

            HISAE "Aren't we going to be rockstars, Kana-chan? Live a little."
            "You were twelve."

        if guitar.currentIterationCount == 7:
            "That's your guitar. It's a Telecaster. It was a thrift store find." 
            "Your father bought it off someone else who gave up on a dream you were clutching onto with hands held tight, with nails biting into palms. Cherry red. The wood grain is gorgeous." 
            "It's the love of your life, until you realize that the girl next to you means a little more. She twirls a utility knife with a practiced flourished and slices her bass strings."
            "Again, again. She restrings. She makes magic that you can only dream of. And she does so with a heavy sigh. An Ibanez. Top of the line." 
            "A sorry about missing your entrance ceremony, your mother loves you, gift. It's white. It's snow white, ash body, ash top, pristine."
            
        if guitar.currentIterationCount == 8:
            "That's your guitar. You don't need it anymore."    
            $ guitar.isActive = False                
            $ guitar.currentIterationCount = 0
            if trueEnd == True:
                $ itemsInteracted += 1

        if trueEnd == False:
            jump pcmapScene 
        if trueEnd == True:
            hide screen iteration_counter
            call screen scen3pcmap 

    label camellia:
        $ currentLocation = setCurrentLocation(camellia)
        if camellia.isInteracted == False and itemsInteracted == 5:
            jump hurryUp
        
        if camellia.isInteracted == False and trueEnd == False:
            $ itemsInteracted += 1
           
        $ camellia.isInteracted = True
        $ camellia.isActive = True
        $ camellia.currentIterationCount += 1 

        show screen iteration_counter(camellia)
        

        if camellia.currentIterationCount == 1:
            "A winter flower. You don't like it very much. It's a deep red."
            
        if camellia.currentIterationCount == 2:
            "A winter flower." 
            "It was a spur of the moment purchase. You saw it for sale during a weekend outing." 
            "Akito said something like, huh... I didn't think they had a nursery over here. And you looked back, like an idiot." 
            "You were entranced. A deep red in a sea of snow white."

        if camellia.currentIterationCount == 3:
            "A winter flower. Hisae Shimozaki has one tattooed onto her thigh." 
            "As if she could embody anything the stupid flower means. Grace? Sophistication? A pig would be better suited." 
            "The studio's photographer has asked her time and time again to get it removed, she's a public figure, for god's sake. And Hisae Shimozaki said, with the authority of a king:"

            HISAE "You can remove it in post."
            
            "She did not say that. But you wished she did."
            "Instead, she bowed deeply."

            HISAE "I'll go back to makeup."

        if camellia.currentIterationCount == 4:
            "A winter flower. You can't help yourself when it comes to her."
            $ camellia.isActive = False
            $ camellia.currentIterationCount = 0
            if trueEnd == True:
                $ itemsInteracted += 1

        if trueEnd == False:
            jump pcmapScene 
        if trueEnd == True:
            hide screen iteration_counter
            call screen scen3pcmap 

    label alyssum:
        $ currentLocation = setCurrentLocation(alyssum)
        if alyssum.isInteracted == False and itemsInteracted == 5:
            jump hurryUp

        if alyssum.isInteracted == False and trueEnd == False:
            $ itemsInteracted += 1
           
        $ alyssum.isInteracted = True
        $ alyssum.isActive = True
        $ alyssum.currentIterationCount += 1 

        show screen iteration_counter(alyssum)
        

        if alyssum.currentIterationCount == 1:
            "A spring flower. Your beloved alyssum plant."
            
        if alyssum.currentIterationCount == 2:
            "A spring flower. Your beloved alyssum plant." 
            "It's an easy to please darling, and very resilient. Most of it is white, but you've noticed other colors starting to peek out. It's so cute."

        if alyssum.currentIterationCount == 3:
            "A spring flower. Sometimes you wonder if you come across like your beloved alyssum plant." 
            "You press a gentle index finger against a petal, and watch it fall."

        if alyssum.currentIterationCount == 4:
            "A spring flower. You can't help yourself when it comes to her. She makes you so angry. She makes you fucking angry."
            "The half-lidded gaze and the horrible grin and the, oh, well, it's been years and years, Manager-chan. I can't say I remember much of our time together at all." 
            "The terrible dye job and the beautiful nails and the perfect origami cranes, tied together with an invisible thread, one hundred, one thousand, I'll make one million cranes, Kana-chan." 
            "I'll make one million cranes if it'd make you happy."

            "{i}She was willing to do all that when you would've been happy enough standing by her side. The empty classroom and the open windows and the messy chalkboards, white dust dancing in the summer breeze.{/i}" 
            "{i}Her sailor uniform and cardigan unkempt, her dark hair short and messy.{/i}"
            "{i}Her chipped nails, her white bass, her fish eyed expression.{/i}"
            "{i}And that would've been enough. You sit on the desk across from her and answer her bassline with a rough chord.{/i}"

        if alyssum.currentIterationCount == 5:
            "A spring flower." 
            "You put your hand into the pot, tear into the roots and dig into the stems." 
            "Your stupid fucking plant."
            $ alyssum.isActive = False
            $ alyssum.currentIterationCount = 0
            if trueEnd == True:
                $ itemsInteracted += 1
                jump scenario_3

        if trueEnd == False:
            jump pcmapScene
        if trueEnd == True:
            hide screen iteration_counter
            call screen scen3pcmap

    #######################################################################################################
    #                                                                                                     #
    #                                               HUBS                                                  #
    #                                                                                                     #
    #######################################################################################################


    label bedmapScene:
        hide screen iteration_counter
        scene bg bed bw

        if areEndingRequirementsMet == True:
            jump endingDecisionBlock

        call screen bedmap

    label pcmapScene:
        hide screen iteration_counter
        scene bg pc bw

        if areEndingRequirementsMet == True:
            jump endingDecisionBlock

        call screen pcmap

    label hurryUp:

        hide screen iteration_counter

        if currentLocation == "bedmap":
            scene bg bed bw
        if currentLocation == "pcmap":
            scene bg pc bw

        "You open up your journal and scan the pages."

        if hasKeys == False and hasPhone == True:
            $ necessaryForEnding = "where are my keys?"
        if hasKeys == True and hasPhone == False:
            $ necessaryForEnding = "where is my phone?"
        if hasKeys == False and hasPhone == False:
            $ necessaryForEnding = "where are my keys and phone?"

        KANADE "Hmm... I think I've wasted enough time. I'm cutting it kind of close. I should've been out the door at least five minutes ago... [necessaryForEnding]"

        if currentLocation == "bedmap":
            call screen bedmap
        if currentLocation == "pcmap":
            call screen pcmap   


    #######################################################################################################
    #                                                                                                     #
    #                                              ENDINGS                                                #
    #                                                                                                     #
    #######################################################################################################

    label endingDecisionBlock:
        hide screen iteration_counter
        if persistent.playthroughNumber == 1:
            jump scenario_1
        if persistent.playthroughNumber == 2:
            jump scenario_2
        if persistent.playthroughNumber >= 3: 
            if guitar.isInteracted == False or alyssum.isInteracted == False or camellia.isInteracted == False or picture_interacted == False:
                jump scenario_3B_ending
            #if guitar.isInteracted == True and alyssum.isInteracted == True and camellia.isInteracted == True and picture_interacted == True and alyssum.currentIterationCount == 6:
                #jump scenario_3

    label scenario_1:

        hide screen iteration_counter
        scene bg bed dark with dissolve
        play music "audio/Ambient Lo-Fi.wav"
        "That should be everything."
        scene bg pc bw with dissolve
        "Although, your gaze lingers on the medicine bottle for another second. Just enough to let you think." 
        "It's been a long, thankless week. It's about to be another one. You shift the weight from your bag down from your shoulder to the crook of your arm."

        "Maybe an extra serving of quietdown wouldn't be too bad. You reach your hand over to the desk but stop short of picking up the little bottle."

        "There's no need. You take a deep breath. It's the nerves. You've been thinking about her a lot lately, everything comes back to Hisae Shimozaki, the eternal ghost in the corner of your room. Sae-kun, age 12, sitting on the edge of your bed, strumming."
        scene bg bed dark with dissolve

        SAE "{i}Aaa, aa, aaa.{/i}" 
        KANA "It's a good thing that you play an instrument, Sae-kun."
        SAE "Aww, you're so mean, Kana-chan."
        SAE "It's hard enough practicing bass, I can barely reach all these notes."
        KANA "{i}Aaa, aa, aaa.{/i}" 
        KANA "See, it should sound like that."
        SAE "{i}Aaa, aaaaaa, aa.{/i}"
        KANA "Now you're just being dumb."
        SAE "It's hard to do it right when it's funnier to do it wrong. You get too worked up."
        KANA "Ugh." 
        SAE "Get your guitar out. Let's try this new song out."
        SAE "I got sheet music from my dad." 
        SAE "He doesn't really like that I'm spending too much time on this, but still tells me to practice the classics."
        KANA "I don't know how classic... the Red Hot Chili Peppers are."
        SAE "It's definitely classic." 
        KANA "Okay, let's see..."
        SAE "I tabbed it out for you."
        KANA"I'm trying to learn to read it properly!"
        SAE "And you say I'm not nice to you."

        "Kana leans against Sae, their shoulders pressed together." 

        KANA "Let's go pro, Sae-kun."
        KANA "I think we could do it. Your mom could put in a good word for us at her shows."
        KANA "And then we could take over the world. We'd be international superstars."

        "Sae's expression changed, just a bit. You didn't see it then, but now. You can see the way her eyebrows furrowed, the way she leaned away." 

        SAE "You'll have to learn how to make more friends before we can do that."
        KANA "And you say I'm mean!" 

        "The peals of laughter echo in the memory."

        "Hisae moved out of the prefecture the following spring. She was quiet when she broke the news, like it didn't affect her. She didn't promise to keep in touch."

        "She said, this was for her future. There's nothing else for me except the bass, you know."
        "Kana didn't know what that meant."

        "You do, though."

        "She left for a prestigious music academy, and she never looked back." 

        scene bg school bw with dissolve

        "What could you do but follow her example? You had your parents sign you up for every cram school in the district. You placed first in all your exams." 
        "You were accepted into every high school in the prefecture, and you were an early invitee for every university after." 
        "When you decided to go out of the country for your higher education, your parents were surprised. They were supportive, of course, but they thought it was strange."

        "After all, you spent years 15 to 18 growing out your hair and hoping your DIY piercings would finally, finally close." 

        "There wasn't room for wannabe rock stars where you were going, that's all."
        "The memory is tinged with a sort of longing that you have not allowed yourself to feel for a long, long time."

        scene bg bed dark with dissolve

        "You shake it off, tuck a strand of dark hair behind your ear. You still wear it short. The shaved sides have been a pain to grow out."

        "Maybe today will be the day you say something. Maybe today, you'll tap Hisae Shimozaki's shoulder, apologize for the interruption, and ask her to meet you at the park." 

        "Maybe you'll say, it's just been a while. I want us to talk."

        "I want us to talk again, Sae-kun." 

        jump endingScene

    label scenario_2:
        hide screen iteration_counter
        scene bg bed dark with dissolve
        play music "audio/The Future Bass.wav"

        "That should be everything. You had your phone, your keys, your uncomfortable memories, all of it was ready to go and face the day." 
        "Setsugekka was on the cusp of something amazing, the prelude to a press tour and twenty sold out shows. You should be more excited for that, you should be more thrilled that your hard work was about to pay off in a way you could have never imagined."
        "But you can't stop thinking about Hisae Shimozaki."

        scene bg lobby bw with dissolve

        KANADE "Shimozaki-san...?"
        HISAE "Huh?"
        "She had dark tinted sunglasses perched on her nose. Her hair was wild and untamed, a mess of long layers and dark roots. She wore hot pants and a flowy chiffon off the shoulder blouse, a thick black belt." 
        "Her thigh had a non-descript tattoo. It looked like a head of lettuce."
        "But how could you forget her eyes. Even behind the glass, she's so tacky for wearing them indoors, god, you will never be able to forget them."
        "She looks at you, up and down."
        HISAE "Shimozaki-san is my father, you can call me Hisae..."
        HISAE "Although... do I know you?"
        "You smiled politely."
        HISAE "A...kane-chan?"
        KANADE "No."
        "Her smile never wavers. A perfect idol."
        HISAE "Kanade Sato-chi... it's been a while."
        "You wish you said something. Anything."
        "Something even like \"it's been a while, yeah.\" Or \"did you miss me? Did you even think about me, all this time away?\""
        "But the answer to that question might be worse."
        HISAE "Not really? We were twelve, Manager-chan."
        HISAE "It was nice catching up, but I do have a job to do here."
        HISAE "I have a lot of things to make up for."
        HISAE "If you will excuse me."
        "Even in your best case scenarios, it ends with you standing there, like a stupid idiot."

        jump endingScene

    label scenario_3:
        hide screen iteration_counter
        scene bg brokenplant bw with dissolve
        play music "audio/Wistful Reflections Distorted.wav"

        "You have a fistful of dirt in your hand. It's all over your table, bits and chunks have a new home on the floor. The alyssum plant is ruined." 
        "There's a part of you that hopes it never grows again, but if there's a place to grow and spread their roots, plants will come back."
        "It's why you like them so much."
        "They're so resistant to all sorts of horrible things. Maybe that's why you wanted to become like one too."
        "You can fix this. You can fix this. You always can. You can see it, you have it scripted out to the amount of breaths Hisae Shimozaki will take, her perfect nails dragging everyone down to her perfect hell." 
        "You can see Akito and Natsume and Haruhi, all shocked at your revelation, that this woman was the reason you were going to quit Setsugekka forever–" 
        "That associate attorney position be damned, you were going to make it as far away as possible from her, because it wasn't fair. "
        "You waited every day at that train station, you waited every day by that phone, you waited for Hisae Shimozaki to remember you, just a little bit. Just enough, just enough to confirm the horrible feeling inside your heart."
        "That you were in love with someone you could never have."
        "You can see her face, on the thick tome that doubled as a fashion magazine. You can see her, successful and beautiful and no longer playing bass guitar, reputation no longer marred by her playboy antics and bad attitude." 
        
        scene bg cafe bw with dissolve

        "You can see her, with those tinted glasses, pressed against the glass of the café window. You will get up, you will run out, you will leave your belongings in a worn-out booth." 
        "She'll throw her head back, and finally deign to look at you, the beloved priestess to her twisted god."
        HISAE "It's nice to see you doing well."
        KANADE "I can say the same thing to you."
        KANADE "This month's spread was beautiful."
        KANADE "Did your mother design the dress you were in?"
        KANADE "It looked like sea glass."
        HISAE "Haha, no. I've never been partial to the sea."
        HISAE "Not like you, at least."
        HISAE "I'm happy enough with the mountains."
        KANADE "Ah..."
        HISAE "Not to say it's bad."
        HISAE "Or good. Or anything."
        HISAE "It's a job."
        "She will never be satisfied." 
        "For as long as you live."
        "Chasing the eternal high of something that just belongs to her."
        KANADE "Do you want to get coffee? I have a table."
        HISAE "I need to get to my next appointment."
        "Her gaze lingers, and there's something there. In the stillness of a sacred lake, there is a ripple. She takes your hand. She squeezes."
        HISAE "Can I call you after?"
        KANADE "If you'd like."
        HISAE "Do you still have the same number..."
        "She rattles off a string of digits. Yes, you do, you do have the same number, and of course she has kept it tucked away safely in the folds of her sleeves, a litany, a prayer, a winning card."
        HISAE "Then."
        HISAE "See you later, Kanade."
        KANADE "See you later, Hisae."
        "This sort of pathetic longing."
        "This sort of happy ending. This sort of make-believe story, all of it. It makes you sick."
        
        scene bg bed dark with dissolve
        
        "You stagger, back against your pull-out couch, a mess of a room asking you to try again. Your keys. Your phone." 
        "You need to go soon. You need to face the music. You need to face the fact that if you open this door, nothing will change."
        "You will continue to live every day in Hisae Shimozaki's shadow, a stupid weed in her ice-cold sun."
        "Open the door, Kanade Sato. You need to open the door."
        "Pick yourself up off the floor. Find something else to wear. Fix your shoes and your makeup and open the door."

        jump scenario3Ending

    label endingScene:
        
        #scenario 1 & 2  
        hide screen iteration_counter
        scene bg bed dark with dissolve 

        "Of course, real life isn't so kind."
        "It'd be stupid to think that one day you could surpass her. Hisae Shimozaki, her bad bleached hair, her callused hands, her crooked teeth." 
        "Her unapproachable and empty existence, a creature made from a father's love and a mother's cool disappointment."
        "So maybe that's why you can't hate her, hate her music. Hate the way that she pours a plastic love, a torrent of camellias, of everlasting and enduring promise, to a crowd you do not belong to."
        "It makes you sick."
        "You lift your hand towards the door handle."
        "And you open the door—"

        stop music fadeout 1.0

        $ quick_menu = False

        if persistent.playthroughNumber == 1:
            scene endcard a with fade
        if persistent.playthroughNumber == 2:
            scene endcard b with fade

        $ persistent.playthroughNumber += 1

        pause

        return

    label scenario3Ending:

        "You open the door."
        "Hisae Shimozaki smiles thinly. She's got a set of keys in her hand. Her father's car is in your driveway."
        HISAE "You were running late. Band told me to come get you."
        KANADE "You can drive?"
        HISAE "Yeah."
        KANADE "Oh."
        "And sometimes, real life is worse. Every argument, every word, every perfect comeback and logical soliloquy burns under the intensity of the realization that is,"

        "You don't know Hisae Shimozaki at all."

        "She tucks a strand of dyed hair behind her pierced ear." 
        "Your matching set aches in the absence of black metal."

        HISAE "Call next time, Manager-chan."

        $ persistent.playthroughNumber += 1
        $ persistent.allRoutesUnlocked = True

        stop music fadeout 1.0 

        $ quick_menu = False
        scene endcard c with fade

        pause

        jump thankyou

    label scenario_3B_ending:

        "That's everything. Checked on the plants, put away the bowl, got your phone and keys. For all intents and purposes, you're ready to go."

        "But."

        "You look at the polaroid over your bed."

        scene bg bed bw with dissolve

        "Hisae Shimozaki stares back."

        KANADE "See you soon, Shimozaki-san."

        "You make your way out the door."

        stop music fadeout 1.0 

        $ quick_menu = False
        scene endcard d with fade

        pause

        return

    label thankyou:

        scene thankyou with fade
        pause
        jump credits

    return

label credits:

    scene bg dark with dissolve
    show screen credits() with fade

    pause

    show screen credits_2() with fade

    pause

    show screen credits_3() with fade

    pause

    show screen credits_4() with fade

    pause

    return
    
$ MainMenu()
