from pynput.keyboard import Key, Controller
import time

class TetrisBeats:
	
	@staticmethod
	def beat1a(qt, beat):
		## Bar 10/11/26/27
		quack(qt, beat)
		
		quack(qt, beat/2)
		quack(qt, beat/2)
		
		quack(qt, beat)

		quack(qt, beat/2)
		quack(qt, beat/2)

	@staticmethod
	def beat1b(qt, beat):
		## Bar 6/14/30
		time.sleep(beat/2)
		
		quack(qt, beat)

		quack(qt, beat/2)

		quack(qt, beat)

		quack(qt, beat/2)
		quack(qt, beat/2)

	@staticmethod
	def beat2a(qt, beat):
		## Bar 11/27
		TetrisBeats.beat1a(qt, beat)

	@staticmethod
	def beat2b(qt, beat):
		## Bar 7/15/31
		quack(qt*2, beat*1.5)
		
		quack(qt, beat/2)

		quack(qt, beat)

		quack(qt, beat/2)
		quack(qt, beat/2)

	@staticmethod
	def beat3(qt, beat):
		## Bar 8/12/16/28/32
		quack(qt, beat)
		
		quack(qt, beat/2)
		quack(qt, beat/2)
		
		quack(qt, beat)
		
		quack(qt, beat)

	@staticmethod
	def beat4(qt, beat):
		## Bar 9/13/17/29/33
		quack(qt, beat)

		quack(qt, beat)

		quack(qt, beat)

		time.sleep(beat)


def quack(qt=.02, wait=0.021):
	keyboard_controller.press(Key.ctrl_r)
	time.sleep(qt)
	keyboard_controller.release(Key.ctrl_r)
	time.sleep(wait-qt)

def spam_quack(quacks=100):
	for i in range(quacks):
		quack(.02, .04)



def tetris_song(bpm=140, repeats=2):
	# 140 bpm
	qt = .03 # Quack - time
	beat = (60/bpm)
	
	for i in range(repeats):
		## Bars 26-29; 10-13
		TetrisBeats.beat1a(qt, beat)
		TetrisBeats.beat2a(qt, beat)
		TetrisBeats.beat3(qt, beat)
		TetrisBeats.beat4(qt, beat)

		## Bar 30-33; 14-17
		TetrisBeats.beat1b(qt, beat)
		TetrisBeats.beat2b(qt, beat)
		TetrisBeats.beat3(qt, beat)
		TetrisBeats.beat4(qt, beat)


if __name__ == "__main__":
	keyboard_controller = Controller()
	time.sleep(.75)
	# tetris_song(200)
	spam_quack(30)
