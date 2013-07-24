import os
# -*- coding: cp1252 -*-
import codecs
import time
import urllib2
import urllib
import json as m_json
import os
import sys
from urllib import FancyURLopener
import time
from BeautifulSoup import BeautifulSoup
import json as simplejson
Soup = BeautifulSoup
from nltk import sent_tokenize, word_tokenize
from collections import Counter
from math import log10
# -*- coding: utf-8 *-*
from flask import Flask, request, Response

app = Flask(__name__)
profanity = ['fuck','asshole','sex','faggot','negro','nigger','boob','tit']

@app.route('/')
def hello():
    return ''' <a href= /about>About</a>
                <center><br><br><br><br><img src="https://lh5.googleusercontent.com/-cjODD9V7AXI/UerIKznIVNI/AAAAAAAAAaU/dSi288GNIr4/w500-h229-no/PaceByte.png" width = 500px><br><br>
                <br><br><br>
                
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

                    <br>

                 </body>

                </center> '''


@app.route('/people', methods=['POST'])
def PeopleSearch():
    try:
        name = request.form.get('search')
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
        adjCareer = ['worked','discovered','wrote','develop','won','invent','practiced','study','research','preside','govern']
        query = name
        raw = query
    
        searchTerm = (raw)

        searchTerm = searchTerm.replace(' ','%20')
    

        class MyOpener(FancyURLopener): 
            version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
        myopener = MyOpener()

        i = 0
        count= 0

        for i in range(0,1):
            url = ('https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q='+searchTerm+'&start='+str(i*4)+'&userip=MyIP')
            reques1 = urllib2.Request(url, None, {'Referer': 'testing'})
            response = urllib2.urlopen(reques1)

            results = simplejson.load(response)
            data = results['responseData']
            dataInfo = data['results']

            for myUrl in dataInfo:
                count = count + 1
                d = count
                print myUrl['unescapedUrl']
                picture = myUrl['unescapedUrl']
                for i in range (0,2):
                    if i is 2:
                        a = myopener.retrieve(myUrl['unescapedUrl'],str(count)+'.jpg')
            myopener.retrieve(myUrl['unescapedUrl'],str(count)+'.jpg')

    except Exception,err:
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
    file = open('/Py/testfile.html','w')
    jet = " "
    
    #First Search
    query = urllib.urlencode ( { 'q' : 'who is '+query } )
    
    
    response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()                           
    json = m_json.loads ( response )
    results = json [ 'responseData' ] [ 'results' ]
    i = 0
    flag = 0
    Title = raw
    Heading = ("<img src='https://lh5.googleusercontent.com/-cjODD9V7AXI/UerIKznIVNI/AAAAAAAAAaU/dSi288GNIr4/w500-h229-no/PaceByte.png' width = 200px> + <center><font size = 14> " + raw + "</font><br><br><img src='" + picture + "' width =400px></center><br><br>")
    body = ""
    Main = ""
    for result in results :
        url = result['url']
        if ('wikipedia') not in (url):              #Removes Wikipedia Entries
            if ('youtube') not in (url):                
                ourUrl = opener.open(url).read()
                soup = BeautifulSoup(ourUrl)
                dem = soup.findAll('p')
                tex = soup.title.string
                Main = (Main + "<a href='" + url + "'>"+ "<font size = 4>" + tex +"</font>" +"</a>" +"<br><br>")
                print ( url )
                print query
                backurl = " "
                URL = url
                try:
                    for i in dem:
                    #Filter
                      if (i.text) not in string:
                         for k in range (l ,QSL-1):
                            if len(i.text)not in range(0,150):
                              if QuerySplit[k] in i.text:
                                if("@") not in i.text:
                                    if ("http") not in i.text:
                                        for a in range (0,8):
                                            if adjEdu[a] in (i.text):
                                                Education = (Education + i.text + "<br><br>")
                                                print Education
                                        for a in range (0,11):
                                            if adjCareer[a] in (i.text):
                                                Career = (Career + i.text + "<br><br>")
                                        if ("born") in (i.text):
                                            summary = (i.text +summary)            
                                        Main = (Main  +"</center>" + i.text + "<br><br> ")
                                        print (Main)
                                        string = (Heading +"<font size = 6 color = #0080FF><u>"+"Summary:<br>"+"</u></font>" +summary + "<br><br>" + "<font size = 6 color = #0080FF><u>Education:</u></font><br>" +Education + "<br><br>" + "<font size = 6 color = #0080FF><u>Career:</u></font><br>" + Career + "<br><br>" + "<font size = 6 color = #0080FF><u>Main Content:</u></font><br><br>"+ Main + "<br><br>" + End)
                                        file = open('/Py/SummarySearch.html', 'w')
                                        a = string.encode('utf-8')
                                        file.write(a) 
                                        file.flush()
                                        print "In"
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
                                            if (sum) not in (summary):
                                                if ("Born") in(sum):
                                                    summary = (sum+summary)
                                                summary = (summary+sum)
                                            print (summary)
                                        except Exception, err:
                                            continue
                                        #querycurs.execute('UPDATE Data1 SET info =? WHERE q =?',(string,raw))
                                        #CreateDB.commit()
                                        print "Yes"
    
                                       
                except Exception,err:
                    continue
    return (string)

    #Second Search
    query = urllib.urlencode ( { 'q' : query + " born"} )
    
    
    response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()                           
    json = m_json.loads ( response )
    results = json [ 'responseData' ] [ 'results' ]
    i = 0
    flag = 0
    Title = raw
    Heading = ("<center><font size = 14> " + raw + "</font><br><br><img src='" + picture + "' width =400px></center><br><br>")
        
    for result in results :
        url = result['url']
        if ('wikipedia') and ('biography')not in (url):              #Removes Wikipedia Entries
            if ('youtube') not in (url):                
                ourUrl = opener.open(url).read()
                soup = BeautifulSoup(ourUrl)
                dem = soup.findAll('p')
                tex = soup.title.string
                Main = (Main + "<a href='" + url + "'>"+ "<font size = 4>" + tex +"</font>" +"</a>" +"<br><br>")
                print ( url )
                print query
                backurl = " "
                URL = url
                try:
                    for i in dem:
                         al = len(i.text)
                         for k in range (l ,QSL-1):
                             for a in range (0,8):
                                    if adjEdu[a] in (i.text):
                                        if (i.text) not in (Education):
                                            Education = (Education + i.text + "<br><br>")
                                            print Education
                             for a in range (0,11):
                                    if adjCareer[a] in (i.text):
                                        if (i.text) not in (Career):
                                            Career = (Career + i.text + "<br><br>")
                             if ("born") in (i.text):
                                   summary = (i.text +summary)            
                             Main = (Main  +"</center>" + i.text + "<br><br> ")                             
                             string = (Heading +"<font size = 6 color = #0080FF><u>"+"Summary:<br>"+"</u></font>" +summary + "<br><br>" + "<font size = 6 color = #0080FF><u>Education:</u></font><br>" +Education + "<br><br>" + "<font size = 6 color = #0080FF><u>Career:</u></font><br>" + Career + "<br><br>" + "<font size = 6 color = #0080FF><u>Main Content:</u></font><br>"+ Main + "<br><br>" +"<center>" +End + "</center>")
                             return (string)
                             file = open('/Py/SummarySearch.html', 'w')
                             a = string.encode('utf-8')
                             file.write(a) 
                             file.flush()
                             if QuerySplit[k] in i.text:
                                if("@") not in i.text:
                                  if("#") not in i.text:
                                     if ("(") not in i.text:
                                       if ("http") not in i.text:
                                        Main = (Main  +"</center>" + i.text + "<br><br> ")
                                        print "In"
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
                                            if (sum) not in (summary):
                                                if ("Born") in (i.text):
                                                    summary = (i.text +summary)
                                                if ("Born") in(sum):
                                                    print "Born is Here"
                                                    summary = (sum+summary)
                                                else:
                                                    summary = (summary+sum)
                                            print summary
                                        except Exception,err:
                                            continue
                                        string = (Heading +"<font size = 6 color = #0080FF><u>"+"Summary:<br>"+"</u></font>" +summary + "<br><br>" + "<font size = 6 color = #0080FF><u>Education:</u></font><br>" +Education + "<br><br>" + "<font size = 6 color = #0080FF><u>Career:</u></font><br>" + Career + "<br><br>" + Main + "<br><br>" +"<center>" +End+"</center>")
                                        file = open('/Py/SummarySearch.html', 'w')
                                        a = string.encode('utf-8')
                                        file.write(a) 
                                        file.flush()

                                        #querycurs.execute('UPDATE Data1 SET info =? WHERE q =?',(string,raw))
                                        #CreateDB.commit()
                                        print "Yes"
    
                                       
                except Exception,err:
                    continue
    
    print "Done"
    return (string)

@app.route('/science', methods=['POST'])
def ScienceSearch():
    
    name = request.form.get('search')
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

    

    adjApp = ['applicat','used in']
    
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
    file = open('/Py/testfile.html','w')
    jet = " "
    
    #First Search
    query = urllib.urlencode ( { 'q' : 'what is '+query } )
    
    
    response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()                           
    json = m_json.loads ( response )
    results = json [ 'responseData' ] [ 'results' ]
    i = 0
    flag = 0
    Title = raw
    Heading = ("<center><font size = 14> " + raw + "</font><br><br><img src='" + picture + "' width =400px></center><br><br>")
    for result in results :
        
        url = result['url']
        if ('wikipedia') not in (url):              #Removes Wikipedia Entries
            if ('youtube') not in (url):
                ourUrl = opener.open(url).read()
                soup = BeautifulSoup(ourUrl)
            
                dem = soup.findAll('p')
                tex = soup.title.string
                Mains = (Mains + "<a href='" + url + "'>"+ "<font size = 4>" + tex +"</font>" +"</a>" +"<br><br>")
                backurl = " "
                URL = url
                try:
                    for i in dem:

                        Mains = (Mains  +"</center>" + i.text + "<br><br> ")
                        string = (Heading +"<font size = 6 color = #0080FF><u>"+"Application:<br>"+"</u></font>" + Application + "<br><br>" +"<font size = 6 color = #0080FF><u>Main Content:</u></font><br><br>"+ Mains)
                        print "Works"
                        file = open('/Py/Science.html', 'w')
                        a = string.encode('utf-8')
                        file.write(a) 
                        file.flush()
                        print "Yes"
                        #for r in range (0,2):     
                         #  if adjApp[r] in (i.text):
                          #   Application = (Application +i.text)       
                                
                        print "Yes"
                                       
                except:
                    pass
    
                                
        
    #Second Search
    querya = urllib.urlencode ( { 'q' : raw } )
    print querya
    response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + querya).read()
    raw = querya
    json = m_json.loads ( response )
    results = json [ 'responseData' ] [ 'results' ]
    i = 0
    for result in results :
        url = result['url']
        if ('wikipedia') not in (url):              #Removes Wikipedia Entries
            if ('youtube') not in (url):
                ourUrl = opener.open(url).read()
                soup = BeautifulSoup(ourUrl)
                dem = soup.findAll('p')
                tex = soup.title.string
                Mains = (Mains + "<a href='" + url + "'>" + "<font size = 4>"+tex + "</font>"+"</a>" +"<br>")
                print ( url )
                print (querya)
                URL = url
                try:
                    for i in dem:
                            Mains = (Mains  +"</center>" + i.text + "<br><br> ")
                            string = (Heading +"<font size = 6 color = #0080FF><u>"+"Application:<br>"+"</u></font>" + Application + "<br><br>" +"<font size = 6 color = #0080FF><u>Main Content:</u></font><br><br>"+ Mains)
                            file = open('/Py/Science.html', 'w')
                            a = string.encode('utf-8')
                            file.write(a) 
                            file.flush()
                            #for r in range (0,2):     
                            #    if adjApp[r] in (i.text):
                            #        Application = (Application +i.text + "<br><br>")
                            
                            #querycurs.execute('UPDATE Data1 SET info =? WHERE q =?',(string,raw))
                            #CreateDB.commit()
                            print "Yes"
                                       
                except:
                    pass
    return (string)





