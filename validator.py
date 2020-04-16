from pathlib import Path

years_list = [ '2020-21', '2019-20', '2018-19', '2017-18', '2016-17', '2015-16', '2014-15', '2013-14' ]
csv_list = [ 'compressed/newpdf' + y for y in years_list ]

for cp in csv_list:
    subpath = Path(cp)
    all_dates = [ d.name[:10] for d in (Path.cwd() / cp).iterdir() if f.is_dir() ]