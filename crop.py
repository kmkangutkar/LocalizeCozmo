import Image
import numpy as np
import sys

if len(sys.argv) > 1:
	image = Image.open(sys.argv[1]).convert("L")
	image.show()
	print image.size
	a = np.asarray(image)
	print a.shape
	k=a[95:180,100:250]
	print sum(sum(k))/k.size
	print k.size
	Image.fromarray(k).show()

 



