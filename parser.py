import camelot
tables = camelot.read_pdf('data-pdf/tester.pdf', pages='2', line_scale=40, strip_text='\n')
print(tables)
tables[6].to_csv('try6.csv')

