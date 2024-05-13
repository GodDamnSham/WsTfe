import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
from keybert import KeyBERT
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append("/Users/malik/Library/Python/3.10/bin")

nltk.download('punkt', download_dir="/Users/malik/Library/Python/3.10/bin")
nltk.download('wordnet', download_dir="/Users/malik/Library/Python/3.10/bin")
print(nltk.data.path)
#nltk.download('punkt')
#nltk.download('wordnet')
# Sentences
sentences = [
    "'The image features a black woman, standing proudly and smiling, in front of an urban scene. She is wearing a sleeveless sports top that reads The People's Journey to Overcoming Running Block. This text emphasizes the significance of personal growth and progress, highlighting the challenges runners encounter while pushing themselves towards their goals. In the background, there are several people engaged in various activities, with some running, while others seem to be interacting with the surrounding environment. A bicycle can also be seen among the diverse urban scene, adding a touch of adventure and movement to the image.",
    "A person is shown in the image, wearing a helmet and climbing gear, standing on top of a snow-covered mountain. They appear to be holding their skis high in the air with great enthusiasm, celebrating their achievement on the mountain.",
    "The image depicts a busy street scene with several men running, one of them standing out by wearing sunglasses and a necklace, while other runners pass behind or beside him. His presence appears to be noteworthy as he stands out from the others due to his accessories. The runners can be seen in different parts of the scene, either in front, to the left, or behind the main focus of the man with the sunglasses. Overall, the image captures the energy and excitement of running and being active outdoors.",
    "The image depicts a humorous situation, where the person from the sports team wearing a red jersey is chasing the cheetah, who appears to be in a playful mood. They are both running on the ground, and the cheetah has its tongue out as it looks back at the person in front of it. In the background, there's a couch, which might suggest that the scene could take place in an environment outside of a typical sports setting. Overall, the image suggests the cheetah has taken an interest in the runner's pursuit and seems to be participating in the chase with a playful attitude.",
    "The image is divided into two parts. In the first part, there is a lady in purple running down the sidewalk on a sunny day. She's wearing a green sports outfit, black shoes, and a green sports backpack. The image captures her running motion and a part of the running path beside the road. In the second part of the image, there is a bunch of colorful flowers hanging from branches, surrounded by a brick wall. The scene has a charming atmosphere with the presence of flowers in the background and the lady on the run in the foreground.",
    "The image shows an orange line on a digital map with GPS coordinates, indicating the route taken by a cyclist from 0 to 83.37 km (km0 to km 83). It's likely a map app is being used to display the bike path or the distance covered during a ride. The app provides essential information for cyclists such as distance, location, and elevation changes throughout the journey. This gives riders helpful insight into their physical effort and helps them plan their routes more efficiently.",
     "The image displays a graph with several countries, ranging from 5 percent to 20 percent represented on the x-axis, and a range of different percentages across the y-axis. The pie chart shows that some countries have 5 percent, others 10 percent, and others 20%. The total percentage of people in the world who match one or more MMR criteria is approximately 73 of the total population. The various countries' colors show their representation in the graph.",
     "The image features a smartphone display showcasing four different apps for fitness enthusiasts. The first app is a personal trainer that allows users to receive exercise advice based on their goals and preferences. The second app is the Nike Run Club, which offers a community for runners to connect with like-minded individuals. The third app is an interval workout app that provides a structured workout plan to help users achieve their fitness goals. The fourth app is the HIIT (High-Intensity Interval Training) app, which helps users develop strength and endurance through short bursts of intense exercise.",
     "In the image, a young man is running in an open field on top of a hill, surrounded by lush green vegetation. The man appears to be in high spirits as he maintains a good pace and focuses on his run. Several trees are scattered throughout the landscape, providing shade and a natural background for the runner. Two umbrellas can be seen in the foreground, possibly held by people watching the man run or taking shelter from the sun.",
     "The image features two men, one in the center and the other on the right side of the scene. They are both holding up their hands with a shape and standing outdoors. The scene looks like they are posing for a photo shoot or celebrating something. In addition to the two main subjects, there are several other people visible around the scene, possibly participants or onlookers. Two more people are positioned near the edge of the image, while two others can be seen in the background at different distances. A person is also visible on the right side of the image, further away from the main subjects.",
     "The image captures a group of people standing in a line, with one person wearing a tennis shirt, sitting on the floor in the middle. Several others are also standing nearby, watching or waiting. One man is particularly focused on the individual on the floor and can be seen trying to adjust his pants while leaning over. Apart from these people, there are also other items scattered around the scene, including three handbags visible close to the edge of the image and several bottles, some placed near the middle and others closer to the side. A pair of cups and spoons can also be seen on the table at the back. Apart from these everyday objects, there are also two umbrellas in the vicinity, one of which appears near the top left corner of the image, and the other closer to the right side.",
     "The image features a man dressed in running attire, leaping across a dock over the water. The man appears to be having fun as he leaps towards the camera, capturing a moment of exhilaration and exercise. The setting is picturesque, with an array of trees and a mountain visible in the background.There are multiple boats scattered throughout the scene, adding to the beautiful outdoor atmosphere. Some of the boats are situated closer to shore, while others can be seen floating further away in the background, reflecting on the water. Apart from the main subject of the image, there are several smaller boats also present, contributing to the overall sense of an oceanic environment",
     "In the image, a group of three people is standing together, all smiling and laughing as they pose for a photo. Two of the individuals are wearing bicycle helmets, and they have their arms around each other, creating a playful and joyful atmosphere. A bicycle can also be seen in the background behind one of the women. The group appears to be friends who are enjoying a fun-filled day on the road or trails.",
     "The image features a group of athletes participating in a running competition on a roadway. These runners are running down a city street, with one leader visible ahead of the rest. There are four people wearing uniforms visible throughout the scene, possibly representing different teams or individuals.The city street is lined with trees and cars parked along the side of the road, adding to the urban atmosphere of the event. The runners appear to be competing in a marathon, showcasing their determination and endurance as they run through the city streets.",
     "In the image, a man in a multi-colored outfit is running down the road, likely competing in an athletic race. Numerous people are watching the event from different angles, with some standing in the background and others seated or positioned near the edge of the road. A bicycle can be seen in the background as well, possibly belonging to a spectator or a participant in the race. The event has drawn quite a large crowd of interested individuals, with the crowd spread out across different areas along the street.",
     "The image shows a beautiful mountain road snaking up the side of a lush hill, with many colorful trees lining either side. The road is adorned with bright red and orange leaves, creating an autumnal atmosphere. Several bicycles can be seen along the road, making the scene appear like a picturesque postcard. In the distance, there is a large vehicle traveling on the road, further emphasizing the winding path through the woods.",
     "A woman in black shorts and a bicycle helmet riding down the middle of a dirt road, with her back facing the viewer. Her figure appears to be in a low position, indicating she might be cycling down a steep or hilly road. In the background, there are a few trees that are dispersed along the dirt path.",
     "In this image, a large crowd has gathered to watch the Tour de France cyclists compete in front of the Arc de Triomphe. These are likely fans from all over Europe who have travelled for the event. The cyclists can be seen riding bicycles through the scene and making their way up a hill. The fans have gathered both near and far from the riders to cheer them on as they race.In the foreground, several people with cameras are ready to capture the action-packed moment, while some fans can be spotted taking selfies or enjoying the excitement of the event. The atmosphere is filled with excitement as the crowd eagerly awaits the next stage of the competition.",
     "In this joyful scene, several people in different areas are celebrating or dancing along the streets. This could be a street festival, where they're enjoying the lively atmosphere and each other's company. Some participants can be seen wearing colorful clothing and holding large balloons, adding to the vibrant atmosphere. The people are scattered throughout the frame, with some nearer to the foreground and others farther away in the background. In the center of the image, a woman stands out as she is holding both arms up in the air and appears to be expressing her excitement. There is also a man in a yellow jacket nearby.",
     "The image captures a person in a wheelchair participating in a marathon. At the location, the runner is using hand controls to move their wheelchair down a street. There are also other vehicles visible on the road, with some cars close to the runner and others further away.In the background, a large, tall building can be seen, likely a skyscraper or a high-rise complex. The presence of various traffic lights in the scene indicates a busy street where pedestrians and vehicles frequently move.",
     "The image captures a group of people on a snowy slope, dressed for skiing. These individuals are dispersed across the landscape, some carrying skis and standing uphill, while others are skiing down the slope. There is a diverse range of skis and backpacks being used, with some closer to the bottom of the image, and others more toward the top. Several trees can be seen in the background, adding to the scenery. The skiers appear to be partaking in an outdoor activity, enjoying the fresh snow on the mountain.",
     "The image captures a beautiful, sunset-lit scene of a person running along a dirt road. Some trees are visible on either side, adding to the scenic atmosphere. \n\nIn the foreground, a parked car can be seen near a trailer. In the background, two tents are visible, potentially indicating that camping is involved in this outdoor adventure. A cell phone is also spotted near the edge of the field, providing a sense of modernity to the otherwise rustic and peaceful setting.",
     "The image captures a group of women standing on the sidewalk outside, enjoying each other's company. They are all wearing matching blue tops, likely indicating a sense of camaraderie or belonging among them. There are four women in total, two of whom are close together while the other two women are slightly apart from them. They appear to be posing for the camera as they happily share a moment with each other, smiling and chatting.",
     "The image captures two men hiking uphill through a mountainous terrain, carrying backpacks as they go. Their focus is on the trail ahead, and each man carries an orange flag attached to their hiking stick. They appear to be making their way across rocky ground, as evidenced by the scattered boulders in the scene. The men's outfits feature short-sleeved shirts and long shorts or tights for their hike. One of the individuals carries a handbag, while the other has a large backpack over their shoulders. Both hikers appear to have experienced some challenges, as they hold onto each other as they make their way along the path.",
     "A scenic white skier is standing on top of a snowy mountain slope, with an untouched ski trail stretching out in front of them. The sun is shining brightly overhead, casting a warm glow across the mountain landscape.In the distance, multiple snow-covered mountains can be seen, creating a dramatic and serene atmosphere. A mountain ridge with a few trees adds some height and depth to the scene. This image captures the essence of winter sports and the natural beauty of the mountains."
]

# Initialize KeyBERT
kw_extractor = KeyBERT()

# Tokenization and Lemmatization
lemmatizer = WordNetLemmatizer()
keywords = []
for sentence in sentences:
    tokens = word_tokenize(sentence.lower())  # Tokenization
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]  # Lemmatization
    keywords.extend(lemmas)

# Get unique keywords
unique_keywords = set(keywords)
List=[]
# Extract keywords using KeyBERT
keyword_count = {}
for keyword in unique_keywords:
    keywords = kw_extractor.extract_keywords(keyword, keyphrase_ngram_range=(1, 1), top_n=1, stop_words='english')
    print(keywords)
    List.append(keywords)
    for key in keywords:
        if key[0] not in keyword_count:
            keyword_count[key[0]] = 1
        else:
            keyword_count[key[0]] += 1

for l in List:
    print(l)
print(len(List))
# Display keyword frequency
table = [[keyword, freq] for keyword, freq in keyword_count.items()]
print(tabulate(table, headers=['Keyword', 'Frequency']))