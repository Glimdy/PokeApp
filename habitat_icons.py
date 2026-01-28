# Pokémon-style habitat icons as SVG base64 data
# These can be embedded directly in HTML or CSS

HABITAT_ICONS = {
    'forest': {
        'name': 'Forest',
        'emoji': '🌲',
        'svg': '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <!-- Sky background -->
            <rect width="100" height="60" fill="#87CEEB"/>
            <!-- Ground -->
            <rect y="60" width="100" height="40" fill="#8B7355"/>
            <!-- Trees -->
            <polygon points="20,60 10,40 30,40" fill="#2D5016"/>
            <polygon points="20,50 15,35 25,35" fill="#3D6B1F"/>
            <rect x="18" y="55" width="4" height="5" fill="#8B4513"/>
            <polygon points="50,60 35,35 65,35" fill="#2D5016"/>
            <polygon points="50,50 40,30 60,30" fill="#3D6B1F"/>
            <rect x="48" y="52" width="4" height="8" fill="#8B4513"/>
            <polygon points="80,60 70,40 90,40" fill="#2D5016"/>
            <polygon points="80,50 73,38 87,38" fill="#3D6B1F"/>
            <rect x="78" y="55" width="4" height="5" fill="#8B4513"/>
        </svg>''',
    },
    'cave': {
        'name': 'Cave',
        'emoji': '⛏️',
        'svg': '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <!-- Dark background -->
            <rect width="100" height="100" fill="#2C2C2C"/>
            <!-- Cave opening -->
            <ellipse cx="50" cy="40" rx="25" ry="20" fill="#1A1A1A"/>
            <!-- Cave entrance rocks -->
            <polygon points="25,60 20,50 30,50" fill="#555"/>
            <polygon points="75,60 70,50 80,50" fill="#555"/>
            <!-- Stalactites -->
            <polygon points="35,20 33,35 37,35" fill="#444"/>
            <polygon points="65,20 63,35 67,35" fill="#444"/>
            <!-- Cave floor rocks -->
            <polygon points="30,80 25,70 35,70" fill="#555"/>
            <polygon points="70,80 65,70 75,70" fill="#555"/>
            <!-- Glow effect -->
            <circle cx="50" cy="50" r="15" fill="#3A5F8F" opacity="0.3"/>
        </svg>''',
    },
    'ocean': {
        'name': 'Ocean',
        'emoji': '🌊',
        'svg': '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <!-- Sky background -->
            <rect width="100" height="40" fill="#87CEEB"/>
            <!-- Water -->
            <rect y="40" width="100" height="60" fill="#1E90FF"/>
            <!-- Waves -->
            <path d="M 0,40 Q 12.5,35 25,40 T 50,40 T 75,40 T 100,40" stroke="#4A90E2" stroke-width="2" fill="none"/>
            <path d="M 0,55 Q 12.5,50 25,55 T 50,55 T 75,55 T 100,55" stroke="#4A90E2" stroke-width="2" fill="none"/>
            <!-- Fish -->
            <ellipse cx="30" cy="65" rx="6" ry="4" fill="#FF6B6B"/>
            <polygon points="36,65 42,63 42,67" fill="#FF6B6B"/>
            <ellipse cx="70" cy="75" rx="5" ry="3" fill="#FFD93D"/>
            <polygon points="75,75 80,74 80,76" fill="#FFD93D"/>
            <!-- Bubbles -->
            <circle cx="50" cy="70" r="2" fill="#87CEEB" opacity="0.5"/>
            <circle cx="45" cy="80" r="1.5" fill="#87CEEB" opacity="0.5"/>
        </svg>''',
    },
    'mountain': {
        'name': 'Mountain',
        'emoji': '⛰️',
        'svg': '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <!-- Sky background -->
            <rect width="100" height="60" fill="#87CEEB"/>
            <!-- Ground -->
            <rect y="60" width="100" height="40" fill="#8B7355"/>
            <!-- Left mountain -->
            <polygon points="0,60 30,20 60,60" fill="#696969"/>
            <!-- Right mountain -->
            <polygon points="40,60 70,25 100,60" fill="#505050"/>
            <!-- Snow peaks -->
            <polygon points="30,20 25,30 35,30" fill="#FFFFFF"/>
            <polygon points="70,25 65,35 75,35" fill="#FFFFFF"/>
            <!-- Clouds -->
            <ellipse cx="20" cy="15" rx="10" ry="6" fill="#FFFFFF" opacity="0.7"/>
            <ellipse cx="85" cy="20" rx="12" ry="7" fill="#FFFFFF" opacity="0.7"/>
        </svg>''',
    },
    'desert': {
        'name': 'Desert',
        'emoji': '🏜️',
        'svg': '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <!-- Sky background -->
            <rect width="100" height="50" fill="#87CEEB"/>
            <!-- Sand -->
            <rect y="50" width="100" height="50" fill="#EDC9AF"/>
            <!-- Sand dunes -->
            <ellipse cx="20" cy="70" rx="20" ry="12" fill="#DEB887"/>
            <ellipse cx="70" cy="75" rx="25" ry="15" fill="#DEB887"/>
            <!-- Cactus -->
            <rect x="45" y="65" width="8" height="25" fill="#228B22"/>
            <rect x="35" y="75" width="6" height="8" fill="#228B22"/>
            <rect x="57" y="75" width="6" height="8" fill="#228B22"/>
            <!-- Sun -->
            <circle cx="85" cy="20" r="10" fill="#FFD700"/>
            <!-- Sand ripples -->
            <path d="M 0,85 Q 12.5,82 25,85" stroke="#C9A876" stroke-width="1" fill="none" opacity="0.5"/>
            <path d="M 30,90 Q 42.5,87 55,90" stroke="#C9A876" stroke-width="1" fill="none" opacity="0.5"/>
        </svg>''',
    },
    'fields': {
        'name': 'Fields',
        'emoji': '🌾',
        'svg': '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <!-- Sky background -->
            <rect width="100" height="60" fill="#87CEEB"/>
            <!-- Ground -->
            <rect y="60" width="100" height="40" fill="#90EE90"/>
            <!-- Grass tufts -->
            <line x1="15" y1="65" x2="12" y2="50" stroke="#228B22" stroke-width="2"/>
            <line x1="25" y1="65" x2="23" y2="48" stroke="#228B22" stroke-width="2"/>
            <line x1="35" y1="65" x2="32" y2="50" stroke="#228B22" stroke-width="2"/>
            <line x1="50" y1="65" x2="48" y2="45" stroke="#228B22" stroke-width="2"/>
            <line x1="65" y1="65" x2="63" y2="48" stroke="#228B22" stroke-width="2"/>
            <line x1="80" y1="65" x2="78" y2="50" stroke="#228B22" stroke-width="2"/>
            <!-- Flowers -->
            <circle cx="20" cy="75" r="2" fill="#FF69B4"/>
            <circle cx="55" cy="78" r="2" fill="#FFD700"/>
            <circle cx="85" cy="75" r="2" fill="#FF1493"/>
            <!-- Sun -->
            <circle cx="85" cy="15" r="8" fill="#FFD700"/>
        </svg>''',
    },
    'urban': {
        'name': 'Urban',
        'emoji': '🏙️',
        'svg': '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <!-- Sky background -->
            <rect width="100" height="60" fill="#87CEEB"/>
            <!-- Ground/Street -->
            <rect y="60" width="100" height="40" fill="#696969"/>
            <!-- Buildings -->
            <rect x="10" y="35" width="20" height="25" fill="#8B7355"/>
            <rect x="35" y="25" width="20" height="35" fill="#A9A9A9"/>
            <rect x="60" y="40" width="20" height="20" fill="#8B7355"/>
            <!-- Windows -->
            <rect x="12" y="40" width="3" height="3" fill="#FFFF00"/>
            <rect x="17" y="40" width="3" height="3" fill="#FFFF00"/>
            <rect x="12" y="48" width="3" height="3" fill="#FFFF00"/>
            <rect x="17" y="48" width="3" height="3" fill="#FFFF00"/>
            <rect x="37" y="30" width="4" height="4" fill="#87CEEB"/>
            <rect x="44" y="30" width="4" height="4" fill="#87CEEB"/>
            <rect x="37" y="40" width="4" height="4" fill="#FFFF00"/>
            <rect x="44" y="40" width="4" height="4" fill="#87CEEB"/>
            <rect x="62" y="45" width="3" height="3" fill="#FFFF00"/>
            <rect x="68" y="45" width="3" height="3" fill="#FFFF00"/>
        </svg>''',
    },
    'sky': {
        'name': 'Sky',
        'emoji': '☁️',
        'svg': '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <!-- Sky gradient background -->
            <rect width="100" height="100" fill="#87CEEB"/>
            <!-- Sun -->
            <circle cx="85" cy="20" r="8" fill="#FFD700"/>
            <!-- Clouds -->
            <ellipse cx="20" cy="30" rx="12" ry="8" fill="#FFFFFF"/>
            <ellipse cx="12" cy="32" rx="8" ry="6" fill="#FFFFFF"/>
            <ellipse cx="28" cy="32" rx="10" ry="7" fill="#FFFFFF"/>
            <!-- Birds in flight -->
            <path d="M 50,50 L 55,45 L 58,50" stroke="#000000" stroke-width="1" fill="none"/>
            <path d="M 42,55 L 46,51 L 49,56" stroke="#000000" stroke-width="1" fill="none"/>
            <!-- More clouds -->
            <ellipse cx="70" cy="70" rx="14" ry="9" fill="#FFFFFF" opacity="0.8"/>
            <ellipse cx="60" cy="72" rx="10" ry="7" fill="#FFFFFF" opacity="0.8"/>
            <ellipse cx="80" cy="72" rx="12" ry="8" fill="#FFFFFF" opacity="0.8"/>
        </svg>''',
    }
}

def get_habitat_icon(habitat_type):
    """Get habitat icon data by type"""
    return HABITAT_ICONS.get(habitat_type, HABITAT_ICONS.get('fields', {}))

def get_habitat_emoji(habitat_type):
    """Get emoji for habitat type"""
    icon = get_habitat_icon(habitat_type)
    return icon.get('emoji', '📍')

def get_habitat_svg(habitat_type):
    """Get SVG for habitat type"""
    icon = get_habitat_icon(habitat_type)
    return icon.get('svg', '')
