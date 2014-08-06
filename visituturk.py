import urllib2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-w', '--wids', type=str, dest='workerid_file', default='ids.txt')
parser.add_argument('-t', '--target', type=str, dest='target_project', default='9e0e88e7ebcd8e42c7445933fef4c1d2')
args = parser.parse_args()

#print(parser)
#print(args)

baseurl = 'http://uniqueturker.myleott.com/'
workerid_file = args.workerid_file
target_project = args.target_project

print 'Reading %s' % workerid_file
print 'Targeting project %s' % target_project

with open(workerid_file, mode='r') as fin:
    for line in fin:
        targ_url = baseurl + target_project + '/' + line.strip()
        print(targ_url)
        response = urllib2.urlopen(targ_url)
        print(response.read())


