

import numpy as np
import matplotlib.pyplot as plt
import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import FLARE.filters
import SynthObs
import SynthObs.Morph 
from SynthObs.SED import models
from SynthObs.Morph import measure 







test = SynthObs.test_data() # --- read in some test data


# ------ Make rest-frame luminosity image

img = SynthObs.Morph.physical_image(test.X, test.Y, test.Masses)


m = measure.intrinsic(img)

m.detect_sources()


r_e = m.r_e()

r_e['simple'] = measure.simple(test.X, test.Y, test.Masses)[0]

print(r_e) # --- measure effective_radius in several different ways




