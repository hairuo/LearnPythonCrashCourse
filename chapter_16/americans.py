from pygal.maps.world import World

wm = World()
wm.title = 'North, Centrial, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
	'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.add('China', ['cn'])
wm.add('Japan', ['jp'])
wm.add('Australia', ['au'])
wm.add('New Zealand', ['nz'])
wm.add('Antarctica', ['aq'])
wm.add('India', ['in'])
# see more: 
# http://www.pygal.org/en/stable/documentation/types/maps/pygal_maps_world.html	
	
wm.render_to_file('americas.svg')
