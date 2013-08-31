import os
# -*- coding: cp1252 -*-
import codecs
import time
import requests
import urllib2
import urllib
import json as m_json
import os
import sys
from urllib import FancyURLopener
import time
from flask import Flask, request, Response
from BeautifulSoup import BeautifulSoup, Comment
import json as simplejson
Soup = BeautifulSoup
from nltk import sent_tokenize, word_tokenize
from collections import Counter
from collections import defaultdict
from math import log10
# -*- coding: utf-8 *-*
import nltk.data
from nltk.corpus import wordnet as wn

syno =[]
hg = 0

app = Flask(__name__)
profanity = ['fuck','asshole','sex','faggot','negro','nigger','boob','tit','sex','shit','breast','porn']


URLA = "https://mykey:mykey@api.datamarket.azure.com/Bing/Search/Web?$format=json&Query=%(q)s"
API_KEY = 'WdxgHLzMYWAsYipg/tv/RpK1mFk5YhuFeLQZxH2I1Uw'
URLI = "https://mykey:mykey@api.datamarket.azure.com/Bing/Search/Image?$format=json&Query=%(q)s"
def requester(que, **params):
    que = ('%27'+que+ '%27')
    r = requests.get(URLA % {'q': que}, auth=('', API_KEY))
    return [res['Url'] for res in r.json()['d']['results']]

def check_for_div_parent(mark):
    mark = mark.parent
    if 'div' == mark.name:
        return True
    if 'html' == mark.name:
        return False
    return check_for_div_parent(mark)


def check_for_div_parent(mark):
    mark = mark.parent
    if 'div' == mark.name:
        print "hello"
        return True
    if 'html' == mark.name:
        print "yop"
        return False
    return check_for_div_parent(mark)

def imagery(imaas, **params):
    print "Yolo"
    print imaas
    r = requests.get(URLI % {'q': imaas}, auth=('', API_KEY))
    g = r.json()['d']['results']
    print g[0]['Thumbnail']
    return g[0]['Thumbnail']['MediaUrl']

def splitParagraphIntoSentences(paragraph):
    import re

    sentenceEnders = re.compile('[.!?][\s]{1,2}(?=[A-Z])')
    sentenceList = sentenceEnders.split(paragraph)
    return sentenceList
    if __name__ == '__main__':
        mylist = []
        sentences = splitParagraphIntoSentences(text)
        for s in sentences:
            mylist.append(s.strip())
            for i in mylist:
                print i

def Ti(enter):
    sentence = nltk.word_tokenize(enter)
    sent = pos_tag(sentence)
    alpha = [s for s in sent if s[1] == 'NN'  ]
    for i in range(0,len(alpha)-1):
       for ss in wn.synsets(alpha[i][0]): # Each synset represents a diff concept.
          syno.extend(ss.lemma_names)
          word_counter = {}
    newm =[]
    for i in range(0,len(alpha)-1):
        newm.append (alpha[i][0])

    counts = defaultdict(int)
    for x in newm:
        counts[x]+=1
    #print counts
    popular_words = sorted(counts, key = counts.get, reverse = True)   
    top = popular_words[:8]
    #print top
    results = []
    for i in range(0, len(top)-1):
        indx = sentence.index(top[i])
        results.append(" ".join(sentence[indx-1:indx+2]))
    return results

@app.route('/')
def hello():
    return ''' <a href= /about>About</a>
                <center><br><br><img src="https://lh5.googleusercontent.com/-MISGJsdATlo/Ufo2xq2lGfI/AAAAAAAAAbk/3lG9hKOSN5A/w500-h229-no/PaceByte.png" width = 500px><br><br>
                <br><br><br>

                
                <head>
		<meta name="msvalidate.01" content="C0A6DA20A34D64388F0FA37AD2028052" />
                </head>
                
                <form method="POST" action="/people">
                    <font size = "4">I am looking for?</font><br>
                    <font size = 2>Please enter atleast two words. </font><br><br>
                    <input name="search" type="text" width=1000px>
                    <br>
                    <input type="submit" value="People Search"/>
                    <br>
                </form>

                <form method="POST" action="/science">
                

                    <input name="search" type="text" width=1000px> 
                    <br>
                     <input type="submit" value="Science Search"/>
                     <br>
                     <br>
                     <br>
                     <br>
                     <br>
                     Please send your feedback to: <a href="mailto:'admin@pacebyte.com'">admin@pacebyte.com</a>
                     <script>
                      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                          m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                          })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

                          ga('create', 'UA-42935531-1', 'pacebyte.com');
                          ga('send', 'pageview');

                </script>
                </center>
              </form>'''

@app.route('/about')
def About():
    return '''<html>
                <center>
            
            <img src="https://lh5.googleusercontent.com/-cjODD9V7AXI/UerIKznIVNI/AAAAAAAAAaU/dSi288GNIr4/w500-h229-no/PaceByte.png" width = 500px>
                <br><br><h1> About</h1>
                <body> 
                <font size = 4> PaceByte is an online data mining and aggregation tool that generates write-ups using information available on the internet.
                <script>
                  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                     (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

                      ga('create', 'UA-42935531-1', 'pacebyte.com');
                      ga('send', 'pageview');

                </script>
                    <br>

                 </body>

                </center> '''


@app.route('/people', methods=['POST'])
def PeopleSearch():
    try:
        name = request.form.get('search')
        print (name)
        name = name.title()
        name_s = name.split()
        al = len(name_s)
        if (al < 2):
            return "You need to enter atleast two words"
        for x in range (0,7):
            if profanity[x] in (name):
                return ("We will not process that")
        
        
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    
        
          
        adjEdu = ['school','educa,','university','colleg','scholar','merit','young','teenag']
        ael = (len(adjEdu)-1)
        adjCareer = ['worked','discovered','wrote','develop','won','invent','practiced','study','research','preside','govern','act']
        acl = (len(adjCareer)-1)
        query = name
        raw = query
        searchTerm = (raw)
        
        searchTerm = ('%27'+raw+'%27')
        print "Hi"
        picture = imagery(searchTerm)
        print picture
    except:
        pass

    #Imports Text
    Education =""
    End = ("<font size = 1><center>The information provided on this webpage does not belong to Pace Byte and has been re-quoted from other website whose urls have been embedded in the headline of the articles</center></font>")
    Career =""
    print picture
    QuerySplit = query.split()
    print QuerySplit
    QSL = len(QuerySplit)
    print str(query)
    string = ("")
    summary = ""
    cli =0
    
    

    print QuerySplit[0]
    j = 0
    l = 0
    k = 0
    v = 0
    Abst = "Nothing Here"
    jet = " "
    
    #First Search
    quer =('"' +name+ '"')
    print (quer)
    o = requester(quer)
    #print o
    i = 0
    flag = 0
    Title = raw
    Heading = ("<img src='https://lh5.googleusercontent.com/-cjODD9V7AXI/UerIKznIVNI/AAAAAAAAAaU/dSi288GNIr4/w500-h229-no/PaceByte.png' width = 200px> + <center><font size = 14> " + raw + "</font><br><br><img src='" + picture + "' width =400px></center><br><br>")
    body = ""
    Main = ""
    for f in range(0,len(o)-1):
        if (f>10):
            break
        print "Going"
        url = o[f]
        print url
        if ('wikipedia') not in (url):              #Removes Wikipedia Entries
            if ('youtube') not in (url):
                try:
                    ourUrl = opener.open(url).read()
                except Exception,err:
                    pass
                soup = BeautifulSoup(ourUrl)
                
                for div in soup.findAll('div'):
                        div.replaceWith(Comment(unicode(div)))
                for link in soup.findAll('a', href=True):
                        link.replaceWith(Comment(unicode(link)))
                
                dem = soup.findAll('p')
                #print soup
                print "yo"
                tex = soup.title.string
                Main = (Main + "<a href='" + url + "'>"+ "<font size = 4>" + tex +"</font>" +"</a><br><br>")
                
                backurl = " "
                URL = url
                try:
                    for i in dem:
                       #print i.text
                       if (i.text) not in Main:
                         for k in range (l ,QSL-1):
                            if len(i.text)not in range(0,150):
                              if QuerySplit[k] in i.text:
                                if("@") not in i.text:
                                    if ("http") not in i.text:
                                        for a in range (0,ael):
                                            if adjEdu[a] in (i.text):
                                                if (i.text) not in (Education):
                                                    Education = (Education + i.text )
                                                    continue
                                                
                                        for a in range (0,acl):
                                            if adjCareer[a] in (i.text):
                                                if (i.text) not in (Career):
                                                    Career = (Career + i.text)
                                                    continue
                                                    
                                        if ("born") in (i.text):
                                            summary = (i.text +summary)
                                       
                                        
                                        Main = (Main  +"</center>" + "<font size=5 color=#0080FF >" + i.text+"</font><br>"+"</font>" +"<br><br></font>")
                                        deg = ""
                                        #print (Main)
                                        
                                        #print "In"
                                        body = body +i.text
                                        text = body
                                        
                                        try:
                                            sentences = sent_tokenize(text)
                                            tekan = len(sentences)*0.5
                                            print len(sentences)
                                            collections_tokens = word_tokenize(text)
                                            collection_counter = Counter(collections_tokens)
                                            sent_saliences = []
                                            scored_sents = []
                                            num_to_extract = 1

                                            for index, sentence in enumerate(sentences):
                                                sent_salience = 0
                                                sent_tokens = word_tokenize(sentence)
                                                sent_counter = Counter(sent_tokens)
                                                for token in sent_tokens:
                                                    tf = sent_counter[token]
                                                    idf = log10(len(sentences) / sent_counter[token])
                                                    tfidf = tf * idf
                                                    sent_salience += tfidf
                                                normalized_salience = sent_salience / len(sent_tokens)
                                                sent_saliences.append(normalized_salience)
                                                scored_sents.append((normalized_salience, sentence, index))

                                            scored_sents.sort(key=lambda tup: tup[0], reverse=True)
                                            selected_sents = sorted(scored_sents[:num_to_extract], key=lambda tup: tup[2])
                                        
                                            sum = '%s' % (
                                            ' '.join([i[1] for i in selected_sents]))
                                            if hg != 1:
                                              if (sum) not in (summary):
                                                if ("Born") in(sum):
                                                    fgh = sum
                                                if ("Born") in(sum):
                                                    summary = ("<font size =4"> + sum+"</font>" + summary)
                                                    hg =1
                                                summary = (summary + sum)
                                            print (summary)
                                            
                                        except Exception, err:
                                            continue
                                        
                                        print "Yes"
    
                    continue
                
                except Exception,err:
                    continue
    
    
    #summary = fgh
    Ed = ""
    a = splitParagraphIntoSentences(Education)
    
    for i in range (0,len(a)-1):
        for f in range (0,ael):
            if adjEdu[f] in (a[i]):
                Ed = (Ed + a[i] +"<br>")
                break
    ca = ""
    a = splitParagraphIntoSentences(Career)
    for i in range (0,len(a)-1):
        for f in range (0,acl):
            if adjCareer[f] in (a[i]):
                ca = (ca + a[i] +"<br>")  
                break
    
    string = (Heading +"<font size = 6 color = #0080FF><u>"+"Summary:<br>"+"</u></font>" +"<font size=4>"+summary + "</font><br><br>"
              + "<font size = 6 color = #0080FF><u>Education:</u></font><br><font size=4>" +Ed + "</font><br><br>" + "<font size = 6 color = #0080FF><u>Career:</u></font><br><font size=4>"
              + ca + "</font><br><br>" + "<font size = 6 color = #0080FF><u>Main Content:</u></font><br><br>"+ Main + "<br><br>" + End)
    
    return (string)

@app.route('/science', methods=['POST'])
def ScienceSearch():
    body = ""
    summary =""
    name = request.form.get('search')
    name = name.title()
    name_s = name.split()
    al = len(name_s)
    if (al <2):
        return "You need to enter atleast two words"
    for x in range (0,7):
            if profanity[x] in (name):
                return ("We will not process that")
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    
    Mains = ""
    query = name
    raw = query
            
    # Define search term
    searchTerm = (raw)

    # Replace spaces ' ' in search term for '%20' in order to comply with request
    searchTerm = searchTerm.replace(' ','%20')


    # Start FancyURLopener with defined version 
    class MyOpener(FancyURLopener): 
        version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
    myopener = MyOpener()

    i = 0
    # Set count to 0
    count= 0

    for i in range(0,1):
        # Notice that the start changes for each iteration in order to request a new set of images for each loop
        url = ('https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q='+searchTerm+'&start='+str(i*4)+'&userip=MyIP')
        reques1 = urllib2.Request(url, None, {'Referer': 'testing'})
        response = urllib2.urlopen(reques1)

        # Get results using JSON
        results = simplejson.load(response)
        data = results['responseData']
        dataInfo = data['results']

        # Iterate for each result and get unescaped url
        for myUrl in dataInfo:
            count = count + 1
            d = count
            print myUrl['unescapedUrl']
            picture = myUrl['unescapedUrl']
            for i in range (0,2):
                if i is 2:
                    a = myopener.retrieve(myUrl['unescapedUrl'],str(count)+'.jpg')
        myopener.retrieve(myUrl['unescapedUrl'],str(count)+'.jpg')

#New Scan for formula

     # Define search term
    searchTerm = (raw + 'equation')

    # Replace spaces ' ' in search term for '%20' in order to comply with request
    searchTerm = searchTerm.replace(' ','%20')


    # Start FancyURLopener with defined version 
    class MyOpener(FancyURLopener): 
        version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
    myopener = MyOpener()

    i = 0
    # Set count to 0
    count= 0

    for i in range(0,1):
        # Notice that the start changes for each iteration in order to request a new set of images for each loop
        url = ('https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q='+searchTerm+'&start='+str(i*4)+'&userip=MyIP')
        reques1 = urllib2.Request(url, None, {'Referer': 'testing'})
        response = urllib2.urlopen(reques1)

        # Get results using JSON
        results = simplejson.load(response)
        data = results['responseData']
        dataInfo = data['results']

        # Iterate for each result and get unescaped url
        for myUrl in dataInfo:
            count = count + 1
            d = count
            print myUrl['unescapedUrl']
            picfor = myUrl['unescapedUrl']
            for i in range (0,2):
                if i is 2:
                    a = myopener.retrieve(myUrl['unescapedUrl'],str(count)+'.jpg')
        myopener.retrieve(myUrl['unescapedUrl'],str(count)+'.jpg')


    #scanning done

    adjApp = ['applicat','used in']
    aal = (len(adjApp)-1)
    
    Application = ""
    
    #Imports Text
    print picture
    QuerySplit = query.split()
    print QuerySplit
    QSL = len(QuerySplit)
    print str(query)
    string = ""
    print QuerySplit[0]
    j = 0
    l = 0
    k = 0
    v = 0
    Abst = "Nothing Here"
    jet = " "
    
    #First Search
    quer =('"' +name+ '"')
    print (quer)
    o = requester(quer)
    print o
    i = 0
    flag = 0
    Title = raw
    Heading = ("<img src='https://lh5.googleusercontent.com/-cjODD9V7AXI/UerIKznIVNI/AAAAAAAAAaU/dSi288GNIr4/w500-h229-no/PaceByte.png' width = 200px> + <center><font size = 14> " + raw + "</font><br><br><img src='" + picture + "' width =400px></center><br><br>")
    body = ""
    Main = ""
    for f in range(0,len(o)-1):
        if (f>10):
            break
        print "Going"
        url = o[f]
        print url
        if ('wikipedia') not in (url):              #Removes Wikipedia Entries
            if ('youtube') not in (url):
                ourUrl = opener.open(url).read()
                soup = BeautifulSoup(ourUrl)
            
                dem = soup.findAll('p')
                tex = soup.title.string
                Mains = (Mains + "<a href='" + url + "'>"+ "<font size = 4>" + tex +"</font>" +"</a>" +"<br><br>")
                backurl = " "
                URL = url
                for i in dem:
                                    print (url)
                                    Mains = (Mains  +"</center>" + "<font size = 4>" +i.text + "<br><br> "+"</font>")  
                                    
                                    body = (body +i.text)
                                    text = (body)
                                        
                                    try:
                                            sentences = sent_tokenize(text)
                                            tekan = len(sentences)*0.5
                                            
                                            collections_tokens = word_tokenize(text)
                                            collection_counter = Counter(collections_tokens)
                                            sent_saliences = []
                                            scored_sents = []
                                            num_to_extract = 1
                                            
                                            for index, sentence in enumerate(sentences):
                                                sent_salience = 0
                                                sent_tokens = word_tokenize(sentence)
                                                sent_counter = Counter(sent_tokens)
                                                for token in sent_tokens:
                                                    tf = sent_counter[token]
                                                    idf = log10(len(sentences) / sent_counter[token])
                                                    tfidf = tf * idf
                                                    sent_salience += tfidf
                                                normalized_salience = sent_salience / len(sent_tokens)
                                                sent_saliences.append(normalized_salience)
                                                scored_sents.append((normalized_salience, sentence, index))

                                            scored_sents.sort(key=lambda tup: tup[0], reverse=True)
                                            selected_sents = sorted(scored_sents[:num_to_extract], key=lambda tup: tup[2])
                                        
                                            sum = '%s' % (' '.join([i[1] for i in selected_sents]))
                                            if (sum) not in summary:
                                                summary = ("<font size=4>"+summary +"<br>"+ sum + "</font>")

                                            

                                                        
                   
                                    except Exception,err:
                                        pass
    
                                
     

    string = (Heading +"<font size = 6 color = #0080FF><u>"+"Summary:<br>"+"</u></font>" +"<font size=4>" + summary +"</font><br><br>" +"<font size = 6 color = #0080FF><u>Main Content:</u></font><br><br>"
              + Mains)
    
    return (string)

@app.errorhandler(500)
def pageNotFound(error):
    nopage = ("<br><br><br><br><br><br>"+"<center><font size =6>Oops...your search timed out. Please refresh your page and try again.</font></center>")
    return (nopage)

