#developer Abdul Mohamed M
#This is external package download the xlwt
#Read the ReadMe file
import xlwt
from xlwt import Workbook
wb = Workbook()
r1,c1,r2=0,0,0
c2,n=1,1
sheet1 = wb.add_sheet('Sheet 1')
#open the txt file location and name
file1 = open("<path>\<filename.txt>","r")
for a in file1:
    sheet1.write(r1,c1,n)
    sheet1.write(r2,c2,a)
    r1+=1
    r2+=1
    n+=1
    #Destination file location and file name
    wb.save('<path>\<filename.xls>')

print("The txt file is successfully converted to xls file")