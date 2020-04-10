from lxml import html
import requests
import tkinter
from tkinter import *


class GUI():

	def Setup(title, loop, text, row, column):
		root = tkinter.Tk()
		root.title(title)
		root.geometry('400x300')

		for i in range(loop):
			labeli = Label(root, text=text)
			labeli.grid(column=column, row=row)
			column += 1
			row += 1

		root.mainloop()


def Main():
	GUI.Setup("Hello", 5, "weather", 1, 2)

	WriteString = ""

	url = "http://www.bom.gov.au/wa/forecasts/fremantle.shtml"

	source = requests.get(url)
	tree = html.fromstring(source.content)

	MaxTemp = tree.xpath('//em[@class="max"]/text()')
	MinTemp = tree.xpath('//em[@class="min"]/text()')
	Summary = tree.xpath('//dd[@class="summary"]/text()')
	Days = tree.xpath('//h2/text()')

	Var = len(Days)
	
	for i in range(Var):
		if "Friday" in Days[i]:
			Days[i] = "Friday"
		if "Thursday" in Days[i]:
			Days[i] = "Thursday"
		if "Wednesday" in Days[i]:
			Days[i] = "Wednesday"
		if "Tuesday" in Days[i]:
			Days[i] = "Tuesday"
		if "Monday" in Days[i]:
			Days[i] = "Monday"
		if "Sunday" in Days[i]:
			Days[i] = "Sunday"
		if "Saturday" in Days[i]:
			Days[i] = "Saturday"


	for i in range(Var-1):
		if i > 0:
			print(Days[i] + ": Max = " + MaxTemp[i] + ", Min = " + MinTemp[i] + "\n" + Summary[i])
		elif i <= 0:
			print(Days[i] + ": Max = " + MaxTemp[i] + "\n" + Summary[i])

Main()
