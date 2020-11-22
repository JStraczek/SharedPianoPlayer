from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class PianoPlayer():
    def __init__(self):
        self.driver = webdriver.Chrome('C:\Windows\chromedriver.exe')

    def start(self):
        self.driver.get("https://musiclab.chromeexperiments.com/Shared-Piano/#BbwPYxoqc")

        time.sleep(5)
        piano = self.driver.find_element_by_xpath('//*[@id="piano"]/piano-keyboard')

        self.actions = ActionChains(self.driver)

        self.playNote('h', 0.25)

        self.actions.pause(0.25)

        self.playNote('h', 0.2)

        # self.actions.pause(0.2)

        self.playNote(';', 0.2)

        #self.actions.pause(0.1)

        self.playNote('l', 0.2)
        self.actions.pause(0.2)
        self.playNote('k', 0.2)
        self.actions.pause(0.2)
        self.playNote('j', 0.3)
        self.actions.pause(0.1)

        self.playNote('j', 0.1)
        self.actions.pause(0.1)
        self.playNote('j', 0.1)
        self.actions.pause(0.1)

        self.playNote('l', 0.2)
        self.actions.pause(0.2)
        self.playNote('k', 0.1)
        self.actions.pause(0.1)
        self.playNote('j', 0.1)
        self.actions.pause(0.1)
        self.playNote('h', 0.3)
        self.actions.pause(0.3)

        self.actions.send_keys('x')  # change key

        self.playNote('h', 0.05)
        self.actions.pause(0.15)
        self.playNote('y', 0.05)
        self.actions.pause(0.15)
        self.playNote('h', 0.05)
        self.actions.pause(0.15)
        self.playNote('y', 0.05)
        self.actions.pause(0.15)
        self.playNote('h', 0.05)
        self.actions.pause(0.15)

        self.actions.send_keys('z')  # change key

        self.playNote('h', 0.3)
        self.actions.pause(0.3)

        self.actions.send_keys('x')  # change key

        self.playNote('h', 0.05)
        self.actions.pause(0.15)
        self.playNote('y', 0.05)
        self.actions.pause(0.15)
        self.playNote('h', 0.05)
        self.actions.pause(0.15)
        self.playNote('y', 0.05)
        self.actions.pause(0.15)
        self.playNote('h', 0.05)
        self.actions.pause(0.15)

        self.actions.send_keys('z')  # change key

        self.playNote('h', 0.3)
        self.actions.pause(0.3)

        self.actions.perform()

        self.driver.quit()

    def playNote(self, key, dur):
        self.actions.key_down(key)
        self.actions.pause(dur)
        self.actions.key_up(key)


if __name__ == "__main__":
    bot = PianoPlayer()

    bot.start()
