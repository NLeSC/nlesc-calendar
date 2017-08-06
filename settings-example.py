roomOutlookIds = {
    'cloud-chamber'    : '',
    'library'          : '',
    'stellarator'      : '',
    'compass'          : '',
    'observatory'      : '',
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
    { 'id': 'observatory' , 'title': 'Observatory', 'eventColor': 'blue' }
]

locations = {
    'up'  : { 'title': 'Upstairs'  , 'rooms': roomsUpstairs  , map: 'img/nlesc_room_name_map_down.png' },
    'down': { 'title': 'Downstairs', 'rooms': roomsDownstairs, map: 'img/nlesc_room_name_map_up.png' }
}
