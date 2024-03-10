import numpy as np


'''
Class to manage collection of the BCI data and store into a buffer store. Used as the input of
the pipeline to apply functions onto the data storage in the BCICollector.
'''
class BCI:
	def __init__(self, BCI_name="MuseS", BCI_params={}):
		self.name = BCI_name
		if BCI_params == "MuseS":
			if BCI_params:
				self.BCI_params == BCI_params
			else:
				self.BCI_params = {"sampling_rate": 256, "streaming_software":"Petals", "streaming_protocol":"OSC", "cache_size":256*30}
		else:
			raise Exception("Unsupported BCI board") # change this when adding other headsets
		
		self.sampling_rate = self.BCI_params["sampling_rate"]
		self.streaming_software = self.BCI_params["streaming_software"]
		self.streaming_protocol = self.BCI_params["streaming_protocol"]
		self.cache_size = self.BCI_params["cache_size"]
		self.cache = ... # TODO: create a NumPy array with 