#coding:utf8
import nuke
import nukescripts
import check
import openfile
import MakeWrite

tb = nuke.toolbar("Nodes")
m = tb.addMenu("smoke", icon="one_eyed_prince.png")
m.addMenu("Draw")
m.addCommand("Draw/slate", "nuke.createNode('slate')")
m.addCommand("Draw/jonas_slate", "nuke.createNode('jonas_slate')")
m.addCommand("Draw/timecode_burnin", "nuke.createNode('timecode_burnin')")

mb = menubar.addMenu("smoke")
mb.addCommand("Issue_and_Bugs", "nukescripts.start('https://github.com/lazypic/nuke/issues')")
mb.addCommand("slack", "nukescripts.start(https://lazypic.slack.com')")
mb.addCommand("Clip Library", "nukescripts.start('https://www.youtube.com/channel/UC0L_YtB4PWSkOwp2m9587MA/playlists?view_as=subscriber')")
mb.addCommand("StartPerformanceTimers", "nuke.startPerformanceTimers()")
mb.addCommand("StopPerformanceTimers", "nuke.stopPerformanceTimers()")
mb.addCommand("OpenFile", "reload(openfile);openfile.main()", "F8", shortcutContext=2)
mb.addCommand("Write node", "reload(MakeWrite);MakeWrite.main()", "F10", shortcutContext=2)
