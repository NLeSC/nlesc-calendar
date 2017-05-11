roomOutlookIds = {
    'cloud-chamber'    : '',
    'library'          : '',
    'stellarator'      : '',
    'compass'          : '',
    'observa​​tory​​​​'      : '',
    'mass-spectrometer': '',
    'microscope'       : '',
    'radar'            : ''
}

roomsUpstairs = [
    { 'id': 'cloud-chamber', 'title': 'Cloud Chamber', 'eventColor': 'blue'   },
    { 'id': 'library'      , 'title': 'Library'      , 'eventColor': 'green'  },
    { 'id': 'stellarator'  , 'title': 'Stellarator'  , 'eventColor': 'orange' }
]

roomsDownstairs = [
    { 'id': 'radar'             , 'title': 'Radar'  , 'eventColor': 'blue' },
    { 'id': 'compass'           , 'title': 'Compass', 'eventColor': 'green' },
    { 'id': 'microscope'        , 'title': 'Microscope', 'eventColor': 'orange' },
    { 'id': 'mass-spectrometer' , 'title': 'Mass Spectrometer', 'eventColor': 'red' },
    { 'id': 'observa​​tory​​​​' , 'title': 'Observa​​tory​​​​', 'eventColor': 'blue' }
]

locations = {
    'up'  : { 'title': 'Upstairs'  , 'rooms': roomsUpstairs   },
    'down': { 'title': 'Downstairs', 'rooms': roomsDownstairs }
}
