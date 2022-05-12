# importing the required libraries

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt
import sys
import numpy as np
from questions_answers_probabilities import *

# Define questions and answers using the following syntax:
# Each line corresponds between the tables. 
# In the question list write down the text of the question.
# In the answer list, write down a LIST of texts for each answer.
# In the probability list, define a function that gives the corresponding probability
# distribution for each answer. This list should have the same number of elements
# as the answer text list does.

ages = []
for i in range(11,67):
	ages.append(int(i))


choice_parameter = True

def add_new_question(question_table, question_text, answer_text_table, probability_dist_table, self_):
	toReturn = list(question_table)
	toReturn.append([])
	index = len(toReturn)-1
	toReturn[index].append(QLabel(question_text))
	toReturn[index].append([])
	toReturn[index][1].append(QButtonGroup(self_))
	toReturn[index][1][0].setExclusive(True)
	for j in range(0,len(answer_text_table)):
		toReturn[index][1].append(QRadioButton(answer_text_table[j]))
		toReturn[index][1][0].addButton(toReturn[index][1][j+1])
	return toReturn

def make_question_widgets(question_table, widget_to_edit):
	widget_to_edit.addWidget(QLabel("Answer each question to the best of your ability and then we'll guess your age!"), 0, 1, 1, 4)
	position = 2
	for i in range(0,len(question_table)):
		widget_to_edit.addWidget(question_table[i][0], position, 0, 1, 3)
		position = position + 1
		for j in range(1,len(question_table[i][1])):
			widget_to_edit.addWidget(question_table[i][1][j], position, j-1, 1, 1)
		position = position + 1
		widget_to_edit.addWidget(QLabel(" "), position, 1)
		position = position + 1
	return position

def try_finish(question_table, label_to_edit, window_to_close, window_to_show):
	global choice_parameter
	done_or_not = True
	probability_values = []
	for (i, q) in enumerate(question_table):
		this_q_done = False
		for (index, a) in enumerate(q[1]):
			if index == 0:
				pass
			elif a.isChecked() == True:
				this_q_done = True
				probability_values.append(probability_list[i][index-2])
				break
			else:
				this_q_done = this_q_done
		if this_q_done == False:
			done_or_not = False
			break
		else:
			done_or_not = done_or_not
	if done_or_not == True:
		window_to_close.hide()
		window_to_show.show()
		if choice_parameter == 1:
			this_distribution = np.multiply(np.ones(len(ages)), 1/len(ages)).tolist()
			for entry in probability_values:
				for (index, value) in enumerate(entry):
					try:
						this_distribution[index] = this_distribution[index] * value
					except:
						this_distribution.append(value)
					this_distribution = np.divide(this_distribution, sum(this_distribution)/100).tolist()
		else:
			this_distribution = []
			for entry in probability_values:
				for (index, value) in enumerate(entry):
					try:
						this_distribution[index] = this_distribution[index] + value
					except:
						this_distribution.append(value)
		this_distribution = np.divide(np.round(np.divide(this_distribution, sum(this_distribution)/100000)), 1000).tolist()
		try:
			result_low = ages[this_distribution.index(max(this_distribution))]
			print("Result Low Index = " + str(this_distribution.index(max(this_distribution))))
		except:
			print("Error in Result Low, Index = " + str(this_distribution.index(max(this_distribution))))
			result_low = 66
		try:
			result_high = ages[len(ages)-1-this_distribution[::-1].index(max(this_distribution))]
			print("Result High Index = " + str(len(ages)-1-this_distribution[::-1].index(max(this_distribution))))
		except:
			print("Error in Result High, Index = " + str(len(ages)-1-this_distribution[::-1].index(max(this_distribution))))
			print(len(ages)-1-this_distribution[::-1].index(max(this_distribution)))
			result_high = 66

		print("Ages = " + str(ages))
		print([entry for entry in this_distribution])
		print("Result Low = " + str(result_low))
		print("Result High = " + str(result_high))
		window_to_show.layout.addWidget(QLabel(" "), 0, 0)
		window_to_show.layout.addWidget(QLabel(" "), 2, 2)
		window_to_show.layout.addWidget(QLabel(" "), 2, 0)
		window_to_show.layout.addWidget(QLabel(" "), 0, 2)
		if result_low == result_high and result_low != 11 and result_high != 66:
			window_to_show.result_text.setText("Your age is " + str(result_low) + " years old")
		elif result_low == result_high and result_high != 66:
			window_to_show.result_text.setText("You are too young for this program (less than 12 years old)")
		elif result_low == result_high and result_low != 11:
			window_to_show.result_text.setText("Your age range is 65+ years old")
		elif result_high < 66 and result_low > 11:
			window_to_show.result_text.setText("Your age range is between " + str(result_low) + " and " + str(result_high) + " years old")
		elif result_low > 11:
			window_to_show.result_text.setText("Your age range is " + str(result_low) + "+ years old")
		elif result_high < 66:
			window_to_show.result_text.setText("Your age ranges from below 12 to " + str(result_high) + " years old")
		else:
			window_to_show.result_text.setText("You have an age, probably. It ranges from younger than 12 to older than 66, so this program is broken.")
	else:
		label_to_edit.setText("You haven't answered every question yet!")

def accuracy_choice(choice, window_to_close, window_to_show):
	global choice_parameter
	if choice == "Terrible":
		choice_parameter = 0
		result = np.random.randint(0,100)
		window_to_show.layout.addWidget(QLabel(" "), 0, 0)
		window_to_show.layout.addWidget(QLabel(" "), 2, 2)
		window_to_show.layout.addWidget(QLabel(" "), 2, 0)
		window_to_show.layout.addWidget(QLabel(" "), 0, 2)
		if result == 1:
			window_to_show.result_text.setText("Your age is: " + str(result) + " year old")
		else:
			window_to_show.result_text.setText("Your age is: " + str(result) + " years old")
	elif choice == "Decent":
		choice_parameter = 1
	else:
		choice_parameter = 2
	window_to_close.hide()
	window_to_show.show()

class AccuracyWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.widget = QWidget()
		self.layout = QGridLayout()
		accuracy_label = QLabel("How good of a guess would you like?")
		accuracy_buttons = [QPushButton("Terrible"), QPushButton("Decent"), QPushButton("Decent but Different")]
		self.layout.addWidget(accuracy_label, 0, 0, 1, 3)
		self.layout.addWidget(accuracy_buttons[0], 1, 0)
		self.layout.addWidget(accuracy_buttons[1], 1, 1)
		self.layout.addWidget(accuracy_buttons[2], 1, 2)
		accuracy_buttons[0].clicked.connect(lambda: accuracy_choice(str(accuracy_buttons[0].text()), self, rwindow))
		accuracy_buttons[1].clicked.connect(lambda: accuracy_choice(str(accuracy_buttons[1].text()), self, qwindow))
		accuracy_buttons[2].clicked.connect(lambda: accuracy_choice(str(accuracy_buttons[2].text()), self, qwindow))
		self.widget.setLayout(self.layout)
		self.setCentralWidget(self.widget)
		self.setGeometry(500, 500, 300, 80)
		self.setWindowTitle("Age Guesser!")

class QuestionsWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.scroll = QScrollArea()
		self.widget = QWidget()
		self.layout = QGridLayout()

		questions = [] # Question/answer stuff
		for i in range(0,len(question_list)):
			questions = add_new_question(questions, question_list[i], answer_list[i], probability_list, self)
		last_question_row = make_question_widgets(questions, self.layout)

		test_finish_button = QPushButton("Finished") # Button to finish the test
		test_finish_button.setToolTip("Make sure to answer every question!")
		not_done_text = QLabel("")
		test_finish_button.clicked.connect(lambda: try_finish(questions, not_done_text, self, rwindow))

		self.layout.addWidget(not_done_text, last_question_row + 1, 2, 1, 2)
		self.layout.addWidget(test_finish_button, last_question_row, 2)
		self.widget.setLayout(self.layout)
		
		self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
		self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.scroll.setWidgetResizable(True)
		self.scroll.setWidget(self.widget)
		self.setCentralWidget(self.scroll)
		self.setWindowTitle("Age Guesser!")
		self.setGeometry(50, 50, 1800, 600)

class ResultsWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.scroll = QScrollArea()
		self.widget = QWidget()
		self.layout = QGridLayout()
		self.widget.setLayout(self.layout)
		self.result_text = QLabel("Something went wrong!")
		self.layout.addWidget(self.result_text, 1, 1)
		texts = [
		QLabel("Sports Fans"), # 0
		QLabel("https://www.statista.com/statistics/1018802/sports-fans-usa-age/"), # 1
		QLabel("Internet Use"), # 2
		QLabel("https://www.statista.com/statistics/266587/percentage-of-internet-users-by-age-groups-in-the-us/"), # 3
		QLabel("Facebook"), # 4
		QLabel("https://www.statista.com/statistics/187549/facebook-distribution-of-users-age-group-usa/"), # 5
		QLabel("Marijuana Use"), # 6
		QLabel("https://www.statista.com/statistics/737849/share-americans-age-group-smokes-marijuana/"), # 7
		QLabel("Truth Social"), # 8
		QLabel("https://www.statista.com/statistics/1298407/us-adults-social-media-donald-trump-truth-platform-by-age/"), # 9
		QLabel("Video Games"), # 10
		QLabel("https://www.statista.com/statistics/189582/age-of-us-video-game-players/"), # 11
		QLabel("Radio Reach"), # 12
		QLabel("https://www.statista.com/statistics/252185/radios-weekly-reach-in-the-us-by-age-and-gender/"), # 13
		QLabel("Online Radio Reach"), # 14
		QLabel("https://www.statista.com/statistics/475950/online-radio-reach-age-usa/"), # 15
		QLabel("News Feeds"), # 16
		QLabel("https://www.statista.com/statistics/717651/most-popular-news-platforms/"), # 17
		QLabel("Alcohol consumption"), # 18
		QLabel("https://www.statista.com/statistics/354265/current-binge-heavy-alcohol-use-among-persons-in-the-us-by-age/"), # 19
		QLabel("Twitter Usage"), # 20
		QLabel("https://www.statista.com/statistics/1304685/us-twitter-users-age-and-frequency/"), # 21
		QLabel("Photography"), # 22
		QLabel("https://www.statista.com/statistics/227424/number-of-photographers-usa/"), # 23
		QLabel("Sci-Fi TV shows"), # 24
		QLabel("https://www.statista.com/statistics/229115/tv-viewers-who-typically-watch-science-fiction-programs-usa/"), # 25
		QLabel("Music Genres"), # 26
		QLabel("https://www.statista.com/statistics/253915/favorite-music-genres-in-the-us/"), # 27
		QLabel("Social Media Society"), # 28
		QLabel("https://www.statista.com/statistics/1268356/us-opinion-social-media-good-or-bad-by-age/"), # 29
		]
		self.layout.addWidget(QLabel("Resources Used:"), 3, 1)
		self.layout.addWidget(QLabel("Statista for all of the statistics/questions (links for each question below)"), 4, 0, 1, 3)
		self.layout.addWidget(QLabel("PyQt5 for the GUI"), 5, 0, 1, 3)
		self.layout.addWidget(QLabel("NumPy for some of the mathematics"), 6, 0, 1, 3)
		self.layout.addWidget(QLabel("		"), 7, 0, 1, 3)
		for (index, entry) in enumerate(texts):
			self.layout.addWidget(entry, int(np.floor(index/2).item())+8, index%2)
		self.setCentralWidget(self.scroll)
		self.scroll.setWidget(self.widget)
		self.setWindowTitle("Age Guesser!")
		self.setGeometry(500, 500, 800, 300)



App = QApplication(sys.argv)

accwindow = AccuracyWindow()
accwindow.show()

qwindow = QuestionsWindow()

rwindow = ResultsWindow()


sys.exit(App.exec_())