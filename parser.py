from pathlib import Path
import camelot

years_list = [ #'2020-21','2019-20', '2018-19', '2017-18', '2016-17', '2015-16', 
'2014-15', '2013-14' 
]
newpdf_list = [ 'newpdf' + y for y in years_list ]

bad_list = []

for np in newpdf_list:
    pdf_path_list = [ f for f in (Path.cwd() / np).iterdir() if f.is_file() and f.suffix == '.pdf' ]
    for pdf_path in pdf_path_list:
        try:
            csv_dir = pdf_path.parent / pdf_path.stem
            csv_dir.mkdir(parents=True, exist_ok=True)
            tables = camelot.read_pdf(str(pdf_path), pages='1', line_scale=60, strip_text='\n')
            if len(tables) < 2:
                tables = camelot.read_pdf(str(pdf_path), pages='2', line_scale=60, strip_text='\n')
            if len(tables) < 2:
                tables = camelot.read_pdf(str(pdf_path), pages='3', line_scale=60, strip_text='\n')
            for i, t in enumerate(tables):
                t.to_csv(str(csv_dir / (str(i) + '.csv')))
            # pdf_path.rename(csv_dir / pdf_path.name)
        except Exception as e:
            bad_list.append(pdf_path)
            print(e)
            print(str(pdf_path))

print('bad boys================================================')
print(bad_list)
