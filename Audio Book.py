import pyttsx3
import pyPDF2
book = open('file','rb') #to ensure that the book will be read as binary book
pdfREader = pyPDF2.pdffileREader(book)
pages = pdfReader.numPages
print(pages) #num.of pages
speaker = pyttsx3.init()
for num in pages:      #range(7,pages)
  page=pdfReader.getPage(8)
  text = page.extractText()
  speaker.say('text')
  speaker.runAndWait()
