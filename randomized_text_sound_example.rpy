init python:

    def sml_speak(event, **kwargs):
        beeps = 0
        while beeps < 50: # To avoid an infinite loop
            randosound = renpy.random.randint(1, 5)
            if event == "show":
                if randosound == 1:
                    renpy.sound.queue("audio/sml1.wav", channel="sound", loop=False)
                elif randosound == 2:
                    renpy.sound.queue("audio/sml2.wav", channel="sound", loop=False)
                elif randosound == 3:
                    renpy.sound.queue("audio/sml3.wav", channel="sound", loop=False)
                elif randosound == 4:
                    renpy.sound.queue("audio/sml4.wav", channel="sound", loop=False)
                elif randosound == 5:
                    renpy.sound.queue("audio/beeps/sml5.wav", channel="sound", loop=False)
            elif event == "slow_done" or event == "end":
                renpy.sound.stop(channel="sound")
            beeps += 1

image sml neutral = "images/sml.webp"

define sml = Character("Senate Majority Leader", namebox_background="gui/sml_namebox.webp", window_background ="gui/sml_textbox.webp", color="#272020", what_color="#ffeda3", voice_tag="sml", image="sml", callback=sml_speak)


label start:
    show sml neutral at center with dissolve
    sml "fjksdhfjkdsh fjksdfh kjsdfhjdksf hksjdfhsjkdfh ksjdfhjskd hfkjdsh fkjsdhf kjsdhf jksdhf kjsdhf kjsdhf kjsdhfjk sdhfkj sdhfkjsfh kjshdf kjsdhjfk"
    sml "fjksdhfjkdsh {w=.25}fjksdfh {w=.25}kjsdfhjdksf {w=.25}hksjdfhsjkdfh {w=.25}ksjdfhjskd {w=.25}hfkjdsh {w=.25}fkjsdhf {w=.25}kjsdhf {w=.25}jksdhf {w=.25}kjsdhf {w=.25}kjsdhfk"
    sml "fjksdhfjkdsh fjksjk sdhfkj sdhfkjsfh kjshdf kjsdhjfk"
    extend " fjksdhfjkdsh fjksdsh fkjsdhf kjdhf kjs kjsdhfjk sj kjsdhjfk"
    sml "{cps=15}fsd jlkhsdf jlksfd lkjsdf kjlsdf lkjsfdlkjsflkjdfjklsdf fdsfsd"