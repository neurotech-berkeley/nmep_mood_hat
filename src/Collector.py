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
		self.cache = ... # TODO: create a NumPy array with size = cache_size


class PreProcessingSubBlock:
	pass

class PostProcessingSubBlock:
	pass

class MovingAverageFilter(PreProcessingSubBlock):
	def __init__(self, kernel_size=8, channel_count=4):
		self.kernel_size = kernel_size
		self.channel_count = channel_count

	def start(self, stream):
		#TODO implement moving average filter
		raise NotImplementedError("FIXME")


class OutputBlock:
	pass


class ProcessingPipeline:
	def __init__(self, bci:BCI, **args):
		self.board = bci
		self.PreProcessingBlock = []
		self.PostProcessingBlock = []
		for arg in args:
			if arg is PreProcessingSubBlock:
				self.PreProcessingBlock.append(arg)
			elif arg is PostProcessingSubBlock:
				self.PostProcessingBlock.append(arg)
			else:
				raise TypeError("Argument is not a processing subblock")
				
	def run(self):
		'''
		Processing pipeline should maintain ordering. All preprocessing blocks should run
		  first in order and store the results of preprocessing into the cache in the BCI object.
		  Post processing will operate on cache blocks (for Phase 3)
		'''
		raise NotImplementedError("FIXME")