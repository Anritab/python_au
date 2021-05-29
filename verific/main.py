TOKEN = ''

import requests

PREFIX = ['LEETCODE', 'GENERATOR', 'TRIANGLE', 'HEXNUMBER']
GROUP = ['1021', '1022']
ACTION = ['Added', 'Deleted']

def prepare_headers():
  return{'Authorization': 'Token {}'.format(TOKEN),
         'Content-Type': "application/json",
         'Accept': "application/vnd.github.v3+json"
        }

def create_link (user_name, repos_name):
  return 'https://api.github.com/repos/{}/{}/pulls?state=open'.format(user_name, repos_name)

def return_pullreq(user_name, repos_name):
  pulls = requests.get(create_link(user_name, repos_name), headers=prepare_headers())
  return pulls

def return_commits(req):
  comms = []
  commits = requests.get(req['commits_url'], headers=prepare_headers())
  for com in commits.json():
    comm = com['commit']
    comms.append((comm['message']))
  return comms

def check_comment(msg):
  res = []
  mass = []
  mass = msg.split('-')
  pre = mass[0]
  post = mass[1].split(' ')
  if pre not in PREFIX:
    res.append("Prefix of commit {}".format(PREFIX))
  if post[0] not in GROUP:
    res.append("Number of group {}".format(GROUP))
  if len(post) > 1 and post[1] not in ACTION:
    res.append("Action of comment {}".format(ACTION))
  return '\n'.join(res)

def create_message(pull_req):
  msg = "Pull request: {}\n".format(pull_req['title'])
  msg += check_comment(pull_req['title'])
  msg += '\n\n'
  for com in return_commits(pull_req):
    msg += 'Commit: {}\n'.format(com)
    msg += check_comment(com)
    msg += '\n'
  return msg

def sendmsg(pull_req, msg):
  data = {'body': msg,
          'path': requests.get(pull_req['url']+'/files', headers=prepare_headers()).json()[0]['filename'],
          'position': 1,
          'commit_id': pull_req['head']['sha']}
  r = requests.post(pull_req['url']+'/comments', headers=prepare_headers(), json=data)
  print(r.json())

def main():
  for pr in return_pullreq('Anritab', 'python_au').json():
    if len(create_message(pr)) != 0:
      sendmsg(pr, create_message(pr))

main()
