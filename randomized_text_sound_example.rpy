init python:

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

# Make sure the "callback" function is the same name as our text sounds function
define e = Character("Eileen", callback=text_sounds)

label start:
    show eileen neutral at center with dissolve
    e "cap. gyatt.. . . . .. bussy . . . .sksksksk, rizz, jam, moot, awoooooga. and I , , ,, Ooooooop! Ohio? Yes??!?!?!??!?!?!??!?!?!??!?!?? No more news no more news no more news test . . .. . .. .. CatJam"
    extend " fjks, dh....fjkdsh fjks..d,sh fkjsd. hf , ,  kjdhf  , kjs kjsdhfjk sj kjsdhjfk"
