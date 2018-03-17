#! /usr/bin/env python
# -*- coding: utf-8 *-*

fr = open('sendTelCode.txt')

stat = {}

for line in fr:
  if len(line) == 0:
    continue
  ip = line.split(' - - ')[0]

  if not stat.has_key(ip):
    stat[ip] = 0
  stat[ip] +=1

stat = sorted(stat.iteritems(), key = lambda d:d[1], reverse = True)

fw = open("banthis.resore",'w')
fw.write('create banthis hash:net family inet hashsize 1024 maxelem 65536\n')

for item in stat:
  if item[1] >= 10:
    #fw.write( item[0] + ',' + str(item[1]) + '\n')
    fw.write( 'add banthis ' + item[0] + '\n')
  else:
    pass

fw.close() 

fr.close()
