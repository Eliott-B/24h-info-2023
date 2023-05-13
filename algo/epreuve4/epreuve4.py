import string
d = dict.fromkeys(string.ascii_lowercase, 0) # création dico avec clé lettre
d[' '] = 0




def nombreTriangulaire(size:int) -> list[int]:
    T=0
    l = []
    for n in range(1,size) :
        T = T+n
        l.append(T)
    print(l)
    return l

l = nombreTriangulaire(100000)

def isTrianguaire(num: int, l: list[int]) -> bool:
    return num in l


def setDict(dict: dict) -> dict:
    cnt = 1
    for key in dict.keys():
        dict[key] = cnt
        cnt += 1 
    dict[" "] = 0
    dict["."] = 0
    dict["'"] = 0
    dict[","] = 0
    dict['"'] = 0
    dict["!"] = 0
    dict["?"] = 0
    dict[";"] = 0
    dict["2"] = 0
    dict["\n"] = 0
    dict["-"] = 0
    dict[":"] = 0
    dict["("] = 0
    dict[")"] = 0
    dict["0"] = 0
    dict["1"] = 0
    dict["8"] = 0
    dict["9"] = 0
    dict["7"] = 0
    dict["5"] = 0
    dict["3"] = 0
    dict["6"] = 0
    dict["1"] = 0
    dict["1"] = 0
    dict["4"] = 0
    dict["ì"] = 0
    dict["{"] = 0
    dict["}"] = 0
    dict[">"] = 0
    dict["<"] = 0
    return dict

d = setDict(d)

def poidMot(mot: str, d: dict, li: list[int]) -> int:
    sum = 0
    for lettre in mot:
        sum += d[lettre]

    if isTrianguaire(sum, li):
        return sum*(li.index(sum)+1)
    return 0

def poidPhrase(phrase: str, d:dict, l: list[int]) ->int:
    liMot = phrase.split(" ")
    sum = 0
    for mot in liMot:
        sum += poidMot(mot, d, l)
    return sum
#print(poidPhrase("sky", d))

def code() -> int:
    return poidPhrase("""Chapter 2
Aunt Marge's Big Mistake

Harry went down to breakfast the next morning to find the three Dursleys already sitting around the kitchen table. They were watching a brand-new television, a welcome- home-for- the-summer present for Dudley, who had been complaining loudly about the long walk between the fridge and the television in the living room. Dudley had spent most of the summer in the kitchen, his piggy little eyes fixed on the screen and his five chins wobbling as he ate continually.

Harry sat down between Dudley and Uncle Vernon, a large, beefy man with very little neck and a lot of mustache. Far from wishing Harry a happy birthday, none of the Dursleys made any sign that they had noticed Harry enter the room, but Harry was far too used to this to care. He helped himself to a piece of toast and then looked up at the reporter on the television, who was halfway through a report on an escaped convict:

"... The public is warned that Black is armed and extremely dangerous. A special hotline has been set up, and any sighting of Black should be reported immediately."

"No need to tell us he's no good," snorted Uncle Vernon, staring over the top of his newspaper at the prisoner. "Look at the state of him, the filthy layabout! Look at his hair!"

He shot a nasty look sideways at Harry, whose untidy hair had always been a source of great annoyance to Uncle Vernon. Compared to the man on the television, however, whose gaunt face was surrounded by a matted, elbow-length tangle, Harry felt very well groomed indeed.

The reporter had reappeared.

"The Ministry of Agriculture and Fisheries will announce today --"

"Hang on!" barked Uncle Vernon, staring furiously at the reporter. "You didn't tell us where that maniac's escaped from! What use is that? Lunatic could be coming up the street right now!"

Aunt Petunia, who was bony and horse-faced, whipped around and peered intently out of the kitchen window. Harry knew Aunt Petunia would simply love to be the one to call the hotline number. She was the nosiest woman in the world and spent most of her life spying on the boring, law-abiding neighbors.

"When will they learn," said Uncle Vernon, pounding the table with his large purple fist, "that hanging's the only way to deal with these people?"

"Very true," said Aunt Petunia, who was still squinting into next door's runner beans.

Uncle Vernon drained his teacup, glanced at his watch, and added, "I'd better be off in a minute, Petunia. Marge's train gets in at ten."

Harry, whose thoughts had been upstairs with the Broomstick Servicing Kit, was brought back to earth with an unpleasant bump.

"Aunt Marge?" he blurted out. "Sh - she's not coming here, is she?"

Aunt Marge was Uncle Vernon's sister. Even though she was not a blood relative of Harry's (whose mother had been Aunt Petunia's sister), he had been forced to call her "Aunt" all his life. Aunt Marge lived in the country, in a house with a large garden, where she bred bulldogs. She didn't often stay at Privet Drive, because she couldn't bear to leave her precious dogs, but each of her visits stood out horribly vividly in Harry's mind.

At Dudley's fifth birthday party, Aunt Marge had whacked Harry around the shins with her walking stick to stop him from beating Dudley at musical statues. A few years later, she had turned up at Christmas with a computerized robot for Dudley and a box of dog biscuits for Harry. On her last visit, the year before Harry started at Hogwarts, Harry had accidentally trodden on the tail of her favorite dog. Ripper had chased Harry out into the garden and up a tree, and Aunt Marge had refused to call him off until past midnight. The memory of this incident still brought tears of laughter to Dudley's eyes.

"Marge'll be here for a week," Uncle Vernon snarled, "and while we're on the subject" - he pointed a fat finger threateningly at Harry - "we need to get a few things straight before I go and collect her."

Dudley smirked and withdrew his gaze from the television. Watching Harry being bullied by Uncle Vernon was Dudley's favorite form of entertainment.

"Firstly," growled Uncle Vernon, "you'll keep a civil tongue in your head when you're talking to Marge."

"All right," said Harry bitterly, "if she does when she's talking to me."

"Secondly," said Uncle Vernon, acting as though he had not heard Harry's reply, "as Marge doesn't know anything about your abnormality, I don't want any - any funny stuff while she's here. You behave yourself, got me?"

"I will if she does," said Harry through gritted teeth.

"And thirdly," said Uncle Vernon, his mean little eyes now slits in his great purple face, "we've told Marge you attend St. Brutus's Secure Center for Incurably Criminal Boys."

"What?" Harry yelled.

"And you'll be sticking to that story, boy, or there'll be trouble," spat Uncle Vernon.

Harry sat there, white-faced and furious, staring at Uncle Vernon, hardly able to believe it. Aunt Marge coming for a week-long visit - it was the worst birthday present the Dursleys had ever given him, including that pair of Uncle Vernon's old socks.

"Well, Petunia," said Uncle Vernon, getting heavily to his feet, "I'll be off to the station, then. Want to come along for the ride, Dudders?"

"No," said Dudley, whose attention had returned to the television now that Uncle Vernon had finished threatening Harry.

"Duddy's got to make himself smart for his auntie," said Aunt Petunia, smoothing Dudley's thick blond hair. "Mummy's bought him a lovely new bow tie."

Uncle Vernon clapped Dudley on his porky shoulder.

"See you in a bit, then," he said, and he left the kitchen.

Harry, who had been sitting in a kind of horrified trance, had a sudden idea. Abandoning his toast, he got quickly to his feet and followed Uncle Vernon to the front door.

Uncle Vernon was pulling on his car coat.

"I'm not taking you," he snarled as he turned to see Harry watching him.

"Like I wanted to come," said Harry coldly. "I want to ask you something."

Uncle Vernon eyed him suspiciously.

"Third years at Hog - at my school are allowed to visit the village sometimes," said Harry.

"So?" snapped Uncle Vernon, taking his car keys from a hook next to the door.

"I need you to sign the permission form," said Harry in a rush.

"And why should I do that?" sneered Uncle Vernon.

"Well," said Harry, choosing his words carefully, "it'll be hard work, pretending to Aunt Marge I go to that St. Whatsits -"

"St. Brutus's Secure Center for Incurably Criminal Boys!" bellowed Uncle Vernon, and Harry was pleased to hear a definite note of panic in Uncle Vernon's voice.

"Exactly," said Harry, looking calmly up into Uncle Vernon's large, purple face. "It's a lot to remember. I'll have to make it sound convincing, won't I? What if I accidentally let something slip?"

"You'll get the stuffing knocked out of you, won't you?" roared Uncle Vernon, advancing on Harry with his fist raised. But Harry stood his ground.

"Knocking the stuffing out of me won't make Aunt Marge forget what I could tell her," he said grimly.

Uncle Vernon stopped, his fist still raised, his face an ugly puce.

"But if you sign my permission form," Harry went on quickly, "I swear I'll remember where I'm supposed to go to school, and I'll act like a Mug - like I'm normal and everything."

Harry could tell that Uncle Vernon was thinking it over, even if his teeth were bared and a vein was throbbing in his temple.

"Right," he snapped finally. "I shall monitor your behavior carefully during Marge's visit. If, at the end of it, you've toed the line and kept to the story, I'll sign your ruddy form."

He wheeled around, pulled open the front door, and slammed it so hard that one of the little panes of glass at the top fell out.

Harry didn't return to the kitchen. He went back upstairs to his bedroom. If he was going to act like a real Muggle, he'd better start now. Slowly and sadly he gathered up all his presents and his birthday cards and hid them under the loose floorboard with his homework. Then he went to Hedwig's cage. Errol seemed to have recovered; he and Hedwig were both asleep, heads under their wings. Harry sighed, then poked them both awake.

"Hedwig," he said gloomily, "you're going to have to clear off for a week. Go with Errol. Ron'll look after you. I'll write him a note, explaining. And don't look at me like that" - Hedwig's large amber eyes were reproachful - "it's not my fault. It's the only way I'll be allowed to visit Hogsmeade with Ron and Hermione."

Ten minutes later, Errol and Hedwig (who had a note to Ron bound to her leg) soared out of the window and out of sight. Harry, now feeling thoroughly miserable, put the empty cage away inside the wardrobe.

But Harry didn't have long to brood. In next to no time, Aunt Petunia was shrieking up the stairs for Harry to come down and get ready to welcome their guest.

"Do something about your hair!" Aunt Petunia snapped as he reached the hall.

Harry couldn't see the point of trying to make his hair lie flat. Aunt Marge loved criticizing him, so the untidier he looked, the happier she would be.

All too soon, there was a crunch of gravel outside as Uncle Vernon's car pulled back into the driveway, then the clunk of the car doors and footsteps on the garden path.

"Get the door!" Aunt Petunia hissed at Harry.

A feeling of great gloom in his stomach, Harry pulled the door open.

On the threshold stood Aunt Marge. She was very like Uncle Vernon: large, beefy, and purple-faced, she even had a mustache, though not as bushy as his. In one hand she held an enormous suitcase, and tucked under the other was an old and evil-tempered bulldog.

"Where's my Dudders?" roared Aunt Marge. "Where's my neffy- poo?"

Dudley came waddling down the hall, his blond hair plastered flat to his fat head, a bow tie just visible under his many chins. Aunt Marge thrust the suitcase into Harry's stomach, knocking the wind out of him, seized Dudley in a tight one-armed hug, and planted a large kiss on his cheek.

Harry knew perfectly well that Dudley only put up with Aunt Marge's hugs because he was well paid for it, and sure enough, when they broke apart, Dudley had a crisp twenty-pound note clutched in his fat fist.

"Petunia!" shouted Aunt Marge, striding past Harry as though he was a hat stand. Aunt Marge and Aunt Petunia kissed, or rather, Aunt Marge bumped her large jaw against Aunt Petunia's bony cheekbone.

Uncle Vernon now came in, smiling jovially as he shut the door.

"Tea, Marge?" he said. "And what will Ripper take?"

"Ripper can have some tea out of my saucer," said Aunt Marge as they all proceeded into the kitchen, leaving Harry alone in the hall with the suitcase. But Harry wasn't complaining; any excuse not to be with Aunt Marge was fine by him, so he began to heave the case upstairs into the spare bedroom, taking as long as he could.

By the time he got back to the kitchen, Aunt Marge had been supplied with tea and fruitcake, and Ripper was lapping noisily in the corner. Harry saw Aunt Petunia wince slightly as specks of tea and drool flecked her clean floor. Aunt Petunia hated animals.

"Who's looking after the other dogs, Marge?" Uncle Vernon asked.

"Oh, I've got Colonel Fubster managing them," boomed Aunt Marge. "He's retired now, good for him to have something to do. But I couldn't leave poor old Ripper. He pines if he's away from me."

Ripper began to growl again as Harry sat down. This directed Aunt Marge's attention to Harry for the first time.

"So!" she barked. "Still here, are you?"

"Yes," said Harry.

"Don't you say 'yes' in that ungrateful tone," Aunt Marge growled. "It's damn good of Vernon and Petunia to keep you. Wouldn't have done it myself. You'd have gone straight to an orphanage if you'd been dumped on my doorstep."

Harry was bursting to say that he'd rather live in an orphanage than with the Dursleys, but the thought of the Hogsmeade form stopped him. He forced his face into a painful smile.

"Don't you smirk at me!" boomed Aunt Marge. "I can see you haven't improved since I last saw you. I hoped school would knock some manners into you." She took a large gulp of tea, wiped her mustache, and said, "Where is it that you send him, again, Vernon?"

"St. Brutus's," said Uncle Vernon promptly. "It's a first-rate institution for hopeless cases."

"I see," said Aunt Marge. "Do they use the cane at St. Brutus's, boy?" she barked across the table.

"Er -"

Uncle Vernon nodded curtly behind Aunt Marge's back.

"Yes," said Harry. Then, feeling he might as well do the thing properly, he added, "all the time."

"Excellent," said Aunt Marge. "I won't have this namby-pamby, wishy-washy nonsense about not hitting people who deserve it. A good thrashing is what's needed in ninety-nine cases out of a hundred. Have you been beaten often?"

"Oh, yeah," said Harry, "loads of times."

Aunt Marge narrowed her eyes.

"I still don't like your tone, boy," she said. "If you can speak of your beatings in that casual way, they clearly aren't hitting you hard enough. Petunia, I'd write if I were you. Make it clear that you approve the use of extreme force in this boy's case."

Perhaps Uncle Vernon was worried that Harry might forget their bargain; in any case, he changed the subject abruptly.

"Heard the news this morning, Marge? What about that escaped prisoner, eh?"

As Aunt Marge started to make herself at home, Harry caught himself thinking almost longingly of life at number four without her. Uncle Vernon and Aunt Petunia usually encouraged Harry to stay out of their way, which Harry was only too happy to do. Aunt Marge, on the other hand, wanted Harry under her eye at all times, so that she could boom out suggestions for his improvement. She delighted in comparing Harry with Dudley, and took huge pleasure in buying Dudley expensive presents while glaring at Harry, as though daring him to ask why he hadn't got a present too. She also kept throwing out dark hints about what made Harry such an unsatisfactory person.

"You mustn't blame yourself for the way the boy's turned out, Vernon," she said over lunch on the third day. "If there's something rotten on the inside, there's nothing anyone can do about it."

Harry tried to concentrate on his food, but his hands shook and his face was starting to burn with anger. Remember the form, he told himself. Think about Hogsmeade. Don't say anything. Don't rise --

Aunt Marge reached for her glass of wine.

"It's one of the basic rules of breeding," she said. "You see it all the time with dogs. If there's something wrong with the bitch, there'll be something wrong with the pup -"

At that moment, the wineglass Aunt Marge was holding exploded in her hand. Shards of glass flew in every direction and Aunt Marge sputtered and blinked, her great ruddy face dripping.

"Marge!" squealed Aunt Petunia. "Marge, are you all right?"

"Not to worry," grunted Aunt Marge, mopping her face with her napkin. "Must have squeezed it too hard. Did the same thing at Colonel Fubster's the other day. No need to fuss, Petunia, I have a very firm grip ..."

But Aunt Petunia and Uncle Vernon were both looking at Harry suspiciously, so he decided he'd better skip dessert and escape from the table as soon as he could.

Outside in the hall, he leaned against the wall, breathing deeply. It had been a long time since he'd lost control and made something explode. He couldn't afford to let it happen again. The Hogsmeade form wasn't the only thing at stake - if he carried on like that, he'd be in trouble with the Ministry of Magic.

Harry was still an underage wizard, and he was forbidden by wizard law to do magic outside school. His record wasn't exactly clean either. Only last summer he'd gotten an official warning that had stated quite clearly that if the Ministry got wind of any more magic in Privet Drive, Harry would face expulsion from Hogwarts.

He heard the Dursleys leaving the table and hurried upstairs out of the way.

Harry got through the next three days by forcing himself to think about his Handbook of Do-It-Yourself Broomcare whenever Aunt Marge started on him. This worked quite well, though it seemed to give him a glazed look, because Aunt Marge started voicing the opinion that he was mentally subnormal.

At last, at long last, the final evening of Marge's stay arrived. Aunt Petunia cooked a fancy dinner and Uncle Vernon uncorked several bottles of wine. They got all the way through the soup and the salmon without a single mention of Harry's faults; during the lemon meringue pie, Uncle Vernon bored them all with a long talk about Grunnings, his drill-making company; then Aunt Petunia made coffee and Uncle Vernon brought out a bottle of brandy.

"Can I tempt you, Marge?"

Aunt Marge had already had quite a lot of wine. Her huge face was very red.

"Just a small one, then," she chuckled. "A bit more than that . . . and a bit more . . . that's the ticket."

Dudley was eating his fourth slice of pie. Aunt Petunia was sipping coffee with her little finger sticking out. Harry really wanted to disappear into his bedroom, but he met Uncle Vernon's angry little eyes and knew he would have to sit it out.

"Aah," said Aunt Marge, smacking her lips and putting the empty brandy glass back down. "Excellent nosh, Petunia. It's normally just a fry-up for me of an evening, with twelve dogs to look after. . . ." She burped richly and patted her great tweed stomach. "Pardon me. But I do like to see a healthy-sized boy," she went on, winking at Dudley. "You'll be a proper-sized man, Dudders, like your father. Yes, I'll have a spot more brandy, Vernon. . . ."

"Now, this one here -"

She jerked her head at Harry, who felt his stomach clench. The Handbook, he thought quickly.

"This one's got a mean, runty look about him. You get that with dogs. I had Colonel Fubster drown one last year. Ratty little thing it was. Weak. Underbred."

Harry was trying to remember page twelve of his book: A Charm to Cure Reluctant Reversers.

"It all comes down to blood, as I was saying the other day. Bad blood will out. Now, I'm saying nothing against your family, Petunia" - she patted Aunt Petunia's bony hand with her shovel-like one - "but your sister was a bad egg. They turn up in the best families. Then she ran off with a wastrel and here's the result right in front of us."

Harry was staring at his plate, a funny ringing in his ears. Grasp your broom firmly by the tail, he thought. But he couldn't remember what came next. Aunt Marge's voice seemed to be boring into him like one of Uncle Vernon's drills.

"This Potter," said Aunt Marge loudly, seizing the brandy bottle and splashing more into her glass and over the tablecloth, "you never told me what he did?"

Uncle Vernon and Aunt Petunia were looking extremely tense. Dudley had even looked up from his pie to gape at his parents.

"He - didn't work," said Uncle Vernon, with half a glance at Harry. "Unemployed."

"As I expected!" said Aunt Marge, taking a huge swig of brandy and wiping her chin on her sleeve. "A no-account, good-for-nothing, lazy scrounger who -"

"He was not," said Harry suddenly. The table went very quiet. Harry was shaking all over. He had never felt so angry in his life.

"MORE BRANDY!" yelled Uncle Vernon, who had gone very white. He emptied the bottle into Aunt Marge's glass. "You, boy," he snarled at Harry. "Go to bed, go on -"

"No, Vernon," hiccuped Aunt Marge, holding up a hand, her tiny bloodshot eyes fixed on Harry's. "Go on, boy, go on. Proud of your parents, are you? They go and get themselves killed in a car crash (drunk, I expect) -"

"They didn't die in a car crash!" said Harry, who found himself on his feet.

"They died in a car crash, you nasty little liar, and left you to be a burden on their decent, hardworking relatives!" screamed Aunt Marge, swelling with fury. "You are an insolent, ungrateful little --"

But Aunt Marge suddenly stopped speaking. For a moment, it looked as though words had failed her. She seemed to be swelling with inexpressible anger - but the swelling didn't stop. Her great red face started to expand, her tiny eyes bulged, and her mouth stretched too tightly for speech - next second, several buttons had just burst from her tweed jacket and pinged off the walls - she was inflating like a monstrous balloon, her stomach bursting free of her tweed waistband, each of her fingers blowing up like a salami --

"MARGE!" yelled Uncle Vernon and Aunt Petunia together as Aunt Marge's whole body began to rise off her chair toward the ceiling. She was entirely round, now, like a vast life buoy with piggy eyes, and her hands and feet stuck out weirdly as she drifted up into the air, making apoplectic popping noises. Ripper came skidding into the room, barking madly.

"NOOOOOOO!"

Uncle Vernon seized one of Marge's feet and tried to pull her down again, but was almost lifted from the floor himself. A second later, Ripper leapt forward and sank his teeth into Uncle Vernon's leg.

Harry tore from the dining room before anyone could stop him, heading for the cupboard under the stairs. The cupboard door burst magically open as he reached it. In seconds, he had heaved his trunk to the front door. He sprinted upstairs and threw himself under the bed, wrenching up the loose floorboard, and grabbed the pillowcase full of his books and birthday presents. He wriggled out, seized Hedwig's empty cage, and dashed back downstairs to his trunk, just as Uncle Vernon burst out of the dining room, his trouser leg in bloody tatters.

"COME BACK IN HERE!" he bellowed. "COME BACK AND PUT HER RIGHT!"

But a reckless rage had come over Harry. He kicked his trunk open, pulled out his wand, and pointed it at Uncle Vernon.

"She deserved it," Harry said, breathing very fast. "She deserved what she got. You keep away from me."

He fumbled behind him for the latch on the door.

"I'm going," Harry said. "I've had enough."

And in the next moment, he was out in the dark, quiet street, heaving his heavy trunk behind him, Hedwig's cage under his arm.""".lower(), d, l) + poidPhrase("""Chapter One: Tuesday, March 20

He turned onto the boardwalk and felt the full impact of the stinging blast from the ocean. Observing the shifting clouds, he decided it wouldn't be surprising if they had a snow flurry later on, even though tomorrow was the first day of spring. It had been a long winter, and everyone said how much they were looking forward to the warm weather ahead. He wasn't.

He enjoyed Spring Lake best once late autumn set in. By then the summer people had closed their houses, not appearing even for weekends.

He was chagrined, though, that with each passing year more and more people were selling their winter homes and settling here permanently. They had decided it was worth the seventy-mile commute into New York so that they could begin and end the day in this quietly beautiful New Jersey seaside community.

Spring Lake, with its Victorian houses that appeared unchanged from the way they had been in the 1890s, was worth the inconvenience of the trip, they explained.

Spring Lake, with the fresh, bracing scent of the ocean always present, revived the soul, they agreed.

Spring Lake, with its two-mile boardwalk, where one could revel in the silvery magnificence of the Atlantic, was a treasure, they pointed out.

All of these people shared so much -- the summer visitors, the permanent dwellers -- but none of them shared his secrets. He could stroll down Hayes Avenue and visualize Madeline Shapley as she had been in late afternoon on September 7, 1891, seated on the wicker sofa on the wraparound porch of her home, her wide-brimmed bonnet beside her. She had been nineteen years old then, brown-eyed, with dark brown hair, sedately beautiful in her starched white linen dress.

Only he knew why she had had to die an hour later.

St. Hilda Avenue, shaded with heavy oaks that had been mere saplings on August 5, 1893, when eighteen-year-old Letitia Gregg had failed to return home, brought other visions. She had been so frightened. Unlike Madeline, who had fought for her life, Letitia had begged for mercy.

The last one of the trio had been Ellen Swain, small and quiet, but far too inquisitive, far too anxious to document the last hours of Letitia's life.

And because of her curiosity, on March 31, 1896, she had followed her friend to the grave.

He knew every detail, every nuance of what had happened to her and to the others.

He had found the diary during one of those cold, rainy spells that sometimes occur in summer. Bored, he'd wandered into the old carriage house, which served as a garage.

He climbed the rickety steps to the stuffy, dusty loft, and for lack of something better to do, began rummaging through the boxes he found there.

The first one was filled with utterly useless odds and ends: rusty old lamps; faded, outdated clothing; pots and pans and a scrub board; chipped vanity sets, the glass on the mirrors cracked or blurred. They all were the sorts of items one shoves out of sight with the intention of fixing or giving away, and then forgets altogether.

Another box held thick albums, the pages crumbling, filled with pictures of stiffly posed, stern-faced people refusing to share their emotions with the camera.

A third contained books, dusty, swollen from humidity, the type faded. He'd always been a reader, but even though only fourteen at the time, he could glance through these titles and dismiss them. No hidden masterpieces in the lot.

A dozen more boxes proved to be filled with equally worthless junk.

In the process of throwing everything back into the boxes, he came across a rotted leather binder that had been hidden in what looked like another photo album. He opened it and found it stuffed with pages, every one of them covered with writing.

The first entry was dated, September 7, 1891. It began with the words "Madeline is dead by my hand."

He had taken the diary and told no one about it. Over the years, he'd read from it almost daily, until it became an integral part of his own memory. Along the way, he realized he had become one with the author, sharing his sense of supremacy over his victims, chuckling at his playacting as he grieved with the grieving.

What began as a fascination gradually grew to an absolute obsession, a need to relive the diary writer's journey of death on his own. Vicarious sharing was no longer enough.

Four and a half years ago he had taken the first life.

It was twenty-one-year-old Martha's fate that she had been present at the annual end-of-summer party her grandparents gave. The Lawrences were a prominent, long-established Spring Lake family. He was at the festive gathering and met her there. The next day, September 7th, she left for an early morning jog on the boardwalk. She never returned home.

Now, over four years later, the investigation into her disappearance was still ongoing. At a recent gathering, the prosecutor of Monmouth County had vowed there would be no diminution in the effort to learn the truth about what had happened to Martha Lawrence. Listening to the empty vows, he chuckled at the thought.

How he enjoyed participating in the somber discussions about Martha that came up from time to time over the dinner table.

I could tell you all about it, every detail, he said to himself, and I could tell you about Carla Harper too. Two years ago he had been strolling past the Warren Hotel and noticed her coming down the steps. Like Madeline, as described in the diary, she had been wearing a white dress, although hers was barely a slip, sleeveless, clinging, revealing every inch of her slender young body. He began following her.

When she disappeared three days later, everyone believed Carla had been accosted on the trip home to Philadelphia. Not even the prosecutor, so determined to solve the mystery of Martha's disappearance, suspected that Carla had never left Spring Lake.

Relishing the thought of his omniscience, he had lightheartedly joined the late afternoon strollers on the boardwalk and exchanged pleasantries with several good friends he met along the way, agreeing that winter was insisting on giving them one more blast on its way out.

But even as he bantered with them, he could feel the need stirring within him, the need to complete his trio of present-day victims. The final anniversary was coming up, and he had yet to choose her.

The word in town was that Emily Graham, the purchaser of the Shapley house, as it was still known, was a descendant of the original owners.

He had looked her up on the Internet. Thirty-two years old, divorced, a criminal defense attorney. She had come into money after she was given stock by the grateful owner of a fledgling wireless company whom she'd successfully defended pro bono. When the stock went public and she was able to sell it, she made a fortune.

He learned that Graham had been stalked by the son of a murder victim after she won an acquittal for the accused killer. The son, protesting his innocence, was now in a psychiatric facility. Interesting.

More interesting still, Emily bore a striking resemblance to the picture he'd seen of her great-great-grandaunt, Madeline Shapley. She had the same wide brown eyes and long, full eyelashes. The same midnight-brown hair with hints of auburn. The same lovely mouth. The same tall, slender body.

There were differences, of course. Madeline had been innocent, trusting, unworldly, a romantic. Emily Graham was obviously a sophisticated and smart woman. She would be more of a challenge than the others, but then again, that made her so much more interesting. Maybe she was the one destined to complete his special trio?

Emily gave a sigh of relief as she passed the sign indicating she was now in Spring Lake. "Made it!" she said aloud. "Hallelujah."

The drive from Albany had taken nearly eight hours. She had left in what was supposed to have been "periods of light to moderate snow," but which had turned into a near blizzard that only tapered off as she exited Rockland County. Along the way the number of fender benders on the New York State Thruway reminded her of the bumper cars she had loved as a child.

In a fairly clear stretch, she had picked up speed, but then witnessed a terrifying spinout. For a horrible moment it had seemed as though two vehicles were headed for a head-on collision. It was avoided only because the driver of one car had somehow managed to regain control and turn right with less than a nanosecond to spare.

Kind of reminds me of my life the last couple of years, she had thought as she slowed down -- constantly in the fast lane, and sometimes almost getting clobbered. I needed a change of direction and a change of pace.

As her grandmother had put it, "Emily, you take that job in New York. I'll feel a lot more secure about you when you're living a couple of hundred miles away. A nasty ex-husband and a stalker at one time are a little too much on your plate for my taste."

And then, being Gran, she continued, "On the bright side, you never should have married Gary White. The fact that three years after you're divorced he'd have the gall to try to sue you because you have money now only proves what I always thought about him."

Remembering her grandmother's words, Emily smiled involuntarily as she drove slowly through the darkened streets. She glanced at the gauge on the dashboard. The outside temperature was a chilly thirty-eight degrees. The streets were wet -- here the storm had produced only rain -- and the windshield was becoming misted. The movement of the tree branches indicated sharp gusts of wind coming in from the ocean.

But the houses, the majority of them restored Victorians, looked secure and serene. As of tomorrow I'll officially own a home here, Emily mused. March 21st. The equinox. Light and night equally divided. The world in balance.

It was a comforting thought. She had experienced enough turbulence of late to both want and need a period of complete and total peace. She'd had stunning good luck, but also frightening problems that had crashed like meteors into each other. But as the old saying went, everything that rises must converge, and God only knows she was living proof of that.

She considered, then rejected, the impulse to drive by the house. There was still something unreal about the knowledge that in only a matter of hours, it would be hers. Even before she saw the house for the first time three months ago, it had been a vivid presence in her childhood imaginings -- half real, half blended with fairy tales. Then, when she stepped into it that first time, she had known immediately that for her the place held a feeling of coming home. The real estate agent had mentioned that it was still called the Shapley house.

Enough driving for now, she decided. It's been a long, long day. Concord Reliable Movers in Albany were supposed to have arrived at eight. Most of the furniture she wanted to keep was already in her new Manhattan apartment, but when her grandmother downsized she had given her some fine antique pieces, so there was still a lot to move.

"First pickup, guaranteed," the Concord scheduler had vehemently promised. "Count on me."

The van had not made its appearance until noon. As a result she got a much later start than she'd expected, and it was now almost ten-thirty.

Check into the inn, she decided. A hot shower, she thought longingly. Watch the eleven o'clock news. Then, as Samuel Pepys wrote, "And so to bed."

When she'd first come to Spring Lake, and impulsively put a deposit down on the house, she had stayed at the Candlelight Inn for a few days, to be absolutely sure she'd made the right decision. She and the inn's owner, Carrie Roberts, a septuagenarian, had immediately hit it off. On the drive down today, she'd phoned to say she'd be late, but Carrie had assured her that was no problem.

Turn right on Ocean Avenue, then four more blocks. A few moments later, with a grateful sigh, Emily turned off the ignition and reached in the backseat for the one suitcase she'd need overnight.

Carrie's greeting was warm and brief. "You look exhausted, Emily. The bed's turned down. You said you'd stopped for dinner, so there's a thermos of hot cocoa with a couple of biscuits on the night table. I'll see you in the morning."

The hot shower. A nightshirt and her favorite old bathrobe. Sipping the cocoa, Emily watched the news and felt the stiffness in her muscles from the long drive begin to fade.

As she snapped off the television, her cell phone rang. Guessing who it was, she picked it up.

"Hi, Emily."

She smiled as she heard the worried-sounding voice of Eric Bailey, the shy genius who was the reason she was in Spring Lake now.

As she reassured him that she'd had a safe, relatively easy trip, she thought of the day she first met him, when he moved into the closet-sized office next to hers. The same age, their birthdays only a week apart, they'd become friendly, and she recognized that underneath his meek, little-boy-lost exterior, Eric had been gifted with massive intelligence.

One day, when she realized how depressed he seemed, she'd made him tell her the reason. It turned out that his fledgling dot-com company was being sued by a major software provider who knew he could not afford an expensive lawsuit.

She took the case without asking for a fee, expecting it to be a pro bono situation, and joked to herself that she would be papering the walls with the stock certificates Eric promised her.

But she won the case for him. He made a public offering of the stock, which immediately rose in value. When her shares were worth ten million dollars, she sold them.

Now Eric's name was on a handsome new office building. He loved the races and bought a lovely old home in Saratoga from which he commuted to Albany. Their friendship had continued, and he'd been a rock during the time she was being stalked. He even had a high-tech camera installed at her townhouse. The camera had caught the stalker on tape.

"Just wanted to see that you made it okay. Hope I didn't wake you up?"

They chatted for a few minutes and promised to talk again soon. When she put the cell phone down, Emily went to the window and opened it slightly. A rush of cold, salty air made her gasp, but then she deliberately inhaled slowly. It's crazy, she thought, but at this moment it seems to me that all my life I've been missing the smell of the ocean.

She turned and walked to the door to be absolutely sure it was double locked. Stop doing that, she snapped at herself. You already checked before you showered.

But in the year before the stalker was caught, despite her efforts to convince herself that if the stalker wanted to hurt her he could have done so on many occasions, she had begun to feel fearful and apprehensive.

Carrie had told her that she was the only guest at the inn. "I'm booked full over the weekend," she'd said. "All six bedrooms. There's a wedding reception at the country club on Saturday. And after Memorial Day, forget it. I don't have a closet available."

The minute I heard that only the two of us were here, I started wondering if all the outside doors were locked and if the alarm was on, Emily thought, once again angry that she could not control her anxiety.

She slipped out of her bathrobe. Don't think about it now, she warned herself.

But her hands were suddenly clammy as she remembered the first time she had come home and realized he'd been there. She had found a picture of herself propped up against the lamp on her bedside table, a photograph showing her standing in the kitchen in her nightgown, a cup of coffee in her hand. She had never seen the picture before. That day she'd had the locks of the townhouse changed and a blind put on the window over the sink.

After that there'd been a number of other incidents involving photographs, pictures taken of her at home, on the street, in the office. Sometimes a silky-voiced predator would call to comment on what she was wearing. "You looked cute jogging this morning, Emily..." "With that dark hair, I didn't think I'd like you in black. But I do...." "I love those red shorts. Your legs are really good..."

And then a picture would turn up of her wearing the described outfit. It would be in her mailbox at home, or stuck on the windshield of her car, or folded inside the morning newspaper that had been delivered to her doorstep.

The police had traced the telephone calls, but all had been made from different pay phones. Attempts to lift fingerprints from the items that she had received had been unsuccessful.

For over a year the police had been unable to apprehend the stalker. "You've gotten some people acquitted who were accused of vicious crimes, Miss Graham," Marty Browski, the senior detective, told her. "It could be someone in a victim's family. It could be someone who saw you in a restaurant and followed you home. It could be someone who knows you came into a lot of money and got fixated on you."

And then they'd found Ned Koehler, the son of a woman whose accused killer she had successfully defended, lurking outside her townhouse. He's off the streets now, Emily reassured herself. There's no need to worry about him anymore. He'll get the care he needs.

He was in a secure psychiatric facility in upstate New York, and this was Spring Lake, not Albany. Out of sight, out of mind, Emily thought, prayerfully. She got into bed, pulled up the covers, and reached for the light switch.

Across Ocean Avenue, standing on the beach in the shadows of the deserted boardwalk, the wind from the ocean whipping his hair, a man watched as the room became dark.

"Sleep well, Emily," he whispered, his voice gentle.""".lower(), d, l) + poidPhrase("""Chapter 1

On a very hot day in August of 1994, my wife told me she was going down to the Derry Rite Aid to pick up a refill on her sinus medicine prescription -- this is stuff you can buy over the counter these days, I believe. I'd finished my writing for the day and offered to pick it up for her. She said thanks, but she wanted to get a piece of fish at the supermarket next door anyway; two birds with one stone and all of that. She blew a kiss at me off the palm of her hand and went out. The next time I saw her, she was on TV. That's how you identify the dead here in Derry -- no walking down a subterranean corridor with green tiles on the walls and long fluorescent bars overhead, no naked body rolling out of a chilly drawer on casters; you just go into an office marked PRIVATE and look at a TV screen and say yep or nope.

The Rite Aid and the Shopwell are less than a mile from our house, in a little neighborhood strip mall which also supports a video store, a used-book store named Spread It Around (they do a very brisk business in my old paperbacks), a Radio Shack, and a Fast Foto. It's on Up-Mile Hill, at the intersection of Witcham and Jackson.

She parked in front of Blockbuster Video, went into the drugstore, and did business with Mr. Joe Wyzer, who was the druggist in those days; he has since moved on to the Rite Aid in Bangor. At the checkout she picked up one of those little chocolates with marshmallow inside, this one in the shape of a mouse. I found it later, in her purse. I unwrapped it and ate it myself, sitting at the kitchen table with the contents of her red handbag spread out in front of me, and it was like taking Communion. When it was gone except for the taste of chocolate on my tongue and in my throat, I burst into tears. I sat there in the litter of her Kleenex and makeup and keys and half-finished rolls of Certs and cried with my hands over my eyes, the way a kid cries.

The sinus inhaler was in a Rite Aid bag. It had cost twelve dollars and eighteen cents. There was something else in the bag, too -- an item which had cost twenty-two-fifty. I looked at this other item for a long time, seeing it but not understanding it. I was surprised, maybe even stunned, but the idea that Johanna Arlen Noonan might have been leading another life, one I knew nothing about, never crossed my mind. Not then.

Jo left the register, walked out into the bright, hammering sun again, swapping her regular glasses for her prescription sunglasses as she did, and just as she stepped from beneath the drugstore's slight overhang (I am imagining a little here, I suppose, crossing over into the country of the novelist a little, but not by much; only by inches, and you can trust me on that), there was that shrewish howl of locked tires on pavement that means there's going to be either an accident or a very close call.

This time it happened -- the sort of accident which happened at that stupid X-shaped intersection at least once a week, it seemed. A 1989 Toyota was pulling out of the shopping-center parking lot and turning left onto Jackson Street. Behind the wheel was Mrs. Esther Easterling of Barrett's Orchards. She was accompanied by her friend Mrs. Irene Deorsey, also of Barrett's Orchards, who had shopped the video store without finding anything she wanted to rent. Too much violence, Irene said. Both women were cigarette widows.

Esther could hardly have missed the orange Public Works dump truck coming down the hill; although she denied this to the police, to the newspaper, and to me when I talked to her some two months later, I think it likely that she just forgot to look. As my own mother (another cigarette widow) used to say, "The two most common ailments of the elderly are arthritis and forgetfulness. They can be held responsible for neither."

Driving the Public Works truck was William Fraker, of Old Cape. Mr. Fraker was thirty-eight years old on the day of my wife's death, driving with his shirt off and thinking how badly he wanted a cool shower and a cold beer, not necessarily in that order. He and three other men had spent eight hours putting down asphalt patch out on the Harris Avenue Extension near the airport, a hot job on a hot day, and Bill Fraker said yeah, he might have been going a little too fast -- maybe forty in a thirty-mile-an-hour zone. He was eager to get back to the garage, sign off on the truck, and get behind the wheel of his own F-150, which had air conditioning. Also, the dump truck's brakes, while good enough to pass inspection, were a long way from tip-top condition. Fraker hit them as soon as he saw the Toyota pull out in front of him (he hit his horn, as well), but it was too late. He heard screaming tires -- his own, and Esther's as she belatedly realized her danger -- and saw her face for just a moment.

"That was the worst part, somehow," he told me as we sat on his porch, drinking beers -- it was October by then, and although the sun was warm on our faces, we were both wearing sweaters. "You know how high up you sit in one of those dump trucks?"

I nodded.

"Well, she was looking up to see me -- craning up, you'd say -- and the sun was full in her face. I could see how old she was. I remember thinking, 'Holy shit, she's gonna break like glass if I can't stop.' But old people are tough, more often than not. They can surprise you. I mean, look at how it turned out, both those old biddies still alive, and your wife..."

He stopped then, bright red color dashing into his cheeks, making him look like a boy who has been laughed at in the schoolyard by girls who have noticed his fly is unzipped. It was comical, but if I'd smiled, it only would have confused him.

"Mr. Noonan, I'm sorry. My mouth just sort of ran away with me."

"It's all right," I told him. "I'm over the worst of it, anyway." That was a lie, but it put us back on track.

"Anyway," he said, "we hit. There was a loud bang, and a crumping sound when the driver's side of the car caved in. Breaking glass, too. I was thrown against the wheel hard enough so I couldn't draw a breath without it hurting for a week or more, and I had a big bruise right here." He drew an arc on his chest just below the collarbones. "I banged my head on the windshield hard enough to crack the glass, but all I got up there was a little purple knob...no bleeding, not even a headache. My wife says I've just got a naturally thick skull. I saw the woman driving the Toyota, Mrs. Easterling, thrown across the console between the front bucket seats. Then we were finally stopped, all tangled together in the middle of the street, and I got out to see how bad they were. I tell you, I expected to find them both dead."

Neither of them was dead, neither of them was even unconscious, although Mrs. Easterling had three broken ribs and a dislocated hip. Mrs. Deorsey, who had been a seat away from the impact, suffered a concussion when she rapped her head on her window. That was all; she was "treated and released at Home Hospital," as the Derry News always puts it in such cases.

My wife, the former Johanna Arlen of Malden, Massachusetts, saw it all from where she stood outside the drugstore, with her purse slung over her shoulder and her prescription bag in one hand. Like Bill Fraker, she must have thought the occupants of the Toyota were either dead or seriously hurt. The sound of the collision had been a hollow, authoritative bang which rolled through the hot afternoon air like a bowling ball down an alley. The sound of breaking glass edged it like jagged lace. The two vehicles were tangled violently together in the middle of Jackson Street, the dirty orange truck looming over the pale-blue import like a bullying parent over a cowering child.

Johanna began to sprint across the parking lot toward the street. Others were doing the same all around her. One of them, Miss Jill Dunbarry, had been window-shopping at Radio Shack when the accident occurred. She said she thought she remembered running past Johanna -- at least she was pretty sure she remembered someone in yellow slacks -- but she couldn't be sure. By then, Mrs. Easterling was screaming that she was hurt, they were both hurt, wouldn't somebody help her and her friend Irene.

Halfway across the parking lot, near a little cluster of newspaper dispensers, my wife fell down. Her purse-strap stayed over her shoulder, but her prescription bag slipped from her hand, and the sinus inhaler slid halfway out. The other item stayed put.

No one noticed her lying there by the newspaper dispensers; everyone was focused on the tangled vehicles, the screaming women, the spreading puddle of water and antifreeze from the Public Works truck's ruptured radiator. ("That's gas!" the clerk from Fast Foto shouted to anyone who would listen. "That's gas, watch out she don't blow, fellas!") I suppose one or two of the would-be rescuers might have jumped right over her, perhaps thinking she had fainted. To assume such a thing on a day when the temperature was pushing ninety-five degrees would not have been unreasonable.

Roughly two dozen people from the shopping center clustered around the accident; another four dozen or so came running over from Strawford Park, where a baseball game had been going on. I imagine that all the things you would expect to hear in such situations were said, many of them more than once. Milling around. Someone reaching through the misshapen hole which had been the driver's-side window to pat Esther's trembling old hand. People immediately giving way for Joe Wyzer; at such moments anyone in a white coat automatically becomes the belle of the ball. In the distance, the warble of an ambulance siren rising like shaky air over an incinerator.

All during this, lying unnoticed in the parking lot, was my wife with her purse still over her shoulder (inside, still wrapped in foil, her uneaten chocolate-marshmallow mouse) and her white prescription bag near one outstretched hand. It was Joe Wyzer, hurrying back to the pharmacy to get a compress for Irene Deorsey's head, who spotted her. He recognized her even though she was lying face-down. He recognized her by her red hair, white blouse, and yellow slacks. He recognized her because he had waited on her not fifteen minutes before.

"Mrs. Noonan?" he asked, forgetting all about the compress for the dazed but apparently not too badly hurt Irene Deorsey. "Mrs. Noonan, are you all right?" Knowing already (or so I suspect; perhaps I am wrong) that she was not.

He turned her over. It took both hands to do it, and even then he had to work hard, kneeling and pushing and lifting there in the parking lot with the heat baking down from above and then bouncing back up from the asphalt. Dead people put on weight, it seems to me; both in their flesh and in our minds, they put on weight.

There were red marks on her face. When I identified her I could see them clearly even on the video monitor. I started to ask the assistant medical examiner what they were, but then I knew. Late August, hot pavement, elementary, my dear Watson. My wife died getting a sunburn.

Wyzer got up, saw that the ambulance had arrived, and ran toward it. He pushed his way through the crowd and grabbed one of the attendants as he got out from behind the wheel. "There's a woman over there," Wyzer said, pointing toward the parking lot.

"Guy, we've got two women right here, and a man as well," the attendant said. He tried to pull away, but Wyzer held on.

"Never mind them right now," he said. "They're basically okay. The woman over there isn't."

The woman over there was dead, and I'm pretty sure Joe Wyzer knew it...but he had his priorities straight. Give him that. And he was convincing enough to get both paramedics moving away from the tangle of truck and Toyota, in spite of Esther Easterling's cries of pain and the rumbles of protest from the Greek chorus.

When they got to my wife, one of the paramedics was quick to confirm what Joe Wyzer had already suspected. "Holy shit," the other one said. "What happened to her?"

"Heart, most likely," the first one said. "She got excited and it just blew out on her."

But it wasn't her heart. The autopsy revealed a brain aneurysm which she might have been living with, all unknown, for as long as five years. As she sprinted across the parking lot toward the accident, that weak vessel in her cerebral cortex had blown like a tire, drowning her control-centers in blood and killing her. Death had probably not been instantaneous, the assistant medical examiner told me, but it had still come swiftly enough...and she wouldn't have suffered. Just one big black nova, all sensation and thought gone even before she hit the pavement.

"Can I help you in any way, Mr. Noonan?" the assistant ME asked, turning me gently away from the still face and closed eyes on the video monitor. "Do you have questions? I'll answer them if I can."

"Just one," I said. I told him what she'd purchased in the drugstore just before she died. Then I asked my question.

The days leading up to the funeral and the funeral itself are dreamlike in my memory -- the clearest memory I have is of eating Jo's chocolate mouse and crying...crying mostly, I think, because I knew how soon the taste of it would be gone. I had one other crying fit a few days after we buried her, and I will tell you about that one shortly.

I was glad for the arrival of Jo's family, and particularly for the arrival of her oldest brother, Frank. It was Frank Arlen -- fifty, red-cheeked, portly, and with a head of lush dark hair -- who organized the arrangements...who wound up actually dickering with the funeral director.

"I can't believe you did that," I said later, as we sat in a booth at Jack's Pub, drinking beers.

"He was trying to stick it to you, Mikey," he said. "I hate guys like that." He reached into his back pocket, brought out a handkerchief, and wiped absently at his cheeks with it. He hadn't broken down -- none of the Arlens broke down, at least not when I was with them -- but Frank had leaked steadily all day; he looked like a man suffering from severe conjunctivitis.

There had been six Arlen sibs in all, Jo the youngest and the only girl. She had been the pet of her big brothers. I suspect that if I'd had anything to do with her death, the five of them would have torn me apart with their bare hands. As it was, they formed a protective shield around me instead, and that was good. I suppose I might have muddled through without them, but I don't know how. I was thirty-six, remember. You don't expect to have to bury your wife when you're thirty-six and she herself is two years younger. Death was the last thing on our minds.

"If a guy gets caught taking your stereo out of your car, they call it theft and put him in jail," Frank said. The Arlens had come from Massachusetts, and I could still hear Malden in Frank's voice -- caught was coowat, car was cah, call was caul. "If the same guy is trying to sell a grieving husband a three-thousand-dollar casket for forty-five hundred dollars, they call it business and ask him to speak at the Rotary Club luncheon. Greedy asshole, I fed him his lunch, didn't I?"

"Yes. You did."

"You okay, Mikey?"

"I'm okay."

"Sincerely okay?"

"How the fuck should I know?" I asked him, loud enough to turn some heads in a nearby booth. And then: "She was pregnant."

His face grew very still. "What?"

I struggled to keep my voice down. "Pregnant. Six or seven weeks, according to the...you know, the autopsy. Did you know? Did she tell you?"

"No! Christ, no!" But there was a funny look on his face, as if she had told him something. "I knew you were trying, of course...she said you had a low sperm count and it might take a little while, but the doctor thought you guys'd probably...sooner or later you'd probably..." He trailed off, looking down at his hands. "They can tell that, huh? They check for that?"

"They can tell. As for checking, I don't know if they do it automatically or not. I asked."

"Why?"

"She didn't just buy sinus medicine before she died. She also bought one of those home pregnancy-testing kits."

"You had no idea? No clue?"

I shook my head.

He reached across the table and squeezed my shoulder. "She wanted to be sure, that's all. You know that, don't you?"

A refill on my sinus medicine and a piece of fish, she'd said. Looking like always. A woman off to run a couple of errands. We had been trying to have a kid for eight years, but she had looked just like always.

"Sure," I said, patting Frank's hand. "Sure, big guy. I know."

It was the Arlens -- led by Frank -- who handled Johanna's sendoff. As the writer of the family, I was assigned the obituary. My brother came up from Virginia with my mom and my aunt and was allowed to tend the guest-book at the viewings. My mother -- almost completely ga-ga at the age of sixty-six, although the doctors refused to call it Alzheimer's -- lived in Memphis with her sister, two years younger and only slightly less wonky. They were in charge of cutting the cake and the pies at the funeral reception.

Everything else was arranged by the Arlens, from the viewing hours to the components of the funeral ceremony. Frank and Victor, the second-youngest brother, spoke brief tributes. Jo's dad offered a prayer for his daughter's soul. And at the end, Pete Breedlove, the boy who cut our grass in the summer and raked our yard in the fall, brought everyone to tears by singing "Blessed Assurance," which Frank said had been Jo's favorite hymn as a girl. How Frank found Pete and persuaded him to sing at the funeral is something I never found out.

We got through it -- the afternoon and evening viewings on Tuesday, the funeral service on Wednesday morning, then the little pray-over at Fairlawn Cemetery. What I remember most was thinking how hot it was, how lost I felt without having Jo to talk to, and that I wished I had bought a new pair of shoes. Jo would have pestered me to death about the ones I was wearing, if she had been there.

Later on I talked to my brother, Sid, told him we had to do something about our mother and Aunt Francine before the two of them disappeared completely into the Twilight Zone. They were too young for a nursing home; what did Sid advise?

He advised something, but I'll be damned if I know what it was. I agreed to it, I remember that, but not what it was. Later that day, Siddy, our mom, and our aunt climbed back into Siddy's rental car for the drive to Boston, where they would spend the night and then grab the Southern Crescent the following day. My brother is happy enough to chaperone the old folks, but he doesn't fly, even if the tickets are on me. He claims there are no breakdown lanes in the sky if the engine quits.

Most of the Arlens left the next day. Once more it was dog-hot, the sun glaring out of a white-haze sky and lying on everything like melted brass. They stood in front of our house -- which had become solely my house by then -- with three taxis lined up at the curb behind them, big galoots hugging one another amid the litter of tote-bags and saying their goodbyes in those foggy Massachusetts accents.

Frank stayed another day. We picked a big bunch of flowers behind the house -- not those ghastly-smelling hothouse things whose aroma I always associate with death and organ-music but real flowers, the kind Jo liked best -- and stuck them in a couple of coffee cans I found in the back pantry. We went out to Fairlawn and put them on the new grave. Then we just sat there for awhile under the beating sun.

"She was always just the sweetest thing in my life," Frank said at last in a strange, muffled voice. "We took care of Jo when we were kids. Us guys. No one messed with Jo, I'll tell you. Anyone tried, we'd feed em their lunch."

"She told me a lot of stories."

"Good ones?"

"Yeah, real good."

"I'm going to miss her so much."

"Me, too," I said. "Frank...listen...I know you were her favorite brother. She never called you, maybe just to say that she missed a period or was feeling whoopsy in the morning? You can tell me. I won't be pissed."

"But she didn't. Honest to God. Was she whoopsy in the morning?"

"Not that I saw." And that was just it. I hadn't seen anything. Of course I'd been writing, and when I write I pretty much trance out. But she knew where I went in those trances. She could have found me and shaken me fully awake. Why hadn't she? Why would she hide good news? Not wanting to tell me until she was sure was plausible...but it somehow wasn't Jo.

"Was it a boy or a girl?" he asked.

"A girl."

We'd had names picked out and waiting for most of our marriage. A boy would have been Andrew. Our daughter would have been Kia. Kia Jane Noonan.

Frank, divorced six years and on his own, had been staying with me. On our way back to the house he said, "I worry about you, Mikey. You haven't got much family to fall back on at a time like this, and what you do have is far away."

"I'll be all right," I said.

He nodded. "That's what we say, anyway, isn't it?"

"We?"

"Guys. 'I'll be all right.' And if we're not, we try to make sure no one knows it." He looked at me, eyes still leaking, handkerchief in one big sunburned hand. "If you're not all right, Mikey, and you don't want to call your brother -- I saw the way you looked at him -- let me be your brother. For Jo's sake if not your own."

"Okay," I said, respecting and appreciating the offer, also knowing I would do no such thing. I don't call people for help. It's not because of the way I was raised, at least I don't think so; it's the way I was made. Johanna once said that if I was drowning at Dark Score Lake, where we have a summer home, I would die silently fifty feet out from the public beach rather than yell for help. It's not a question of love or affection. I can give those and I can take them. I feel pain like anyone else. I need to touch and be touched. But if someone asks me, "Are you all right?" I can't answer no. I can't say help me.

A couple of hours later Frank left for the southern end of the state. When he opened the car door, I was touched to see that the taped book he was listening to was one of mine. He hugged me, then surprised me with a kiss on the mouth, a good hard smack. "If you need to talk, call," he said. "And if you need to be with someone, just come."

I nodded.

"And be careful."

That startled me. The combination of heat and grief had made me feel as if I had been living in a dream for the last few days, but that got through.

"Careful of what?"

"I don't know," he said. "I don't know, Mikey." Then he got into his car -- he was so big and it was so little that he looked as if he were wearing it -- and drove away. The sun was going down by then. Do you know how the sun looks at the end of a hot day in August, all orange and somehow squashed, as if an invisible hand were pushing down on the top of it and at any moment it might just pop like an overfilled mosquito and splatter all over the horizon? It was like that. In the east, where it was already dark, thunder was rumbling. But there was no rain that night, only a dark that came down as thick and stifling as a blanket. All the same, I slipped in front of the word processor and wrote for an hour or so. It went pretty well, as I remember. And you know, even when it doesn't, it passes the time.

My second crying fit came three or four days after the funeral. That sense of being in a dream persisted -- I walked, I talked, I answered the phone, I worked on my book, which had been about eighty per cent complete when Jo died -- but all the time there was this clear sense of disconnection, a feeling that everything was going on at a distance from the real me, that I was more or less phoning it in.

Denise Breedlove, Pete's mother, called and asked if I wouldn't like her to bring a couple of her friends over one day the following week and give the big old Edwardian pile I now lived in alone -- rolling around in it like the last pea in a restaurant-sized can -- a good stem-to-stern cleaning. They would do it, she said, for a hundred dollars split even among the three of them, and mostly because it wasn't good for me to go on without it. There had to be a scrubbing after a death, she said, even if the death didn't happen in the house itself.

I told her it was a fine idea, but I would pay her and the women she brought a hundred dollars each for six hours' work. At the end of the six hours, I wanted the job done. And if it wasn't, I told her, it would be done, anyway.

"Mr. Noonan, that's far too much," she said.

"Maybe and maybe not, but it's what I'm paying," I said. "Will you do it?"

She said she would, of course she would.

Perhaps predictably, I found myself going through the house on the evening before they came, doing a pre-cleaning inspection. I guess I didn't want the women (two of whom would be complete strangers to me) finding anything that would embarrass them or me: a pair of Johanna's silk panties stuffed down behind the sofa cushions, perhaps ("We are often overcome on the sofa, Michael," she said to me once, "have you noticed?"), or beer cans under the loveseat on the sunporch, maybe even an unflushed toilet. In truth, I can't tell you any one thing I was looking for; that sense of operating in a dream still held firm control over my mind. The clearest thoughts I had during those days were either about the end of the novel I was writing (the psychotic killer had lured my heroine to a high-rise building and meant to push her off the roof) or about the Norco Home Pregnancy Test Jo had bought on the day she died. Sinus prescription, she had said. Piece of fish for supper, she had said. And her eyes had shown me nothing else I needed to look at twice.

Near the end of my "pre-cleaning," I looked under our bed and saw an open paperback on Jo's side. She hadn't been dead long, but few household lands are so dusty as the Kingdom of Underbed, and the lightgray coating I saw on the book when I brought it out made me think of Johanna's face and hands in her coffin -- Jo in the Kingdom of Underground. Did it get dusty inside a coffin? Surely not, but --

I pushed the thought away. It pretended to go, but all day long it kept creeping back, like Tolstoy's white bear.

Johanna and I had both been English majors at the University of Maine, and like many others, I reckon, we fell in love to the sound of Shakespeare and the Tilbury Town cynicism of Edwin Arlington Robinson. Yet the writer who had bound us closest together was no college-friendly poet or essayist but W. Somerset Maugham, that elderly globetrotting novelist-playwright with the reptile's face (always obscured by cigarette smoke in his photographs, it seems) and the romantic's heart. So it did not surprise me much to find that the book under the bed was The Moon and Sixpence. I had read it myself as a late teenager, not once but twice, identifying passionately with the character of Charles Strickland. (It was writing I wanted to do in the South Seas, of course, not painting.)

She had been using a playing card from some defunct deck as her place-marker, and as I opened the book, I thought of something she had said when I was first getting to know her. In Twentieth-Century British Lit, this had been, probably in 1980. Johanna Arlen had been a fiery little sophomore. I was a senior, picking up the Twentieth-Century Brits simply because I had time on my hands that last semester. "A hundred years from now," she had said, "the shame of the mid-twentieth-century literary critics will be that they embraced Lawrence and ignored Maugham." This was greeted with contemptuously good-natured laughter (they all knew Women in Love was one of the greatest damn books ever written), but I didn't laugh. I fell in love.

The playing card marked pages 102 and 103 -- Dirk Stroeve has just discovered that his wife has left him for Strickland, Maugham's version of Paul Gauguin. The narrator tries to buck Stroeve up. My dear fellow, don't be unhappy. She'll come back...

"Easy for you to say," I murmured to the room which now belonged just to me.

I turned the page and read this: Strickland's injurious calm robbed Stroeve of his self-control. Blind rage seized him, and without knowing what he was doing he flung himself on Strickland. Strickland was taken by surprise and he staggered, but he was very strong, even after his illness, and in a moment, he did not exactly know how, Stroeve found himself on the floor.

"You funny little man, " said Strickland.

It occurred to me that Jo was never going to turn the page and hear Strickland call the pathetic Stroeve a funny little man. In a moment of brilliant epiphany I have never forgotten -- how could I? it was one of the worst moments of my life -- I understood it wasn't a mistake that would be rectified, or a dream from which I would awaken. Johanna was dead.

My strength was robbed by grief. If the bed hadn't been there, I would have fallen to the floor. We weep from our eyes, it's all we can do, but on that evening I felt as if every pore of my body were weeping, every crack and cranny. I sat there on her side of the bed, with her dusty paperback copy of The Moon and Sixpence in my hand, and I wailed. I think it was surprise as much as pain; in spite of the corpse I had seen and identified on a high-resolution video monitor, in spite of the funeral and Pete Breedlove singing "Blessed Assurance" in his high, sweet tenor voice, in spite of the graveside service with its ashes to ashes and dust to dust, I hadn't really believed it. The Penguin paperback did for me what the big gray coffin had not: it insisted she was dead.

You funny little man, said Strickland.

I lay back on our bed, crossed my forearms over my face, and cried myself to sleep that way as children do when they're unhappy. I had an awful dream. In it I woke up, saw the paperback of The Moon and Sixpence still lying on the coverlet beside me, and decided to put it back under the bed where I had found it. You know how confused dreams are -- logic like Dalì clocks gone so soft they lie over the branches of trees like throw-rugs.

I put the playing-card bookmark back between pages 102 and 103 -- turn of the index finger away from You funny little man, said Strickland now and forever -- and rolled onto my side, hanging my head over the edge of the bed, meaning to put the book back exactly where I had found it.

Jo was lying there amid the dust-kitties. A strand of cobweb hung down from the bottom of the box spring and caressed her cheek like a feather. Her red hair looked dull, but her eyes were dark and alert and baleful in her white face. And when she spoke, I knew that death had driven her insane.

"Give me that," she hissed. "It's my dust-catcher." She snatched it out of my hand before I could offer it to her. For a moment our fingers touched, and hers were as cold as twigs after a frost. She opened the book to her place, the playing card fluttering out, and placed Somerset Maugham over her face -- a shroud of words. As she crossed her hands on her bosom and lay still, I realized she was wearing the blue dress I had buried her in. She had come out of her grave to hide under our bed.

I awoke with a muffled cry and a painful jerk that almost tumbled me off the side of the bed. I hadn't been asleep long -- the tears were still damp on my cheeks, and my eyelids had that funny stretched feel they get after a bout of weeping. The dream had been so vivid that I had to roll on my side, hang my head down, and peer under the bed, sure she would be there with the book over her face, that she would reach out with her cold fingers to touch me.

There was nothing there, of course -- dreams are just dreams. Nevertheless, I spent the rest of the night on the couch in my study. It was the right choice, I guess, because there were no more dreams that night. Only the nothingness of good sleep.""".lower(), d, l) + poidPhrase("""CHAPTER 1:
TOTALLY OBSESSED
 
The J Argon Clinic was not a state hospital. Nobody stayed there for free. Argon and his staff of psychologists only treated fairies who could afford it. Of all the clinic's wealthy patients, Opal Koboi was unique. She had set up an emergency fund for herself more than a year previously, just in case she ever went insane and needed to pay for treatment. It was a smart move. If Opal hadn't set up the fund, her family would undoubtedly have moved her to a cheaper facility. Not that the facility itself made much difference to Koboi, who had spent the past year drooling and having her reflexes tested. Doctor Argon doubted if Opal would have noticed a bull troll beating its chest before her.

The fund was not the only reason why Opal was unique. Koboi was the Argon Clinic's celebrity patient. Following the attempt of the B'wa Kell goblin triad to seize power, Opal Koboi's name had become the most infamous four syllables under the world. After all, the pixie billionairess had formed an alliance with disgruntled LEP officer Briar Cudgeon, and funded the triad's war on Haven. Koboi had betrayed her own kind, and now her own mind was betraying her.

For the first six months of Koboi's incarceration, the Clinic had been besieged by media filming the pixie's every twitch. The LEP guarded her cell door in shifts, every staff member in the facility was treated to background checks and stern glares. Nobody was exempt. Even Doctor Argon himself was subjected to random DNA swabs to ensure that he was who he said he was. The LEP  weren't taking any chances with Koboi. If she escaped from Argon's Clinic, not only would they be the laughing stock of the fairy world, but a highly dangerous criminal would be unleashed on Haven City.

But as time went by, fewer camera crews turned up at the gates each morning. After all, how many hours of drooling can an audience be expected to sit through? Gradually the LEP crews were downsized from a dozen to six and finally to a single officer per shift. Where could Opal Koboi go, the authorities reasoned? There were a dozen cameras focussed on her twenty four hours a day. There was a subcutaneous seeker-sleeper under the skin of her upper arm and she was DNA swabbed four times daily. And even if someone did get Opal out, what could they do with her? The pixie couldn't even stand without help, and the sensors said her brain waves were little more than flat lines.

That said, Doctor Argon was very proud of his prize patient, and mentioned her name often at dinner parties. Since Opal Koboi had been admitted to the clinic, it had become almost fashionable to have a relative in therapy. Almost every family on the rich list had a crazy uncle in the attic. Now that crazy uncle could receive the best of care in the lap of luxury.

If only every fairy in the facility was as docile as Opal Koboi. All she needed was a few intravenous tubes and a monitor, which had been more than paid for by her first six months' medical fees. Doctor Argon fervently hoped that little Opal never woke up. Because once she did, the LEP would haul her off to court. And when she had been convicted of treason her assets would be frozen, including the Clinic's fund. No, the longer Opal's nap lasted, the better for everyone, especially her. Because of their thin skulls and large brain volume, Pixie's were susceptible to various maladies such as catatonia, amnesia and narcolepsy. So it was quite possible that her coma would last for several years. And even if Opal did wake up, it was quite possible that her memory would stay locked up in some drawer in her huge pixie brain.

Doctor J Argon did his rounds every night. He didn't perform much hands-on therapy anymore, but he felt that it was good for the staff to feel his presence. If the other doctors knew that Jerbal Argon kept his finger on the pulse, then they were more likely to keep their own fingers on that pulse too.

Argon always saved Opal for last. It calmed him somehow to see the small pixie asleep in her harness. Often at the end of a stressful day, he even envied Opal her untroubled existence. When it had all become too much for the pixie, her brain had simply shut down, all except the most vital functions. She still breathed, and occasionally the monitors registered a dream spike in her brain- waves. But other than that, for all intents and purposes, Opal Koboi was no more.

On this fateful night, Jerbal Argon was feeling more stressed than usual. His wife was suing for divorce on the grounds that he hadn't said more than six consecutive words to her in over two years. The Council were threatening to pull his government grant because of all the money he was making from his new celebrity clients, and he had a pain in his hip which no amount of magic could seem to cure. The warlocks said it was probably all in his head. They seemed to think that was funny.
Argon limped down the Clinic's eastern wing, checking the plasma chart of each patient as he passed their room. He winced each time his left foot touched the floor.
The two janitor pixies, Mervall and Descant Brill were outside Opal's room, picking up dust with static brushes. Pixies made wonderful employees. They were methodical, patient and determined. When a pixie was instructed to do something, you could rest assured that thing would be done. Plus they were cute, with their baby faces and disproportionately large heads. Just looking at a pixie cheered most people up. They were walking therapy.

'Evening, boys,' said Argon. 'How's our favourite patient?'

Merv, the elder twin, glanced up from his brush. 'Same old, same old, Jerry,' he said. 'I thought she moved a toe earlier, but it was just a trick of the light.'

Argon laughed, but it was forced. He did not like to be called Jerry. It was his clinic after all, he deserved some respect. But good janitors were gold dust, and the Brill brothers had been keeping the building spotless and ship shape for nearly two years now. The Brills were almost celebrities themselves. Twins were very rare among the People. Mervall and Descant were the only pixie pair currently residing in Haven. They had featured on several TV programmes, including Canto, PPTV's highest rated chat show.

LEP Corporal Grub Kelp was on sentry duty. When Argon reached Opal's room, the corporal was engrossed in a movie on his video goggles. Argon didn't blame him. Guarding Opal Koboi was about as exciting as watching toenails grow.

'Good film?' inquired the doctor pleasantly.

Grub raised the lenses. 'Not bad. It's a human Western. Plenty of shooting and squinting.'

'Maybe I'll borrow it when you're finished?'

'No problem, Doctor. But handle it carefully. Human disks are very expensive. I'll give you a special cloth.'

Argon nodded. He remembered Grub Kelp now. The LEP officer was very particular about his possessions. He had already written two letters of complaint to the clinic board about a protruding floor rivet that had scratched his boots.

Argon consulted Koboi's chart. The plasma screen on the wall displayed a constantly updated feed from the sensors attached to her temples. There was no change, nor did he expect there to be. Her vitals were all normal, and her brain activity was minimal. She'd had a dream earlier in the evening but now her mind had settled. And finally, as if he needed telling, the seeker-sleeper implanted in her arm informed him that Opal Koboi was indeed where she was supposed to be. Generally the seeker-sleepers were implanted in the head, but pixie skulls were too fragile for any local surgery.

Jerbal punched in his personal code on the reinforced door's keypad. The heavy door slid back to reveal a spacious room, with gently pulsing floor mood lights. The walls were soft plastic, and gentle sounds of nature spilled from recessed speakers. At the moment a brook was splashing over flat rocks.

In the middle of the room, Opal Koboi hung suspended in a full body harness. The straps were gel padded and adjusted automatically to any body movement. If Opal did happen to wake the harness could be remotely triggered to seal like a net, preventing her from harming herself.

Argon checked the monitor pads, making sure they had good contact on Koboi's forehead. He lifted one of the pixie's eyelids, shining a pencil light at the pupil. It pupil contracted slightly, but Opal did not avert her eyes.

Well, anything to tell me today, Opal?' asked the doctor softly. 'An opening chapter for my book?'

Argon liked to talk to Koboi, just in case she could hear. When she woke up, he reasoned, he would have already have established a rapport.

'Nothing? Not a single insight?'

Opal did not react. As she hadn't for almost a year.

'Ah well,' said Argon, swabbing the inside of Koboi's mouth with the last cotton bud in his pocket. 'Maybe tomorrow, eh?'

He rolled the cotton bud across a sponge pad on his clipboard. Seconds later, Opal's name flashed up on a tiny screen.

'DNA never lies,' muttered Argon, tossing the bud into a recycling bin.

With one last look at his patient, Jerbal Argon turned towards the door.

'Sleep well, Opal,' he said almost fondly.

He felt calm again, the pain in his leg almost forgotten. Koboi was as far under as she had ever been. She wasn't going to wake up any time soon. The Koboi fund was safe.

It's amazing just how wrong one gnome can be.

Opal Koboi was not catatonic, but neither was she awake. She was somewhere in-between, floating in a liquid world of meditation where every memory was a bubble of multi-coloured light popping gently in her consciousness.

Since her early teens Opal had been a disciple of Gola Schweem, the cleansing coma guru. Schweem's theory was that there was a deeper level of sleep than experienced by most fairies. The cleansing coma state could usually only be reached after decades of discipline and practice. Opal had reached her first cleansing coma at the age of fourteen.

The benefits of the cleansing coma were that a fairy awoke completely refreshed but also spent the sleep time thinking, or in this case, plotting. Opal's coma was so complete, that her mind was almost completely separated from her body. She could fool the sensors and felt no embarrassment at the indignities of intravenous feeding and changing. The longest recorded consciously self-induced coma was forty seven days. Opal had been under for eleven months and counting, though she wasn't planning to be counting much longer.

When Opal Koboi joined forces with Briar Cudgeon and his goblins, she realised that she needed a back-up plan. Their scheme to overthrow the LEP had been ingenious, but there was always a chance that something could go wrong. In the event that it did, Opal had no intention of spending the rest of her life in prison. The only way she could make a clean getaway was if everybody thought she was still locked up. So Opal had begun to make preparations.

The first was to set up the emergency fund for the Argon Clinic. This would ensure she was sent to the right place if she had to induce a cleansing coma. The second step was to get two of her most trusted personnel installed in the clinic, to help with her eventual escape. Then she began siphoning huge amounts of gold from her businesses. Opal did not wish to become an impoverished exile.

The final step was to donate some of her own DNA and green light the creation of a clone that would take her place in the padded cell. Cloning was completely illegal, and had been banned by fairy law for over five hundred years since the first experiments in Atlantis. It was by no means a perfect science. Doctors had never been able to create an exact fairy clone. The clones looked fine, but they were basically shells with only enough brain power to run the body's basic functions. They were missing the spark of true life. A fully grown clone resembled nothing more than the original person in a coma. Perfect.

Opal had had a greenhouse lab constructed far from Koboi industries, and had diverted enough funds to keep the project active for two years. The exact time it would take to grow a clone of herself to adulthood. Then when she wanted to escape from the Argon Clinic, a perfect replica of herself would be left in her place. The LEP would never know she was gone.

As things had turned out, she had been right to plan ahead. Briar had proved treacherous, and a small group of fairies and humans had ensured his betrayal led to her own downfall. Now Opal had a goal to bolster her willpower. She would maintain this coma for as long as it took, because there was a score to be settled. Foaly, Root, Holly Short and the human Artemis Fowl. They were the ones responsible for her defeat. Soon she would be free of this clinic, and then she would visit those who had caused her such despair, and give them a little despair of their own. Once her enemies were defeated she could proceed with the second phase of her plan; introducing the mud men to the People, in a way that could not be covered up by a few mind wipes. The secret life of fairies was almost at an end.

Opal Koboi's brain released a few happy endorphins. The thought of revenge always gave her a warm fuzzy feeling.

The Brill brothers watched Doctor Argon limp up the corridor.

'Moron,' muttered Merv, using his telescopic vacuum pole to chase some dust out of a corner.

'You said it,' agreed Scant. 'Old Jerry couldn't analyse a bowl of vole curry. No wonder his wife is leaving him. If he was any good as a shrink, he would've seen that coming.'

Merv collapsed the vacuum. 'How are we doing?'

Scant checked his moonometer. 'Ten past eight.'

'Good. How's Corporal Kelp?'

'Still watching the movie. This guy is perfect. We have to go tonight. The LEP could send someone smart for the next shift. And if we wait any longer the clone will grow another inch.'

'You're right. Let me check the spy cameras.'

Scant lifted the lid on what appeared to be a janitor's trolley, festooned as it was with mops, rags and sprays. Hidden beneath a tray of vacuum nozzles, was a colour monitor split into several screens.

'Well?' hissed Merv.

Scant did not answer immediately, taking time to check all the screens. The video feed was from various micro-cameras that Opal had installed around the clinic before her incarceration. The spy cameras were actually genetically engineered organic material. So the pictures they sent were literally a live feed. The world's first living machines. Totally undetectable by bug sweepers.

'Night crew only,' he said at last. 'Nobody in this sector except Corporal Idiot over there.'

'What about the parking lot?'

'Clear.'

Merv held out his hand. 'Okay, brother. This is it. No turning back. Are we in? Do we want Opal Koboi back?'

Scant blew a lock of black hair from one round pixie eye.

'Yes, because if she comes back on her own, Opal will find a way to make us suffer,' he said, shaking his brother's hand. 'So yes, we're in.'

Merv took a remote control from his pocket. The device was tuned to a sonix receiver planted in the clinic's gable wall. This in turn was connected to a balloon of acid which lay gently on the clinic's main power cube in the parking lot junction box. A second balloon sat atop the back-up cube in the maintenance basement. As the clinic's janitors, it had been a simple matter for Merv and Scant to plant the acid balloons the previous evening. Of course the Argon Clinic was also connected to the main grid, but if the cubes did go down, there would be a two minute interval before the main power kicked in. There was no need for more elaborate arrangements, after all this was a medical facility not a prison.

Merv took a deep breath, flicked the safety cover and pressed the red button. The remote control emitted an infra red command activating two sonix charges. The charges sent out sound waves bursting the balloons, and the balloons dumped their acidic contents on the clinic's power cubes. Twenty seconds later the cubes were completely eaten away and the clinic was plunged into darkness. Merv and Scant quickly put on night vision goggles.
As soon as the power failed green strip lights began pulsing gently on the floor guiding the way to the exits. Merv and Scant moved quickly and purposefully. Scant steered the trolley, and Merv made straight for Corporal Kelp.

Grub was pulling the video glasses from over his eyes.

'Hey,' he said, disorientated by the sudden darkness. 'What's going on here?'

'Power failure,' said Merv, bumping into him with calculated clumsiness. 'Those lines are a nightmare, I've been telling Doctor Argon, but nobody wants to spend money on maintenance when there are fancy company cars to be bought.'

Merv was not waffling for the fun of it, he was waiting for the soluble pad of sedative he had pressed onto Grub's wrist to take effect.

'Tell me about it,' said Grub, suddenly blinking a lot more than he generally did. 'I've been lobbying for new lockers at Police Plaza. I'm really thirsty. Is anyone else thirsty?' Grub stiffened, frozen by the serum that was spreading through his system. The LEP officer would snap out of it in under two minutes, and be instantly alert. He would have no memory of his unconsciousness, and hopefully he would not notice the time lapse.

'Go,' said Scant tersely.

Merv was already gone. With practised ease, he punched Doctor Argon's code into Opal's door. He completed this action faster than Argon ever could, due to hours spent practising on a stolen pad in his apartment. Argon's code changed every week, but the Brill brothers made certain that they were cleaning outside the room when Argon was on his rounds. The pixies generally had the complete code by mid week.

The pad light winked green, and the door slid back. Opal Koboi swung gently before him, suspended in her harness like a bug in an exotic cocoon.

Merv winched her down onto the trolley. Moving briskly, and with practised precision, he rolled up Opal's sleeve and located the scar in her upper arm where the seeker-sleeper had been inserted. He gripped the hard lump between his thumb and forefinger.

'Scalpel,' he said, holding out his free hand. Scant passed him the instrument. Merv took a breath, held it, and made a two centimetre incision in Opal's flesh. He wiggled his index finger into the hole and rolled out the electronic capsule. It was the encased in silicone and roughly the size of a painkiller.

'Seal it up,' he ordered.

Scant bent close to the wound, placing a thumb at each end.

'Heal,' he whispered, and blue sparks of fairy magic ran rings around his fingers, sinking into the wound. In seconds the folds of skin had zipped themselves together, with only a pale pink scar to show that a cut had been made. A pink scar almost identical to the scar that had already existed. Opal's own magic had dried up months ago, as she was in no position to complete a power restoring ritual.

 'Miss Koboi,' said Merv briskly. 'Time to get up. Wakey wakey.'

He unstrapped Opal completely from the harness. The unconscious pixie collapsed onto the lid of the cleaning trolley. Merv slapped her across the cheek, bringing a blush to her face. Opal's breathing rate increased slightly, but her eyes remained closed.

'Jolt her,' said Scant.

Merv pulled an LEP issue buzz baton from inside his jacket. He powered it up and touched Opal on the elbow. The pixie's body jerked spasmodically, and Opal Koboi shot into consciousness, a sleeper waking from a nightmare.

'Cudgeon,' she screamed. 'You betrayed me!'

Merv grabbed her shoulders. 'Miss Koboi. It's us, Mervall and Descant. It's time.'

Opal glared at him wild eyed.

'Brill?' she said, after several deep breaths.

'That's right. Merv and Scant. We need to go.'

'Go? What do you mean?'

'Leave,' said Merv urgently. 'We have about a minute.'

Opal shook her head, dislodging the after-trance daze. 'Merv and Scant. We need to go.'

Merv helped her from the trolley's lid. 'That's right. The clone is ready.'

Scant peeled back a sealed foil false bottom in the trolley. Inside lay a cloned replica of Opal Koboi wearing an Argon Clinic coma suit. The clone was identical down to the last follicle. Scant removed an oxygen mask from the clone's face, hauled it from its resting place and began cinching her into the harness.

'Remarkable,' said Opal, brushing the clone's skin with her knuckle. 'Am I that beautiful?'

'Oh yes,' said Merv. 'That and more.'

Suddenly Opal screeched. 'Idiots. It's eyes are open. It can see me!' }

Scant closed the clone's lids hurriedly. 'Don't worry, Miss Koboi, it can't tell anyone, even if its brain could decipher what it sees.'

Opal climbed groggily into the trolley. 'But its eyes can register images. Foaly may think to check. That infernal centaur.'

'Don't fret, Miss,' said Scant, folding the trolley's false bottom over his mistress. 'Very soon now, that will be the least of Foaly's worries.'

Opal strapped the oxygen mask across her face. 'Later,' she said, her voice muffled by the plastic. 'Talk, later.'

Koboi drifted into a natural sleep, exhausted by even this small exertion. It could be hours before the pixie regained total consciousness. After a coma of that length, there was even the risk that Opal would never be quite as smart as she once was.

'Time?' said Merv.

Scant glanced at his moonometer. 'Thirty seconds left.'

Merv finished cinching the straps exactly how they had been. Pausing only to dab sweat from his brow, he made a second incision with his scalpel. This time in the clone's arm, and inserted the seeker-sleeper. While Scant sealed the cut with a blast of magical sparks, Merv rearranged the cleaning paraphernalia over the trolley's false section.

Scant bobbed impatiently. 'Eight seconds, seven. By the gods, this is the last time I break the boss out of a clinic and replace her with a clone.'

Merv spun the trolley on its castors, pushing it through the open doorway.

'Five...four...'

Scant did one last check around, running his eyeballs across everything they had touched.

Three..two...'

They were out, pulling the door behind them.

'One..'

Corporal Grub slumped slightly, then jerked to attention.

'Hey...what the? I'm really thirsty? Is anyone else thirsty?'

Merv stuffed the night vision goggles into the trolley, blinking a bead of sweat from his eyelid. 'It's the air in here. I get dehydrated all the time. Terrible headaches.'

Grub pinched the bridge of his nose. 'Me too. I'm going to write a letter, as soon as the lights come back.'

Just then the lights did come back, flickering on one after another down the length of the corridor.

'There we go,' grinned Scant. 'Panic over. Maybe now they'll buy us some new circuits, eh brother?'

Doctor Argon came barrelling down the passageway, almost keeping pace with the flickering lights.

'Your leg is better then, Jerry?' said Merv.

Argon ignored the pixies, his eyes wide, his breath ragged.

'Corporal Kelp,' he panted. 'Koboi, is she? Has she...'

Grub rolled his eyes. 'Calm yourself, Doctor. Miss Koboi is still suspended where you left her. Take a look.'

Argon flattened his palms against the wall, first checking the vitals.

'Okay, no change. No change. A two minute lapse, but that's okay.'

'I told you,' said Grub. 'While you're here, I need to talk to you about these headaches I've been having.'

Argon brushed him aside. 'I need a cotton bud. Scant, do you have any?'

Scant slapped his pockets. 'Sorry, Jerry. Not on me.'

'Don't call me Jerry!' howled Jerbal Argon, ripping the lid from the cleaning trolley. 'There must be cotton buds in here somewhere,' he said, sweat pasting thin hair across a wide gnome's forehead. 'It's a janitor's box for heaven's sake.' His blunt finger scrabbled through the trolley's contents, scraping across the false bottom.

Merv elbowed him out of the way before he could discover the secret compartment or spy screens. 'Here were are, Doctor,' he said grabbing a tub of buds. 'A month's supply. Knock yourself out.'

Argon fumbled a single bud from the pack, discarding the rest.

'DNA never lies,' he muttered, keying his code into the door. 'DNA never lies.'

He rushed into the room, roughly swabbing the inside of the clone's mouth. The Scant brothers held their breath. They had expected to be out of the clinic before this happened. Argon rolled the cotton bud's head across the sponge pad on his clipboard. A moment later, Opal Koboi's name flashed onto the board's mini- plasma screen.

Argon heaved a massive sigh, resting his hands on both knees. He threw the observers a shamefaced grin. 'Sorry. I panicked. If we lost Koboi, the Clinic would never live it down. I'm just a little paranoid, I suppose. Faces can be altered, but...'

'DNA never lies,' said Merv and Scant simultaneously.

Grub reset his video goggles. 'I think Doctor Argon needs a little vacation.'

'You're telling me,' sniggered Merv, rolling the trolley towards the maintenance elevator. 'Anyway, we better get going, brother. We need to isolate the cause of the power failure.'

Scant followed him down the corridor. 'Any idea where the problem could be?'

'I have a hunch. Let's try the parking lot, or maybe the basement.'

'Whatever you say. After all, you are the older brother.'

'And wiser,' added Merv. 'Don't forget that.'

The pixies continued down the corridor, their brisk banter masking the fact that their knees were shaking, and their hearts were battering their rib cages. It wasn't until they had removed the evidence of their acid bombs, and were well on their way home in the van, that they began to breath normally again.

 
Merv unzipped Koboi from her sealed compartment back in the apartment he shared with Scant. Any worries they'd had about Opal's IQ taking a dip were immediately banished. Their employer's eyes were bright and aware.

'Bring me up to speed,' she said, climbing shakily from the trolley. Even though her mind was fully functioning, it would take a couple of days in an electro-massager to get her muscles back to normal.

Merv helped her onto a low sofa. 'Everything is in place. The funds, the surgeon, everything.'

Opal drank greedily, straight from a jug of core water on the coffee table. 'Good, good. And what of my enemies?'

Scant stood beside his brother. They were almost identical except for a slight wideness in Merv's brow. He had always been the smart one.

'We have kept tabs on them, as you asked.' br>
OOpal stopped drinking. 'Asked?'

'Instructed,' stammered Scant. 'Instructed, of course. That's what I meant.'

Koboi's eyes narrowed. 'I do hope the Brill brothers haven't developed any independent notions since I've been asleep.'
 
Scant stooped slightly, almost bowing. 'No, no, Miss Koboi. We live to serve. Only to serve.'

'Yes,' agreed Opal. 'And you live only as long as you do serve. Now, my enemies. They are well and happy, I trust.'

'Oh yes. Julius Root goes from strength to strength as LEP Commander. He has been nominated for the Council.'

Opal smiled, a vicious wolverine's smile. 'The Council. Such a long way to fall. And Holly Short?'

'Back on full active duty. Six successful reconnaissance missions since you induced your coma. Her name has been put on the list for promotion to major.'

'Major, indeed. Well the least we can do is to make sure that promotion never comes through. I plan to wreck Holly Short's career, so she dies in disgrace.'

'The centaur Foaly is as obnoxious as ever,' continued Scant Brill. 'I suggest a particularly nasty...'

Opal raised a delicate finger, cutting him off. 'No. Nothing happens to Foaly just yet. He will be defeated by intellect alone. Twice in my life, someone has outsmarted me. Both times it was Foaly. Just killing him requires no ingenuity. I want him beaten, humiliated and alone.' She clapped her hands in delighted anticipation. 'And then I will kill him.'

'We have been monitoring Artemis Fowl's communications. Apparently the human youth has spent most of the past year trying to find a certain painting. We have traced the painting to Munich.'

'A painting? Really?' Cogs turned in Opal's brain. 'Well, let's make sure we get to it before he does. Maybe we can add a little something to his work of art.'

Scant nodded. 'Yes. That's not a problem. I'll go tonight.'

Opal stretched out on the sofa like a cat in the sunlight. 'Good. This is turning out to be a lovely day. Now, send for the surgeon.'

The Brill brothers glanced at each other.

'Miss Koboi?' said Mervall nervously.

'Yes, what is it?'

'The surgeon. This kind of operation cannot be reversed even by magic. Are you sure you wouldn't like to think...'

Opal leapt from the sofa. Her cheeks were crimson with rage.

'Think! You'd like me to think about it! What do you imagine I have been doing for the past year? Thinking! Twenty four hours a day. I don't care about magic. Magic did not help me to escape, science did. Science will be my magic. Now, no more advice, Merv, or your brother will be an only child. Is that clear?'

Merv was stunned. He had never seen Opal in such a rage. The coma had changed her.

'Yes, Miss Koboi.'

'Now, summon the surgeon.'

'At once, Miss Koboi.'

Opal lay back on the sofa. Soon everything would be right in the world. Her enemies would shortly be dead or discredited. Once those loose ends were tied up, she could get on with her new life. Koboi rubbed the tips of her pointed ears. What would she look like, she wondered, as a human?""".lower(), d, l)

print("LE RESULTAT EST : ", code())
print(poidMot('JK'.lower(),d, l))
print(poidMot('Rowling'.lower(),d, l))
print(poidMot('JK Rowling'.lower(),d, l))
print(poidMot('Mary Higgins Clark'.lower(),d, l))
print(poidMot('StephenKing'.lower(),d, l))
print(poidMot('EionColfer'.lower(),d, l))

"""
Valeur mot = Somme des index des lettres
SSI (valeur du mot in valeur triangulaire)
alors dans l'exemple sky, sky = 55 et 55 = f(10)
DONC
VALEUR POID MOT = 
"""
"""
def valeurPoidMot(occurence: int, valeur_n_triangulaire: int, poidMot: int)):
    return 
"""


print(poidPhrase("My family at home My family lives in a small house. It's simple but pretty. It has a large garden. I like to work in the garden but my sister hates to work in the garden. She prefers to read. She reads in the morning, in the afternoon and at night.".lower(), d, l))

# print(poidMot("family".lower(), d))
# print(poidMot("at".lower(), d))
# print(poidMot("h  as".lower(), d))
# print(poidMot("read".lower(), d))

"""
a_string = "a\tb\tc\td\te"
print(a_string)
PRODUCTION
a	b	c	d	e

split_string = a_string.split("\t")

print(split_string)
PRODUCTION
['a', 'b', 'c', 'd', 'e']
"""