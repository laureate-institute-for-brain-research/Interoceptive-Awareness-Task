#from psychopy import prefs
#prefs.general['audioLib'] = [u'pyo', u'pygame']
#prefs.general['audioLib'] = [u'pygame']
#prefs.general[u'audioDriver'] = [u'ASIO4ALL', u'ASIO', u'Audigy']


from psychopy import event, core, visual, gui, sound, monitors, data#, microphone
import csv, os, ctypes, ast, numpy, StimToolLib, pyo, sys, logging, VMeter



c = core.Clock()
c.reset()


VMeter.print_devices()
vMeter = VMeter.VMeter()
VMeter.print_devices()

vMeter.close()
VMeter.print_devices()
vMeter = VMeter.VMeter()

for i in range(100000):
    
    if i % 100 == 0:
        print i
    vMeter.clear()
    vMeter.send_column(i % 127)
    vMeter.send_config(120) #set to return 127 at touch and 0 at release (119 disables)
    vMeter.send_config(123) #disable touch position output--we're only interested in touch time, not location, for this task (124 reenables it)
    vMeter.send_config(107) #don't let lights respond to touch--will control them manually and make all light up together regardless of finger position (106 reenables)

    vMeter.send_config(119) #set to return 127 at touch and 0 at release (119 disables)
    vMeter.send_config(124) #disable touch position output--we're only interested in touch time, not location, for this task (124 reenables it)
    vMeter.send_config(106) #don't let lights respond to touch--will control them manually and make all light up together regardless of finger position (106 reenables)
    vMeter.read_settings()
vMeter.close()
    
    
core.quit()
prefix = 'test.txt'
    
sys.stdout = open(prefix, 'a', 0)
sys.stderr = open(prefix, 'a', 0)

print 'test'
sys.stdout.close()
sys.stderr.close()
core.wait(20)
core.quit()


win = visual.Window(fullscr=True, screen=0,color=(-1,-1,-1), waitBlanking=True, colorSpace='rgb',winType='pyglet')

win.flip()

all_presses = []
while c.getTime() < 20:
    these_keys = event.getKeys(keyList = None, timeStamped = True)
    if these_keys:
        print these_keys
        for k in these_keys:
            all_presses.append(k[1])

print all_presses
out = open('keytimes.csv', 'w')
out.write(str(all_presses))
out.close()


print times
print numpy.mean(times)
print numpy.std(times)

#print times 

core.quit()

idx1 = range(8)
random.shuffle(idx1)
idx2 = range(3)
idx_list = []
for i in idx1:
    random.shuffle(idx2)
    idx_list.append(i*3 + idx2[0])
    idx_list.append(i*3 + idx2[1])
    idx_list.append(i*3 + idx2[2])

print idx_list
core.quit()

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

l = range(24)
c = chunks(l, 3)
cl = list(c)
random.shuffle(cl)


print cl
core.quit()




win = visual.Window(fullscr=True, screen=1,color=(-1,-1,-1), waitBlanking=False, colorSpace='rgb',winType='pyglet')

for i in range(13):
    print i
    event.waitKeys(keyList = None)
core.quit()


output = open('SS/schedule0.csv', 'w')
d = os.listdir('SS/media')
#d.sort()
d = sorted(d, key=lambda s: s.lower())
output.write('TrialTypes,Stimuli,Durations,ExtraArgs\n')
for line in d:
    output.write(',' + 'media/' + line + ',3,\n')
    
output.close()
core.quit()

s = sound.Sound(value='SS_50ms.wav')

core.wait(2)

print 'playing'
s.play()
print 'played'
print s.getDuration()
core.wait(2)

print 'playing'
s.play()
print 'played'

core.wait(1)

core.quit()

#exp_order = csv.reader(open('MID\schedule1.csv'))
output = open('temp.csv', 'w')



line = exp_order.next()
output.write(line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + '\n')

for line in exp_order:
    print line
    d = line[2].split()
    print d
    output.write(line[0] + ',' + line[1] + ',' + d[1] + ' ' + d[0] + ',' + line[3] + '\n')
    
core.quit()
output = open('temp.csv', 'w')


