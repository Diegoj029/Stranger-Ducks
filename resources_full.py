from PIL import  Image

# extracting title form the title.png image.
title_img = Image.open("title_transp.png").crop((416,0,1610,260)).convert("RGBA")
title_img = title_img.resize(list(map(lambda x:x//2 , title_img.size)))

# extracting game items and characters form the resource.png image.
player_w = Image.open("resources.png").crop((4,24,92,109)).convert("RGBA") # right facing upright alive duck - OLD VAR NAME
player_w = player_w.resize(list(map(lambda x:x//2 , player_w.size)))

player_b = Image.open("resources.png").crop((96,21,187,107)).convert("RGBA") # right facing upside-down dead duck - OLD VAR NAME
player_b = player_b.resize(list(map(lambda x:x//2 , player_b.size)))

player_w_up_r = Image.open("resources.png").crop((4,24,92,109)).convert("RGBA") # right facing upright alive duck - NEW VAR NAME
player_w_up_r = player_w_up_r.resize(list(map(lambda x:x//2 , player_w_up_r.size)))

player_b_dwn_r = Image.open("resources.png").crop((96,21,187,107)).convert("RGBA") # right facing upside-down dead duck - NEW VAR NAME
player_b_dwn_r = player_b_dwn_r.resize(list(map(lambda x:x//2 , player_b_dwn_r.size)))

player_w_dwn_r = Image.open("resources.png").crop((1208,19,1298,105)).convert("RGBA") # right facing upside-down alive duck
player_w_dwn_r = player_w_dwn_r.resize(list(map(lambda x:x//2 , player_w_dwn_r.size)))

player_b_up_r = Image.open("resources.png").crop((1302,21,1393,107)).convert("RGBA") # right facing upright dead duck
player_b_up_r = player_b_up_r.resize(list(map(lambda x:x//2 , player_b_up_r.size)))

player_w_dwn_l = Image.open("resources.png").crop((1489,21,1579,107)).convert("RGBA") # left facing upside-down alive duck
player_w_dwn_l = player_w_dwn_l.resize(list(map(lambda x:x//2 , player_w_dwn_l.size)))

player_b_up_l = Image.open("resources.png").crop((1394,22,1486,110)).convert("RGBA") # left facing upright dead duck
player_b_up_l = player_b_up_l.resize(list(map(lambda x:x//2 , player_b_up_l.size)))

player_w_up_l = Image.open("resources.png").crop((1685,22,1775,108)).convert("RGBA") # left facing upright alive duck
player_w_up_l = player_w_up_l.resize(list(map(lambda x:x//2 , player_w_up_l.size)))

player_b_dwn_l = Image.open("resources.png").crop((1591,21,1680,107)).convert("RGBA") # left facing upside-down dead duck
player_b_dwn_l = player_b_dwn_l.resize(list(map(lambda x:x//2 , player_b_dwn_l.size)))

ground_w = Image.open("resources.png").crop((3,112,2446,130)).convert("RGBA") # whole length
ground_w = ground_w.resize(list(map(lambda x:x//2 , ground_w.size)))

ground_b = Image.open("resources.png").crop((3,0,2446,18)).convert("RGBA") # whole length
ground_b = ground_b.resize(list(map(lambda x:x//2 , ground_b.size)))

# well_w = Image.open("resources.png").crop((1395,112,2446,130)).convert("RGBA")
# well_w = ground_w.resize(list(map(lambda x:x//2 , well_w.size)))

# well_b = Image.open("resources.png").crop((1395,0,2446,18)).convert("RGBA")
# well_b = ground_b.resize(list(map(lambda x:x//2 , well_b.size)))

noise_w_s = Image.open("resources.png").crop((691,38,770,85)).convert("RGBA")
noise_w_s = noise_w_s.resize(list(map(lambda x:x//2 , noise_w_s.size)))

noise_b_s = Image.open("resources.png").crop((793,44,872,92)).convert("RGBA")
noise_b_s = noise_b_s.resize(list(map(lambda x:x//2 , noise_b_s.size)))

noise_w_l = Image.open("resources.png").crop((909,24,1034,99)).convert("RGBA")
noise_w_l = noise_w_l.resize(list(map(lambda x:x//2 , noise_w_l.size)))

noise_b_l = Image.open("resources.png").crop((1069,34,1194,109)).convert("RGBA")
noise_b_l = noise_b_l.resize(list(map(lambda x:x//2 , noise_b_l.size)))

qubit_w_s = Image.open("resources.png").crop((500,40,561,89)).convert("RGBA")
qubit_w_s = qubit_w_s.resize(list(map(lambda x:x//2 , qubit_w_s.size)))

qubit_b_s = Image.open("resources.png").crop((578,42,639,90)).convert("RGBA")
qubit_b_s = qubit_b_s.resize(list(map(lambda x:x//2 , qubit_b_s.size)))

qubit_w_l = Image.open("resources.png").crop((250,26,338,97)).convert("RGBA")
qubit_w_l = qubit_w_l.resize(list(map(lambda x:x//2 , qubit_w_l.size)))

qubit_b_l = Image.open("resources.png").crop((363,28,451,99)).convert("RGBA")
qubit_b_l = qubit_b_l.resize(list(map(lambda x:x//2 , qubit_b_l.size)))

sign_w_r = Image.open("resources.png").crop((1089,29,1908,106)).convert("RGBA") # right facing H gate sign - white world
sign_w_r = sign_w_r.resize(list(map(lambda x:x//2 , sign_w_r.size)))

sign_w_l = Image.open("resources.png").crop((1917,29,2017,106)).convert("RGBA") # left facing H gate sign - white world
sign_w_l = sign_w_l.resize(list(map(lambda x:x//2 , sign_w_l.size)))

sign_b_r = Image.open("resources.png").crop((2028,24,2125,101)).convert("RGBA") # right facing H gate sign - black world
sign_b_r = sign_b_r.resize(list(map(lambda x:x//2 , sign_b_r.size)))

sign_b_l = Image.open("resources.png").crop((2136,24,2233,101)).convert("RGBA") # left facing H gate sign - black world
sign_b_l = sign_w_l.resize(list(map(lambda x:x//2 , sign_b_l.size)))

# extracting gate bits assets form the gates.png image.
ygatebit_w = Image.open("gates.png").crop((5374,7,5468,46)).convert("RGBA") # Y gate bit - white world
ygatebit_w = ygatebit_w.resize(list(map(lambda x:x//2 , ygatebit_w.size)))

ygatebit_b = Image.open("gates.png").crop((5373,73,5468,112)).convert("RGBA") # Y gate bit - black world
ygatebit_b = ygatebit_b.resize(list(map(lambda x:x//2 , ygatebit_b.size)))

zgatebit_w = Image.open("gates.png").crop((5371,129,5469,167)).convert("RGBA") # Z gate bit - white world
zgatebit_w = zgatebit_w.resize(list(map(lambda x:x//2 , zgatebit_w.size)))

zgatebit_b = Image.open("gates.png").crop((5371,194,5469,233)).convert("RGBA") # Z gate bit - black world
zgatebit_b = zgatebit_b.resize(list(map(lambda x:x//2 , zgatebit_b.size)))

notgatebit_w = Image.open("gates.png").crop((5491,10,5583,45)).convert("RGBA") # NOT gate bit - white world
notgatebit_w = notgatebit_w.resize(list(map(lambda x:x//2 , notgatebit_w.size)))

notgatebit_b = Image.open("gates.png").crop((5493,75,5582,110)).convert("RGBA") # NOT gate bit - black world
notgatebit_b = notgatebit_b.resize(list(map(lambda x:x//2 , notgatebit_b.size)))

swapgatebit_w = Image.open("gates.png").crop((5491,131,5583,164)).convert("RGBA") # SWAP gate bit - white world
swapgatebit_w = swapgatebit_w.resize(list(map(lambda x:x//2 , swapgatebit_w.size)))

swapgatebit_b = Image.open("gates.png").crop((5491,187,5583,221)).convert("RGBA") # SWAP gate bit - black world
swapgatebit_b = swapgatebit_b.resize(list(map(lambda x:x//2 , swapgatebit_b.size)))

hgatebit_w = Image.open("gates.png").crop((5618,6,5709,46)).convert("RGBA") # H gate bit - white world
hgatebit_w = hgatebit_w.resize(list(map(lambda x:x//2 , hgatebit_w.size)))

hgatebit_b = Image.open("gates.png").crop((5618,72,5709,111)).convert("RGBA") # H gate bit - black world
hgatebit_b = hgatebit_b.resize(list(map(lambda x:x//2 , hgatebit_b.size)))

# extracting gate screen assets form the gates.png image.
state_w = Image.open("gates.png").crop((8,143,141,237)).convert("RGBA") # pictogram of current state - white world
state_w = state_w.resize(list(map(lambda x:x//2 , state_w.size)))

state_b = Image.open("gates.png").crop((162,142,296,238)).convert("RGBA") # pictogram of current state - black world
state_b = state_b.resize(list(map(lambda x:x//2 , state_b.size)))

xgate_w = Image.open("gates.png").crop((325,7,799,107)).convert("RGBA") # X gate - white world
xgate_w = xgate_w.resize(list(map(lambda x:x//2 , xgate_w.size)))

xgate_b = Image.open("gates.png").crop((326,137,798,234)).convert("RGBA") # X gate - black world
xgate_b = xgate_b.resize(list(map(lambda x:x//2 , xgate_b.size)))

ygate_w = Image.open("gates.png").crop((822,8,1296,104)).convert("RGBA") # Y gate - white world
ygate_w = ygate_w.resize(list(map(lambda x:x//2 , ygate_w.size)))

ygate_b = Image.open("gates.png").crop((822,138,1295,236)).convert("RGBA") # Y gate - black world
ygate_b = ygate_b.resize(list(map(lambda x:x//2 , ygate_b.size)))

zgate_w = Image.open("gates.png").crop((1313,7,1786,104)).convert("RGBA") # Z gate - white world
zgate_w = zgate_w.resize(list(map(lambda x:x//2 , zgate_w.size)))

zgate_b = Image.open("gates.png").crop((1312,137,1787,233)).convert("RGBA") # Z gate - black world
zgate_b = zgate_b.resize(list(map(lambda x:x//2 , zgate_b.size)))

not_w = Image.open("gates.png").crop((1815,7,2289,106)).convert("RGBA") # NOT gate - white world
not_w = not_w.resize(list(map(lambda x:x//2 , not_w.size)))

not_b = Image.open("gates.png").crop((1817,137,2289,235)).convert("RGBA") # NOT gate - black world
not_b = not_b.resize(list(map(lambda x:x//2 , not_b.size)))

cnot_w = Image.open("gates.png").crop((2343,11,2822,243)).convert("RGBA") # CNOT gate - white world
cnot_w = cnot_w.resize(list(map(lambda x:x//2 , cnot_w.size)))

swap_w = Image.open("gates.png").crop((2835,10,3315,243)).convert("RGBA") # SWAP gate - white world
swap_w = swap_w.resize(list(map(lambda x:x//2 , swap_w.size)))

cnot_b = Image.open("gates.png").crop((3322,10,3804,245)).convert("RGBA") # CNOT gate - black world
cnot_b = cnot_b.resize(list(map(lambda x:x//2 , cnot_b.size)))

swap_b = Image.open("gates.png").crop((3814,9,4301,245)).convert("RGBA") # SWAP gate - black world
swap_b = swap_b.resize(list(map(lambda x:x//2 , swap_b.size)))

hgate_w = Image.open("gates.png").crop((4309,10,4784,108)).convert("RGBA") # H gate - white world
hgate_w = hgate_w.resize(list(map(lambda x:x//2 , hgate_w.size)))

hgate_b = Image.open("gates.png").crop((4310,141,4783,238)).convert("RGBA") # H gate - black world
hgate_b = hgate_b.resize(list(map(lambda x:x//2 , hgate_b.size)))

# extracting button assets form the gates.png image.
start_btn = Image.open("gates.png").crop((4890,25,5095,215)).convert("RGBA") # start game button
start_btn = start_btn.resize(list(map(lambda x:x//2 , start_btn.size)))

restart_btn = Image.open("gates.png").crop((5134,26,5339,216)).convert("RGBA") # restart game button
restart_btn = restart_btn.resize(list(map(lambda x:x//2 , restart_btn.size)))
