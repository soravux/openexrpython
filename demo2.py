import OpenEXR

infile = OpenEXR.InputFile("GoldenGate.exr")
h = infile.header()
channels = list(h['channels'].keys())
newchannels = dict(list(zip(channels, infile.channels(channels))))

h['comments'] = "A picture of some delicious pie"

out = OpenEXR.OutputFile("modified.exr", h)
out.writePixels(newchannels)
