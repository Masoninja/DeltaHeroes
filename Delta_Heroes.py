from mcpi.minecraft import Minecraft
from mcpi import block
import random
import time

mc = Minecraft.create() #put --"ip-address", portnumber-- in these parenthasis for remote usage
x, y, z = mc.player.getTilePos()

def ralsei():

	#wool colors
	#0 = white
	#1= orange
	#2= magenta
	#3= light blue
	#4= yellow
	#5=light green
	#6= pink
	#7=grey
	#8= light grey
	#9=cyan
	#10=purple
	#11=dark blue
	#12=brown
	#13= dark green
	#14 = red
	#15= black

	
	#row 1
	mc.setBlocks(x+4, y, z, x+10, y, z, 35, 13)
	mc.setBlocks(x+13, y, z, x+18, y, z, 35, 13)
	#row 2
	mc.setBlock(x+4, y+1, z, 35, 13)
	mc.setBlocks(x+5, y+1, z, x+9, y+1, z, 35, 15)
	mc.setBlock(x+10, y+1, z, 35, 13)
	mc.setBlock(x+12, y+1, z, 35, 13)
	mc.setBlocks(x+13, y+1, z, x+17, y+1, z, 35, 15)
	mc.setBlock(x+18, y+1, z, 35, 13)
	#row 3
	mc.setBlocks(x+5, y+2, z, x+6, y+2, z, 35, 13)
	mc.setBlocks(x+7, y+2, z, x+9, y+2, z, 35, 15)
	mc.setBlock(x+10, y+2, z, 35, 13)
	mc.setBlock(x+12, y+2, z, 35, 13)
	mc.setBlocks(x+13, y+2, z, x+17, y+2, z, 35, 15)
	mc.setBlocks(x+16, y+2, z, x+17, y+2, z, 35, 13)
	mc.setBlock(x+18, y+2, z, 35, 13)
	#row 4
	mc.setBlock(x+7, y+3, z, 35, 13)
	mc.setBlocks(x+8, y+3, z, x+9, y+3, z, 35, 15)
	mc.setBlock(x+10, y+3, z, 35, 13)
	mc.setBlock(x+12, y+3, z, 35, 13)
	mc.setBlocks(x+13, y+3, z, x+14, y+3, z, 35, 15)
	mc.setBlock(x+15, y+3, z, 35, 13)
	#row 5
	mc.setBlocks(x+6, y+4, z, x+7, y+4, z, 35, 15)
	mc.setBlocks(x+8, y+4, z, x+9, y+4, z, 35, 13)
	mc.setBlocks(x+10, y+4, z, x+12, y+4, z, 35, 15)
	mc.setBlocks(x+13, y+4, z, x+14, y+4, z, 35, 13)
	mc.setBlocks(x+15, y+4, z, x+16, y+4, z, 35, 15)
	#row 6
	mc.setBlocks(x+3, y+5, z, x+6, y+5, z, 35, 15)
	mc.setBlock(x+7, y+5, z, 35, 5)
	mc.setBlocks(x+8, y+5, z, x+9, y+5, z, 35, 15)
	mc.setBlock(x+10, y+5, z, 35, 5)
	mc.setBlocks(x+11, y+5, z, x+12, y+5, z, 35, 13)
	mc.setBlocks(x+13, y+5, z, x+14, y+5, z, 35, 15)
	mc.setBlock(x+15, y+5, z, 35, 5)
	mc.setBlocks(x+16, y+5, z, x+19, y+5, z, 35, 15)
	#row 7
	mc.setBlocks(x+1, y+6, z, x+2, y+6, z, 35, 15)
	mc.setBlocks(x+3, y+6, z, x+5, y+6, z, 35, 5)
	mc.setBlock(x+6, y+6, z, 35, 13)
	mc.setBlock(x+7, y+6, z, 35, 5)
	mc.setBlock(x+8, y+6, z, 35, 13)
	mc.setBlocks(x+9, y+6, z, x+13, y+6, z, 35, 5)
	mc.setBlock(x+14, y+6, z, 35, 13)
	mc.setBlocks(x+15, y+6, z, x+19, y+6, z, 35, 5)
	mc.setBlocks(x+20, y+6, z, x+21, y+6, z, 35, 15)
	#row 8
	mc.setBlock(x, y+7, z, 35, 15)
	mc.setBlocks(x+1, y+7, z, x+3, y+7, z, 35, 13)
	mc.setBlocks(x+4, y+7, z, x+18, y+7, z, 35, 5)
	mc.setBlocks(x+19, y+7, z, x+21, y+7, z, 35, 13)
	mc.setBlock(x+22, y+7, z, 35, 15)
	#row 9
	mc.setBlock(x+1, y+8, z, 35, 15)
	mc.setBlocks(x+2, y+8, z, x+4, y+8, z, 35, 13)
	mc.setBlocks(x+5, y+8, z, x+17, y+8, z, 35, 5)
	mc.setBlocks(x+18, y+8, z, x+20, y+8, z, 35, 13)
	mc.setBlock(x+21, y+8, z, 35, 15)
	#row 10
	mc.setBlock(x+2, y+9, z, 35, 15)
	mc.setBlocks(x+3, y+9, z, x+5, y+9, z, 35, 13)
	mc.setBlocks(x+6, y+9, z, x+16, y+9, z, 35, 5)
	mc.setBlocks(x+17, y+9, z, x+19, y+9, z, 35, 13)
	mc.setBlock(x+20, y+9, z, 35, 15)
	#row 11
	mc.setBlock(x+3, y+10, z, 35, 15)
	mc.setBlocks(x+4, y+10, z, x+6, y+10, z, 35, 13)
	mc.setBlocks(x+7, y+10, z, x+16, y+10, z, 35, 5)
	mc.setBlocks(x+17, y+10, z, x+18, y+10, z, 35, 13)
	mc.setBlock(x+19, y+10, z, 35, 15)
	#row 12
	mc.setBlock(x+4, y+11, z, 35, 15)
	mc.setBlocks(x+5, y+11, z, x+7, y+11, z, 35, 2)
	mc.setBlocks(x+8, y+11, z, x+11, y+11, z, 35, 5)
	mc.setBlock(x+12, y+11, z, 35, 15)
	mc.setBlocks(x+13, y+11, z, x+15, y+11, z, 35, 5)
	mc.setBlocks(x+16, y+11, z, x+17, y+11, z, 35, 13)
	mc.setBlock(x+18, y+11, z, 35, 15)
	#row 13
	mc.setBlock(x+4, y+12, z, 35, 15)
	mc.setBlocks(x+5, y+12, z, x+7, y+11, z, 35, 2)
	mc.setBlocks(x+8, y+12, z, x+10, y+12, z, 35, 5)
	mc.setBlocks(x+11, y+12, z, x+13, y+12, z, 35, 15)
	mc.setBlocks(x+14, y+12, z, x+15, y+12, z, 35, 5)
	mc.setBlocks(x+16, y+12, z, x+17, y+12, z, 35, 13)
	mc.setBlock (x+18, y+12, z, 35, 15)
	#row 14
	mc.setBlock(x+4, y+13, z, 35, 15)
	mc.setBlocks(x+5, y+13, z, x+7, y+13, z, 35, 2)
	mc.setBlocks(x+8, y+13, z, x+9, y+13, z, 35, 5)
	mc.setBlocks(x+10, y+13, z, x+14, y+13, z, 35, 15)
	mc.setBlock(x+15, y+13, z, 35, 5)
	mc.setBlocks(x+16, y+13, z, x+17, y+13, z, 35, 13)
	mc.setBlock(x+18, y+13, z, 35, 15)
	#row 15
	mc.setBlock(x+5, y+14, z, 35, 15)
	mc.setBlocks(x+6, y+14, z, x+8, y+14, z, 35, 2)
	mc.setBlock(x+9, y+14, z, 35, 5)
	mc.setBlocks(x+10, y+14, z, x+11, y+14, z, 35, 15)
	mc.setBlock(x+12, y+14, z, 35, 5)
	mc.setBlocks(x+13, y+14, z, x+14, y+14, z, 35, 15)
	mc.setBlock(x+15, y+14, z, 35, 5)
	mc.setBlock(x+16, y+14, z, 35, 13)
	mc.setBlock(x+17, y+14, z, 35, 15)
	#row 16
	mc.setBlock(x+5, y+15, z, 35, 15)
	mc.setBlocks(x+6, y+15, z, x+8, y+15, z, 35, 2)
	mc.setBlocks(x+9, y+15, z, x+11, y+15, z, 35, 5)
	mc.setBlock(x+12, y+15, z, 35, 13)
	mc.setBlocks(x+13, y+15, z, x+15, y+15, z, 35, 5)
	mc.setBlock(x+16, y+15, z, 35, 13)
	mc.setBlock(x+17, y+15, z, 35, 15)
	#row17
	mc.setBlock(x+5, y+16, z, 35, 15)
	mc.setBlocks(x+6, y+16, z, x+8, y+16, z, 35, 2)
	mc.setBlocks(x+9, y+16, z, x+16, y+16, z, 35, 13)
	mc.setBlock(x+17, y+16, z, 35, 15)
	#row 18
	mc.setBlock(x+6, y+17, z, 35, 15)
	mc.setBlock(x+7, y+17, z, 35, 2)
	mc.setBlocks(x+8, y+17, z, x+9, y+17, z, 35, 15)
	mc.setBlocks(x+10, y+17, z, x+13, y+17, z, 35, 2)
	mc.setBlocks(x+14, y+17, z, x+16, y+17, z, 35, 13)
	mc.setBlock(x+17, y+17, z, 35, 15)
	#row 19
	mc.setBlocks(x+6, y+18, z, x+7, y+18, z, 35, 15)
	mc.setBlocks(x+8, y+18, z, x+15, y+18, z, 35, 2)
	mc.setBlock(x+16, y+18, z, 35, 15)
	#row 20
	mc.setBlock(x+6, y+19, z, 35, 15)
	mc.setBlocks(x+7, y+19, z, x+16, y+19, z, 35, 2)
	mc.setBlock(x+17, y+19, z, 35, 15)
	#row 21
	mc.setBlock(x+6, y+20, z, 35, 13)
	mc.setBlocks(x+7, y+20, z, x+16, y+20, z, 35, 2)
	mc.setBlock(x+17, y+20, z, 35, 15)
	#row 22
	mc.setBlock(x+6, y+21, z, 35, 13)
	mc.setBlock(x+7, y+21, z, 35, 15)
	mc.setBlocks(x+8, y+21, z, x+15, y+21, z, 35, 2)
	mc.setBlocks(x+16, y+21, z, x+17, y+21, z, 35, 15)
	mc.setBlock(x+18, y+21, z, 35, 13)
	mc.setBlock(x+20, y+21, z, 35, 13)
	mc.setBlock(x+4, y+21, z, 35, 13)
	#row 23
	mc.setBlocks(x+2, y+22, z, x+3, y+22, z, 35, 13)
	mc.setBlock(x+4, y+22, z, 35, 15)
	mc.setBlock(x+5, y+22, z, 35, 13)
	mc.setBlocks(x+6, y+22, z, x+9, y+22, z, 35, 15)
	mc.setBlock(x+10, y+22, z, 35, 13)
	mc.setBlocks(x+11, y+22, z, x+13, y+22, z, 35, 15)
	mc.setBlock(x+14, y+22, z, 35, 13)
	mc.setBlocks(x+15, y+22, z, x+18, y+22, z, 35, 15)
	mc.setBlock(x+19, y+22, z, 35, 13)
	mc.setBlock(x+20, y+22, z, 35, 15)
	mc.setBlocks(x+21, y+22, z, x+22, y+22, z, 35, 13)
	#row 24
	mc.setBlock(x+1, y+23, z, 35, 13)
	mc.setBlocks(x+2, y+23, z, x+22, y+23, z, 35, 15)
	mc.setBlock(x+23, y+23, z, 35, 13)
	#row 25
	mc.setBlock(x+2, y+24, z, 35, 13)
	mc.setBlocks(x+3, y+24, z, x+7, y+24, z, 35, 15)
	mc.setBlocks(x+8, y+24, z, x+9, y+24, z, 35, 13)
	mc.setBlocks(x+10, y+24, z, x+14, y+24, z, 35, 15)
	mc.setBlocks(x+15, y+24, z, x+16, y+24, z, 35, 13)
	mc.setBlocks(x+17, y+24, z, x+21, y+24, z, 35, 15)
	mc.setBlock(x+22, y+24, z, 35, 13)
	#row 26
	mc.setBlock(x+1, y+25, z, 35, 13)
	mc.setBlocks(x+2, y+25, z, x+6, y+25, z, 35, 15)
	mc.setBlock(x+7, y+25, z, 35, 13)
	mc.setBlocks(x+8, y+25, z, x+9, y+25, z, 35, 15)
	mc.setBlock(x+10, y+25, z, 35, 13)
	mc.setBlocks(x+11, y+25, z, x+13, y+25, z, 35, 15)
	mc.setBlock(x+14, y+25, z, 35, 13)
	mc.setBlocks(x+15, y+25, z, x+16, y+25, z, 35, 15)
	mc.setBlock(x+17, y+25, z, 35, 13)
	mc.setBlocks(x+18, y+25, z, x+22, y+25, z, 35, 15)
	mc.setBlock(x+23, y+25, z, 35, 13)
	#row 27
	mc.setBlock(x+2, y+26, z, 35, 13)
	mc.setBlocks(x+3, y+26, z, x+5, y+26, z, 35, 15)
	mc.setBlock(x+6, y+26, z, 35, 13)
	mc.setBlocks(x+7, y+26, z, x+8, y+26, z, 35, 15)
	mc.setBlock(x+9, y+26, z, 35, 0)
	mc.setBlock(x+10, y+26, z, 35, 15)
	mc.setBlock(x+11, y+26, z, 35, 13)
	mc.setBlock(x+12, y+26, z, 35, 15)
	mc.setBlock(x+13, y+26, z, 35, 13)
	mc.setBlock(x+14, y+26, z, 35, 15)
	mc.setBlock(x+15, y+26, z, 35, 0)
	mc.setBlocks(x+16, y+26, z, x+17, y+26, z, 35, 15)
	mc.setBlock(x+18, y+26, z, 35, 13)
	mc.setBlocks(x+19, y+26, z, x+21, y+26, z, 35, 15)
	mc.setBlock(x+22, y+26, z, 35, 13)
	#row 28
	mc.setBlock(x+3, y+27, z, 35, 13)
	mc.setBlocks(x+4, y+27, z, x+5, y+27, z, 35, 15)
	mc.setBlock(x+6, y+27, z, 35, 13)
	mc.setBlocks(x+7, y+27, z, x+8, y+27, z, 35, 15)
	mc.setBlock(x+9, y+27, z, 35, 0)
	mc.setBlock(x+10, y+27, z, 35, 15)
	mc.setBlocks(x+11, y+27, z, x+13, y+27, z, 35, 13)
	mc.setBlock(x+14, y+27, z, 35, 15)
	mc.setBlock(x+15, y+27, z, 35, 0)
	mc.setBlocks(x+16, y+27, z, x+17, y+27, z, 35, 15)
	mc.setBlock(x+18, y+27, z, 35, 13)
	mc.setBlocks(x+19, y+27, z ,x+21, y+27, z, 35, 15)
	mc.setBlock(x+22, y+27, z, 35, 13)
	#row 29
	mc.setBlock(x+3, y+28, z, 35, 13)
	mc.setBlocks(x+4, y+28, z, x+6, y+28, z, 35, 15)
	mc.setBlock(x+7, y+28, z, 35, 13)
	mc.setBlocks(x+8, y+28, z, x+9, y+28, z, 35, 15)
	mc.setBlock(x+10, y+28, z, 35, 13)
	mc.setBlocks(x+11, y+28, z, x+13, y+28, z, 35, 15)
	mc.setBlock(x+14, y+28, z, 35, 13)
	mc.setBlocks(x+15, y+28, z, x+16, y+28, z, 35, 15)
	mc.setBlock(x+17, y+28, z, 35, 13)
	mc.setBlocks(x+18, y+28, z, x+20, y+28, z, 35, 15)
	mc.setBlock(x+21, y+28, z, 35, 13)
	#row 30
	mc.setBlock(x+3, y+29, z, 35, 13)
	mc.setBlocks(x+4, y+29, z, x+7, y+29, z, 35, 15)
	mc.setBlocks(x+8, y+29, z, x+9, y+29, z, 35, 13)
	mc.setBlocks(x+10, y+29, z, x+14, y+29, z, 35, 15)
	mc.setBlocks(x+15, y+29, z, x+16, y+29, z, 35, 13)
	mc.setBlocks(x+17, y+29, z, x+20, y+29, z, 35, 15)
	mc.setBlock(x+21, y+29, z, 35, 13)
	#row 31
	mc.setBlock(x+4, y+30, z, 35, 13)
	mc.setBlocks(x+5, y+30, z, x+19, y+30, z, 35, 15)
	mc.setBlock(x+20, y+30, z, 35, 13)
	#row 32
	mc.setBlock(x+4, y+31, z, 35, 13)
	mc.setBlocks(x+5, y+31, z, x+19, y+31, z, 35, 15)
	mc.setBlock(x+9, y+31, z, 35, 13)
	mc.setBlock(x+14, y+31, z, 35, 13)
	mc.setBlock(x+20, y+31, z, 35, 13)
	#row 33
	mc.setBlocks(x+4, y+32, z, x+19, y+32, z, 35, 13)
	mc.setBlocks(x+10, y+32, z, x+13, y+32, z, 35, 15)
	mc.setBlock(x+20, y+32, z, 35, 15)
	#row 34
	mc.setBlocks(x+3, y+33, z, x+21, y+33, z, 35, 15)
	mc.setBlocks(x+4, y+33, z, x+20, y+33, z, 35, 5)
	mc.setBlocks(x+10, y+33, z, x+14, y+33, z, 35, 15)
	#row 35
	mc.setBlocks(x+2, y+34, z, x+22, y+34, z, 35, 15)
	mc.setBlocks(x+3, y+34, z, x+10, y+34, z, 35, 5)
	mc.setBlock(x+13, y+34, z, 35, 5)
	mc.setBlocks(x+15, y+34, z, x+21, y+34, z, 35, 5)
	#row 36
	mc.setBlocks(x+2, y+35, z, x+21, y+35, z, 35, 15)
	mc.setBlocks(x+6, y+35, z, x+17, y+35, z, 35, 5)
	#row 37
	mc.setBlocks(x+6, y+36, z, x+17, y+36, z, 35, 15)
	mc.setBlocks(x+7, y+36, z, x+16, y+36, z, 35, 5)
	mc.setBlock(x+9, y+36, z, 35, 13)
	mc.setBlock(x+14, y+36, z, 35, 13)
	#row 38
	mc.setBlocks(x+6, y+37, z, x+17, y+37, z, 35, 15)
	mc.setBlocks(x+7, y+37, z, x+16, y+37, z, 35, 5)
	mc.setBlock(x+8, y+37, z, 35, 13)
	mc.setBlock(x+9, y+37, z, 35, 15)
	mc.setBlock(x+15, y+37, z, 35, 13)
	mc.setBlock(x+14, y+37, z, 35, 15)
	#row 39
	mc.setBlocks(x+7, y+38, z, x+17, y+38, z, 35, 15)
	mc.setBlocks(x+10, y+38, z, x+13, y+38, z, 35, 5)
	#row 40
	mc.setBlocks(x+9, y+39, z, x+15, y+39, z, 35, 15)
	mc.setBlocks(x+10, y+39, z, x+13, y+39, z, 35, 5)
	#row 41
	mc.setBlocks(x+10, y+40, z, x+14, y+40, z, 35, 15)
	mc.setBlocks(x+11, y+40, z, x+12, y+40, z, 35, 5)
	#row 42
	mc.setBlocks(x+10, y+41, z, x+14, y+41, z, 35, 15)
	mc.setBlocks(x+11, y+41, z, x+12, y+41, z, 35, 5)
	#row 43
	mc.setBlocks(x+11, y+42, z, x+13, y+42, z, 35, 15)
	mc.setBlock(x+12, y+42, z, 35, 5)
	#row 44
	mc.setBlock(x+11, y+43, z, 35, 15)

def susie():
	#wool colors
	#0 = white
	#1= orange
	#2= magenta
	#3= light blue
	#4= yellow
	#5=light green
	#6= pink
	#7=grey
	#8= light grey
	#9=cyan
	#10=purple
	#11=dark blue
	#12=brown
	#13= dark green
	#14 = red
	#15= black

	'''IMPORTANT: Susie's sprite, unlike Ralsei's, is from 1 - endnumber instread of 0 - endnumber'''
	#row 1
	mc.setBlocks(x+6, y, z, x+20, y, z, 35, 15)
	mc.setBlocks(x+7, y, z, x+11, y, z, 35, 4)
	mc.setBlock(x+13, y, z, 0)
	mc.setBlocks(x+15, y, z, x+19, y, z, 35, 4)
	#row 2
	mc.setBlocks(x+6, y+1, z, x+20, y+1, z, 35, 15)
	mc.setBlock(x+12, y+1, z, 35, 4)
	mc.setBlock(x+14, y+1, z, 35, 4)
	#row 3
	mc.setBlocks(x+7, y+2, z, x+19, y+2, z, 35, 15)
	#row 4
	mc.setBlocks(x+8, y+3, z, x+18, y+3, z, 35, 15)
	mc.setBlock(x+13, y+3, z, 35, 10)
	#row 5
	mc.setBlocks(x+9, y+4, z, x+17, y+4, z, 35, 15)
	mc.setBlock(x+13, y+4, z, 35, 10)
	#row 6
	mc.setBlocks(x+9, y+5, z, x+17, y+5, z, 35, 15)
	mc.setBlock(x+13, y+5, z, 35, 10)
	#row 7
	mc.setBlocks(x+9, y+6, z, x+17, y+6, z, 35, 15)
	mc.setBlock(x+13, y+6, z, 35, 10)
	#row 8
	mc.setBlocks(x+8, y+7, z, x+18, y+7, z, 35, 15)
	mc.setBlock(x+13, y+7, z, 35, 10)
	#row 9
	mc.setBlocks(x+7, y+8, z, x+19, y+8, z, 35, 15)
	mc.setBlocks(x+9, y+8, z, x+13, y+8, z, 35, 2)
	mc.setBlocks(x+15, y+8, z, x+18, y+8, z, 35, 2)
	#row 10
	mc.setBlocks(x+4, y+9, z, x+23, y+9, z, 35, 15)
	mc.setBlocks(x+8, y+9, z, x+12, y+9, z, 35, 2)
	mc.setBlocks(x+14, y+9, z, x+19, y+9, z, 35, 2)
	#row 11
	mc.setBlocks(x+3, y+10, z, x+23, y+10, z, 35, 15)
	mc.setBlocks(x+4, y+10, z, x+6, y+10, z, 35, 6)
	mc.setBlocks(x+8, y+10, z, x+12, y+10, z, 35, 2)
	mc.setBlocks(x+14, y+10, z, x+19, y+10, z, 35, 2)
	mc.setBlocks(x+21, y+10, z, x+22, y+10, z, 35, 6)
	#row 12
	mc.setBlocks(x+2, y+11, z, x+24, y+11, z, 35, 15)
	mc.setBlocks(x+3, y+11, z, x+5, y+11, z, 35, 6)
	mc.setBlocks(x+6, y+11, z, x+7, y+11, z, 35, 10)
	mc.setBlocks(x+9, y+11, z, x+12, y+11, z, 35, 2)
	mc.setBlocks(x+14, y+11, z, x+18, y+11, z, 35, 2)
	mc.setBlock(x+20, y+11, z, 35, 10)
	mc.setBlocks(x+21, y+11, z, x+23, y+11, z, 35, 6)
	#row 13
	mc.setBlocks(x+2, y+12, z, x+24, y+12, z, 35, 15)
	mc.setBlocks(x+3, y+12, z, x+7, y+12, z, 35, 6)
	mc.setBlock(x+6, y+12, z, 35, 10)
	mc.setBlocks(x+9, y+12, z, x+18, y+12, z, 35, 2)
	mc.setBlock(x+12, y+12, z, 35, 10)
	mc.setBlock(x+20, y+12, z, 35, 10)
	mc.setBlocks(x+21, y+12, z, x+23, y+12, z, 35, 6)
	#row 14
	mc.setBlocks(x+2, y+13, z, x+24, y+13, z, 35, 15)
	mc.setBlock(x+3, y+13, z, 35, 10)
	mc.setBlocks(x+4, y+13, z, x+7, y+13, z, 35, 6)
	mc.setBlocks(x+9, y+13, z, x+18, y+13, z, 35, 2)
	mc.setBlocks(x+20, y+13, z, x+22, y+13, z, 35, 6)
	mc.setBlock(x+23, y+13, z, 35, 10)
	#row 15
	mc.setBlocks(x+2, y+14, z, x+25, y+14, z, 35, 15)
	mc.setBlocks(x+10, y+14, z, x+12, y+14, z, 35, 2)
	mc.setBlocks(x+15, y+14, z, x+17, y+14, z, 35, 2)
	#row 16
	mc.setBlocks(x+1, y+15, z, x+26, y+15, z, 35, 15)
	mc.setBlock(x+2, y+15, z, 35, 4)
	mc.setBlock(x+4, y+15, z, 35, 4)
	mc.setBlock(x+6, y+15, z, 35, 4)
	mc.setBlock(x+9, y+15, z, 35, 10)
	mc.setBlocks(x+13, y+15, z, x+14, y+15, z, 35, 4)
	mc.setBlock(x+18, y+15, z, 35, 10)
	mc.setBlock(x+21, y+15, z, 35, 4)
	mc.setBlock(x+23, y+15, z, 35, 4)
	mc.setBlock(x+25,  y+15, z, 35, 4)
	#row 17
	mc.setBlocks(x+2, y+16, z, x+25, y+16, z, 35, 15)
	mc.setBlock(x+10, y+16, z, 35, 10)
	mc.setBlocks(x+12, y+16, z, x+15, y+16, z, 35, 4)
	mc.setBlock(x+17, y+16, z, 35, 10)
	#row 18
	mc.setBlocks(x+2, y+17, z, x+24, y+17, z, 35, 15)
	mc.setBlock(x+3, y+17, z, 35, 10)
	mc.setBlocks(x+4, y+17, z, x+6, y+17, z, 35, 6)
	mc.setBlock(x+7, y+17, z, 35, 10)
	mc.setBlock(x+10, y+17, z, 35, 10)
	mc.setBlock(x+12, y+17, z, 35, 4)
	mc.setBlock(x+15, y+17, z, 35, 4)
	mc.setBlock(x+17, y+17, z, 35, 10)
	mc.setBlocks(x+20, y+17, z, x+22, y+17, z, 35, 6)
	mc.setBlock(x+23, y+17, z, 35, 10)
	#row 19
	mc.setBlocks(x+3, y+18, z, x+23, y+18, z, 35, 15)
	mc.setBlocks(x+4, y+18, z, x+7, y+18, z, 35, 6)
	mc.setBlock(x+11, y+18, z, 35, 10)
	mc.setBlocks(x+13, y+18, z, x+14, y+18, z, 35, 10)
	mc.setBlock(x+16, y+18, z, 35, 10)
	mc.setBlocks(x+20, y+18, z, x+22, y+18, z, 35, 6)
	#row 20
	mc.setBlocks(x+3, y+19, z, x+23, y+19, z, 35, 15)
	mc.setBlock(x+4, y+19, z, 35, 10)
	mc.setBlocks(x+5, y+19, z, x+7, y+19, z, 35, 6)
	mc.setBlock(x+11, y+19, z, 35, 10)
	mc.setBlocks(x+13, y+19, z, x+14, y+19, z, 35, 10)
	mc.setBlock(x+16, y+19, z, 35, 10)
	mc.setBlocks(x+20, y+19, z, x+22, y+19, z, 35, 10)
	mc.setBlock(x+21, y+19, z, 35, 6)
	#row 21
	mc.setBlocks(x+4, y+20, z, x+22, y+20, z, 35, 15)
	mc.setBlock(x+5, y+20, z, 35, 10)
	mc.setBlock(x+6, y+20, z, 35, 6)
	mc.setBlock(x+11, y+20, z, 35, 10)
	mc.setBlocks(x+13, y+20, z, x+14, y+20, z, 35, 10)
	mc.setBlock(x+16, y+20, z, 35, 10)
	mc.setBlock(x+22, y+20, z, 35, 15)
	#row 22
	mc.setBlocks(x+4, y+21, z, x+22, y+21, z, 35, 15)
	mc.setBlock(x+7, y+21, z, 35, 4)
	mc.setBlock(x+11, y+21, z, 35, 10)
	mc.setBlocks(x+13, y+21, z, x+14, y+21, z, 35, 10)
	mc.setBlock(x+16, y+21, z, 35, 10)
	mc.setBlock(x+20, y+21, z, 35, 4)
	#row 23
	mc.setBlocks(x+4, y+22, z, x+23, y+22, z, 35, 15)
	mc.setBlock(x+6, y+22, z, 35, 4)
	mc.setBlock(x+11, y+22, z, 35, 10)
	mc.setBlock(x+16, y+22, z, 35, 10)
	mc.setBlock(x+21, y+22, z, 35, 4)
	#row 24
	mc.setBlocks(x+4, y+23, z, x+25, y+23, z, 35, 15)
	mc.setBlock(x+8, y+23, z, 35, 2)
	mc.setBlock(x+11, y+23, z, 35, 10)
	mc.setBlocks(x+13, y+23, z, x+14, y+23, z, 35, 10)
	mc.setBlock(x+16, y+23, z, 35, 10)
	mc.setBlock(x+19, y+23, z, 35, 2)
	mc.setBlocks(x+22, y+23, z, x+23, y+23, z, 35, 2)
	#row 25
	mc.setBlocks(x+2, y+24, z, x+25, y+24, z, 35, 15)
	mc.setBlock(x+5, y+24, z, 35, 2)
	mc.setBlocks(x+7, y+24, z, x+8, y+24, z, 35, 2)
	mc.setBlock(x+12, y+24, z, 35, 10)
	mc.setBlock(x+15, y+24, z, 35, 10)
	mc.setBlock(x+19, y+24, z, 35, 2)
	mc.setBlocks(x+21, y+24, z, x+22, y+24, z, 35, 2)
	#row 26
	mc.setBlocks(x+2, y+25, z, x+25, y+25, z, 35, 15)
	mc.setBlock(x+3, y+25, z, 35, 2)
	mc.setBlocks(x+5, y+25, z, x+9, y+25, z, 35, 2)
	mc.setBlock(x+11, y+25, z, 35, 10)
	mc.setBlock(x+16, y+25, z, 35, 10)
	mc.setBlocks(x+18, y+25, z, x+21, y+25, z, 35, 2)
	mc.setBlocks(x+23, y+25, z, x+24, y+25, z, 35, 2)
	mc.setBlocks(x+13, y+25, z, x+14, y+25, z, 35, 6)
	#row 27
	mc.setBlocks(x+2, y+26, z, x+24, y+26, z, 35, 15)
	mc.setBlocks(x+3, y+26, z, x+8, y+26, z, 35, 2)
	mc.setBlock(x+13, y+26, z, 35, 10)
	mc.setBlock(x+14, y+26, z, 35, 6)
	mc.setBlocks(x+18, y+26, z, x+23, y+26, z, 35, 2)
	#row 28
	mc.setBlocks(x+3, y+27, z, x+23, y+27, z, 35, 15)
	mc.setBlocks(x+4, y+27, z, x+7, y+27, z, 35, 2)
	mc.setBlocks(x+11, y+27, z, x+14, y+27, z, 35, 10)
	mc.setBlocks(x+17, y+27, z, x+22, y+27, z, 35, 2)
	#row 29
	mc.setBlocks(x+4, y+28, z, x+22, y+28, z, 35, 15)
	mc.setBlocks(x+5, y+28, z, x+6, y+28, z, 35, 2)
	mc.setBlocks(x+14, y+28, z, x+15, y+28, z, 35, 6)
	mc.setBlocks(x+18, y+28, z, x+21, y+28, z, 35, 2)
	#row 30
	mc.setBlocks(x+5, y+29, z, x+21, y+29, z, 35, 15)
	mc.setBlocks(x+8, y+29, z, x+13, y+29, z, 35, 6)
	mc.setBlocks(x+15, y+29, z, x+16, y+29, z, 35, 6)
	mc.setBlocks(x+17, y+29, z, x+19, y+29, z, 35, 2)
	#row 31
	mc.setBlocks(x+6, y+30, z, x+22, y+30, z, 35, 15)
	mc.setBlocks(x+7, y+30, z, x+14, y+30, z, 35, 6)
	mc.setBlock(x+9, y+30, z, 35, 10)
	mc.setBlock(x+11, y+30, z, 35, 10)
	mc.setBlock(x+17, y+30, z, 35, 2)
	mc.setBlocks(x+20, y+30, z, x+21, y+30, z, 35, 2)
	#row 32
	mc.setBlocks(x+5, y+31, z, x+22, y+31, z, 35, 15)
	mc.setBlocks(x+7, y+31, z, x+13, y+31, z, 35, 6)
	mc.setBlock(x+21, y+31, z, 35, 2)
	#row 33
	mc.setBlocks(x+3, y+32, z, x+22, y+32, z, 35, 15)
	mc.setBlocks(x+4, y+32, z, x+7, y+32, z, 35, 2)
	mc.setBlocks(x+17, y+32, z, x+19, y+32, z, 35, 2)
	mc.setBlock(x+21, y+32, z, 35, 2)
	#row 34
	mc.setBlocks(x+2, y+33, z, x+22, y+33, z, 35, 15)
	mc.setBlocks(x+3, y+33, z, x+6, y+33, z, 35, 2)
	mc.setBlocks(x+16, y+33, z, x+18, y+33, z, 35, 2)
	mc.setBlocks(x+20, y+33, z, x+21, y+33, z, 35, 2)
	#row 35
	mc.setBlocks(x+1, y+34, z, x+22, y+34, z, 35, 15)
	mc.setBlocks(x+4, y+34, z, x+7, y+34, z, 35, 2)
	mc.setBlocks(x+12, y+34, z, x+13, y+34, z, 35, 2)
	mc.setBlocks(x+15, y+34, z, x+17, y+34, z, 35, 2)
	mc.setBlocks(x+19, y+34, z, x+21, y+34, z, 35, 2)
	#row 36
	mc.setBlocks(x+4, y+35, z, x+22, y+35, z, 35, 15)
	mc.setBlocks(x+5, y+35, z, x+7, y+35, z, 35, 2)
	mc.setBlocks(x+10, y+35, z, x+12, y+35, z, 35, 2)
	mc.setBlocks(x+14, y+35, z, x+17, y+35, z, 35, 2)
	mc.setBlocks(x+19, y+35, z, x+21, y+35, z, 35, 2)
	#row 37
	mc.setBlocks(x+4, y+36, z, x+22, y+36, z, 35, 15)
	mc.setBlocks(x+6, y+36, z, x+7, y+36, z, 35, 2)
	mc.setBlocks(x+9, y+36, z, x+12, y+36, z, 35, 2)
	mc.setBlocks(x+14, y+36, z, x+21, y+36, z, 35, 2)
	#row 38
	mc.setBlocks(x+3, y+37, z, x+21, y+37, z, 35, 15)
	mc.setBlocks(x+4, y+37, z, x+7, y+37, z, 35, 2)
	mc.setBlocks(x+9, y+37, z, x+20, y+37, z, 35, 2)
	#row 39
	mc.setBlocks(x+2, y+38, z, x+21, y+38, z, 35, 15)
	mc.setBlocks(x+3, y+38, z, x+20, y+38, z, 35, 2)
	#row 40
	mc.setBlocks(x+2, y+39, z, x+20, y+39, z, 35, 15)
	mc.setBlocks(x+6, y+39, z, x+19, y+39, z, 35, 2)
	#row 41
	mc.setBlock(x+2, y+40, z, 35, 15)
	mc.setBlocks(x+6, y+40, z, x+19, y+40, z, 35, 15)
	mc.setBlocks(x+8, y+40, z, x+18, y+40, z, 35, 2)
	#row 42
	mc.setBlocks(x+8, y+41, z, x+18, y+41, z, 35, 15)
	mc.setBlocks(x+11, y+41, z, x+16, y+41, z, 35, 2)
	#row 43
	mc.setBlocks(x+11, y+42, z, x+16, y+42, z, 35, 15)
	
	
	#wool colors
	#0 = white
	#1= orange
	#2= magenta
	#3= light blue
	#4= yellow
	#5=light green
	#6= pink
	#7=grey
	#8= light grey
	#9=cyan
	#10=purple
	#11=dark blue
	#12=brown
	#13= dark green
	#14 = red
	#15= black
	#57 is diamond which is only for Kris.
	
	
def kris():
	#row 1
	mc.setBlocks(x+5, y, z, x+16, y, z, 35, 11)
	mc.setBlock(x+11, y, z, 35, 35, 3)
	#row 2
	mc.setBlocks(x+5, y+1, z, x+16, y+1, z, 35, 11)
	mc.setBlocks(x+6, y+1, z, x+15, y+1, z, 35, 3)
	mc.setBlock(x+7, y+1, z, 35, 8)
	mc.setBlocks(x+13, y+1, z, x+14, y+1, z, 35, 8)
	mc.setBlock(x+10, y+1, z, 35, 11)
	#row 3
	mc.setBlocks(x+6, y+2, z, x+15, y+2, z, 35, 11)
	mc.setBlocks(x+7, y+2, z, x+14, y+2, z, 35, 3)
	mc.setBlock(x+8, y+2, z, 35, 8)
	mc.setBlock(x+12, y+2, z, 35, 8)
	mc.setBlock(x+10, y+2, z, 35, 11)
	#row 4
	mc.setBlocks(x+6, y+3, z, x+15, y+3, z, 35, 11)
	mc.setBlocks(x+7, y+3, z, x+14, y+3, z, 35, 8)
	mc.setBlock(x+9, y+3, z, 35, 3)
	mc.setBlock(x+11, y+3, z, 35, 3)
	mc.setBlock(x+10, y+3, z, 35, 11)
	#row 5
	mc.setBlocks(x+6, y+4, z, x+15, y+4, z, 35, 11)
	mc.setBlocks(x+7, y+4, z, x+8, y+4, z, 35, 8)
	mc.setBlocks(x+12, y+4, z, x+14, y+4, z, 35, 8)
	#row 6
	mc.setBlocks(x+7, y+5, z, x+14, y+5, z, 35, 11)
	mc.setBlock(x+10, y+5, z, 35, 15)
	#row 7
	mc.setBlocks(x+7, y+6, z, x+14, y+6, z, 35, 11)
	mc.setBlock(x+10, y+6, z, 35, 15)
	#row 8
	mc.setBlocks(x+4, y+7, z, x+17, y+7, z, 35, 11)
	mc.setBlock(x+10, y+7, z, 35, 15)
	#row 9
	mc.setBlocks(x+3, y+8, z, x+18, y+8, z, 35, 11)
	mc.setBlocks(x+4, y+8, z, x+5, y+8, z, 35, 3)
	mc.setBlock(x+6, y+8, z, 35, 8)
	mc.setBlock(x+15, y+8, z, 35, 8)
	mc.setBlocks(x+16, y+8, z, x+17, y+8, z, 35, 3)
	#row 10
	mc.setBlocks(x+2, y+9, z, x+19, y+9, z, 35, 11)
	mc.setBlocks(x+3, y+9, z, x+6, y+9, z, 35, 3)
	mc.setBlocks(x+4, y+9, z, x+5, y+9, z, 35, 8)
	mc.setBlocks(x+15, y+9, z, x+18, y+9, z, 35, 3)
	mc.setBlocks(x+16, y+9, z, x+17, y+9, z, 35, 8)
	#row 11
	mc.setBlocks(x+2, y+10, z, x+19, y+10, z, 35, 11)
	mc.setBlocks(x+3, y+10, z, x+4, y+10, z, 35, 3)
	mc.setBlocks(x+5, y+10, z, x+6, y+10, z, 35, 8)
	mc.setBlocks(x+15, y+10, z, x+16, y+10, z, 35, 8)
	mc.setBlocks(x+17, y+10, z, x+18, y+10, z, 35, 3)
	#row 12
	mc.setBlocks(x+3, y+11, z, x+18, y+11, z, 35, 11)	
	mc.setBlocks(x+4, y+11, z, x+5, y+11, z, 35, 3)
	mc.setBlocks(x+16, y+11, z, x+17, y+11, z, 35, 3)
	#row 13
	mc.setBlocks(x+3, y+12, z, x+18, y+12, z, 35, 11)
	mc.setBlocks(x+4, y+12, z, x+5, y+12, z, 35, 3)
	mc.setBlocks(x+16, y+12, z, x+17, y+12, z, 35, 3)
	mc.setBlocks(x+9, y+12, z, x+12, y+12, z, 35, 3)
	mc.setBlocks(x+10, y+12, z, x+11, y+12, z, 35, 8)
	#row 14
	mc.setBlocks(x+3, y+13, z, x+18, y+13, z, 35, 11)
	mc.setBlocks(x+4, y+13, z, x+5, y+13, z, 57)
	mc.setBlocks(x+8, y+13, z, x+13, y+13, z, 35, 8)
	mc.setBlocks(x+16, y+13, z, x+17, y+13, z, 57)
	#row 15
	mc.setBlocks(x+2, y+14, z, x+17, y+14, z, 35, 11)
	mc.setBlock(x+3, y+14, z, 35, 2)
	mc.setBlock(x+8, y+14, z, 35, 3)
	mc.setBlocks(x+9, y+14, z, x+13, y+14, z, 35, 8)
	mc.setBlock(x+16, y+14, z, 57)
	#row 16
	mc.setBlocks(x+2, y+15, z, x+17, y+15, z, 35, 11)
	mc.setBlocks(x+3, y+15, z, x+5, y+15, z, 35, 2)
	mc.setBlocks(x+9, y+15, z, x+14, y+15, z, 35, 3)
	mc.setBlock(x+16, y+15, z, 35, 3)
	#row 17
	mc.setBlocks(x+3, y+16, z, x+17, y+16, z, 35, 11)
	mc.setBlocks(x+4, y+16, z, x+7, y+16, z, 35, 2)
	mc.setBlocks(x+11, y+16, z, x+13, y+16, z, 35, 3)
	#row 18
	mc.setBlocks(x+3, y+17, z, x+18, y+17, z, 35, 11)
	mc.setBlock(x+4, y+17, z, 35, 3)
	mc.setBlocks(x+5, y+17, z, x+9, y+17, z, 35, 2)
	mc.setBlock(x+15, y+17, z, 35, 3)
	mc.setBlocks(x+16, y+17, z, x+17, y+17, z, 35, 8)
	#row 19
	mc.setBlocks(x+4, y+18, z, x+17, y+18, z, 35, 11)
	mc.setBlocks(x+5, y+18, z, x+6, y+18, z, 35, 3)
	mc.setBlocks(x+7, y+18, z, x+10, y+18, z, 35, 2)
	mc.setBlock(x+11, y+18, z, 35, 3)
	mc.setBlock(x+14, y+18, z, 35, 3)
	mc.setBlocks(x+15, y+18, z, x+16, y+18, z, 35, 8)
	#row 20
	mc.setBlocks(x+4, y+19, z, x+16, y+19, z, 35, 11)
	mc.setBlocks(x+7, y+19, z, x+12, y+19, z, 35, 3)
	mc.setBlocks(x+8, y+19, z, x+11, y+19, z, 35, 2)
	mc.setBlocks(x+14, y+19, z, x+15, y+19, z, 35, 8)
	#row 21
	mc.setBlock(x+2, y+20, z, 35, 11)
	mc.setBlocks(x+4, y+20, z, x+16, y+20, z, 35, 11)
	mc.setBlock(x+18, y+20, z, 35, 11)
	mc.setBlock(x+8, y+20, z, 35, 3)
	#row 22
	mc.setBlocks(x+2, y+21, z, x+19, y+21, z, 35, 11)
	mc.setBlocks(x+10, y+21, z, x+11, y+21, z, 57)
	#row 23
	mc.setBlocks(x+1, y+22, z, x+19, y+22, z, 35, 11)
	mc.setBlocks(x+7, y+22, z, x+13, y+22, z, 35, 3)
	mc.setBlocks(x+8, y+22, z, x+12, y+22, z, 57)
	#row 24
	mc.setBlocks(x+1, y+23, z, x+19, y+23, z, 35, 11)
	mc.setBlocks(x+6, y+23, z, x+7, y+23, z, 57)
	mc.setBlocks(x+12, y+23, z, x+14, y+23, z, 57)
	#row 25
	mc.setBlocks(x+1, y+24, z, x+19, y+24, z, 35, 11)
	mc.setBlocks(x+5, y+24, z, x+15, y+24, z, 57)
	#row 26
	mc.setBlocks(x+1, y+25, z, x+19, y+25, z, 35, 11)
	mc.setBlock(x+5, y+25, z, 35, 3)
	mc.setBlocks(x+6, y+25, z, x+14, y+25, z, 57)
	mc.setBlock(x+15, y+25, z, 35, 3)
	#row 27
	mc.setBlocks(x+1, y+26, z, x+19, y+26, z, 35, 11)
	mc.setBlocks(x+5, y+26, z, x+12, y+26, z, 35, 3)
	#row 28
	mc.setBlocks(x+1, y+27, z, x+19, y+27, z, 35, 11)
	mc.setBlocks(x+6, y+27, z, x+7, y+27, z, 35, 3)
	mc.setBlocks(x+9, y+27, z, x+10, y+27, z, 35, 3)
	#row 29
	mc.setBlocks(x+1, y+28, z, x+19, y+28, z, 35, 11)
	mc.setBlock(x+6, y+28, z, 35, 3)
	mc.setBlock(x+9, y+28, z, 35, 3)
	#row 30
	mc.setBlocks(x+1, y+29, z, x+19, y+29, z, 35, 11)
	#row 31
	mc.setBlocks(x+2, y+30, z, x+18, y+30, z, 35, 11)
	#row 32
	mc.setBlocks(x+2, y+31, z, x+18, y+31, z, 35, 11)
	#row 33
	mc.setBlocks(x+3, y+32, z, x+17, y+32, z, 35, 11)
	#row 34
	mc.setBlocks(x+3, y+33, z, x+17, y+33, z, 35, 11)
	#row 35
	mc.setBlocks(x+4, y+34, z, x+16, y+34, z, 35, 11)
	#row 36
	mc.setBlocks(x+6, y+35, z, x+14, y+35, z, 35, 11)
	#row 37
	mc.setBlock(x+13, y+36, z, 35, 11)
	mc.setBlock(x+15, y+36, z, 35, 11)
	#and FINALLY DONE
	
	

	
mc.postToChat("the art will spawn where the program was run.")
mc.postToChat("type a name in the console.")
mc.postToChat("or hit enter in the terminal, then click a block")
mc.postToChat("(Diamond, Gold, Obsidian) with a sword,")


	
name = raw_input("alternatively, enter a character's name here. (kris, susie, ralsei): ")
		


variable = 0
yeet = 0
		 
def execute():
	if name == "susie":
		susie()
		mc.postToChat("Creating 'Susie'...")
		yeet = yeet + 1
	elif name == "kris":
		kris()
		mc.postToChat("Creating 'Kris'...")
		yeet = yeet + 1
	elif name == "ralsei":
		ralsei()
		mc.postToChat("Creating 'ralsei'...")
		yeet = yeet + 1
		
	 
	
	


#deltaheroes main code
#basically, if you hit different blocks with a sword, it makes specific heroes!



while variable == 0:
	execute()			
	variable = variable + 1
	
while yeet == 0:
	for hitBlock in mc.events.pollBlockHits():
		if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == block.DIAMOND_BLOCK.id:
			mc.postToChat("Creating 'Kris'...")
			kris()
			yeet = yeet + 1
		elif mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == block.GOLD_BLOCK.id:
			mc.postToChat("Creating 'Ralsei'...")
			yeet = yeet + 1
			ralsei()
		elif mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == block.OBSIDIAN.id:
			mc.postToChat("Creating 'Susie'...")
			yeet = yeet + 1
			susie()
		


