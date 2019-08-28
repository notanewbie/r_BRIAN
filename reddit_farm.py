import os
import urllib2
import unicodedata
def harshChars(t):
    t = parseChars(t);
    t = t.replace("'", "")
    t = t.replace('"', "")
    t = t.replace('[', "")
    t = t.replace(']', "")
    t = t.replace('|', "")
    return t
def parseChars(t):
    import HTMLParser;
    parser = HTMLParser.HTMLParser();
    try:
        t = parser.unescape(t);
    except TypeError:
        t = t.replace("â€™", "'");
    except UnicodeDecodeError:
        t = t.replace("â€™", "'");
    t = t.replace("&#x200B;", "");
    t = t.replace("?", "")
    t = t.replace('"', "")
    t = t.replace('PH/', "")
    t = t.replace('\n', "")
    t = t.replace('<', "")
    t = t.replace('>', "")
    t = t.replace('/', "")
    t = t.replace(':', "")
    t = t.replace('*', "")
    t = t.replace('\\', "")
    return t
def returnURL(url):
    try:
        req = urllib2.Request(url, None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
        response = urllib2.urlopen(req).read()
        return response;
    except IOError:
        url = url;
statements = [];
links = [];
z = 0;
def getThread(URL):
    global statements
    global z
    global links
    code = returnURL(URL);
    i = 1;
    z = 0;
    while(len(code.split('<h3 class="_eYtD2XCVieq6emjKBH3m">')) > i):
        statements.append(code.split('<h3 class="_eYtD2XCVieq6emjKBH3m">')[i].split("</h3>")[0]);
        print statements[z];
        print "";
        z = z + 1;
        i = i + 1;
    i = 0;
    links = [];
    while(len(code.split('_1UoeAeSRhOKSNdY_h3iS1O _1Hw7tY9pMr-T1F4P1C-xNU _2qww3J5KKzsD7e5DO0BvvU" href="')) > i):
        if i > 0:
            links.append(returnURL("https://old.reddit.com" + code.split('_1UoeAeSRhOKSNdY_h3iS1O _1Hw7tY9pMr-T1F4P1C-xNU _2qww3J5KKzsD7e5DO0BvvU" href="')[i].split('"')[0]));
            #print "https://reddit.com" + code.split('_1UoeAeSRhOKSNdY_h3iS1O _1Hw7tY9pMr-T1F4P1C-xNU _2qww3J5KKzsD7e5DO0BvvU" href="')[i].split('"')[0];
            #print "";
            #z = z + 1;
        i = i + 1;
def learn(threads):
    z = len(statements) - 1;
    i = 0;
    a = 0;
    while(len(threads) > a):
        print "Thread #" + str(a + 1);
        i = 0;
        while(len(threads[a].split('<div class="md"><p>')) > i):
            if i > 0:
                statements.append(threads[a].split('<div class="md"><p>')[i].split('</p>')[0]);
                if i > 1:
                    try:
                        print statements[z];
                        statements[z] = parseChars(statements[z])
                        print statements[z];
                        Respo = open("PH/" + harshChars(statements[z - 1])[:200] + ".ph", "w");
                        Respo.write(statements[z].replace(u'\u200b', ""));
                        file.close(Respo);
                    except UnicodeDecodeError:
                        Respo.write(parseChars(statements[z]));
                        file.close(Respo);
                    print "";
                    print i;
                z = z + 1;
            i = i + 1;
        a = a + 1;
def learnSub(dis):
    global g
    g = 0;
    getThread(dis);
    while(g < len(links)):
        try:
            learn(links[g].split('itemtype'));
        except AttributeError:
            g = g;
        g = g + 1;
subs = ["https://www.reddit.com/r/unpopularopinion/", "https://www.reddit.com/r/AskReddit/", "https://www.reddit.com/r/24_Show/", "https://www.reddit.com/r/24Show/", "https://www.reddit.com/r/FanTheory/", "https://www.reddit.com/r/FortniteBattleRoyale/", "https://www.reddit.com/r/FORTnITE/", "https://www.reddit.com/r/FortNiteBR/", "https://www.reddit.com/r/gadgets/", "https://www.reddit.com/r/google/", "https://www.reddit.com/r/googleassistant/", "https://www.reddit.com/r/GooglePixel/", "https://www.reddit.com/r/gravityfalls/", "https://www.reddit.com/r/gumball/", "https://www.reddit.com/r/homeautomation/", "https://www.reddit.com/r/Hulu/", "https://www.reddit.com/r/InfinityTrain/", "https://www.reddit.com/r/iphone/", "https://www.reddit.com/r/JakePaul/", "https://www.reddit.com/r/LazorWulf/", "https://www.reddit.com/r/learnpython/", "https://www.reddit.com/r/LouderWithCrowder/", "https://www.reddit.com/r/Martingarrix/", "https://www.reddit.com/r/marvelstudios/", "https://www.reddit.com/r/Mastodon/", "https://www.reddit.com/r/mkbhd/", "https://www.reddit.com/r/motorola/", "https://www.reddit.com/r/MrRobot/", "https://www.reddit.com/r/NCAAFBseries/", "https://www.reddit.com/r/NCAAFOOTBALL14/", "https://www.reddit.com/r/Piracy/", "https://www.reddit.com/r/PewdiepieSubmissions/", "https://www.reddit.com/r/PS4/", "https://www.reddit.com/r/PS5/", "https://www.reddit.com/r/Python/", "https://www.reddit.com/r/radio/", "https://www.reddit.com/r/raspberry_pi/", "https://www.reddit.com/r/rickandmorty/", "https://www.reddit.com/r/Roku/", "https://www.reddit.com/r/Saberspark/", "https://www.reddit.com/r/ShouldIbuythisgame/", "https://www.reddit.com/r/Skullcandy/", "https://www.reddit.com/r/spotify/", "https://www.reddit.com/r/StraightTalk/", "https://www.reddit.com/r/technology/", "https://www.reddit.com/r/teenagers/", "https://www.reddit.com/r/teenagersnew/", "https://www.reddit.com/r/television/", "https://www.reddit.com/r/TicPods/", "https://www.reddit.com/r/TOR/", "https://www.reddit.com/r/Twitch/", "https://www.reddit.com/r/Unboxtherapy/", "https://www.reddit.com/r/UniversalProfile/", "https://www.reddit.com/r/UpliftingNews/", "https://www.reddit.com/r/vidgo/", "https://www.reddit.com/r/xbox/", "https://www.reddit.com/r/youtube/", "https://www.reddit.com/r/StarWars/", "https://www.reddit.com/r/starwarscanon/", "https://www.reddit.com/r/starwarsspeculation/"];
x = 0;
while(len(subs) > x):
    learnSub(subs[x]);
    print "";
    print "Parsing of comments from " + subs[x] + " completed sucessfully.";
    print "";
    x = x + 1;
#except UnicodeEncodeError:
#print "No wubba-lubba-dub-dub here broh.";
#print "Yikes. Parsing r/unpopularopinion failed epicly.";
