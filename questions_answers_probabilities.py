def create_array(length, probs, sections):
	toReturn = []
	section = 0
	loop = 0
	while len(toReturn) < length:
		if loop > sections[section]-11:
			section = section + 1
		toReturn.append(probs[section])
		loop = loop + 1
	return toReturn

array = range(11,67)

question_list = ["Do you like sports?", # 1
				 "Do you ever use the internet?", # 2
				 "Do you have a facebook?", # 3
				 "Do you smoke weed?", # 4
				 "Were you interested in Trump's Truth Social in March?", # 5
				 "Do you play video games?", # 6
				 "Do you listen to the radio at all, by any means?", # 7
				 "Do you use the internet to listen to the radio?", # 8
				 "How do you usually obtain news about current events?", #9
				 "Describe your alcohol use in one word:", # 10
				 "Do you use twitter?", # 11
				 "Is photography a hobby of yours?", # 12
				 "Do you watch sci-fi/fantasy tv shows?", # 13
				 "Out of the following, which is your favorite genre of music?", # 14
				 "Do you think that social media is good or bad for society?", # 15
				 ]

answer_list = [["Yes, a lot", "Yes, a bit", "No"], # 1, 3 answers
			   ["Yes", "No"], # 2, 2
			   ["Yes", "No"], # 3, 2
			   ["Yes", "No"], # 4, 2
			   ["Yes, a lot", "Yes, somewhat", "A little bit", "No, not at all"], # 5, 4
			   ["Yes", "No"], # 6, 2
			   ["Yes", "No"], # 7, 2
			   ["Yes", "No"], # 8, 2
			   ["Newspapers", "Radio", "Cable (local) news", "Broadcast (national) news", "Web news", "Social media", "Podcasts"], # 9, 7
			   ["Nonexistent", "Occasional", "Often", "Hepatitis"], # 10, 4
			   ["Yes, and I tweet frequently", "Yes, but I don't tweet often/ever", "No"], # 11, 3
			   ["Yes", "No"], # 12, 2
			   ["Yes", "No"], # 13, 2
			   ["Pop Music", "Rock Music", "Hip Hop/Rap", "Indie/Alternative Rock", "Classic Rock", "Soundtracks", "Rhythm and Blues", "Instrumental", "Country", "Singer/Songwriter", "Rock 'n' Roll", "Show Music/Musicals"], # 14, 12
			   ["It's good", "It's bad", "It isn't really either", "I'm not sure"] # 15, 4
			   ]

probability_list = [[create_array(len(array), [0.21, 0.23, 0.26, 0.20], [34, 44, 64, 67]), create_array(len(array), [0.45, 0.43, 0.40, 0.40], [34, 44, 64, 67]), create_array(len(array), [0.33, 0.33, 0.34, 0.39], [34, 44, 64, 67])], # 1
[create_array(len(array), [0.99, 0.98, 0.96, 0.75], [29, 49, 64, 67]), create_array(len(array), [0.01, 0.02, 0.04, 0.25], [29, 49, 64, 67])], # 2
[create_array(len(array), [0.038, 0.174, 0.254, 0.185, 0.138, 0.108, 0.104], [17, 24, 34, 44, 54, 64, 67]), create_array(len(array), [1-0.038, 1-0.174, 1-0.254, 1-0.185, 1-0.138, 1-0.108, 1-0.104], [17, 24, 34, 44, 54, 64, 67])], # 3
[create_array(len(array), [0.22, 0.11, 0.12, 0.03], [29, 49, 64, 67]), create_array(len(array), [1-0.22, 1-0.11, 1-0.12, 1-0.03], [29, 49, 64, 67])], # 4
[create_array(len(array), [0.07, 0.12, 0.10, 0.05], [34, 44, 64, 67]), create_array(len(array), [0.28, 0.25, 0.21, 0.15], [34, 44, 64, 67]), create_array(len(array), [0.15, 0.15, 0.12, 0.14], [34, 44, 64, 67]), create_array(len(array), [0.50, 0.49, 0.57, 0.66], [34, 44, 64, 67])], # 5
[create_array(len(array), [0.20, 0.38, 0.14, 0.12, 0.09, 0.07], [18, 34, 44, 54, 64, 67]), create_array(len(array), [1-0.20, 1-0.38, 1-0.14, 1-0.12, 1-0.09, 1-0.07], [18, 34, 44, 54, 64, 67])], # 6
[create_array(len(array), [0.711, 0.757, 0.847, 0.845], [17, 24, 54, 67]), create_array(len(array), [1-0.711, 1-0.757, 1-0.847, 1-0.845], [17, 24, 54, 67])], # 7
[create_array(len(array), [0.86, 0.71, 0.44], [34, 54, 67]), create_array(len(array), [1-0.86, 1-0.71, 1-0.44], [34, 54, 67])], # 8
[create_array(len(array), [0.10, 0.09, 0.10, 0.21], [34, 44, 64, 67]), create_array(len(array), [0.19, 0.24, 0.22, 0.15], [34, 44, 64, 67]), create_array(len(array), [0.12, 0.18, 0.24, 0.32], [34, 44, 64, 67]), create_array(len(array), [0.12, 0.18, 0.32, 0.41], [34, 44, 64, 67]), create_array(len(array), [0.17, 0.16, 0.20, 0.20], [34, 44, 64, 67]), create_array(len(array), [0.45, 0.44, 0.33, 0.24], [34, 44, 64, 67]), create_array(len(array), [0.11, 0.12, 0.06, 0.04], [34, 44, 64, 67])], # 9
[create_array(len(array), [1-0.009, 1-0.075, 1-0.170, 1-0.319, 1-0.631, 1-0.612, 1-0.607, 1-0.587, 1-0.591, 1-0.586, 1-0.568, 1-0.502, 1-0.565, 1-0.453], [13, 15, 17, 20, 25, 29, 34, 39, 44, 49, 54, 59, 64, 67]), create_array(len(array), [0.009, 0.075, 0.170, 0.319, 0.631, 0.612, 0.607, 0.587, 0.591, 0.586, 0.568, 0.502, 0.565, 0.453], [13, 15, 17, 20, 25, 29, 34, 39, 44, 49, 54, 59, 64, 67]), create_array(len(array), [0.003, 0.033, 0.091, 0.193, 0.385, 0.342, 0.323, 0.292, 0.287, 0.270, 0.248, 0.199, 0.227, 0.098], [13, 15, 17, 20, 25, 29, 34, 39, 44, 49, 54, 59, 64, 67]), create_array(len(array), [0.001, 0.006, 0.011, 0.042, 0.111, 0.078, 0.089, 0.075, 0.078, 0.086, 0.063, 0.082, 0.077, 0.034], [13, 15, 17, 20, 25, 29, 34, 39, 44, 49, 54, 59, 64, 67])], # 10
[create_array(len(array), [0.41, 0.32, 0.20, 0.07], [29, 49, 64, 67]), create_array(len(array), [0.14, 0.59, 0.20, 0.07], [29, 49, 64, 67]), create_array(len(array), [1-0.41-0.14, 1-0.32-0.59, 1-0.40, 1-0.14], [29, 49, 64, 67])], # 11
[create_array(len(array), [0.24, 0.21, 0.15, 0.15], [29, 49, 64, 67]), create_array(len(array), [1-0.24, 1-0.21, 1-0.15, 1-0.15], [29, 49, 64, 67])], # 12
[create_array(len(array), [0.24, 0.34, 0.35, 0.35], [29, 49, 64, 67]), create_array(len(array), [1-0.24, 1-0.34, 1-0.35, 1-0.35], [29, 49, 64, 67])], # 13
[create_array(len(array), [0.52, 0.54, 0.56, 0.46, 0.42, 0.25, 0.19], [19, 24, 34, 44, 54, 64, 67]), create_array(len(array), [0.28, 0.39, 0.44, 0.42, 0.48, 0.31, 0.17], [19, 24, 34, 44, 54, 64, 67]), create_array(len(array), [0.48, 0.54, 0.42, 0.33, 0.15, 0.05, 0.01], [19, 24, 34, 44, 54, 64, 67]), create_array(len(array), [0.31, 0.40, 0.35, 0.28, 0.21, 0.13, 0.05], [19, 24, 34, 44, 54, 64, 67]), create_array(len(array), [0.26, 0.36, 0.44, 0.46, 0.62, 0.60, 0.48], [19, 24, 34, 44, 54, 64, 67]), create_array(len(array), [0.15, 0.23, 0.24, 0.21, 0.18, 0.15, 0.16], [19, 24, 34, 44, 54, 64, 67]), create_array(len(array), [0.23, 0.22, 0.22, 0.22, 0.21, 0.15, 0.16], [19, 24, 34, 44, 54, 64, 67]), create_array(len(array), [0.22, 0.23, 0.20, 0.13, 0.13, 0.17, 0.16], [19, 24, 34, 44, 54, 64, 67]), create_array(len(array), [0.19, 0.26, 0.37, 0.31, 0.38, 0.38, 0.40], [19, 24, 34, 44, 54, 64, 67]), create_array(len(array), [0.21, 0.21, 0.20, 0.17, 0.15, 0.18, 0.15], [19, 24, 34, 44, 54, 64, 67]), create_array(len(array), [0.28, 0.30, 0.40, 0.42, 0.49, 0.40, 0.41], [19, 24, 34, 44, 54, 64, 67]), create_array(len(array), [0.20, 0.19, 0.17, 0.14, 0.15, 0.16, 0.24], [19, 24, 34, 44, 54, 64, 67])], # 14
[create_array(len(array), [0.23, 0.31, 0.25, 0.17, 0.17], [24, 34, 44, 54, 67]), create_array(len(array), [0.30, 0.29, 0.38, 0.46, 0.45], [24, 34, 44, 54, 67]), create_array(len(array), [0.26, 0.29, 0.25, 0.26, 0.27], [24, 34, 44, 54, 67]), create_array(len(array), [0.21, 0.11, 0.13, 0.11, 0.12], [24, 34, 44, 54, 67])] # 15
]

#new_array = []
#probability_array = []
#probability_function = '''new_array = []
#for (index, entry) in enumerate(array):
#	mult = math.floor(entry/40.1)/120
#	new_array.append(mult)
#probability_array = list(new_array)
#'''
#
#test_string = "math.exp((-(entry-30)**2)/200)/(math.sqrt(200*math.pi))"
#
#probability_function_2 = '''new_array = []
#for (index, entry) in enumerate(array):
#	mult = ''' + test_string + '''
#	new_array.append(mult*probability_array[index])
#probability_array = list(new_array)
#'''

#exec(probability_function)
#exec(probability_function_2)

#print(probability_array)

#print(max(probability_array))
#print(array[probability_array.index(max(probability_array))]) # First instance of our maximum
#print(array[len(array)-1-probability_array[::-1].index(max(probability_array))]) # Last instance of our maximum (If they're equal, not an age range)