from kivy.app import App
from kivy.lang import Builder

from uifile import UIFile
from uibutton import UIButton
from icon import Icon

Builder.load_file("kvwids.kv")

class Main(App):
	def build(self):
		return UIFile()
	

if __name__ == "__main__":
	Main().run()
	
