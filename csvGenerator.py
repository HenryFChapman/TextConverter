import pandas as pd 
import sys

def spreadsheetGenerator(filename):
	with open(filename, 'r') as file:
		data = file.read().replace('\n', '')

	data = data.split("APPENDIX")[0]
	sentences = data.split(". ")

	total = 0
	allSentances = []
	allSentLen = []
	percentThroughBook = []
	for sent in sentences:

		sentLen = len(sent)
		total = total + sentLen

		allSentances.append(sent)
		allSentLen.append(sentLen)
		percentThroughBook.append(total)

	aGameOfThrones = pd.DataFrame(pd.date_range("1-jan-2000", freq="H", periods=len(percentThroughBook)), columns=["Date"])

	aGameOfThrones['percentThroughBook'] = percentThroughBook
	aGameOfThrones['percentThroughBook'] = aGameOfThrones['percentThroughBook']/total
	aGameOfThrones['Sentance'] = allSentances
	aGameOfThrones['allSentLen'] = sentLen

	csvLen = filename.split('.txt')[0]
	aGameOfThrones.to_excel(csvLen + ".xlsx")

	file.close()

spreadsheetGenerator(sys.argv[1])

