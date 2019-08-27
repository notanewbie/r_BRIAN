import os
import urllib2
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
                    import HTMLParser;
                    parser = HTMLParser.HTMLParser();
                    try:
                        statements[z] = parser.unescape(statements[z]);
                    except TypeError:
                        statements[z] = statements[z].replace("â€™", "'");
                    except UnicodeDecodeError:
                        statements[z] = statements[z].replace("â€™", "'");
                    print statements[z];
                    Respo = open("PH/" + harshChars(statements[z - 1])[:200] + ".ph", "w");
                    Respo.write(statements[z]);
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
#learnSub("https://www.reddit.com/r/AskReddit/")
#learnSub("https://www.reddit.com/r/24_Show/")
#learnSub("https://www.reddit.com/r/24Show/")
#learnSub("https://www.reddit.com/r/FanTheory/")
#learnSub("https://www.reddit.com/r/FortniteBattleRoyale/")
#learnSub("https://www.reddit.com/r/FORTnITE/")
#learnSub("https://www.reddit.com/r/FortNiteBR/")
#learnSub("https://www.reddit.com/r/gadgets/")
#learnSub("https://www.reddit.com/r/google/")
#learnSub("https://www.reddit.com/r/googleassistant/")
#learnSub("https://www.reddit.com/r/GooglePixel/")
#learnSub("https://www.reddit.com/r/gravityfalls/")
#learnSub("https://www.reddit.com/r/gumball/")
#learnSub("https://www.reddit.com/r/homeautomation/")
#learnSub("https://www.reddit.com/r/Hulu/")
#learnSub("https://www.reddit.com/r/InfinityTrain/")
#learnSub("https://www.reddit.com/r/iphone/")
#learnSub("https://www.reddit.com/r/JakePaul/")
#learnSub("https://www.reddit.com/r/LazorWulf/")
#learnSub("https://www.reddit.com/r/learnpython/")
#learnSub("https://www.reddit.com/r/LouderWithCrowder/")
#learnSub("https://www.reddit.com/r/Martingarrix/")
#learnSub("https://www.reddit.com/r/marvelstudios/")
#learnSub("https://www.reddit.com/r/Mastodon/")
#learnSub("https://www.reddit.com/r/mkbhd/")
#learnSub("https://www.reddit.com/r/motorola/")
#learnSub("https://www.reddit.com/r/MrRobot/")
#learnSub("https://www.reddit.com/r/NCAAFBseries/")
#learnSub("https://www.reddit.com/r/NCAAFOOTBALL14/")
#learnSub("https://www.reddit.com/r/Piracy/")
#learnSub("https://www.reddit.com/r/PewdiepieSubmissions/")
#learnSub("https://www.reddit.com/r/PS4/")
#learnSub("https://www.reddit.com/r/PS5/")
#learnSub("https://www.reddit.com/r/Python/")
#learnSub("https://www.reddit.com/r/radio/")
#learnSub("https://www.reddit.com/r/raspberry_pi/")
#learnSub("https://www.reddit.com/r/rickandmorty/")
#learnSub("https://www.reddit.com/r/Roku/")
#learnSub("https://www.reddit.com/r/Saberspark/")
#learnSub("https://www.reddit.com/r/ShouldIbuythisgame/")
#learnSub("https://www.reddit.com/r/Skullcandy/")
#learnSub("https://www.reddit.com/r/spotify/")
#learnSub("https://www.reddit.com/r/StraightTalk/")
#learnSub("https://www.reddit.com/r/technology/")
#learnSub("https://www.reddit.com/r/teenagers/")
#learnSub("https://www.reddit.com/r/teenagersnew/")
#learnSub("https://www.reddit.com/r/television/")
#learnSub("https://www.reddit.com/r/TicPods/")
#learnSub("https://www.reddit.com/r/TOR/")
#learnSub("https://www.reddit.com/r/Twitch/")
#learnSub("https://www.reddit.com/r/Unboxtherapy/")
#learnSub("https://www.reddit.com/r/UniversalProfile/")
#learnSub("https://www.reddit.com/r/unpopularopinion/")
#learnSub("https://www.reddit.com/r/UpliftingNews/")
#learnSub("https://www.reddit.com/r/vidgo/")
#learnSub("https://www.reddit.com/r/xbox/")
#learnSub("https://www.reddit.com/r/youtube/")
#learnSub("https://www.reddit.com/r/StarWars/")
#learnSub("https://www.reddit.com/r/starwarscanon/")
#learnSub("https://www.reddit.com/r/starwarsspeculation/")
