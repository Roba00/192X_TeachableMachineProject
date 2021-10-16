import os
import random
from shutil import copyfile

random.seed(10)

#cats 20%

for i in range(1, 8):
	cats_20 = []
	while (len(cats_20) < 20) :
		current_cat = str(random.randint(0, 99)) + ".jpg"
		if not(current_cat in cats_20):
			cats_20.append(current_cat)
	for cat in cats_20:
		copyfile("Animal_Dataset/Training/0_Cats/" + cat, "20/" + str(i) + "/0_Cats/" + cat)

#cats 40%

for i in range(1, 8):
	cats_40 = []
	while (len(cats_40) < 40) :
		current_cat = str(random.randint(0, 99)) + ".jpg"
		if not(current_cat in cats_40):
			cats_40.append(current_cat)
	for cat in cats_40:
		copyfile("Animal_Dataset/Training/0_Cats/" + cat, "40/" + str(i) + "/0_Cats/" + cat)

#cats 60%

for i in range(1, 8):
	cats_60 = []
	while (len(cats_60) < 60) :
		current_cat = str(random.randint(0, 99)) + ".jpg"
		if not(current_cat in cats_60):
			cats_60.append(current_cat)
	for cat in cats_60:
		copyfile("Animal_Dataset/Training/0_Cats/" + cat, "60/" + str(i) + "/0_Cats/" + cat)

#cats 80%

for i in range(1, 8):
	cats_80 = []
	while (len(cats_80) < 80) :
		current_cat = str(random.randint(0, 99)) + ".jpg"
		if not(current_cat in cats_80):
			cats_80.append(current_cat)
	for cat in cats_80:
		copyfile("Animal_Dataset/Training/0_Cats/" + cat, "80/" + str(i) + "/0_Cats/" + cat)

#dogs 20%

for i in range(1, 8):
	dogs_20 = []
	while (len(dogs_20) < 20) :
		current_dog = str(random.randint(0, 99)) + ".jpg"
		if not(current_dog in dogs_20):
			dogs_20.append(current_dog)
	for dog in dogs_20:
		copyfile("Animal_Dataset/Training/1_Dogs/" + dog, "20/" + str(i) + "/1_Dogs/" + dog)

#dogs 40%

for i in range(1, 8):
	dogs_40 = []
	while (len(dogs_40) < 40) :
		current_dog = str(random.randint(0, 99)) + ".jpg"
		if not(current_dog in dogs_40):
			dogs_40.append(current_dog)
	for dog in dogs_40:
		copyfile("Animal_Dataset/Training/1_Dogs/" + dog, "40/" + str(i) + "/1_Dogs/" + dog)

#dogs 60%

for i in range(1, 8):
	dogs_60 = []
	while (len(dogs_60) < 60) :
		current_dog = str(random.randint(0, 99)) + ".jpg"
		if not(current_dog in dogs_60):
			dogs_60.append(current_dog)
	for dog in dogs_60:
		copyfile("Animal_Dataset/Training/1_Dogs/" + dog, "60/" + str(i) + "/1_Dogs/" + dog)

#dogs 80%

for i in range(1, 8):
	dogs_80 = []
	while (len(dogs_80) < 80) :
		current_dog = str(random.randint(0, 99)) + ".jpg"
		if not(current_dog in dogs_80):
			dogs_80.append(current_dog)
	for dog in dogs_80:
		copyfile("Animal_Dataset/Training/1_Dogs/" + dog, "80/" + str(i) + "/1_Dogs/" + dog)

#chickens 20%

for i in range(1, 8):
	chickens_20 = []
	while (len(chickens_20) < 20) :
		current_chicken = str(random.randint(0, 99)) + ".jpg"
		if not(current_chicken in chickens_20):
			chickens_20.append(current_chicken)
	for chicken in chickens_20:
		copyfile("Animal_Dataset/Training/2_chickens/" + chicken, "20/" + str(i) + "/2_chickens/" + chicken)

#chickens 40%

for i in range(1, 8):
	chickens_40 = []
	while (len(chickens_40) < 40) :
		current_chicken = str(random.randint(0, 99)) + ".jpg"
		if not(current_chicken in chickens_40):
			chickens_40.append(current_chicken)
	for chicken in chickens_40:
		copyfile("Animal_Dataset/Training/2_chickens/" + chicken, "40/" + str(i) + "/2_chickens/" + chicken)

#chickens 60%

for i in range(1, 8):
	chickens_60 = []
	while (len(chickens_60) < 60) :
		current_chicken = str(random.randint(0, 99)) + ".jpg"
		if not(current_chicken in chickens_60):
			chickens_60.append(current_chicken)
	for chicken in chickens_60:
		copyfile("Animal_Dataset/Training/2_chickens/" + chicken, "60/" + str(i) + "/2_chickens/" + chicken)

#chickens 80%

for i in range(1, 8):
	chickens_80 = []
	while (len(chickens_80) < 80) :
		current_chicken = str(random.randint(0, 99)) + ".jpg"
		if not(current_chicken in chickens_80):
			chickens_80.append(current_chicken)
	for chicken in chickens_80:
		copyfile("Animal_Dataset/Training/2_chickens/" + chicken, "80/" + str(i) + "/2_chickens/" + chicken)

#horses 20%

for i in range(1, 8):
	horses_20 = []
	while (len(horses_20) < 20) :
		current_horse = str(random.randint(0, 99)) + ".jpg"
		if not(current_horse in horses_20):
			horses_20.append(current_horse)
	for horse in horses_20:
		copyfile("Animal_Dataset/Training/3_Horses/" + horse, "20/" + str(i) + "/3_Horses/" + horse)

#horses 40%

for i in range(1, 8):
	horses_40 = []
	while (len(horses_40) < 40) :
		current_horse = str(random.randint(0, 99)) + ".jpg"
		if not(current_horse in horses_40):
			horses_40.append(current_horse)
	for horse in horses_40:
		copyfile("Animal_Dataset/Training/3_Horses/" + horse, "40/" + str(i) + "/3_Horses/" + horse)

#horses 60%

for i in range(1, 8):
	horses_60 = []
	while (len(horses_60) < 60) :
		current_horse = str(random.randint(0, 99)) + ".jpg"
		if not(current_horse in horses_60):
			horses_60.append(current_horse)
	for horse in horses_60:
		copyfile("Animal_Dataset/Training/3_Horses/" + horse, "60/" + str(i) + "/3_Horses/" + horse)

#horses 80%

for i in range(1, 8):
	horses_80 = []
	while (len(horses_80) < 80) :
		current_horse = str(random.randint(0, 99)) + ".jpg"
		if not(current_horse in horses_80):
			horses_80.append(current_horse)
	for horse in horses_80:
		copyfile("Animal_Dataset/Training/3_Horses/" + horse, "80/" + str(i) + "/3_Horses/" + horse)
