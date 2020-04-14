import pdftotext
from pathlib import Path
from pprint import pprint

years_list = [ '2019-20', '2018-19', '2017-18', '2016-17', '2015-16', '2014-15', '2013-14' ]
rawpdf_list = [ 'rawpdf' + y for y in years_list ]

bad_list = []

for rp in rawpdf_list:
    pdf_path_list = [ f for f in (Path.cwd() / rp).iterdir() if '.pdf' in str(f) ]
    for pdf_path in pdf_path_list:
        with pdf_path.open('rb') as f:
            try:
                pdf = pdftotext.PDF(f)
                #print(pdf)
                text = "\n\n".join(pdf)
                #print(text)
                date_text = text.split('Date of Reporting')[1].split('A. ')[0].replace(':', '').strip()
                print(date_text)
            except Exception as e:
                bad_list.append(pdf_path)
                print(e)
                print(str(pdf_path))

print('bad boys--------------------------------------------------')
pprint(bad_list)

