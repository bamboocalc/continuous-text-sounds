init python:

##############################################################################
# This function is optional. Only include it if you want automatic pauses between punctuation
    def typography(what) :
        replacements = [
                ('. ','. {w=.2}'), # Moderate pause after periods
                ('? ','? {w=.25}'), # Long pause after question marks
                ('! ','! {w=.25}'), # Long pause after exclamation marks
                (', ',', {w=.15}'), # Short pause after commas
        ]
        for item in replacements:
            what = what.replace(item[0],item[1])
        return what
    config.say_menu_text_filter = typography # This ensure the text block has the same ID value, even after all the replacements are made
##############################################################################

##############################################################################
    # This function makes the continuous text sounds
    def text_sounds(event, interact=False, **kwargs):
        if event == "show": # If textbox is shown
            what = renpy.store._last_say_what # Grabs the text that was most recently spoken on-screen
            if what:
                sound_count = len(what)
            else:
                sound_count = 5
            for _ in range(sound_count): # Creates a sound queue based on how many characters are in the dialog block
                randosound = renpy.random.randint(1, 11)
                renpy.sound.queue(f"audio/sml{randosound}.wav", channel="sound", loop=False)
        elif event == "end" or event == "slow_done": # If there is a pause in the dialog or the text has finished displaying
            renpy.sound.stop(channel="sound")
##############################################################################

image sml neutral = "images/sml.webp"

# Make sure the "callback" function is the same name as our text sounds function
define sml = Character("Senate Majority Leader", namebox_background="gui/sml_namebox.webp", window_background ="gui/sml_textbox.webp", color="#272020", what_color="#ffeda3", voice_tag="sml", image="sml", callback=text_sounds)


label start:
    show sml neutral at center with dissolve
    sml "cap. gyatt.. . . . .. bussy . . . .sksksksk, rizz, jam, moot, awoooooga. and I , , ,, Ooooooop! Ohio? Yes??!?!?!??!?!?!??!?!?!??!?!?? No more news no more news no more news test . . .. . .. .. CatJam"
    extend " fjks, dh....fjkdsh fjks..d,sh fkjsd. hf , ,  kjdhf  , kjs kjsdhfjk sj kjsdhjfk"
