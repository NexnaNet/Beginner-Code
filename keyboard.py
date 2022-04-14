#Coding project #1 Goal: make a decent keyboard buying simulator project with 300 lines of code.

#imports from python libraries or other files inside this project
import random
import time

switches = {
  'Linear': ['Cherry Reds', 'Banana Splits', 'Tangerines', 'Alpacas', 'NovelKey Creams', 'Tealios', 'Durock Linears'], 
  'Tactile': ['Cherry Browns', 'Kiwis', 'Holy Pandas', 'Boba 4UT', 'Zealios', 'Durock Tactiles'],
'Silents': ['Roseilos', 'Cherry MX Silent', 'Zilents', 'Silent Alpacaas']
}

keyboard_name_list = []
class Keyboard(object):
    def __init__(self, layout, pcb, plate, switches):
        self.layout = layout
        self.pcb = pcb
        self.plate = plate
        self.switches = switches
    
    def __repr__(self):
        return ('Important tools in a keyboard: %ss, the %s, the %s, and most importantly the %s and how they sound!') % (self.layout, self.pcb, self.plate, self.switches)

#Area of random generators

def layout():
    layout_list = [60, 65, 75, "TKL", "Full-sized", "board", 
    " Alice"]

    return (random.choice(layout_list))


#random word generator
def random_words():
    word_list = ["Love", "Queen", "King", "Ace", "Joker", "Mental", "Atlas", "Mr. Suit", "Cyber", "Oni", "Hanja", "Wind", "Honey", "Bakeneko", "Wolf", "Galaxy", "Bubble", "Glorious", "Cafe", "Star", "Adept", "Nightmare", "Shadow", "Angel", "Unikorn", "Jane", "Dragon", "Play", "Focus", "Viking", "Archon", "Satisfaction", "Blade", "Python", "Comet", "Mind", "Destruction", "Glacier", "Inferno", "Nature", "Blank"]
    generate_words = word_list.copy()
    random.shuffle(generate_words)
    return generate_words[0]

build_keyboard = Keyboard("layout", "PCB", "plate", "switches")
start = input("Welcome to the world of keyboards. Would you like an introduction?(Y/N)")
while start.upper() != 'Y' and start.upper() != 'N':
    start = input("Error: unacceptable input, try again. (Y/N)")

if start.upper() == 'Y':
    print("Great! Let me get your started with the important areas of a keyboard")
    time.sleep(1)
    print (build_keyboard)

if start.upper() == 'N':
    print("Well you must be a recurring user here!. welcome back! Lets get you to the main lobby!")
    time.sleep(1)    
   
#Decide what areas to go into

keyboard_Rooms = ['Shop', 'Live Events', 'Inventory', 'News', 'Exit']
keyboard_inventory = ['Basic keyboard (Prebuilt, Membrane)']
unbuilt_keyboard_inventory = []
switch_inventory = []
print("\nSo... we are in the main lobby. Right now this code is in development. so we have \"Shop\" \"Live Events\" \"Inventory\" \"News\", \"Build Keyboard\" and if you decide you are done. Type in \"Exit\"")
choose_room = input("\nHere we are! Now press enter to continue!")
while choose_room.title() != 'Exit':
    choose_room = input("\nChoose a room!")
    if choose_room.title() != 'Shop' and choose_room.title() != 'News' and choose_room.title() != 'Inventory' and choose_room.title() != 'Live Events' and choose_room.title() != 'Exit' and choose_room.title() != 'Build Keyboard':
      continue
    if choose_room.title() == 'Exit':
      print("Well then... Goodbye! See you around~")
      break

    if choose_room.title() == 'News':
      pass
      continue

    if choose_room.title() == 'Build Keyboard':
      if unbuilt_keyboard_inventory == [] or switch_inventory == []:
        print("You don't have the parts to build a keyboard")
      continue

    if choose_room.title() == 'Live Events':
      print('There are no live events at the moment. Sorry!')
      continue

    if choose_room.title() == 'Inventory':
      count = 0
      print("Keyboard Inventory\n" + str(keyboard_inventory))

      print("\nUnbuilt Keyboards\n" + str(unbuilt_keyboard_inventory))

      print("\n Switch Inventory\n" + str(switch_inventory))
      count += 1
      if count == 1:
        continue

    if choose_room.title() == 'Shop':
      time.sleep(1)
      print("\nWelcome to the shop\n")
      choose_shop_room = input("Choose an area to shop! (Keyboard Kit, Switches, Stabilizers, Keycaps, or Return)")

    while choose_shop_room.title() != 'Keyboard Kit' and choose_shop_room.title() != 'Switches' and choose_shop_room.title() != 'Stabilizers' and choose_shop_room.title() != 'Keycaps' and choose_shop_room.title() != 'Return':
        choose_shop_room = input("Choose an area to shop! (Keyboard Kit, Switches, Stabilizers, Keycaps or Return.)")

    if choose_shop_room.title() == 'Keyboard Kit':
        keyboards_available = random.randint(0, 5)

        for i in range(0, keyboards_available):
          keyboard_name = random_words()
          keyboard_layout = layout()
          keyboard_name_list.append(keyboard_name + str(keyboard_layout))
        
        if keyboards_available == 0:
          print("\nWe have no keyboards available. Please come back later.")
          continue
          
        elif keyboards_available == 1:
            print('\n We have only ' + str(keyboards_available) + ' keyboard available today. \n')
            for keyboard in keyboard_name_list:
                print(keyboard)
                buy_keyboard = input("\nWould you like to buy the %s? (Y/N)" % (keyboard))
                if keyboard in unbuilt_keyboard_inventory:
                    keyboard_name_list.remove(keyboard)
                
                if keyboard not in unbuilt_keyboard_inventory:
                    keyboard_name_list.remove(keyboard)
                    
                if buy_keyboard.upper() == 'Y':
                    count = keyboards_available
                    for bought_keyboard in buy_keyboard:
                        unbuilt_keyboard_inventory.append(keyboard)

                if buy_keyboard.upper() == 'N':
                    count = keyboards_available
                    print("\n")
                    count -= 1
                
                if count == 0:
                    for keyboard in keyboard_name_list:
                        if keyboard_name_list not in unbuilt_keyboard_inventory:
                            keyboard_name_list.remove(keyboard)
                continue
                
              
        if keyboards_available > 1:
            count = keyboards_available
            print("\nWe have " + str(keyboards_available) + " keyboards available today. \n")
            time.sleep(1)
            for keyboard in keyboard_name_list:
                print(keyboard)
                buy_keyboard = input("\nWould you like to buy the %s? (Y/N)\n" % (keyboard))
                
                while buy_keyboard.upper() != 'Y' and buy_keyboard.upper() != 'N':
                    buy_keyboard = input("\nWould you like to buy the %s? (Y/N)\n" % (keyboard))
           
                if buy_keyboard.upper() == 'Y':
                    for bought_keyboard in buy_keyboard:
                        unbuilt_keyboard_inventory.append(keyboard)
                        print("\n")
                    count -= 1
            
                if buy_keyboard.upper() == 'N':
                    print("\n")
                    count -= 1

                if count is 0:
                    rejected_keyboards = []
                    accepted_keyboards = []
                    
                    for keyboards in keyboard_name_list:
                        if keyboards in unbuilt_keyboard_inventory:
                            accepted_keyboards.append(keyboards)
                                
                    for keyboards in accepted_keyboards:
                        if keyboards in keyboard_name_list:
                            keyboard_name_list.remove(keyboards)
                                
                    for keyboards in keyboard_name_list:
                        if keyboards not in unbuilt_keyboard_inventory:
                            rejected_keyboards.append(keyboards)
                            
                    for keyboards in rejected_keyboards:
                        if keyboards in keyboard_name_list:
                            keyboard_name_list.remove(keyboards)

    if choose_shop_room.title() == 'Switches':
        time.sleep(1)
        print('\nWelcome to the switch shop! we have several types of switches')
        choose_switch_type = input('Choose What switch type you want to buy. [Linears, Tactiles, Silents]')

        while choose_switch_type.title() != 'Linears' and choose_switch_type.title() != 'Tactiles' and choose_switch_type.title() != 'Silents':
            choose_switch_type = input("Choose a switch type from the list...['Linears', 'Tactiles', 'Silents']")
        if choose_switch_type == 'Clicky':
            print("Do not ever speak of those ungodly switches again!")
            continue
        
        if choose_switch_type.title() == 'Linears':
            print("\nLinear switches that we have available are: \n")
        for linearSwitches in switches['Linear']: 
            print(linearSwitches)
            
        add_switches = input("Pick a switch from the list.")
        if add_switches.title() not in switches['Linear']:
            add_switches = input("Pick a switch from the list.")

        if add_switches.title() == 'Cherry Reds' or add_switches.title() == 'Banana Splits' or add_switches.title() == 'Tangerines' or add_switches.title() == 'Alpacas':
            switches_amount = int(input("How many " + str(add_switches) + " would you like? (50, 70, 90, 110)"))
            while switches_amount != 50 and switches_amount != 70 and switches_amount != 90 and switches_amount != 110:
                switches_amount = int(input("How many switches would you like?"))

            if switches_amount == 50 or switches_amount == 70 or switches_amount == 90 or switches_amount == 110:
                switch_inventory.append(add_switches.title() + ', x' + str(switches_amount))
        if  add_switches.title() == 'Cancel' or add_switches.title() == 'Return':
            pass
        continue

      
    if choose_shop_room.title() == 'Return':
      pass
    continue
    