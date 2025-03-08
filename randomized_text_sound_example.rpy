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
    sml "fjksdhfjkdsh fjksdfh kjsdfhjdksf hksjdfhsjkdfh ksjdfhjskd hfkjdsh fkjsdhf kjsdhf jksdhf kjsdhf kjsdhf kjsdhfjk sdhfkj sdhfkjsfh kjshdf kjsdhjfk"
    sml "fjksdhfjkdsh {w=.25}fjksdfh {w=.25}kjsdfhjdksf {w=.25}hksjdfhsjkdfh {w=.25}ksjdfhjskd {w=.25}hfkjdsh {w=.25}fkjsdhf {w=.25}kjsdhf {w=.25}jksdhf {w=.25}kjsdhf {w=.25}kjsdhfk"
    sml "fjksdhfjkdsh fjksjk sdhfkj sdhfkjsfh kjshdf kjsdhjfk"
    extend " fjksdhfjkdsh fjksdsh fkjsdhf kjdhf kjs kjsdhfjk sj kjsdhjfk"
    sml "{cps=15}fsd jlkhsdf jlksfd lkjsdf kjlsdf lkjsfdlkjsflkjdfjklsdf fdsfsd"
