from slack_webhook import Slack
#import os
cont="Today Sunshine to start, then a few afternoon clouds. High 79F. Winds E at 10 to 15 mph."

def posttochannel(chanfile):
    with open(chanfile, "r") as myfile:
     token=myfile.read().replace('\n','').replace('-', ' ')
    slack = Slack(url=token)
    slack.post(text=cont)

posttochannel("chan1.txt")
posttochannel("chan2.txt")
posttochannel("chan3.txt")
posttochannel("chan4.txt")
posttochannel("chan5.txt")
