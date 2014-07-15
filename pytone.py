import matplotlib.pyplot as plt
from scipy.io import wavfile # get the api
from scipy.fftpack import fft
from pylab import *

def max(arr):
	maxval = arr[0];
	for i, val in enumerate(arr):
		if(val>maxval):
			maxval = val;
			index  = i;
			
	return (i,val);	


def f(filename):
	fs, data = wavfile.read(filename) # load the data
	plt.plot(data.T[0]);
	maxtimedomain = max(data.T[0])[1];
	savefig('new'+filename+'.png',bbox_inches='tight');
	
	time_arr = [];
	for i, val in enumerate(data.T[0]):
		if(val>.5*maxtimedomain and data.T[0][i-100]>.5*maxtimedomain and data.T[0][i+100]>.5*maxtimedomain):
			time_arr.append(i);
	
	print time_arr;
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
	maxi = max(frq)[1];
			
	print maxi;

		
	
	


f('testing.wav');
