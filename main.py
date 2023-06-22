from nicegui import ui

# Theming
ui.query('body').style('background-color: #630000')
ui.colors(primary='#bf3a3a')

ui.markdown('# ***zdkrimson : A Minecraft Launcher***')

ui.run(dark=True, native=True)