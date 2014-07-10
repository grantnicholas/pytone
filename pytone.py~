import matplotlib.pyplot as plt
from scipy.io import wavfile # get the api
from scipy.fftpack import fft
from pylab import *

def f(filename):
	fs, data = wavfile.read(filename) # load the data
	a = data.T[0] # this is a two channel soundtrack, I get the first track
	b=[(ele/2**16.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
	c = fft(b); # create a list of complex number
	d = len(c)/2;  # you only need half of the fft list
	k = arange(len(a));
	T = len(a)/fs;
	frq= k/T;
	frq= frq[range(len(a)/2 -1)];
	out = abs(c[:(d-1)]);
	frq = frq[0:50000];  out = out[0:50000];
	plt.plot(frq,out,'r')
	plt.ylim((0,50000))
	savefig(filename+'.png',bbox_inches='tight')
	max = 0;
	for i in range(len(frq)):
		if(out[i] > max):
			max = frq[i];
			
	print max;	
		
	
	


f('testing.wav');

