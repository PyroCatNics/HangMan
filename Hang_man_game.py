#Cool hangman game that uses python interfaces (a lot of code is from the Hang_Man script i made a while ago)

import random, sys, subprocess, time
from tkinter import *

wordList = ['university','management','technology','government','department','categories','conditions','experience','activities','additional','washington','california','discussion','collection','conference','individual','everything','production','commercial','newsletter','registered','protection','employment','commission','electronic','particular','facilities','statistics','investment','industrial','associated','foundation','population','navigation','operations','understand','connection','properties','assessment','especially','considered','enterprise','processing','resolution','components','assistance','disclaimer','membership','background','trademarks','television','interested','throughout','associates','businesses','restaurant','procedures','themselves','evaluation','references','literature','respective','definition','networking','australian','guidelines','difference','directions','automotive','successful','publishing','developing','historical','scientific','functional','monitoring','dictionary','accounting','techniques','permission','generation','characters','apartments','designated','integrated','compliance','acceptance','strategies','affiliates','multimedia','leadership','comparison','determined','statements','completely','electrical','applicable','basketball','identified','frequently','laboratory','industries','expression','provisions','principles','compatible','consulting','recreation','parameters','introduced','originally','philosophy','regulation','prevention','healthcare','maintained','increasing','containing','guaranteed','convention','previously','conversion','reasonable','importance','javascript','objectives','structures','continuing','accordance','annotation','percentage','supporting','specialist','concerning','developers','equivalent','curriculum','psychology','appliances','elementary','controlled','authorized','retirement','efficiency','commitment','interviews','classified','confidence','consistent','securities','democratic','dimensions','contribute','challenges','submission','regulatory','inspection','manchester','continuous','initiative','disability','contractor','affordable','tournament','publishers','performing','absolutely','calculator','sufficient','resistance','candidates','biological','transition','instrument','favourites','relatively','represents','pittsburgh','revolution','mechanical','recognized','completion','milfhunter','accessible','birmingham','consultant','controller','committees','innovation','newspapers','programmes','eventually','agreements','innovative','conclusion','settlement','purchasing','instructor','bestiality','approaches','highlights','scientists','volunteers','attachment','calculated','appearance','parliament','situations','structural','prohibited','simulation','bankruptcy','substances','discovered','exhibition','nationwide','definitely','commentary','limousines','apparently','popularity','postposted','sacramento','impossible','depression','cincinnati','subsection','wallpapers','subsequent','motorcycle','disclosure','occupation','citysearch','atmosphere','experiment','federation','assignment','counseling','acceptable','medication','metabolism','personally','excellence','attributes','obligation','regardless','restricted','republican','attendance','adventures','appreciate','mechanisms','indicators','physicians','governance','capability','complaints','promotions','geographic','suspension','correction','supplement','admissions','convenient','displaying','encouraged','cartridges','automation','advantages','extensions','applicants','adjustment','treatments','camcorders','difficulty','collective','enrollment','interfaces','opposition','supervisor','attraction','customized','understood','amendments','attractive','recordings','polyphonic','adjustable','allocation','discipline','dispatched','installing','engagement','facilitate','subscriber','priorities','incredible','portuguese','everywhere','housewares','reputation','photograph','underlying','projection','diagnostic','automobile','downloaded','protective','sunglasses','preference','litigation','horizontal','ultimately','artificial','affiliated','activation','mitsubishi','processors','complexity','constantly','substitute','households','montgomery','louisville','algorithms','suggestion','connecting','proportion','essentials','protecting','separation','boundaries','luxembourg','deployment','colleagues','recruiting','prescribed','reproduced','queensland','addressing','discounted','bangladesh','constitute','graduation','variations','soundtrack','profession','separately','physiology','collecting','friendship','provincial','advertiser','encryption','possession','vegetables','thumbnails','respondent','accredited','compressed','scheduling','christians','impressive','relocation','violations','discretion','repository','generating','millennium','exceptions','macromedia','fellowship','copyrights','mastercard','chronicles','distribute','decorative','indigenous','validation','corruption','incentives','transcript','structured','reasonably','recommends','indicating','coordinate','limitation','widescreen','decorating','connectors','perception','infections','configured','analytical','assumption','technician','executives','supporters','withdrawal','veterinary','reflection','invitation','thumbzilla','translated','columnists','delivering','journalism','undertaken','identifier','conducting','impression','charleston','selections','projectors','vocational','pharmacies','completing','comparable','warranties','documented','paperbacks','vulnerable','transexual','mainstream','evaluating','volleyball','creativity','describing','quotations','behavioral','containers','screenshot','officially','consortium','recipients','traditions','humanities','britannica','visibility','strengthen','aggressive','determines','motivation','passengers','quantities','petersburg','powerpoint','obituaries','punishment','providence','remembered','wilderness','headphones','proceeding','volkswagen','subsidiary','terrorists','beneficial','threatened','prediction','ecological','consisting','submitting','mozambique','wellington','aboriginal','remarkable','preventing','productive','trackbacks','programmer','incomplete','legitimate','architects','unexpected','formatting','discussing','meaningful','blackberry','meditation','microphone','organizing','moderators','kazakhstan','kilometers','guarantees','indication','cigarettes','responding','physically','attempting','accurately','ministries','thoroughly','nottingham','identifies','interstate','systematic','madagascar','presenting','uzbekistan','richardson','fragrances','vocabulary','earthquake','geological','introduces','webmasters','acdbentity','conspiracy','cumulative','occasional','explicitly','girlfriend','influenced','complement','requesting','lauderdale','extraction','hypothesis','regression','collectors','recognised','azerbaijan','travelling','widespread','referenced','vietnamese','tremendous','surrounded','accomplish','vegetarian','ambassador','contacting','vegetation','infectious','continuity','phenomenon','charitable','burlington','researcher','qualifying','estimation','institutes','stationery','journalist','afterwards','signatures','simplified','housewives','influences','irrigation','conviction','explaining','nomination','dependence','suggesting','privileges','landscapes','editorials','nationally','waterproof','alexandria','paragraphs','adolescent','occurrence','immigrants','helicopter','surprising','yugoslavia','likelihood','endangered','compromise','expiration','peripheral','greensboro','revelation','delegation','greenhouse','currencies','descending','psychiatry','persistent','adaptation','absorption','excitement','mysterious','indonesian','relaxation','thereafter','forwarding','reductions','portsmouth','harassment','generators','huntington','internship','beastality','antarctica','chancellor','antibodies','immunology','encourages','conceptual','translator','challenged','constraint','insulation','subjective','embroidery','oscommerce','nonfiction','homeowners','attributed','seychelles','cosponsors','memorandum','converting','incredibly','presidents','unofficial','valentines','kensington','weaknesses','underwater','authorised','supportive','repeatedly','similarity','implements','compelling','italicized','chromosome','competence','inadequate','defendants','playground','illustrate','newsgroups','ingredient','copenhagen','expedition','distortion','deviantart','whatsoever','terminated','greenville','profitable','derivative','storesshop','wastewater','decoration','assistants','eliminated','struggling','waterfront','reflecting','definitive','kyrgyzstan','postgresql','georgetown','technorati','simplicity','postscript','concurrent','bargaining','wilmington','manuscript','telephones','pertaining','professors','identities','tajikistan','deficiency','binoculars','stationary','celebrated','comprising','equatorial','scottsdale','percussion','wheelchair','adequately','prevalence','biomedical','performers','enthusiasm','mauritania','practicing','expressing','domination','impairment','dedication','freshwater','recognizes','responsive','travellers','portfolios','accountant','propaganda','amplifiers','executable','mitigation','dependency','approached','winchester','auditorium','audioslave','canterbury','remodeling','minorities','engineered','lancashire','superstore','micronesia','montenegro','advertised','organizers','smartphone','searchable','strawberry','redemption','martinique','craigslist','spermshack','durability','perfection','altogether','nickelback','animations','compulsory','satisfying','maintainer','classrooms','petitioner','deprecated','liberation','indirectly','presidency','breakfasts','inspectors','lieutenant','preventive','negotiated','congestion','accidental','guadeloupe','preferably','inhibitors','privileged','reinforced','specifying','inevitable','theatrical','initiation','autonomous','philippine','horoscopes','assemblies','collateral','transplant','scoreboard','lighthouse','customised','brightness','pharmacist','deliveries','recruiters','correspond','intentions','fitzgerald','hurricanes','pesticides','prosperity','plantation','passionate','combustion','administer','disposable','williamson','questioned','cumberland','preserving','nederlands','reflective','renovation','downstream','diplomatic','linguistic','internally','sweatshirt','conception','unemployed','misleading','capitalism','inequality','outpatient','coldfusion','positioned','conscience','enthusiast','positively','milfseeker','councillor','regulators','benchmarks','retrieving','financials','converters','decreasing','dishwasher','compassion','ecosystems','pronounced','delightful','pediatrics','ridiculous','scattering','contracted','therapists','lifestyles','threesomes','ultrasound','procedural','estimating','advisories','homosexual','spacecraft','montserrat','presumably','stretching','deductible','specialize','deposition','pedestrian','plaintiffs','nucleotide','collegiate','competitor','neighbours','encounters','programmed','negligence','clearwater','underneath','prosecutor','disturbing','sequential','huntsville','gymnastics','irrelevant','compressor','cunningham','gloucester','throughput','sanitation','inhibition','solidarity','frustrated','satellites','critically','localities','reciprocal','accelerate','telefonsex','permitting','apprentice','wavelength','principals','percentile','economical','miniatures','counselors','microscopy','prospectus','protectors','pollutants','chocolates','supervised','attainment','directives','discharged','underworld','reportedly','rebuilding','livingston','quickcheck','commenting','corrective','competency','contingent','refreshing','correlated','frameworks','filtration','incidental','equestrian','capacities','schoolgirl','relational','microscope','broadcasts','emphasized','formulated','hutchinson','succession','phonephone','enclosures','prototypes','sponsoring','sentencing','worthwhile','suspicious','subscribed','grenadines','librarians','crossroads','cinderella','unresolved','eliminates','objections','arithmetic','supposedly','enrichment','sandwiches','anticipate','franchises','deductions','harrisburg','assortment','sportswear','convincing','deviations','alteration','podcasting','centennial','referendum','modulation','demolition','grassroots','instructed','summarized','managerial','destroying','randomized','celebrates','historians','optimistic','announcing','dispersion','continents','recovering','prevailing','originated','condosaver','sculptures','thoughtful','milestones','derbyshire','checkboxes','excursions','allowances','successive','classmates','nineteenth','chesapeake','optimizing','switchfoot','ceremonies','conformity','insightful','fulfilling','exemptions','integrates','contiguous','bookstores','inaccurate','complained','invaluable','clustering','cardiology','oldsmobile','partitions','catalogues','harvesting','inflatable','coursework','solicitors','moderately','repetitive','kilometres','lithuanian','sequencing','polynomial','imperative','stochastic','fertilizer','regulating','ammunition','pneumonoultramicroscopicsilicovolcanoconiosis']
word = (random.choice(wordList))
wrongGuesses = ""
guessedLetters = []
timesDone = 0
for i in range(len(word)):
    list.append(guessedLetters,"_")


def doNothing():
    thisWill = doNothing
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
    /|\    |
           |
           |
        ________|_____'''
    global hangman9
    hangman9 = '''
     ______
     |     |
     O     |
    /|\    |
    /      |
           |
        ________|_____'''
    global hangman10
    hangman10 = '''
     ______
     |     |
     O     |
    /|\    |
    / \    |
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
        main_text.config(width = 50, text = str(guessedLetters)+"\n"+hangmanDisplay+wrongGuesses+accusation+reiteration)
        if timesDone > 9:
            letter.destroy()
            confirm_text.destroy()
        else:
            letter.config(state = NORMAL)
    else:
        main_text.config(width = 50, text = str(guessedLetters)+"\n"+"WELL DONE! You guessed the word! It was:\n"+(word.capitalize()))
        letter.destroy()
        confirm_text.destroy()
        retry_game = Button(width = 10, font = (None,60), bg = "#3acaa6", text = "New Game", command = retry_Game)
        retry_game.pack(padx = 40, pady = 30)
def retry_Game():
    game.destroy()
    subprocess.run([sys.executable, "Hang_man_game.py"])
    sys.exit("Restarting game...")
    

hangmanDraw()

game = Tk()
game.title("Hangman")
game.attributes('-fullscreen', True)

game.configure(bg = "#0f63a8")

main_text = Label(game,width = 45, font = ("Liberation Mono",60), bg = "#70cfec", text = "Welcome to hangman! Enter a letter below.")
main_text.pack(padx = 40, pady = 20)

letter = Entry(width = 10,font = (None,40), bg = "#a5baf0")
letter.pack(padx = 40, pady = 10)

confirm_text = Label(game,width = 28, font = (None,40), bg = "#38b5db", text = "Press enter to confirm your letter")
confirm_text.pack(padx = 40, pady = 10)

exit_game = Button(width = 10,font = (None,40), text = "Exit game", bg = "#2ea7cc", command = game.destroy)
exit_game.pack(padx = 40, pady = 10)

game.bind('<Return>',gatherAndDisplay)

game.mainloop()


