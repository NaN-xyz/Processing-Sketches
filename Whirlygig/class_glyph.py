

class Glyph():

	def __init__(self):

		self.font = ""
		self.fontsize = 180
		self.visible = True
		self.content = ""
		self.r = 0
		self.x = 100
		self.y = 100
		self.yshift = 100

	def Update(self):

		x, y = self.x, self.y 
		x = width / 2
		y = height / 2

		#bg
		fill(255,50)

		#text
		textSize(self.fontsize)
		pushMatrix()
		txt = self.content
		fill(255)
		translate(x,y)
		rotate(self.r)
		text(txt,0,self.yshift)
		popMatrix()
		
