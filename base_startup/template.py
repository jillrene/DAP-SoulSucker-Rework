import pathlib

version             = ipar.extLighting.Ver
req_file            = tdu.expandPath(ipar.extLighting.Pyreqs)
install_target      = tdu.expandPath(ipar.extLighting.Target)
install_script_path = pathlib.Path(install_target).parents[0]

win_file            = install_script_path / 'dep_install.cmd'

win_txt = '''
:: update pip
python -m pip install --user --upgrade pip

:: install from requirements file
py -3.10 -m pip install -r "{reqs}" --target="{target}"
'''

format_win_txt      = win_txt.format(reqs=req_file, target=install_target)

#print(format_win_txt)

with open(str(win_file), 'w+') as win_script: 
    win_script.write(format_win_txt)

print('template has run')