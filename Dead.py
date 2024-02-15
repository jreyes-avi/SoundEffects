from earsketch import *
import random
setTempo(120)

sound_choices = [RD_EDM_SFX_RAZORDROP_1, RD_ELECTRO_SFX_SYNTHDROP_1,RD_TRAP_SFX_SYNTHDROP_1]
index = 0

if index == 0:
    setEffect(1, VOLUME, GAIN, 0, 1, -20, 2)
    fitMedia(sound_choices[index], 1, 1, 2)
else:
    fitMedia(sound_choices[index], 1, 1, 2)
