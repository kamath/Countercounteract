import sys
import fbchat
import markovify

thread = sys.argv[1]
client = fbchat.Client(USERNAME, PASSWORD)

last_messages = client.getThreadInfo(thread,100)
last_messages.reverse()  # messages come in reversed order

messages = ""

for i, message in enumerate(last_messages):
	print message.author
	if str(thread) not in message.author:
		messages += message.body+"\n"

insults = ""
with open('shittalk.txt') as f:
	for a in f.readlines():
		insults+=a.split('" "')[1]+'\n'

self_model = markovify.Text(messages)
insults_model = markovify.Text(insults)

model_combo = markovify.combine([ self_model, insults_model ], [ 1.5, 1 ])

for i in range(5):
	if model_combo.make_sentence() != None:
		sent = client.send(thread, model_combo.make_sentence())
		break