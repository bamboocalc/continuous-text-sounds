init python:
    import random
##############################################################################
# This function is optional. Only include it if you want automatic pauses between punctuation
    def typography(what):
        replacements = [
                ('. ','. {w=.2}'), # Moderate pause after periods
                ('? ','? {w=.25}'), # Long pause after question marks
                ('! ','! {w=.25}'), # Long pause after exclamation marks
                (', ',', {w=.15}'), # Short pause after commas
        ]
        for item in replacements:
            what = what.replace(item[0],item[1])
        return what
    config.say_menu_text_filter = typography # This ensures the text block has the same ID value, even after all the replacements are made
##############################################################################

##############################################################################
    # This function makes the continuous text sounds
    def text_sounds(event, interact=False, **kwargs):
        if event == "show": # If textbox is shown
            what = renpy.store._last_say_what # This grabs the text that was most recently spoken on-screen
            if what:
                sound_count = len(what)
            else:
                sound_count = 5
            for _ in range(sound_count): # This creates a sound queue based on how many characters are in the dialog block
                randosound = renpy.random.randint(1, 11) # This generates a random number between 1 and 11 inclusive. Change this based on how many sound files you have
                renpy.sound.queue(f"audio/popcat{randosound}.wav", channel="sound", loop=False) # Change "popcat" to the name of your sound file
        elif event == "end" or event == "slow_done": # This stops the text sounds if there is a pause in the dialog or the text has finished displaying
            renpy.sound.stop(channel="sound")
##############################################################################

##############################################################################
# This function is an alternative to the above "text_sounds" function. This one plays text sounds at a rate that is based on the current CPS. 
# A slower CPS means that the sounds play at a slower rate. A faster CPS means the sounds play at a faster rate.
# The current limitation with this function, is that it can only handle one text speed per dialog block. It cannot switch between speeds within the same dialog block.
# You need to begin a dialog block with a {cps=} tag in order for this function to use that speed.
# Example:
#    ce "{cps=90}The text sounds will play one after another with almost no pauses in between."
#    ce "{cps=5}The text sounds will have a noticeable pause between each char"
#    ce "{cps=5}Despite the increase in character speed midway through this dialog block, {cps=190} the text sounds will remain at the lower speed. The function will only use the first instance of the CPS tag in a dialog block, and ignore the others"

init python:
    import random, re

    renpy.music.register_channel("textsound", "sfx", False) # Add a new sound channel for the text sounds so that they don't overlap with anything else

    _TAG = re.compile(r'{cps=(\d+)}') # Use regex to find and store the first instance of the {cps=} tag in a character dialog block

    def adaptive_text_sounds(event, interact=True, **kw):
        if event == "show":
            renpy.sound.stop(channel="textsound")
            raw  = renpy.store._last_say_what or ""
            text = renpy.substitute(raw)
            cps  = (kw.get("slow_cps") or kw.get("cps") or renpy.store.preferences.text_cps)

            for chunk in _TAG.split(text):
                if chunk.isdigit():
                    cps = int(chunk)
                    continue
                pause = 0 if cps <= 0 else 1.0 / cps

                for char in chunk:
                    if not char.isspace():
                        renpy.sound.queue(f"audio/popcat{random.randint(1,11)}.wav",channel="textsound") # Replace "audio/popcat{random.randint(1,11)}.wav" with sound files of your choice
                    if pause:
                        renpy.sound.queue(f"<silence {pause}>", channel="textsound")

        elif event in ("slow_done", "end"):
            renpy.sound.stop(channel="textsound")

##############################################################################

# Make sure the "callback" function is the same name as our text sounds function
define e = Character("Eileen", callback=text_sounds)
define ce Character("Cooler Eileen", callback=adaptive_text_sounds)

label start:
    show eileen neutral at center with dissolve
    e "cap. gyatt.. . . . .. bussy . . . .sksksksk, rizz, jam, moot, awoooooga. and I , , ,, Ooooooop! Ohio? Yes??!?!?!??!?!?!??!?!?!??!?!?? No more news no more news no more news test . . .. . .. .. CatJam"
    extend " fjks, dh....fjkdsh fjks..d,sh fkjsd. hf , ,  kjdhf  , kjs kjsdhfjk sj kjsdhjfk"
    ce "THIS TEST THIS TEST THIS TEST THIS TEST THIS TEST THIS TEST THIS TEST"
    ce "{cps=7}SLOW SLOW SLOW SLOW SLOW SLOW {/cps} {cps=90}FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST FAST "
    ce " e e e ee e e e ee e e e ee e e  e e e ee e e e ee e e e eee ee e e e ee e e e ee e e e ee e e e ee e e e ee e e e ee e e e ee e e e ee e e e ee e e e ee"
    ce "{cps=90}AA AHAHAH AHAHHA HAHAH AHAH AH HAH AHAH HA HA HAHAHAH AHAH HA HAHAH AH AHHAH AH AH AH AH AH HA H AHAH H AHAH HA HAHAH AH AHHAH AH AH AH AH AH HA H AHAH AH AH"


