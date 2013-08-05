# -*- coding: utf-8 -*-
import urllib
import sys
import time

def main():
    file_name = sys.argv[1]
    phpsessid = sys.argv[2]
    i = 0
    user_tag_set = {}
    for line in open(file_name, 'r'):
        tag_set = set()
        line = line.split('\t')
        id = line[0]
        #print id
        i += 1
        a = urllib.urlopen("http://spapi.pixiv.net/iphone/member_illust.php?id=%s&PHPSESSID=%s" % ( id ,phpsessid))
        time.sleep(1)
        for member_line in a:
            member_array = member_line.split(',')
            if len(member_array) > 13:
                tags = member_array[13].replace('\"', "")
                tag_array = tags.split(' ')
                if u'艦これ'.encode("utf-8") in tag_array: continue
                for tag in tag_array:
                    tag_set.add(tag)
        if(user_tag_set.has_key(id)):
            user_tag_set[id].union(tag_set)
        else:
            user_tag_set[id] = tag_set
    
    for id, tags in user_tag_set.iteritems():
        for tag in tags:
            print id,"\t", tag

if __name__=="__main__":
    main()
