# constants used in more than one module
# Some of them might find a better home later.

from lib.nofloat import PRECISION


MAIN_METASERVER_URL = open("cfg/metaserver.txt").read().strip()

# old value used by some features (stats, ...)
METASERVER_URL = "http://jlpo.free.fr/soundrts/metaserver/"

# simulation
VIRTUAL_TIME_INTERVAL = 300 # milliseconds
COLLISION_RADIUS = 175 # millimeters # 350 / 2
USE_RANGE_MARGIN = 175 # millimeters
ORDERS_QUEUE_LIMIT = 10
MAX_NB_OF_RESOURCE_TYPES = 10
DEFAULT_MINIMAL_DAMAGE = int(.17 * PRECISION)

# used for packing the orders
NEWLINE_REPLACEMENT = ";"
SPACE_REPLACEMENT = ","

# minimal interval (in seconds) between 2 sounds
ALERT_LIMIT = .5
FOOTSTEP_LIMIT = .1

# don't play events after this limit (in seconds)
EVENT_LIMIT = 3

# use the profiler (warning: will slow down the game)
PROFILE = False
