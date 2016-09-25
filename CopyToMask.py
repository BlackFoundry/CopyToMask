
g = CurrentGlyph()

mask = g.getLayer("mask")

mask.clear() 
g.copyToLayer("mask")
mask.update()

g.update()		
