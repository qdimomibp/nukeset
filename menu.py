import nuke

tb = nuke.toolbar("Nodes")
m = tb.addMenu("smoke", icon="one_eyed_prince.png")
m.addMenu("Draw")
m.addCommand("Draw/slate", "nuke.createNode('slate')")
m.addCommand("Draw/timecode_burnin", "nuke.createNode('timecode_burnin')")
