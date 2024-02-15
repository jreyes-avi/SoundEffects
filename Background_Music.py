# description: 
from earsketch import *

setTempo(120)

pointA = 1
pointB = 3.5
pointC = 7
pointD = 8.5
pointE = 10

background_music = ELECTRO_MOTORBASS_005
second_part = ELECTRO_DRUM_MAIN_BEAT_004
first_transition = RD_POP_SFX_NOISEDROP_1

fitMedia(background_music, 1, pointA, pointC)
setEffect(1, VOLUME, GAIN, 12)

setEffect(1, VOLUME, GAIN, 12, 6, 0, pointC)

fitMedia(first_transition, 2, pointC, pointD)

setEffect(1, FILTER, FILTER_FREQ, 1500, 1, 2000, 8.5)
setEffect(2, FILTER, FILTER_FREQ, 2000, 7, 2000, 8.5)


for i in range(6):
    fitMedia(EIGHT_BIT_VIDEO_GAME_LOOP_014, 3, 8 + 2*i, 10 + 2*i)
    fitMedia(RD_FUTURE_DUBSTEP_SFX_1, 4, 9 + 2*i, 10 + 2*i)
    
fitMedia(Y46_FX_2, 3, 20, 22)
