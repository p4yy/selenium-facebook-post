from PIL.ImageOps import grayscale
import pyautogui
from time import sleep
from json import load
def scanImage(self):
	if pyautogui.locateOnScreen(image=self,confidence=0.9,grayscale=True) is not None:
		return True
	else:
		return False 

def clickImage(self):
	click = pyautogui.locateCenterOnScreen(image=self,confidence=0.9,grayscale=True)
	return pyautogui.click(click) 

def main():
	data = load(open('configMobile.json','r'))
	whatsOnYourMind_Path = "image\\whatsOnYourMind.PNG"
	typeUrTeks_Path = "image\\whatsOnYourMind.PNG"
	tagFriends_Path = "image\\tagFriends.PNG"
	startTypingName_Path = "image\\startTypingName.PNG"
	doneTypingName_Path = "image\\doneTypingName.PNG"
	post_Path = "image\\post.PNG"
	start = data["start"]
	end = data["end"]
	tagPeople_Path = data["tagPeople_Path"]
	teks = data["teks"]
	tagPeople = data["tagPeople"]
	delayPost = data["delayPost"]
	breakEveryPostOn = data["breakEveryPostOn"]
	sleepAt = 1 
	while start <= end:
		if sleepAt - breakEveryPostOn[0] == 0:
			sleep(breakEveryPostOn[1])
			sleepAt = 1
		while True:
			if scanImage(whatsOnYourMind_Path) == True:
				break
			else:
				sleep(2)
		sleep(0.2)
		clickImage(whatsOnYourMind_Path)
		sleep(1.5)
		while True:
			if scanImage(typeUrTeks_Path) == True:
				break 
			else:
				sleep(2)
		sleep(0.2)
		clickImage(typeUrTeks_Path)
		sleep(3)
		for x in teks:
			pyautogui.write(x,interval=0.05)
			pyautogui.press('enter')
			sleep(0.2)
		pyautogui.write(str(f'#{start:,}'))
		sleep(1)
		clickImage(tagFriends_Path)
		sleep(1)
		numberPath=0
		for x in tagPeople:
			while True:
				if scanImage(startTypingName_Path) == True:
					break 
				else:
					sleep(2)
			sleep(0.2)
			clickImage(startTypingName_Path)
			sleep(0.3)
			pyautogui.write(x)
			sleep(1.5)
			while True:
				if scanImage(tagPeople_Path[numberPath]) == True:
					break
				else:
					sleep(2)
			sleep(0.2)
			clickImage(tagPeople_Path[numberPath])
			sleep(1.5)
			numberPath+=1
		sleep(0.5)
		while True:
			if scanImage(doneTypingName_Path) == True:
				break 
			else:
				sleep(2)
		sleep(0.2)
		clickImage(doneTypingName_Path)
		sleep(1)
		while True:
			if scanImage(post_Path) == True:
				break 
			else:
				sleep(2)
		sleep(0.5)
		clickImage(post_Path)
		sleep(delayPost)
		start+=1
		sleepAt+=1

if __name__ == "__main__":
	main()