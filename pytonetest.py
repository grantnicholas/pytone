import matplotlib.pyplot as plt
from scipy.io import wavfile # get the api
from scipy.fftpack import fft
from pylab import *


fs, data = wavfile.read('testing.wav'); # load the data
plt.plot(data);
savefig('new'+'testing.wav'+'.png',bbox_inches='tight');
show_info("data", data)

max=0;
out = [];
for i in enumerate(data):
		if(out[i] > max):
			max = frq[i];
