from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen

from kivy.properties import (StringProperty, 
ListProperty,
NumericProperty)
from kivy.clock import Clock
from kivy.logger import Logger

from uibutton import UIButton


import os
from os import path

class UIFile(Screen):
	
	rootpath = StringProperty("/storage/emulated/0")
	selection = StringProperty("")
	content = ListProperty([])
	nume = NumericProperty(0)
	
	icons = {
		"py":"language-python",
		"java":"language-java",
		"html":"language-html5",
		"css":"language-css3",
		"png":"image",
		"xml":"xml",
		"jpg":"image",
		"jpeg":"image",
		"mp4":"video",
		"mp3":"music",
		"db":"database",
		"zip":"folder-zip",
		"apk":"android",
		"pdf":"file-pdf-box",
		"PDF":"file-pdf-box",
		"ttf":"format-font",
		"TTF":"format-font",
		"ini":"file",
		"js":"language-javascript",
		"php":"language-php",
		"txt":"text",
		"gif":"file-gif-box",
		"kv":"assets/uik_logo.png",
	}
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		
		Clock.schedule_once(self.start_file)
		self.register_event_type("on_select")
		
		
		
			
			
	
	def start_file(self, *args):
		
		self.ids.grid.clear_widgets()		
		esc = UIButton(icon="arrow-left",text="/..")
		esc.bind(on_release=self._go_back)
		self.ids.grid.add_widget(esc)
			
		try:
			self.nume = 0
			self.content = sorted(os.listdir(self.rootpath))
			Clock.schedule_interval(self.typing_items, 0.1)
			
			
			
		except Exception as e:
				Logger.error(e)
		
		
	def typing_items(self, *args):
		try:
			if self.nume < len(self.content):
				item = self.content[self.nume]
			else:
				Clock.unschedule(self.typing_items)
				return
				
			realpath = os.path.join(self.rootpath,item)
					
			if path.isdir(str(realpath)):
				btn = UIButton(icon="folder",text=item)
						
			elif path.isfile(str(realpath)):
				filetype = str(item).split(".")[-1]
				if filetype in self.icons.keys():
					btn = UIButton(icon=self.icons.get(filetype),text=item)
				else:
					btn = UIButton(icon="file",text=item)
							
			btn.bind(on_release=self._is_clicked)
			self.ids.grid.add_widget(btn)
			self.nume +=1
		except Exception as e:
			pass
		
	def _is_clicked(self,*args):
		pathe = self.rootpath + os.sep + args[0].text
		if path.isdir(pathe):
			self.rootpath = pathe
			self.start_file()
		self.dispatch("on_select")
		self.selection = pathe
	
	def _go_back(self,*args):
		_li = str(self.rootpath).split(os.sep)[:-1]
		self.rootpath = f"{os.sep}".join(str(i) for i in _li)
		self.start_file()
		
				
	def on_select(self):
		"__init__"
		
		
		

		
				
						
								
										
												
														
																		
		
	