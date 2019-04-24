import math
import random
from class_glyph import Glyph

r = 0 #rotation
rinc = 0.01

textlist = "#,S,£,{,ß,*,?,Å,&,y,¶,8,#,&,t,Q,@,•,¥,f,°,3,ä,t,†,§,2,>,r,0,Ç"
textlist = textlist.split(",")
allglyphs = []

textcounter=-1

timer = 0

def setup():

	size(800,800)
	font01 = createFont("AbrilFatface-Regular.ttf", 200);
	
	textFont(font01)
	textAlign(CENTER,CENTER)

	frameRate(20)

def draw():

	global timer

	background(0)
	DrawAll()

	timer+=1

	saveFrame("frames/A_####.jpg")

def DrawAll():

	global r, rinc, allglyphs, textcounter, textlist
	r+=rinc

	if timer%20==0: textcounter+=1
	if textcounter>len(textlist)-1:textcounter=0

	for n in range(0, len(allglyphs)):

		glyph = allglyphs[n]
		glyph.r = glyph.r + r
		glyph.Update()

	nglyph = Glyph()
	nglyph.r = r+rinc

	txt = textlist[textcounter]
	ntxt = txt.decode('utf8')

	nglyph.content = ntxt
	allglyphs.append(nglyph)

	maxsize = 10

	if len(allglyphs) > maxsize: allglyphs.pop(0)

	#nglyph.Update()

	r+=rinc
