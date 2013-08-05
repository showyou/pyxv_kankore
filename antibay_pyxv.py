# -*- coding: utf-8 -*-
import urllib
import sys
import time


def main():
  keyword = sys.argv[1]
  file_name = sys.argv[2]
  page_max = int(sys.argv[3])
  if len(sys.argv) == 5:
    phpsessid = sys.argv[4]
  else:
    phpsessid = ''
  with open(file_name, 'w') as wfp:
    print page_max, file_name
    for p in range(page_max):
      a = urllib.urlopen("http://spapi.pixiv.net/iphone/search.php?s_mode=s_tag&p=" + str(p) + "&word=" + keyword + "&PHPSESSID=" + phpsessid)
      time.sleep(1)
      for line in a:
        line = line.split(',')
        if len(line) > 13 and keyword in line[13]:
          user_id = line[1].replace('\"', "")
          wfp.write(str(user_id)+"\t"+ line[12].replace('\"', '') +"\t"+ line[13].replace('\"', '') + "\n")


if __name__=="__main__":
  if len(sys.argv) < 4:
    print "error occurred. please, 3 or more arguments. arguments is 1.tag-keyword 2.output-file-name 3. get-page-max 4.phpsessid"
    sys.exit()
  main()
