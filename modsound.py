#2021-11-07  lafy  <lafy@mailo.com>

import time
import fluidsynth

class PlaySound():
	def __init__(self):
		
		self.fs = fluidsynth.Synth()
		self.fs.start(driver="alsa")     # alsa, file, jack, oss, pulseaudio, sdl2
		# alsa ->linux / dsound-> windows  

		self.sfid = self.fs.sfload("/usr/share/sounds/sf2/FluidR3_GM.sf2")
		ret = self.fs.program_select(0,self.sfid,0, 0)   #channel, soundfont, bank_num, preset_num
		#bank 0 preset 0 ="Acoustic Grand Piano"
		#1 Bright Piano
		

	def play_chord(self,k1,k2,k3):
		self.fs.noteon(0, k1, 90)    #channel, key(0-127), velocity
		self.fs.noteon(0, k2, 90)
		self.fs.noteon(0, k3, 90)

		time.sleep(0.8)

		self.fs.noteoff(0, k1)
		self.fs.noteoff(0, k2)
		self.fs.noteoff(0, k3)

		#time.sleep(0.1)

	def play_chord_M(self, index):
		#chords_M=["C ","C #/Db ","D ","D# /Eb ","E ","F ","F# /Gb ","G ","G# /Ab ","A ","A# /Bb ","B "]
		k1=(60+index)
		k2=k1+4
		k3=k1+7
		self.play_chord(k1,k2,k3)
		
	def play_chord_m(self, index):
		#chords_m=["Cm","Cm#/Dmb","Dm","Dm#/Emb","Em","Fm","Fm#/Gmb","Gm","Gm#/Amb","Am","Am#/Bmb","Bm"]
		k1=(60+index)
		k2=k1+3
		k3=k1+7
		self.play_chord(k1,k2,k3)
				
	def play_note(self,k):
		try:
			if (k>=0 and k<=127): 
				self.fs.noteon(0, k, 90)
				time.sleep(0.8)
				self.fs.noteoff(0, k)
				#time.sleep(0.1)
		except TypeError:
			pass
			
	def melody(self):
		sheet=[60,62,64,65,64,65,69,67,64,62,60]  
		for k in sheet:
			self.play_note(k)
			
	def list_sounds(self):
		if self.sfid !=0:
			channel = 0 # to 0 based
			
			#print(instrument)
		#	return (self.sf, instrument)
		#ret = self.fs.program_change(0,0, 1)   #fsinstance, channel, numprog
		
	def quit(self):
		self.fs.delete
		
		
		
#test
if __name__ == '__main__':
	
	sound=PlaySound()
	#test a triad
	sound.play_chord(60,67,70)
	#try list_sounds
	sound.list_sounds()
	
	sound.quit()
