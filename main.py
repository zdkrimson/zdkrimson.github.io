from nicegui import ui

# Theming
ui.query('body').style('background-color: #630000')
ui.colors(primary='#bf3a3a')

# with ui.image('https://github.com/zdkrimson/zdkrimson.github.io/blob/main/assets/bg/blur/crim1.png?raw=true'):

with ui.card().tight() as card:
with ui.splitter() as splitter:
	with splitter.before:
		ui.image('assets/logo/image/shaded/white.png')
	with splitter.after:
		ui.markdown('## ***zdkrimson : A Minecraft Launcher***')
		ui.label('A Minecraft Laucnher packed with Quality-Of-Life features.')


ui.run(dark=True, native=True)