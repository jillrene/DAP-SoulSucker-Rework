import sys

spacer = "- " * 5


python_ext = tdu.expandPath(ipar.extLighting.Target)

if python_ext not in sys.path: 
    sys.path.append(python_ext)

for each in sys.path:
	print(each)

