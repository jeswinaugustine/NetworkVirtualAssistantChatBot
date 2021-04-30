from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import re

def convert_pdf_to_txt(path, codec='utf-8'):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    i = 0
    max = PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True)
    print(max)
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
        text = retstr.getvalue()
        
    if re.match(".*", retstr.getvalue()):
        print(re.match(".*", retstr.getvalue()))

		
    fp.close()
    device.close()
    retstr.close()
    return text


#def feature_description_extract(data):
    #result = re.match(r"(?:Best effort service[\w\W]+)", data)
    #print(data)
    # result = re.match(r"\w\n\s\t+ Aruba", data)
    # return result

data = convert_pdf_to_txt("QOS_ConfigurationGuide_8400_SwitchSeries.pdf")
#print(data)

#result = feature_description_extract(data)
#print(result)

texfile=open("file.txt", "r")

#if re.match("[A-Za-z]+[\d\w\n\t]+Best effort service\n\w+\W+", retstr):
#	   print(line)

'''
# importing required modules 
import PyPDF2 
  
# creating a pdf file object 
pdfFileObj = open("QOS_ConfigurationGuide_8400_SwitchSeries.pdf", 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# printing number of pages in pdf file 
print(pdfReader.numPages) 

print("Arya")
  
# creating a page object 
pageObj = pdfReader.getPage(10) 
count = pdfReader.numPages
for i in range(count):
    page = pdfReader.getPage(i)
    page_content = page.extractText().split('\n')
    print(page_content)
	
	
# extracting text from page 
print(pageObj.extractText()) 

# closing the pdf file object 
pdfFileObj.close() 


from tika import parser

raw = parser.from_file("QOS_ConfigurationGuide_8400_SwitchSeries.pdf")
raw = str(raw)

safe_text = raw.encode('utf-8', errors='ignore')

safe_text = str(safe_text).replace("\n", "").replace("\\", "")
print('--- safe text ---' )
print( safe_text )
'''
