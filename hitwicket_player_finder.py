from __future__ import division
import mechanize
from BeautifulSoup import BeautifulSoup as bs
import urllib2
import re
 
 
br = mechanize.Browser()
#list of teams in leagues
teams = []
state_players = {}


#VARIABLES 
STATE = "Kerala"
USERNAME = "username"
PASS = "password"
NUMBER = 30





br.open("http://hitwicket.com")
br.select_form(nr=0)
br["LoginForm[email]"] = USERNAME
br["LoginForm[password]"] = PASS
br.submit()

def addTeamsFromLeague(league_number):
	br.open("http://hitwicket.com/league/show/{0}".format(league_number))
	html = br.response().read()
	soup = bs(html)
	allTd = soup.findAll("td")
	for i in allTd:
		try:
			teams.append("http://hitwicket.com/players/index/" + i.a["href"].split('/')[-2])
		except:
			pass
 
def getAllPlayersFromTeam(team_link):
	print "team:", team_link
	link = team_link + "?skill=skill_index&ajax=true"
	# print "link", link
	br.open(link)
	html = br.response().read()
	soup = bs(html)
	alla = soup.findAll("a")[:NUMBER]
	#print alla
	players = []
	for i in alla:
		players.append("http://hitwicket.com" + i["href"])
	return players

def playerBelongsToState(player_url, state=STATE):
	global state_players
	try:
		response = urllib2.urlopen(player_url)
		str_content = response.read().decode('utf-8')
		matchs= re.search('<div class="level">([\w\s()]+)</div>',str_content)
		if matchs:
			if matchs.group(1) == state:
				skill_index = re.search('<span class=\"skill_value show_tooltip\" title=\"This is a metric used to measure the overall skill set of your players that gives a general idea of the player\'s worth\">[\s]+([\w\d,]+)[\s]+',str_content)
				if skill_index:
					skill = int(skill_index.group(1).replace(',',''))
					state_players[skill] = player_url
					#print player_url
					return True
	except urllib2.HTTPError:
		print 'There was an error with the request'
	return False
 
def main():
	global state_players
	import sys
	# print sys.argv[1]
	leagues = xrange(int(sys.argv[1]), int(sys.argv[2]))
	for i in leagues:
		#print i
		addTeamsFromLeague(i)
	l = len(teams)
	c = 1
	print l, "teams"
	for i in teams:
		players =  getAllPlayersFromTeam(i)
		for j in players:
			#print j
			if playerBelongsToState(j):
				pass
		print c/l * 100, "% done..." 
		c+=1
	#print state_players
	sort = sorted(state_players)
	#print sort
	f = open("{0}-players.txt".format(STATE), "w")
	f.write("{0}       {1}\n".format("skill","player_url"))
	for i in sort:
		print i, state_players[i]
		
		f.write("{0}		{1}\n".format(i, state_players[i]))
	f.close()
 
if __name__ == '__main__':
	main()
