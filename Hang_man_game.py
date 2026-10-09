#Cool hangman game that uses python interfaces (a lot of code is from the Hang_Man script i made a while ago)
#The text display of the stage hangman is at needs a monospace font to work properly (best fix is to make sure you have liberation mono downloaded)

import random
from tkinter import *

def doNothing():
    thisWill = "doNothing"
def hangmanDraw():
    global hangman1
    hangman1 = '''
                





       _____________'''
    global hangman2
    hangman2 = '''
                
           |
           |
           |
           |
           |
        ________|_____'''
    global hangman3
    hangman3 = '''
     ______
           |
           |
           |
           |
           |
        ________|_____'''
    global hangman4
    hangman4 = '''
     ______
     |     |
           |
           |
           |
           |
        ________|_____'''
    global hangman5
    hangman5 = '''
     ______
     |     |
     O     |
           |
           |
           |
        ________|_____'''
    global hangman6
    hangman6 = '''
     ______
     |     |
     O     |
     |     |
           |
           |
        ________|_____'''
    global hangman7
    hangman7 = '''
     ______
     |     |
     O     |
    /|     |
           |
           |
        ________|_____'''
    global hangman8
    hangman8 = '''
     ______
     |     |
     O     |
    /|\\    |
           |
           |
        ________|_____'''
    global hangman9
    hangman9 = '''
     ______
     |     |
     O     |
    /|\\    |
    /      |
           |
        ________|_____'''
    global hangman10
    hangman10 = '''
     ______
     |     |
     O     |
    /|\\    |
    / \\    |
           |
        _______|_____'''
def gatherAndDisplay(event):
    global wrongGuesses
    global timesDone
    global hangmanDisplay
    global accusation
    accusation = ""
    global reiteration
    reiteration = ""
    
    guess = letter.get()
    if guess in word:
            for index in range(len(word)):
                if word[index] == guess:  
                    guessedLetters[index] = guess

    else:
            wrongGuesses = wrongGuesses + guess
            timesDone = timesDone + 1
    if timesDone == 0:
        hangmanDisplay = ""
    elif timesDone == 1:
        hangmanDisplay = hangman1+"\n"
    elif timesDone == 2:
        hangmanDisplay = hangman2+"\n"
    elif timesDone == 3:
        hangmanDisplay = hangman3+"\n"
    elif timesDone == 4:
        hangmanDisplay = hangman4+"\n"
    elif timesDone == 5:
        hangmanDisplay = hangman5+"\n"
    elif timesDone == 6:
        hangmanDisplay = hangman6+"\n"
    elif timesDone == 7:
        hangmanDisplay = hangman7+"\n"
    elif timesDone == 8:
        hangmanDisplay = hangman8+"\n"
    elif timesDone == 9:
        hangmanDisplay = hangman9+"\n"
    elif timesDone == 10:
        hangmanDisplay = hangman10+"\n"
        accusation = "\n"+"HE'S DEAD! YOU KILLED HIM"
    else:
        reiteration = "\n"+"The game's over, he's already dead."

    letter.delete(0, 'end')

    if "_" in guessedLetters:
        word_display.config(width = 50, bg = display_colour, text = f"{str(guessedLetters)}\n")
        main_text.config(width = 50, text = hangmanDisplay+wrongGuesses+accusation+reiteration)
        if timesDone > 9:
            letter.destroy()
            confirm_text.destroy()
            retry_game_lose = Button(width = 10, font = (None,medium_size), bg = retry_colour, text = "New Game", command = retryGameLose)
            retry_game_lose.pack(padx = 40, pady = 30)
        elif timesDone == 0:
            global flawless_colour1, flawless_colour2, flawless_colour3, flawless_colour4, flawless_colour5, flawless_colour6, bonus

            flawless_colour1 = "#ffd95c"
            flawless_colour2 = "#e7b308"
            flawless_colour3 = "#ffcd2b"
            flawless_colour4 = "#f0b901"
            flawless_colour5 = "#ffd139"
            flawless_colour6 = "#FFC400"

            bonus = 1
        else:
            flawless_colour1 = background_colour
            flawless_colour2 = display_colour
            flawless_colour3 = exit_game_colour
            flawless_colour4 = confirm_text_colour
            flawless_colour5 = retry_colour
            flawless_colour6 = enter_letter_colour

            bonus = 0
    else:
        word_display.destroy()

        main_text.config(bg = flawless_colour2)
        game.config(bg = flawless_colour1)
        letter.config(bg = flawless_colour6)
        confirm_text.config(bg = flawless_colour4)
        exit_game.config(bg = flawless_colour3)
        streak.config(bg = flawless_colour2)

        frame.config(bg = flawless_colour1)

        main_text.config(width = 50, font = (None,large_size), text = str(guessedLetters)+"\n"+"WELL DONE! You guessed the word! It was:\n"+(word.capitalize()))
        letter.destroy()
        confirm_text.destroy()
        retry_game_win = Button(width = 10, font = (None,medium_size), bg = retry_colour, text = "New Game", command = retryGameWin)
        retry_game_win.pack(padx = 40, pady = 30)
        retry_game_win.config(bg = flawless_colour5)
def retryGameLose():
    global score
    score = 0
    game.destroy()
    playGame(font_size, bg_colour, text_colour, exit_colour, letter_colour, new_colour, entry_colour, category_list)
def retryGameWin():
    global score, score_display, bonus_score

    score += 1
    bonus_score += 1 + bonus
    score_display = str(f"Score = {bonus_score}, Streak = {score}")
    game.destroy()
    playGame(font_size, bg_colour, text_colour, exit_colour, letter_colour, new_colour, entry_colour, category_list)
def playGame(size, colour1, colour2, colour3, colour4, colour5, colour6, word_list):
    global game, main_text, letter, confirm_text, exit_game, word, guessedLetters, wrongGuesses, timesDone, small_size, medium_size, large_size, retry_colour, word_display, display_colour, background_colour, streak, enter_letter_colour, exit_game_colour, confirm_text_colour, frame

    background_colour = colour1
    display_colour = colour2
    exit_game_colour = colour3
    confirm_text_colour = colour4
    retry_colour = colour5
    enter_letter_colour = colour6
    
    word = (random.choice(word_list))
    wrongGuesses = ""
    guessedLetters = []
    timesDone = 0
    for i in range(len(word)):
        if word[i] == " ":
            list.append(guessedLetters," ")
        else:    
            list.append(guessedLetters,"_")

    num_to_divide_by = len(word) // 10

    if len(word) > 10:
        large_size = int(size // num_to_divide_by)
    else:
        large_size = size

    small_size = int(size // 1.35)
    medium_size = int(size // 1.2)

    hangmanDraw()

    game = Tk()
    game.title("Hangman")
    game.attributes('-fullscreen', True)

    game.configure(bg = colour1)

    word_display = Label(game, font = (None,large_size), bg = colour1, text = "")
    word_display.pack(padx = 40, pady = 10)

    main_text = Label(game,width = 45, font = ("Consolas",size), bg = colour2, text = "Welcome to hangman! Enter a letter below.")
    main_text.pack(padx = 40, pady = 10)

    letter = Entry(width = 10, font = (None,medium_size), bg = colour6)
    letter.pack(padx = 40, pady = 10)

    confirm_text = Label(game,width = 28, font = (None,small_size), bg = colour4, text = "Press enter to confirm your letter")
    confirm_text.pack(padx = 40, pady = 10)

    frame = Frame(game, width = 50, bg = colour1)
    frame.pack(padx = 40, pady = 10)

    exit_game = Button(frame, width = 20,font = (None,small_size), text = "Exit game", bg = colour3, command = game.destroy)
    exit_game.pack(side = LEFT, padx = 20)

    streak = Label(frame, bg = display_colour, font = (None,small_size), text = score_display)
    streak.pack(side = RIGHT, padx = 20)

    game.bind('<Return>',gatherAndDisplay)

    game.mainloop()
def playGameFirst():
    global difficulty_choose

    getRatio()
    getColour()
    getCategory()
    
    config_window.destroy()

    if chosen_category == "General":
        global difficulty_select

        difficulty_select = Tk()
        difficulty_select.configure(bg = "#9660d3")
        difficulty_select.title("Difficulty Select")

        difficulty_text = Label(difficulty_select, font = (None,15), width = 16, bg = "#7b3ec0", text = "Select a difficulty:")
        difficulty_text.pack(padx = 40, pady = 10)

        difficulty_choose = Listbox(difficulty_select)
        difficulty_choose.insert(1,"Easy")
        difficulty_choose.insert(2,"Medium")
        difficulty_choose.insert(3,"Hard")
        difficulty_choose.pack(padx = 40, pady = 5)

        confirm_difficulty = Button(width = 10,font = (None,15), text = "Start Game", bg = "#8c31e1", command = getDifficulty)
        confirm_difficulty.pack(padx = 40, pady = 5)

        difficulty_select.mainloop()
    else:
        pass

    playGame(font_size, bg_colour, text_colour, exit_colour, letter_colour, new_colour, entry_colour, category_list)
def getRatio():
    global font_size

    ratio = aspect_ratio.get(aspect_ratio.curselection())

    if ratio == "640x360":
        font_size = 15
    elif ratio == "1280x720":
            font_size = 30
    elif ratio == "1600x900":
            font_size = 40
    elif ratio == "1920x1080":
            font_size = 45
    elif ratio == "2560x1440":
            font_size = 60
def getColour():
    global bg_colour
    global text_colour
    global exit_colour
    global letter_colour
    global new_colour
    global entry_colour

    chosen_colour = colour.get(colour.curselection())

    if chosen_colour == "Red":
        bg_colour = "#eb9e9e"
        text_colour = "#e06666"
        exit_colour = "#cf3737"
        letter_colour = "#f55757"
        new_colour = "#e94646"
        entry_colour = "#f5cbcb"
    elif chosen_colour == "Orange":
        bg_colour = "#ebc19e"
        text_colour = "#e0ab66"
        exit_colour = "#f19b29"
        letter_colour = "#f5ab57"
        new_colour = "#e98746"
        entry_colour = "#f5decb"
    elif chosen_colour == "Yellow":
        bg_colour = "#ebd99e"
        text_colour = "#e0c366"
        exit_colour = "#ebcc1c"
        letter_colour = "#f5dd57"
        new_colour = "#e9cb46"
        entry_colour = "#f5f1cb"
    elif chosen_colour == "Green":
        bg_colour = "#bdeb9e"
        text_colour = "#8de066"
        exit_colour = "#55cf37"
        letter_colour = "#7cf557"
        new_colour = "#59e946"
        entry_colour = "#d5f5cb"
    elif chosen_colour == "Blue":
        bg_colour = "#9ec6eb"
        text_colour = "#6691e0"
        exit_colour = "#3760cf"
        letter_colour = "#57aef5"
        new_colour = "#4692e9"
        entry_colour = "#cbd8f5"
    elif chosen_colour == "Purple":
        bg_colour = "#ae7de6"
        text_colour = "#b15de2"
        exit_colour = "#9423c0"
        letter_colour = "#803cb8"
        new_colour = "#ce34d3"
        entry_colour = "#ba98e7"  
    elif chosen_colour == "Multicolour":
        bg_colour = "#da5555"
        text_colour = "#e1833b"
        exit_colour = "#5fc023"
        letter_colour = "#2d76e5"
        new_colour = "#8e34d3"
        entry_colour = "#ddd647" 
def getCategory():
    global category_list
    global chosen_category

    chosen_category = category.get(category.curselection())

    if chosen_category == "General":
        category_list = []
    elif chosen_category == "Animals":
        category_list = ['aardvark','aardwolf','african elephant','alligator','albatross','anaconda','antelope','armadillo','axolotl','baboon','badger','bactrian camel','bald eagle','barn owl','barracuda','bison','blue whale','boa constrictor','bonobo','caiman','camel','capybara','caracal','cassowary','cheetah','chimpanzee','cobra','cougar','crocodile','damselfish','deer','dingo','dolphin','dragonfly','dugong','duck','eagle','earthworm','echidna','eel','egret','elephant seal','elk','emu','ermine','falcon','fennec fox','ferret','flamingo','flatfish','flounder','flying squirrel','fox','frigatebird','gazelle','gecko','gerbil','gibbon','giraffe','goose','gorilla','grasshopper','great white shark','haddock','hammerhead shark','hamster','hare','harpy eagle','hedgehog','hippopotamus','hornbill','horse','hummingbird','ibex','ibis','iguana','impala','indian star tortoise','jackal','jaguar','jellyfish','jerboa','junco','kangaroo','kestrel','king cobra','kingfisher','koala','komodo dragon','kookaburra','krill ','ladybug','lamprey','lemur','leopard','lion','lizard','lobster','lynx','macaw','magpie','manatee','manta ray','meerkat','millipede','mink','mole','moose','moray eel','nighthawk','numbat','nurse shark','nutria','octopus','okapi','opossum','orangutan','ostrich','otter','owl','ox','panda','panther','parrot','peacock','pelican','penguin','piranha','platypus','porcupine','puma','quail','quetzal','quokka','quoll','rabbit','raccoon','ram','rat','raven','red panda','reindeer','rhinoceros','roadrunner','salamander','scorpion','seahorse','seal','serval','sheep','sloth','snow leopard','sparrow','squid','tapir','tarantula','tasmanian devil','termite','tiger','toad','toucan','tuna','turtle','uromastyx','vampire bat','vervet monkey','viper','vole','vulture','walrus','warthog','weasel','whale','wombat','woodpecker','wren','yak','yellowfin tuna','yeti crab','zebra']
    elif chosen_category == "Space":
        category_list = ['planet','star','mercury','venus','earth','mars','jupiter','saturn','uranus','neptune','pluto','dwarf planet','black hole','sol','moon','luna','solar system','asteroid','meteor','comet','galaxy','milky way','andromeda','nebula','supernova','space station','astronaut','rocket','telescope','cosmos']
    elif chosen_category == "Brands":
        category_list = ['costco','chick fil a','netflix','apple','nike','target','google','amazon','spotify','zoom','disney','roblox','nintendo','lego','microsoft','instagram','rockstar','chanel','linkedin','sony','tesla','starbucks','nvidia','honda','audi','red bull','hershey','chipotle','porsche','pinterest','logitech','crocs','gucci','amd','coca cola','national geographic','adidas','sephora','hbo','american express','puma','visa','adobe','youtube','ubisoft','riot games','airbnb','toyota','mcdonalds','fedex','twitter','uber','meta','best buy','samsung','walmart','pepsico','verison','paypal','intel','dominos','mattel','ford','dell','snapchat','hulu','kfc','warner brothers','gap','nestle','taco bell','ups','pizza hut','doordash','activision','universal','canon','bp','hp','under armour','ikea','tiktok','discord michelin','github','vmware','hasbro','olive garden','nokia','blizzard','reddit','tripadvisor','fitbit','valve','razer','lg','nickelodeon','dairy queen','shell','malwarebytes','reebok']
    elif chosen_category == "Python Keywords":
        category_list = ['print']
def getDifficulty():
    global category_list

    chosen_difficulty = difficulty_choose.get(difficulty_choose.curselection())

    if chosen_difficulty == "Easy":
        category_list = ['about','acute','adopt','agent','agree','alarm','alert','alley','allow','alone','angle','apple','argue','arise','array','aside','asset','avoid','award','aware','badge','basic','basis','beach','began','begin','belly','below','bench','birth','blame','blank','blast','blind','block','blood','board','boast','bonus','boost','brain','brand','bread','break','brick','brief','bring','broad','broke','brown','brush','buddy','build','burnt','burst','buyer','cabin','cable','camel','canal','candy','canoe','cargo','carry','carve','catch','cause','cease','chain','chair','chalk','chaos','charm','chase','cheap','cheat','check','chest','chief','child','civil','claim','class','clean','clear','clerk','click','cliff','climb','clock','close','cloth','cloud','coach','coast','color','couch','cough','could','count','court','cover','crack','craft','crane','crash','crazy','cream','crime','cross','crowd','crown','cruel','crush','crust','curve','cycle','daily','dance','dated','death','debit','debut','decay','decor','delay','delta','dense','depth','derby','deter','detox','diary','dicta','digit','diner','dirty','disco','ditch','diver','dizzy','dodge','donor','doubt','dough','dozen','draft','drain','drama','drank','drape','drawi','dream','dress','dried','drift','drill','drink','drive','drone','droop','drove','drown','drumy','dusty','dying','eager','early','earth','eaten','edgy','eerie','eight','eject','elite','email','empty','enact','ended','endow','enemy','enjoy','enter','entry','envoy','equal','equip','erase','erect','error','erupt','essay','ester','ether','ethic','evade','event','every','evict','evoke','exact','exalt','excel','exert','exile','exist','exit','expel','expel','extra','fable','facet','facts','fader','faint','fairy','faith','false','fancy','farce','fault','favor','feast','feats','fedup','feeds','feign','felix','feral','ferry','fetch','fever','fiber','field','fifth','fifty','fight','filee','filmy','final','finch','fined','finer','fired','first','fishy','fixer','fjord','flack','flame','flank','flare','flash','flask','flawy','fleck','fleet','flesh','flick','flier','fling','flint','flirt','float','flock','flood','floor','flora','floss','flour','flowy','fluid','flunk','flush','flute','flyer','foamy','focal','focus','foggy','foist','folia','folly','foody','footy','force','forge','forgo','forte','forum','found','foyer','frail','frame','fraud','freak','freed','freer','fresh','fried','frill','frisk','frock','frond','front','frost','froth','frown','froze','fruit','fudge','fugue','fulma','fully','fundy','funky','funny','furor','furry','fused','fussy','fuzzy','macro','magic','major','maker','malky','mammy','mango','manic','manor','maple','march','marry','marsh','mason','match','matey','mayor','mealy','meant','meaty','medal','media','medic','meets','melon','mercy','merge','merit','merry','metal','meter','metro','micro','midst','might','minor','minus','mirth','misty','mixer','model','modem','moist','molar','moldy','money','month','moody','moose','moral','moron','morph','motel','motor','motto','mould','moult','mount','mourn','mouse','mouth','mover','movie','mucke','muddi','muddy','mulct','multi','mummy','mural','murky','mushy','music','musky','musty','muted','mutto','myrrh','naive','naked','named','nappy','nasty','natal','navel','navy','nears','neat','necky','needy','negro','neigh','nerdy','nerve','pesky','petty','phase','phone','photo','piano','piece','pilot','pitch','place','plain','plane','plant','plate','plaza','point','polar','porch','pound','power','press','price','pride','prime','print','prior','prize','probe','prone','prose','proud','prove','proxy','psalm','pulse','punch','puppy','purge','purse','pushy','quail','quake','qualm','quark','quart','queen','queer','quell','query','quest','queue','quick','quiet','quilt','quirk','quota','quote','rabbi','rabid','radar','radio','radon','rainy','raise','ranch','randi','range','rapid','rarer','raspy','ratio','ratty','razor','reach','react','ready','realm','ream','rear','rebel','refer','regal','reign','reins','relax','relay','relic','remap','remit','renal','renew','repay','repel','reply','rerun','reset','resin','resit','retro','retry','reuse','revel','revue','rhino','rhyme','rider','ridge','rifle','right','rigid','rigor','riled','rimer','rinse','ripen','riser','rival','river','rivet','roach','roast','robin','robot','rocky','rodeo','rogue','Roman','romps','roofi','rooky','roomy','roost','rooty','ropes','rosei','rosin','rossy','rotas','rotor','roués','rouge','rough','round','rouse','route','rover','rowdy','rower','royal','ruble','ruddy','ruger','ruins','ruled','ruler','rumba','rummy','rumor','rumps','runny','rupee','rural','rushy','rusks','rusts','rusty','rutty','sable','sabre','sabot','sache','sacks','sadhu','sadly','safer','saga','sager','saggy','sahib','saids','saint','salad','sales','sally','salon','salsa','salty','salve','salvo','samba','samey','sandy','saner','sarge','sassy','satan','satin','satyr','sauce','saucy','sauna','saunter','saved','saver','savor','savvy','sawed','sawer','sayed','sayer','scabbed','scale','scalp','scamp','scant','scare','scarf','scarp','scary','scene','scent','schwa','scion','scoff','scold','scone','scoop','scoot','scope','score','scorn','scour','scout','scowl','scram','scrap','scrape','screw','scrub','scrum','scuba','scuff','scull','scum','scurf','seamy','sears','seats','sebum','sedan','sedge','sedum','seedy','segue','seize','selam','selfs','sella','seine','seize','sense','sepia','septa','seral','serer','serfs','seria','serif','serio','serra','serum','serve','servo','sesso','setup','seven','sever','sewer','shack','shade','shady','shaft','shake','shaky','shale','shall','shalt','shame','shank','shape','shard','share','shark','sharp','shave','shawl','shear','sheds','sheen','sheep','sheer','sheet','shelf','shell','shift','shill','shily','shint','shire','shirk','shirt','shoal','shock','shoji','shone','shook','shoot','shops','shore','shorn','short','shout','shove','shown','showy','shred','shrew','shrub','shrug','shuck','shunt','shush','shuty','sicko','sided','sider','sides','siege','sieve','sight','sigma','signs','silen','silfa','silky','silly','silts','silty','since','sinew','singe','sings','sinks','sinue','sinus','sired','siren','sirih','sirop','sirup','sisal','sissy','sists','sitar','sited','sites','sithe','situs','sixte','sixth','sixty','sized','sizer','sizes','skate','skeet','skewr','skids','skied','skier','skies','skill','skimp','skims','skink','skins','skips','skirt','skits','skive','skulk','skull','skunk','slack','slain','slang','slant','slash','slate','slats','slave','sleak','sleds','sleek','sleep','sleet','sleet','slept','slews','slice','slick','slide','slime','slimy','sling','slink','slips','slirk','slish','slite','slive','sloop','slope','slops','slosh','sloth','slots','slowy','slued','slues','slugs','sluice','slum','slung','slunk','slur','slush','smack','small','smart','smash','smear','smell','smelt','smile','smirk','smite','smith','smock','smog','smoke','smoky','smolt','smote','smugg','snack','snafu','snag','snail','snake','snaky','snap','snare','snarl','sneak','sneer','snick','snide','sniff','snipe','snips','snobs','snood','snoop','snoot','snore','snort','snout','snows','snowy','snub','snuff','snug','soaks','soaps','soapy','soars','sober','socko','socks','sodas','soddy','sodom','sofas','softs','softy','sogged','soggy','soily','solar','solde','soldi','solen','solid','solum','solve','soman','somer','somme','sonar','songs','sonic','sonny','sooey','sooks','soote','sooth','soots','sooty','sopor','soppy','sorb','sorbs','sored','sorel','sorer','sores','sorgo','sorra','sorry','sort','sorty','sough','souls','sound','soupe','sourd','sourer','sours','souse','south','sowar','sowed','sower','soyas','space','spade','spain','spake','spam','spang','spank','spans','spare','spark','spars','spasm','spate','spats','spawn','speak','spear','speck','sped','speed','spell','spend','spent','sperm','spew','spice','spicy','spied','spiel','spier','spies','spiff','spike','spiky','spill','spilt','spine','spiny','spire','spiry','spite','spits','spivs','splat','splay','split','spoil','spoke','spoof','spool','spoon','spoor','spore','sport','sposh','spots','spout','sprag','sprat','spray','spree','sprig','sprit','sprog','sprot','sprug','spuds','spued','spumes','spumy','spunk','spurn','spurt','sputa','squab','squad','squat','squaw','squib','squid','stade','staff','stage','stagg','staid','stain','stair','stake','stale','stalk','stall','stamp','stand','stank','staph','stare','stark','stars','start','stash','state','stats','stave','stays','stead','steak','steal','steam','steed','steel','steep','steer','stein','stela','stele','stemm','stend','stent','steps','stern','stert','stews','stick','stiff','still','stilt','sting','stink','stint','stipe','stips','stirk','stirp','stirs','stoat','stock','stogy','stoic','stoke','stole','stoma','stomp','stone','stony','stood','stool','stoop','stops','store','stork','storm','story','stoss','stout','stove','stow','stows','strap','straw','stray','strep','strew','strip','strop','strut','stubs','stuck','studs','study','stuff','stump','stung','stunk','stunt','stupe','stupo','stupy','sturt','styed','style','styli','stylo','suave','suede','suers','suety','sucre','sudan','sudas','suder','sudes','sudsy','suede','suers','suety','sugar','suggy','suids','suite','suits','sulfa','sulfo','sulks','sulky','sully','sumac','sumas','sumed','sumer','sumes','sumis','sumos','sumps','sunay','sunda','sundi','sungi','sunk','sunks','sunny','sunup','supes','super','supgh','supra','sura','sural','suras','surds','surfs','surfy','surge','surly','surma','surra','sushi','susie','sutra','sutro','sutur','suzer','swabs','swage','swain','swale','swami','swamp','swamy','swang','swank','swans','swaps','sward','sware','swarf','swarm','swart','swash','swath','swats','swath','sway','swear','sweat','swede','sweep','sweet','swell','swept','swift','swig','swill','swim','swine','swing','swink','swipe','swirl','swish','swiss','swith','swive','swizz','swoon','swoop','sword','swore','sworn','swosh','swung','swy','sycee','sycon','sykes','sylis','sylla','sylph','sylvan','symes','symph','synch','syncs','synod','synth','syrup','syrup','sysop','syste','sythe','syzed','syzes','tabby','table','taboo','taboo','tabun','tabus','tacan','tacet','tacha','tache','tachs','tacit','tacks','tacky','tacos','tacts','taels','taiga','tails','taint','taken','taker','takes','talc','taler','tales','talis','talks','talky','tally','talon','talus','tamed','tamer','tames','tamis','tammy','tampo','tamps','tamus','tanas','tanco','tandy','taned','taner','tanes','tanga','tangi','tango','tangs','tangy','tanh','tanka','tanks','tanly','tanny','tansy','tansi','tanto','tants','taped','taper','tapes','tapet','tapir','tapis','tappi','tapsy','taras','tardy','tared','tares','target','tariff','taroc','taros','tarot','tarps','tarre','tarry','tarsa','tarsi','tarts','tarty','taser','tasha','tasks','taste','tasty','tatar','tater','tates','tatty','taunt','taupe','taurd','tauro','tauts','tava','taver','tavis','tawed','tawer','tawny','tawse','taxes','taxis','taxol','taxon','taxus','tayra','tchur','teads','teaks','teals','teams','teany','tears','teary','tease','teats','techy','tecta','teddy','tedis','tedks','teels','teems','teens','teeny','teeth','tegua','teiid','teind','tajes','Tekea','teler','teles','telex','telia','telic','telos','telsu','temat','temel','temer','tempi','tempo','temps','tempt','tench','tenda','tende','tends','tenns','tenon','tenor','tense','tenth','tents','tenue','tepal','tepas','tepid','teras','terce','tered','teres','terfs','terga','terms','terne','terns','terra','terry','terse','tesla','testa','teste','tests','testy','tetes','teths','tetra','tetri','tewel','tewer','texas','texes','texis','texti','texts','thack','thai','thali','thane','thank','thati','thats','thaw','thaws','theta','theca','theft','their','thems','theme','thens','there','therm','these','theta','thews','thick','thief','thigh','thill','thine','thing','think','thins','third','thirl','thole','thong','thorn','thorx','those','thout','thowl','thrall','thrash','thraw','thread','threo','three','thren','thresh','thrice','thrift','thrill','thrive','throat','throe','throm','throne','throng','throw','thrum','thuds','thug','thule','thumb','thump','thunk','thuya','thymi','thyme','tiara','tibet','tibia','tical','ticca','ticks','tidal','tided','tides','tided','tidew','tidid','tidys','tied','tierc','tiers','tiffs','tiger','tight','tigon','tigon','tikes','tikka','tilak','tilde','tiled','tiler','tiles','tills','tilth','tiltm','tilts','tilts','timed','timer','times','timid','timon','timor','timps','tined','tines','tinga','tinge','tings','tinny','tints','tiny','tipis','tippy','tipsy','tired','tires','tirls','tirrs','titan','tithe','titi','titre','titst','titty','tivol','tizes','tizzy','toads','toady','toast','toby','today','todde','todea','toddy','toedo','toffs','toffy','tofts','tofus','togas','toged','togee','toger','toget','togue','toing','toise','toits','tokay','token','toked','toker','tokes','toks','tokyo','tolas','toles','tolks','toll','tolls','tolu','tolus','tombs','tommy','tomos','tonai','tonal','tonda','tondo','toned','toner','tones','toney','tongs','tonic','tonne','tonus','tools','toots','toped','toper','topes','tophi','tophs','topic','topoi','topos','toppy','toqir','torah','toras','torch','torcs','tores','toric','torii','toros','torot','torrs','torse','torso','torte','torts','torus','tosas','tosed','toses','toset','toshy','tossy','total','toted','toter','totes','totty','totus','touch','tough','touns','toups','tours','touse','tousy','touts','touze','towed','towel','tower','towie','towns','towse','towzy','toxic','toxin','toyed','toyer','toyos','tozed','tozes','trace','track','tract','trade','trail','train','trait','tramp','trams','trank','trant','traps','trapt','trash','trass','trata','trate','trats','trash','trays','tread','treat','trees','treet','trefo','trefs','trek','treks','trems','trend','tress','trets','trews','treys','triad','trial','trias','tribe','trice','trick','tried','trier','tries','triff','trigg','trigo','trigs','trike','trill','trim','trims','trine','trios','tripe','trips','trise','trite','tritt','trive','triws','troad','troat','trock','troco','trode','trogs','troic','trois','troke','troll','tromp','trona','trond','trone','troop','troot','trope','trops','troth','trots','trout','trove','trows','troys','truce','truck','trued','truer','trues','truff','trull','truly','trump','trunk','truss','trust','truth','tryma','trying','tryst','tsche','tshap','tsine','tsume','tsums','tsuru','tuans','tubas','tubby','tubed','tuber','tubes','tubis','tuchu','tucum','tudos','tueds','tufts','tufty','tuism','tuktu','tulal','tules','tulip','tulla','tulsi','tumid','tummy','tumor','tumpa','tumps','tumus','tunas','tuned','tuner','tunes','tungs','tunic','tunny','tupai','tuple','tuque','turas','turbo','turds','turfs','turfy','turks','turns','turps','tusks','tutee','tutor','tutus','tutuy','tuyer','tvsts','twain','twang','twank','twats','tweak','tweed','tween','tweet','twice','twieg','twigs','twill','twine','twins','twiny','twirl','twirp','twist','twite','twits','twixt','twled','twode','twoer','twoni','tyees','tyers','tykes','tynde','typha','typic','typos','typps','tyred','tyree','tyres','tyros','tzars','tzatz ']
    elif chosen_difficulty == "Medium":
        category_list = ['university','management','technology','government','department','categories','conditions','experience','activities','additional','washington','california','discussion','collection','conference','individual','everything','production','commercial','newsletter','registered','protection','employment','commission','electronic','particular','facilities','statistics','investment','industrial','associated','foundation','population','navigation','operations','understand','connection','properties','assessment','especially','considered','enterprise','processing','resolution','components','assistance','disclaimer','membership','background','trademarks','television','interested','throughout','associates','businesses','restaurant','procedures','themselves','evaluation','references','literature','respective','definition','networking','australian','guidelines','difference','directions','automotive','successful','publishing','developing','historical','scientific','functional','monitoring','dictionary','accounting','techniques','permission','generation','characters','apartments','designated','integrated','compliance','acceptance','strategies','affiliates','multimedia','leadership','comparison','determined','statements','completely','electrical','applicable','basketball','identified','frequently','laboratory','industries','expression','provisions','principles','compatible','consulting','recreation','parameters','introduced','originally','philosophy','regulation','prevention','healthcare','maintained','increasing','containing','guaranteed','convention','previously','conversion','reasonable','importance','javascript','objectives','structures','continuing','accordance','annotation','percentage','supporting','specialist','concerning','developers','equivalent','curriculum','psychology','appliances','elementary','controlled','authorized','retirement','efficiency','commitment','interviews','classified','confidence','consistent','securities','democratic','dimensions','contribute','challenges','submission','regulatory','inspection','manchester','continuous','initiative','disability','contractor','affordable','tournament','publishers','performing','absolutely','calculator','sufficient','resistance','candidates','biological','transition','instrument','favourites','relatively','represents','pittsburgh','revolution','mechanical','recognized','completion','milfhunter','accessible','birmingham','consultant','controller','committees','innovation','newspapers','programmes','eventually','agreements','innovative','conclusion','settlement','purchasing','instructor','bestiality','approaches','highlights','scientists','volunteers','attachment','calculated','appearance','parliament','situations','structural','prohibited','simulation','bankruptcy','substances','discovered','exhibition','nationwide','definitely','commentary','limousines','apparently','popularity','postposted','sacramento','impossible','depression','cincinnati','subsection','wallpapers','subsequent','motorcycle','disclosure','occupation','citysearch','atmosphere','experiment','federation','assignment','counseling','acceptable','medication','metabolism','personally','excellence','attributes','obligation','regardless','restricted','republican','attendance','adventures','appreciate','mechanisms','indicators','physicians','governance','capability','complaints','promotions','geographic','suspension','correction','supplement','admissions','convenient','displaying','encouraged','cartridges','automation','advantages','extensions','applicants','adjustment','treatments','camcorders','difficulty','collective','enrollment','interfaces','opposition','supervisor','attraction','customized','understood','amendments','attractive','recordings','polyphonic','adjustable','allocation','discipline','dispatched','installing','engagement','facilitate','subscriber','priorities','incredible','portuguese','everywhere','housewares','reputation','photograph','underlying','projection','diagnostic','automobile','downloaded','protective','sunglasses','preference','litigation','horizontal','ultimately','artificial','affiliated','activation','mitsubishi','processors','complexity','constantly','substitute','households','montgomery','louisville','algorithms','suggestion','connecting','proportion','essentials','protecting','separation','boundaries','luxembourg','deployment','colleagues','recruiting','prescribed','reproduced','queensland','addressing','discounted','bangladesh','constitute','graduation','variations','soundtrack','profession','separately','physiology','collecting','friendship','provincial','advertiser','encryption','possession','vegetables','thumbnails','respondent','accredited','compressed','scheduling','christians','impressive','relocation','violations','discretion','repository','generating','millennium','exceptions','macromedia','fellowship','copyrights','mastercard','chronicles','distribute','decorative','indigenous','validation','corruption','incentives','transcript','structured','reasonably','recommends','indicating','coordinate','limitation','widescreen','decorating','connectors','perception','infections','configured','analytical','assumption','technician','executives','supporters','withdrawal','veterinary','reflection','invitation','thumbzilla','translated','columnists','delivering','journalism','undertaken','identifier','conducting','impression','charleston','selections','projectors','vocational','pharmacies','completing','comparable','warranties','documented','paperbacks','vulnerable','transexual','mainstream','evaluating','volleyball','creativity','describing','quotations','behavioral','containers','screenshot','officially','consortium','recipients','traditions','humanities','britannica','visibility','strengthen','aggressive','determines','motivation','passengers','quantities','petersburg','powerpoint','obituaries','punishment','providence','remembered','wilderness','headphones','proceeding','volkswagen','subsidiary','terrorists','beneficial','threatened','prediction','ecological','consisting','submitting','mozambique','wellington','aboriginal','remarkable','preventing','productive','trackbacks','programmer','incomplete','legitimate','architects','unexpected','formatting','discussing','meaningful','blackberry','meditation','microphone','organizing','moderators','kazakhstan','kilometers','guarantees','indication','cigarettes','responding','physically','attempting','accurately','ministries','thoroughly','nottingham','identifies','interstate','systematic','madagascar','presenting','uzbekistan','richardson','fragrances','vocabulary','earthquake','geological','introduces','webmasters','acdbentity','conspiracy','cumulative','occasional','explicitly','girlfriend','influenced','complement','requesting','lauderdale','extraction','hypothesis','regression','collectors','recognised','azerbaijan','travelling','widespread','referenced','vietnamese','tremendous','surrounded','accomplish','vegetarian','ambassador','contacting','vegetation','infectious','continuity','phenomenon','charitable','burlington','researcher','qualifying','estimation','institutes','stationery','journalist','afterwards','signatures','simplified','housewives','influences','irrigation','conviction','explaining','nomination','dependence','suggesting','privileges','landscapes','editorials','nationally','waterproof','alexandria','paragraphs','adolescent','occurrence','immigrants','helicopter','surprising','yugoslavia','likelihood','endangered','compromise','expiration','peripheral','greensboro','revelation','delegation','greenhouse','currencies','descending','psychiatry','persistent','adaptation','absorption','excitement','mysterious','indonesian','relaxation','thereafter','forwarding','reductions','portsmouth','harassment','generators','huntington','internship','beastality','antarctica','chancellor','antibodies','immunology','encourages','conceptual','translator','challenged','constraint','insulation','subjective','embroidery','oscommerce','nonfiction','homeowners','attributed','seychelles','cosponsors','memorandum','converting','incredibly','presidents','unofficial','valentines','kensington','weaknesses','underwater','authorised','supportive','repeatedly','similarity','implements','compelling','italicized','chromosome','competence','inadequate','defendants','playground','illustrate','newsgroups','ingredient','copenhagen','expedition','distortion','deviantart','whatsoever','terminated','greenville','profitable','derivative','storesshop','wastewater','decoration','assistants','eliminated','struggling','waterfront','reflecting','definitive','kyrgyzstan','postgresql','georgetown','technorati','simplicity','postscript','concurrent','bargaining','wilmington','manuscript','telephones','pertaining','professors','identities','tajikistan','deficiency','binoculars','stationary','celebrated','comprising','equatorial','scottsdale','percussion','wheelchair','adequately','prevalence','biomedical','performers','enthusiasm','mauritania','practicing','expressing','domination','impairment','dedication','freshwater','recognizes','responsive','travellers','portfolios','accountant','propaganda','amplifiers','executable','mitigation','dependency','approached','winchester','auditorium','audioslave','canterbury','remodeling','minorities','engineered','lancashire','superstore','micronesia','montenegro','advertised','organizers','smartphone','searchable','strawberry','redemption','martinique','craigslist','spermshack','durability','perfection','altogether','nickelback','animations','compulsory','satisfying','maintainer','classrooms','petitioner','deprecated','liberation','indirectly','presidency','breakfasts','inspectors','lieutenant','preventive','negotiated','congestion','accidental','guadeloupe','preferably','inhibitors','privileged','reinforced','specifying','inevitable','theatrical','initiation','autonomous','philippine','horoscopes','assemblies','collateral','transplant','scoreboard','lighthouse','customised','brightness','pharmacist','deliveries','recruiters','correspond','intentions','fitzgerald','hurricanes','pesticides','prosperity','plantation','passionate','combustion','administer','disposable','williamson','questioned','cumberland','preserving','nederlands','reflective','renovation','downstream','diplomatic','linguistic','internally','sweatshirt','conception','unemployed','misleading','capitalism','inequality','outpatient','coldfusion','positioned','conscience','enthusiast','positively','milfseeker','councillor','regulators','benchmarks','retrieving','financials','converters','decreasing','dishwasher','compassion','ecosystems','pronounced','delightful','pediatrics','ridiculous','scattering','contracted','therapists','lifestyles','threesomes','ultrasound','procedural','estimating','advisories','homosexual','spacecraft','montserrat','presumably','stretching','deductible','specialize','deposition','pedestrian','plaintiffs','nucleotide','collegiate','competitor','neighbours','encounters','programmed','negligence','clearwater','underneath','prosecutor','disturbing','sequential','huntsville','gymnastics','irrelevant','compressor','cunningham','gloucester','throughput','sanitation','inhibition','solidarity','frustrated','satellites','critically','localities','reciprocal','accelerate','telefonsex','permitting','apprentice','wavelength','principals','percentile','economical','miniatures','counselors','microscopy','prospectus','protectors','pollutants','chocolates','supervised','attainment','directives','discharged','underworld','reportedly','rebuilding','livingston','quickcheck','commenting','corrective','competency','contingent','refreshing','correlated','frameworks','filtration','incidental','equestrian','capacities','schoolgirl','relational','microscope','broadcasts','emphasized','formulated','hutchinson','succession','phonephone','enclosures','prototypes','sponsoring','sentencing','worthwhile','suspicious','subscribed','grenadines','librarians','crossroads','cinderella','unresolved','eliminates','objections','arithmetic','supposedly','enrichment','sandwiches','anticipate','franchises','deductions','harrisburg','assortment','sportswear','convincing','deviations','alteration','podcasting','centennial','referendum','modulation','demolition','grassroots','instructed','summarized','managerial','destroying','randomized','celebrates','historians','optimistic','announcing','dispersion','continents','recovering','prevailing','originated','condosaver','sculptures','thoughtful','milestones','derbyshire','checkboxes','excursions','allowances','successive','classmates','nineteenth','chesapeake','optimizing','switchfoot','ceremonies','conformity','insightful','fulfilling','exemptions','integrates','contiguous','bookstores','inaccurate','complained','invaluable','clustering','cardiology','oldsmobile','partitions','catalogues','harvesting','inflatable','coursework','solicitors','moderately','repetitive','kilometres','lithuanian','sequencing','polynomial','imperative','stochastic','fertilizer','regulating','ammunition','pneumonoultramicroscopicsilicovolcanoconiosis']
    elif chosen_difficulty == "Hard":
        category_list = ['abstractionism','abstractionist','acanthocephalan','acceptability','accessibility','acclimatisation','acclimatization','accommodatingly','accommodational','accomplishment','accountantship','acculturational','acetophenetidin','achondroplasia','achondroplastic','achromaticity','acknowledgeable','acknowledgement','acknowledgment','acquisitiveness','actinotherapy','adenocarcinoma','adenohypophysis','adenoidectomy','admirableness','admissibility','adrenalectomy','adventurousness','aftersensation','aggrandisement','aggrandizement','agranulocytosis','agreeableness','agriculturalist','airworthiness','alphabetisation','alphabetization','ambassadorship','ambidexterity','ambitiousness','ammonification','amphidiploidy','amphitheatrical','anagrammatise','anagrammatize','anisotropically','anomalousness','answerability','antepenultimate','anthropocentric','anthropogenesis','anthropogenetic','anthropolatry','anthropological','anthropologist','anthropometry','anthropomorphic','anthropophagite','anthropophagous','anthropophagy','anthroposophy','antiarrhythmic','anticholinergic','anticlimactical','anticonvulsant','antidepressant','antimetabolite','antineoplastic','antiperspirant','antisyphilitic','appealingness','applicability','apprenticeship','approachability','appropriateness','arbitrariness','arboriculturist','archaebacterium','archaeopteryx','archidiaconate','architecturally','argumentatively','arteriography','artificiality','asclepiadaceous','assertiveness','assiduousness','associability','associationism','astronavigation','astrophysicist','atherosclerosis','atherosclerotic','atrociousness','attainability','attentiveness','audaciousness','authentication','authoritatively','autobiographer','autobiography','autoradiograph','autoradiography','autosuggestion','availableness','bacteriological','bacteriologist','bacteriophagous','barbarousness','basidiomycetous','bastardisation','bastardization','beauteousness','beautification','believability','bellicoseness','benzodiazepine','bibliographical','bioengineering','biogeographical','bioluminescence','bioremediation','biotechnology','blamelessness','blameworthiness','blaxploitation','bloodthirsty','boundlessness','bounteousness','bountifulness','boustrophedonic','bowdlerisation','bowdlerization','brachycephalism','brachycephaly','brachydactylia','brachydactylous','brachydactyly','breakableness','bronchodilator','bumptiousness','businessperson','capaciousness','capitalisation','capitalization','carcinosarcoma','cardiopulmonary','categorisation','categorization','catheterisation','catheterization','ceaselessness','centralisation','centralization','centrifugation','centrosymmetric','cephalochordate','cerebrovascular','ceremoniousness','chancellorship','changeability','changefulness','channelization','cheerlessness','childlessness','chincherinchee','chloramphenicol','chlorothiazide','chlorpromazine','cholangiography','cholecalciferol','cholecystectomy','cholecystitis','cholecystokinin','cholinesterase','chordamesoderm','chorioallantois','chromatographic','chronologically','churrigueresque','cinematographer','circularization','circumambulate','circumferential','circumlocution','circumnavigate','circumscription','circumspection','circumstantiate','circumvallate','circumvolution','classification','claustrophobia','cloudlessness','coldheartedness','collateralize','colorlessness','combativeness','combustibleness','comfortableness','commercialise','commercialize','commissionaire','commonplaceness','communicational','commutability','comparability','compassionately','compatibility','competitiveness','complementarity','complementary','complementation','complicatedness','compositeness','comprehensively','compressibility','comptrollership','computationally','computerization','comradeliness','conceitedness','conceivableness','concentricity','conceptualise','conceptualistic','conceptuality','conceptualize','concessionaire','condescendingly','confectionary','confectionery','confidentiality','configurational','confrontational','congenialness','conglomeration','conglutination','congratulation','congratulations','congruousness','connectedness','connoisseurship','consanguinity','conscientiously','consequentially','conservationist','considerateness','conspicuousness','constitutional','constructivism','constructivist','consubstantiate','contemporaneity','contemporaneous','contemptibility','contentedness','contentiousness','contractility','contradictorily','contradictory','contraindicate','controllership','controversially','conventionalise','conventionalism','conventionality','conventionalize','conversationist','cooperativeness','correlativity','correspondence','correspondingly','corticosteroid','corticosterone','corticotrophin','corynebacterium','councillorship','counsellorship','counteractively','counterargument','counterattack','counterbalance','counterbalanced','counterchange','countercheck','counterclaim','counterculture','countercurrent','counterexample','counterirritant','countermarch','countermeasure','counterplot','counterpoint','counterproposal','counterweight','credulousness','criminalisation','criminalization','crossopterygian','crotchetiness','cryptographical','cryptorchidism','crystallisation','crystallization','crystallography','cyanocobalamin','cyproheptadine','cytogeneticist','cytomegalovirus','cytophotometric','cytoplasmically','dangerousness','dastardliness','dauntlessness','decalcification','decarboxylate','decarboxylation','deceitfulness','deceptiveness','decimalisation','decimalization','decolonisation','decolonization','decommission','deconcentrate','deconstruction','decontaminate','decontamination','decriminalise','decriminalize','dedifferentiate','defectiveness','defencelessness','defenestration','defenselessness','defensibility','defensiveness','defibrillation','dehumanization','dehydrogenate','delectability','deliciousness','demagnetisation','demagnetization','dematerialise','dematerialize','demisemiquaver','demobilisation','demobilization','democratisation','democratization','demonetisation','demonetization','demonstrability','demonstratively','demoralisation','demoralization','demythologise','demythologize','denationalise','denationalize','denazification','dependability','depersonalise','depersonalize','depigmentation','depolarisation','depolarization','dermatoglyphic','dermatoglyphics','dermatomyositis','dermatophytosis','desalinisation','desalinization','desensitisation','desensitization','desertification','deservingness','desirableness','despicability','dessertspoonful','destabilisation','destabilization','destructibility','destructiveness','determinateness','detoxification','detribalisation','detribalization','developmentally','devitalisation','devitalization','dextrorotation','diagonalization','dichotomization','differentiate','differentiation','differentiator','digestibility','digitalisation','digitalization','dimenhydrinate','dinoflagellate','diphenhydramine','disaccharidase','disadvantageous','disaffirmation','disambiguation','disappointingly','disappointment','disapprobation','disarrangement','disarticulate','disassociation','disciplinarian','discolouration','discombobulate','discombobulated','disconcertingly','disconcertment','discontentment','discontinuance','discontinuation','discontinuity','discountenance','discouragement','discrimination','disembarkation','disembarrass','disembowelment','disenchantment','disenfranchise','disenfranchised','disentanglement','disequilibrium','disestablish','disgracefulness','disgruntlement','disheartenment','disillusion','disillusionment','disinclination','disinfestation','disinformation','disinheritance','disintegration','disinterestedly','disorganisation','disorganization','disorientation','disparateness','dispassionately','dispensableness','disproportional','disreputability','disrespectfully','dissatisfaction','dissatisfactory','dissimilarity','dissolubility','dissoluteness','distastefulness','distinctiveness','distinguishable','distressfulness','distrustfulness','diversification','dolichocephalic','domineeringness','downheartedness','downrightness','duplicability','easygoingness','ecclesiasticism','echocardiogram','echocardiograph','econometrician','educationalist','effectiveness','effectualness','efficaciousness','effortfulness','egalitarianism','elaborateness','electioneering','electrification','electrochemical','electromagnetic','electromyogram','electromyograph','electronegative','electrophoresis','electrophoretic','electrophorus','electropositive','emancipationist','emotionlessness','enantiomorphism','encephalography','encyclopaedism','encyclopaedist','endocrinologist','endocrinology','enfranchisement','enjoyableness','enthronisation','enthronization','entrepreneurial','environmentally','ephemeralness','epicondylitis','epidemiological','epidemiologist','epistemological','epistemologist','equalitarianism','equivocalness','ergocalciferol','erroneousness','erythropoietin','essentialness','euphemistically','eutrophication','evangelicalism','everlastingness','excessiveness','exchangeability','excitableness','exclusiveness','excommunicate','excommunication','exemplification','exhibitionistic','existentialism','existentialist','expansiveness','expeditiousness','expensiveness','experimentalism','experimentation','exponentiation','expressionistic','exquisiteness','extemporisation','extemporization','extensiveness','exteriorisation','exteriorization','externalisation','externalization','extracurricular','extralinguistic','extraordinarily','facetiousness','faithlessness','familiarisation','familiarization','faultlessness','favorableness','featherbedding','federalisation','federalization','ferociousness','ferrimagnetism','ferromagnetism','fibrinopeptide','fibrocartilage','fingerprinting','fingerspelling','flibbertigibbet','foolhardiness','foreordination','foresightedness','forgetfulness','forgivingness','formidability','fortunetelling','fraction','fractiousness','frangibleness','fraternisation','fraternization','frightfulness','frivolousness','fructification','fruitlessness','fugaciousness','functionality','fundamentalism','fundamentalist','furfuraldehyde','garrulousness','gastroenteritis','generalisation','generalization','gentrification','geomorphology','glucocorticoid','glutinousness','glyceraldehyde','gracelessness','grandiloquence','grandiloquently','gravitationally','greensickness','grotesqueness','groundbreaking','guiltlessness','gynandromorphic','gyrostabiliser','gyrostabilizer','habitableness','halfpennyworth','haphazardness','hardheartedness','harpsichordist','hazardousness','headmastership','healthfulness','heartlessness','heartsickness','hemagglutinate','hemimetabolism','hemochromatosis','hemoglobinuria','hereditarianism','hermaphroditism','heterogeneity','heterosexuality','hexachlorophene','historiographer','holometabolism','homogeneousness','homogenisation','homogenization','homosexuality','honorableness','horizontality','horticulturally','horticulturist','hospitalisation','hospitalization','humanitarianism','hydrocephalus','hydrocortisone','hydroxyproline','hyperactivity','hyperadrenalism','hypercalcaemia','hypercatalectic','hyperextension','hyperglycaemia','hyperlipidemia','hypersecretion','hypersensitised','hypersensitized','hyperthyroidism','hypertonicity','hypervelocity','hyperventilate','hypochondriacal','hypochondriasis','hypostatization','hypothyroidism','ichthyosaur','ichthyosaurus','identicalness','identification','ideographically','ignominiousness','illogicalness','illustriousness','imaginativeness','immaterialise','immateriality','immaterialize','immediateness','immobilisation','immobilization','immovableness','immunochemistry','immunocompetent','immunodeficient','immunoglobulin','immunologically','immunopathology','immunotherapy','immutableness','impalpability','impassiveness','impeccability','impecuniousness','impenetrability','imperfectness','imperiousness','imperishability','impermeableness','impetuousness','implausibleness','implementation','impossibility','impoverishment','impreciseness','impressionistic','improbability','impulsiveness','inaccessibility','inadmissibility','inanimateness','inapplicability','inappropriately','inattentiveness','inaudibleness','incapableness','incessantness','incommensurable','incommunicative','incommutability','incompatibility','incomprehension','incomprehensive','incongruousness','inconsequential','inconsiderately','inconsideration','inconsistency','inconspicuously','inconvenience','incoordination','incorrectness','incorruptness','incredibility','inculpability','incurableness','indemnification','indeterminacy','indetermination','indigestibility','indisputability','individualise','individualistic','individuality','individualize','indoctrination','industrialise','industrialize','industriousness','ineffectiveness','ineffectualness','inefficaciously','ineligibility','inevitability','inexorability','inexpensiveness','infallibility','infeasibility','inflexibility','infrastructure','ingeniousness','ingenuousness','inhomogeneity','inhospitality','initialisation','initialization','injudiciousness','injuriousness','innumerableness','inopportuneness','inquisitiveness','insensibility','insensitiveness','insensitivity','insidiousness','insignificance','insignificantly','inspirationally','instantaneously','institutionally','instructorship','instrumentalism','instrumentalist','instrumentality','instrumentation','insubordination','insubstantially','insufficiency','insurrectionary','insurrectionism','insurrectionist','intangibility','intelligentsia','intelligibility','intemperateness','intensification','intensiveness','interchangeable','interchangeably','intercollegiate','intercommunion','interconnect','interconnection','interdependence','interdependency','interestingness','interferometer','intermediation','intermittency','internalisation','internalization','internationally','interpellation','interpenetrate','interpretation','interrogatively','interrogatory','interscholastic','interstratify','intractableness','intramuscularly','intransigency','intrusiveness','intussuscept','intussusception','invariability','inventiveness','invincibility','invisibleness','involuntariness','invulnerability','irrationality','irreligiousness','irresistibility','irreversibility','judiciousness','jurisprudential','keratinisation','keratinization','kindergartener','kindheartedness','kinesthetically','laboriousness','labyrinthitis','labyrinthodont','lackadaisically','lamellibranch','lateralisation','lateralization','latitudinarian','lecherousness','legislatorship','leisureliness','lepidopterology','lexicalisation','lexicalization','lexicographical','liberalisation','liberalization','libertarianism','lightheadedness','lightsomeness','limitlessness','litigiousness','loathsomeness','logarithmically','longsightedness','lucrativeness','luxuriousness','lymphadenitis','lymphadenopathy','lymphangiogram','lymphogranuloma','lyophilisation','lyophilization','lysogenization','macroeconomist','macroevolution','macroscopically','macrosporangium','magnanimousness','malacopterygian','maladroitness','maliciousness','malnourishment','manageability','maneuverability','manoeuvrability','marginalisation','marginalization','marriageability','masculinization','masochistically','mastoidectomy','materfamilias','materialisation','materialization','meaninglessness','measurability','mechanistically','megagametophyte','megalocephaly','megasporophyll','melodiousness','memorialization','mercaptopurine','merchantability','mercilessness','meritoriousness','metamathematics','metastability','methamphetamine','methylphenidate','microbiologist','microelectronic','microevolution','micrometeorite','micrometeoritic','micrometeoroid','micromillimetre','microphotometer','microprocessor','microscopically','microsporangium','microsporophyll','militarisation','militarization','millenarianism','millionairess','miniaturisation','miniaturization','misapplication','misapprehend','misapprehension','misappropriate','misappropriated','miscalculation','mischievousness','misconstruction','miserableness','misinformation','misinterpret','misrepresent','misshapenness','mistranslation','momentousness','monochromatism','monopolization','monosaccharide','monounsaturated','morphologically','morphophonemics','mountaineering','multiplication','multiprocessing','multiprocessor','murderousness','musculoskeletal','musicologically','myelencephalon','mythologisation','mythologization','nationalisation','nationalization','naturalisation','naturalization','nearsightedness','nebuchadnezzar','nefariousness','neighbourliness','neocolonialism','neoconservatism','neoconservative','nervelessness','neuroanatomical','neurobiological','neurobiologist','neurohypophysis','neurophysiology','neuropsychiatry','neuropsychology','neuroscientist','neutralisation','neutralization','nitrocellulose','nitrochloroform','nitroglycerine','noctambulation','noiselessness','nonachievement','noncommissioned','noncommunicable','nonconformance','nonconformity','nondevelopment','nondisjunction','nonequivalence','nonhierarchical','noninflammatory','nonintellectual','noninterference','nonintersecting','nonintervention','nonparticipant','nonpartisanship','nonperformance','nonprescription','nonprofessional','nonspecifically','nontransferable','nonuniformity','norepinephrine','northeastwardly','northwestwardly','noticeability','notwithstanding','nucleosynthesis','numismatologist','numismatology','objectification','objectiveness','obliviousness','obnoxiousness','obsessiveness','obstructionism','obstructionist','obtrusiveness','occidentalise','offensiveness','officiousness','oligodendrocyte','oligodendroglia','oligosaccharide','omnidirectional','operationalism','ophthalmologist','ophthalmology','ophthalmoplegia','ophthalmoscope','opisthognathous','opportuneness','organophosphate','orthogonality','orthophosphate','osteomyelitis','outspokenness','overachievement','overbearingness','overcapitalise','overcapitalize','overcompensate','overconfidence','overcredulity','overdramatise','overdramatize','overemphasize','overestimation','overgeneralize','overindulgence','overpopulation','overproduction','overprotection','overrefinement','oversimplify','overspecialise','overspecialize','overutilization','oxidoreductase','oxyhaemoglobin','oxyphenbutazone','oxytetracycline','palaeobiology','palaeoecology','palaeogeography','palaeontologist','palaeontology','palaeopathology','palaeozoology','palatableness','paleontological','paleontologist','parallelepiped','parallelopiped','paramyxovirus','parasympathetic','parenthetically','parliamentarian','parthenocarpy','parthenogenesis','parthenogenetic','particularise','particularistic','particularity','pasteurisation','pasteurization','paterfamilias','peaceableness','penetrability','pennilessness','penuriousness','perdurability','perfluorocarbon','periodontitis','peripateticism','perishability','permutability','perpendicularly','personification','perspicuousness','pervasiveness','pessimistically','phantasmagoria','pharmaceutical','pharmacological','pharmacologist','phenobarbitone','phenolphthalein','phenomenology','phenylbutazone','phenylketonuria','philanthropist','philosophically','phosphocreatine','phosphoprotein','phosphorescence','photoconductive','photoelectrical','photoengraving','photojournalism','photojournalist','photolithograph','photomechanical','photometrically','photomicrograph','photosensitise','photosensitize','physicochemical','physiologically','physiotherapist','physiotherapy','picturesqueness','pigheadedness','plagiocephaly','plainclothesman','plaintiveness','platitudinarian','platitudinize','plausibleness','plenipotentiary','plenteousness','plentifulness','plethysmograph','pleuropneumonia','plumbaginaceous','pneumonectomy','pointlessness','poliomyelitis','polycrystalline','polyelectrolyte','polymerisation','polymerization','polysaccharide','polyunsaturated','ponderousness','popularisation','popularization','porcupinefish','postoperatively','powerlessness','practicableness','preachification','prearrangement','precipitateness','precipitousness','precondition','predestinarian','predestination','predisposition','prefabrication','prematureness','prepositionally','prescriptivism','preservationist','prestidigitator','prestigiousness','presupposition','pretentiousness','preternaturally','pricelessness','primitiveness','problematically','procrastinate','procrastination','procrastinator','professionalise','professionalism','professionalize','profitability','prognosticate','prognostication','prognosticative','prognosticator','progressiveness','progressivity','prohibitionist','promiscuousness','pronunciamento','proportionality','proportionately','proprietorship','proprioception','prosencephalon','prostatectomy','prosthodontist','protozoological','protozoologist','pseudoephedrine','pseudoscorpion','psychoanalyse','psychoanalyze','psycholinguist','psychologically','psychoneurotic','psychopathology','psychophysicist','psychosexuality','psychosurgery','psychotherapist','psychotherapy','pulchritudinous','punctiliousness','purposelessness','pusillanimity','pusillanimously','pycnodysostosis','pyroelectricity','quadruplicate','quantification','quarrelsomeness','quatercentenary','querulousness','quincentenary','quincentennial','radioactivity','radiobiologist','radiophotograph','radioprotection','radiotelegraph','radiotelegraphy','radiotelephone','radiotelephonic','radiotherapist','rapaciousness','rationalisation','rationalization','reapportionment','recalcitrancy','recapitulation','receptiveness','reciprocality','reclusiveness','recommencement','recommendation','reconciliation','reconditeness','reconnaissance','reconsideration','reconstruction','redetermination','redistribution','reflexiveness','regularisation','regularization','rehabilitation','reintroduction','religiousness','relinquishment','reorganisation','reorganization','repetitiousness','representation','reproducibility','repulsiveness','requisiteness','resourcefulness','responsibleness','restrengthen','restrictiveness','retentiveness','retinoblastoma','retrospectively','reversibility','revitalisation','revitalization','revivification','revolutionary','revolutionise','rheumatologist','rhinencephalon','rhombencephalon','righteousness','rigidification','roentgenography','romanticisation','romanticization','sadomasochistic','sagaciousness','salaciousness','salpingectomy','sanctification','sanctimoniously','sanguification','saponification','scandalisation','scandalization','scaphocephaly','schematisation','schematization','schistosomiasis','schlockmeister','seaworthiness','secretiveness','secularisation','secularization','segregationist','semicentennial','semiterrestrial','semitransparent','sensationalism','sensationalist','senselessness','sensitiveness','sentimentalise','sentimentalism','sentimentalist','sentimentalize','septuagenarian','serviceableness','servomechanical','servomechanism','sesquipedalian','shamelessness','shapelessness','shiftlessness','sidesplittingly','sightlessness','sigmoidectomy','sigmoidoscopy','simplification','slaughterhouse','sledgehammer','sleeplessness','sociobiological','sociobiologist','sociolinguistic','softheartedness','solidification','solitudinarian','somnambulation','sophistication','sorrowfulness','soundlessness','southeastwardly','southwestwardly','specialisation','specialization','spectroscopical','speculativeness','spermatogenesis','sphericalness','spinelessness','spironolactone','spontaneousness','sporangiophore','sprightliness','squeamishness','squeezability','standardisation','standardization','standoffishness','steadfastness','steganography','stereotypically','stigmatisation','stigmatization','stoichiometry','straightforward','straightjacket','stratification','strenuousness','streptobacillus','streptocarpus','streptodornase','streptothricin','strikebreaking','stultification','subordinateness','substantialness','substantiation','succinylcholine','sumptuousness','superabundance','superannuation','supererogation','superinfection','superintendence','superintendent','supernaturalism','supernaturalist','supernumerary','superordinate','superordination','superpatriotism','superscription','superstitiously','superstructure','supersymmetry','supplementation','surreptitiously','susceptibleness','syllabification','symmetricalness','sympathectomy','sympathetically','sympathomimetic','symptomatically','synchronicity','synchronisation','synchronization','synergistically','systematisation','systematization','talkativeness','tastelessness','tatterdemalion','technologically','telecommunicate','teleconference','telegraphically','telephotograph','telephotography','teleprocessing','teletypewriter','temperamentally','temperateness','tempestuousness','temporariness','tenaciousness','tendentiousness','tenosynovitis','tergiversation','territorialise','territorialize','tetrasporangium','thaumatolatry','theatricality','therapeutically','thermocautery','thermochemistry','thermodynamical','thermojunction','thermoreceptor','thermoregulator','thermotherapy','thoracocentesis','thoughtlessness','thromboembolism','thromboplastin','thyrocalcitonin','thyroidectomy','tightfistedness','tintinnabulate','tomboyishness','tonsillectomy','toothsomeness','topographically','totalitarianism','tractableness','traditionalism','traditionalist','transamination','transcendency','transferability','transfiguration','transformation','transistorise','transliterate','transliteration','transmigration','transmogrify','transmutability','transparentness','transplantation','transportation','transposability','transsexualism','transvestitism','triangularity','tribromoethanol','trinitrotoluene','troubleshoot','troubleshooter','troublesomeness','trustworthiness','turbogenerator','tympanoplasty','typographically','tyrannosaurus','ultracentrifuge','ultramicroscope','ultramontanism','ultrasonography','unacceptability','unaccommodating','unascertainable','unassertiveness','unboundedness','unbreakableness','unceremoniously','uncertainness','unchallengeable','unchangeability','uncleanliness','uncloudedness','uncommunicative','uncompassionate','uncomplainingly','uncomplimentary','uncomprehending','unconditionally','unconnectedness','unconscientious','unconsciousness','uncontroversial','undemonstrative','underdevelop','underestimate','underestimation','undernourish','underperform','underperformer','underprivileged','underproduction','understandingly','understatement','undervaluation','undistinguished','undutifulness','unexceptionable','unfamiliarity','unfavorableness','unfeelingness','ungentlemanlike','ungrammatically','unhealthfulness','unhealthiness','unimaginatively','uninformatively','unintelligently','unintentionally','uninterestingly','uninterruptedly','unknowingness','unknowledgeable','unmindfulness','unnaturalness','unobjectionable','unobtrusiveness','unoriginality','unparliamentary','unpatriotically','unprecedentedly','unprepossessing','unpretentiously','unprofitability','unpronounceable','unprotectedness','unquestioningly','unrealistically','unreconstructed','unreliability','unrighteousness','unselfconscious','unselfishness','unsightliness','unsociability','unsophisticated','unsportsmanlike','unstatesmanlike','unsubstantiated','unsuitability','unsymmetrically','unwholesomeness','unwillingness','utilitarianism','valetudinarian','valuelessness','vascularisation','vascularization','vasoconstrictor','venerableness','venturesomeness','verisimilitude','vespertilionid','vivisectionist','voicelessness','voraciousness','voyeuristically','vulnerability','warmheartedness','watercolourist','waterlessness','weatherboarding','weatherliness','weatherproof','weatherstrip','whippersnapper','wholesomeness','withdrawnness','wonderfulness','worthlessness','xeroradiography']
    difficulty_select.destroy()

score = 0
bonus_score = 0
score_display = "Score = N/A, Streak = N/A"

config_window = Tk()
config_window.title("Config Menu")
config_window.configure(bg = "#9af09d")

aspect_ratio_text = Label(config_window, width = 19, font = (None,15), bg = "#48bd3d", text = "Select an aspect ratio:")
aspect_ratio_text.pack(padx = 40, pady = 10)

aspect_ratio = Listbox(config_window, exportselection = False)
aspect_ratio.insert(1,"640x360")
aspect_ratio.insert(2,"1280x720")
aspect_ratio.insert(3,"1600x900")
aspect_ratio.insert(4,"1920x1080")
aspect_ratio.insert(5,"2560x1440")
aspect_ratio.pack(padx = 40, pady = 5)

colour_text = Label(config_window, width = 14, font = (None,15), bg = "#48bd3d", text = "Select a colour:")
colour_text.pack(padx = 40, pady = 10)

colour = Listbox(config_window, exportselection = False)
colour.insert(1,"Red")
colour.insert(2,"Orange")
colour.insert(3,"Yellow")
colour.insert(4,"Green")
colour.insert(5,"Blue")
colour.insert(6,"Purple")
colour.insert(7,"Multicolour")
colour.pack(padx = 40, pady = 5)

category_text = Label(config_window, width = 16, font = (None,15), bg = "#48bd3d", text = "Select a category:")
category_text.pack(padx = 40, pady = 10)

category = Listbox(config_window, exportselection = False)
category.insert(1,"General")
category.insert(2,"Animals")
category.insert(3,"Space")
category.insert(4,"Brands")
category.insert(5,"Python Keywords")
category.pack(padx = 40, pady = 5)

begin_game = Button(width = 10,font = (None,20), text = "Start game", bg = "#48c452", command = playGameFirst)
begin_game.pack(padx = 40, pady = 10)

config_window.mainloop()
