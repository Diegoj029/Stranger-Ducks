from PIL import  Image

# extracting game items and characters form the resource.png image.
player_w = Image.open("resources.png").crop((4,24,92,109)).convert("RGBA")
player_w = player_w.resize(list(map(lambda x:x//2 , player_w.size)))

player_b = Image.open("resources.png").crop((108,21,196,106)).convert("RGBA")
player_b = player_b.resize(list(map(lambda x:x//2 , player_b.size)))

ground_w = Image.open("resources.png").crop((3,112,1395,130)).convert("RGBA")
ground_w = ground_w.resize(list(map(lambda x:x//2 , ground_w.size)))

ground_b = Image.open("resources.png").crop((3,0,1395,18)).convert("RGBA")
ground_b = ground_b.resize(list(map(lambda x:x//2 , ground_b.size)))

well_w = Image.open("resources.png").crop((1395,112,2446,130)).convert("RGBA")
well_w = ground_w.resize(list(map(lambda x:x//2 , well_w.size)))

well_b = Image.open("resources.png").crop((1395,0,2446,18)).convert("RGBA")
well_b = ground_b.resize(list(map(lambda x:x//2 , well_b.size)))

noise_w_s = Image.open("resources.png").crop((691,0,770,92)).convert("RGBA")
noise_w_s = noise_w_s.resize(list(map(lambda x:x//2 , noise_w_s.size)))

noise_b_s = Image.open("resources.png").crop((793,0,872,92)).convert("RGBA")
noise_b_s = noise_b_s.resize(list(map(lambda x:x//2 , noise_b_s.size)))

noise_w_l = Image.open("resources.png").crop((909,0,1034,99)).convert("RGBA")
noise_w_l = noise_w_l.resize(list(map(lambda x:x//2 , noise_w_l.size)))

noise_b_l = Image.open("resources.png").crop((1069,0,1194,109)).convert("RGBA")
noise_b_l = noise_b_l.resize(list(map(lambda x:x//2 , noise_b_l.size)))

qubit_w_s = Image.open("resources.png").crop((500,0,561,89)).convert("RGBA")
qubit_w_s = qubit_w_s.resize(list(map(lambda x:x//2 , qubit_w_s.size)))

qubit_b_s = Image.open("resources.png").crop((578,42,639,90)).convert("RGBA")
qubit_b_s = qubit_b_s.resize(list(map(lambda x:x//2 , qubit_b_s.size)))

qubit_w_l = Image.open("resources.png").crop((250,26,338,97)).convert("RGBA")
qubit_w_l = qubit_w_l.resize(list(map(lambda x:x//2 , qubit_w_l.size)))

qubit_b_l = Image.open("resources.png").crop((363,28,451,99)).convert("RGBA")
qubit_b_l = qubit_b_l.resize(list(map(lambda x:x//2 , qubit_b_l.size)))