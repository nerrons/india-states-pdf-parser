import pdftotext
from pathlib import Path
from pprint import pprint
import dateparser

years_list = [ #'2020-21', '2019-20', '2018-19', '2017-18', '2016-17', '2015-16', 
'2014-15', '2013-14' ]
rawpdf_list = [ 'rawpdf' + y for y in years_list ]

bad_list = []

for rp in rawpdf_list:
    newpdf_dir = Path.cwd() / ('newpdf' + rp[6:])
    Path(newpdf_dir).mkdir(parents=True, exist_ok=True)

    pdf_path_list = [ f for f in (Path.cwd() / rp).iterdir() if '.pdf' in str(f) ]
    for pdf_path in pdf_path_list:
        with pdf_path.open('rb') as f:
            try:
                pdf = pdftotext.PDF(f)
                text = "\n\n".join(pdf)
                date_text = text.split('Date of Reporting')[1].split('A. ')[0].replace(':', '').strip()
                date = dateparser.parse(date_text).strftime("%Y-%m-%d")
                newpdf_name = f'{date}__{pdf_path.name}__.pdf'
                pdf_path.replace(newpdf_dir / newpdf_name)

            except Exception as e:
                bad_list.append(pdf_path)
                print(e)
                print(str(pdf_path))

print('bad boys--------------------------------------------------')
pprint(bad_list)

