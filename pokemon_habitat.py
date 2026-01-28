# Pokemon Habitat Data
# Simplified habitat types with standardized values

# Habitat types:
# - forest: Trees, woodland, dense vegetation
# - cave: Underground caves, rocky interiors
# - ocean: Sea, water bodies, coastlines
# - mountain: Mountains, peaks, rocky terrain
# - fields: Grassland, meadows, plains
# - urban: Cities, towns, human settlements
# - sky: Flying areas, clouds, space

POKEMON_HABITATS = {
    # Gen 1
    1: 'fields', 2: 'fields', 3: 'fields', 4: 'mountain', 5: 'mountain', 6: 'mountain',
    7: 'ocean', 8: 'ocean', 9: 'ocean', 10: 'forest', 11: 'forest', 12: 'forest',
    13: 'forest', 14: 'forest', 15: 'forest', 16: 'fields', 17: 'fields', 18: 'fields',
    19: 'fields', 20: 'fields', 21: 'fields', 22: 'fields', 23: 'fields', 24: 'fields',
    25: 'forest', 26: 'forest', 27: 'mountain', 28: 'mountain', 29: 'fields', 30: 'fields',
    31: 'fields', 32: 'fields', 33: 'fields', 34: 'fields', 35: 'urban', 36: 'urban',
    37: 'fields', 38: 'fields', 39: 'fields', 40: 'fields', 41: 'cave', 42: 'cave',
    43: 'fields', 44: 'fields', 45: 'fields', 46: 'forest', 47: 'forest', 48: 'forest',
    49: 'forest', 50: 'cave', 51: 'cave', 52: 'fields', 53: 'fields', 54: 'ocean',
    55: 'ocean', 56: 'mountain', 57: 'mountain', 58: 'fields', 59: 'fields', 60: 'ocean',
    61: 'ocean', 62: 'ocean', 63: 'urban', 64: 'urban', 65: 'urban', 66: 'mountain',
    67: 'mountain', 68: 'mountain', 69: 'fields', 70: 'fields', 71: 'fields', 72: 'ocean',
    73: 'ocean', 74: 'cave', 75: 'cave', 76: 'cave', 77: 'fields', 78: 'fields',
    79: 'ocean', 80: 'ocean', 81: 'mountain', 82: 'mountain', 83: 'fields', 84: 'fields',
    85: 'fields', 86: 'ocean', 87: 'ocean', 88: 'urban', 89: 'urban', 90: 'ocean',
    91: 'ocean', 92: 'urban', 93: 'urban', 94: 'urban', 95: 'cave', 96: 'fields',
    97: 'fields', 98: 'ocean', 99: 'ocean', 100: 'urban', 101: 'urban', 102: 'forest',
    103: 'forest', 104: 'mountain', 105: 'mountain', 106: 'urban', 107: 'urban', 108: 'fields',
    109: 'urban', 110: 'urban', 111: 'fields', 112: 'fields', 113: 'urban', 114: 'forest',
    115: 'fields', 116: 'ocean', 117: 'ocean', 118: 'ocean', 119: 'ocean', 120: 'ocean',
    121: 'ocean', 122: 'urban', 123: 'fields', 124: 'urban', 125: 'urban', 126: 'urban',
    127: 'forest', 128: 'fields', 129: 'ocean', 130: 'ocean', 131: 'ocean', 132: 'urban',
    133: 'urban', 134: 'urban', 135: 'urban', 136: 'urban', 137: 'urban', 138: 'ocean',
    139: 'ocean', 140: 'ocean', 141: 'ocean', 142: 'mountain', 143: 'mountain', 144: 'sky',
    145: 'sky', 146: 'sky', 147: 'ocean', 148: 'ocean', 149: 'ocean', 150: 'sky',
    151: 'sky',
    
    # Gen 2
    152: 'fields', 153: 'fields', 154: 'fields', 155: 'fields', 156: 'fields', 157: 'fields',
    158: 'ocean', 159: 'ocean', 160: 'ocean', 161: 'fields', 162: 'fields', 163: 'fields',
    164: 'fields', 165: 'forest', 166: 'forest', 167: 'forest', 168: 'forest', 169: 'forest',
    170: 'ocean', 171: 'ocean', 172: 'fields', 173: 'urban', 174: 'fields', 175: 'fields',
    176: 'fields', 177: 'forest', 178: 'forest', 179: 'fields', 180: 'fields', 181: 'fields',
    182: 'fields', 183: 'ocean', 184: 'ocean', 185: 'forest', 186: 'ocean', 187: 'fields',
    188: 'fields', 189: 'fields', 190: 'forest', 191: 'fields', 192: 'fields', 193: 'forest',
    194: 'ocean', 195: 'ocean', 196: 'urban', 197: 'urban', 198: 'fields', 199: 'ocean',
    200: 'cave', 201: 'sky', 202: 'cave', 203: 'fields', 204: 'forest', 205: 'forest',
    206: 'cave', 207: 'fields', 208: 'cave', 209: 'urban', 210: 'urban', 211: 'ocean',
    212: 'forest', 213: 'ocean', 214: 'forest', 215: 'forest', 216: 'mountain', 217: 'mountain',
    218: 'mountain', 219: 'mountain', 220: 'mountain', 221: 'mountain', 222: 'ocean', 223: 'ocean',
    224: 'ocean', 225: 'ocean', 226: 'ocean', 227: 'fields', 228: 'fields', 229: 'fields',
    230: 'ocean', 231: 'fields', 232: 'fields', 233: 'urban', 234: 'forest', 235: 'urban',
    236: 'urban', 237: 'urban', 238: 'urban', 239: 'urban', 240: 'urban', 241: 'fields',
    242: 'urban', 243: 'sky', 244: 'sky', 245: 'sky', 246: 'mountain', 247: 'mountain',
    248: 'mountain', 249: 'ocean', 250: 'sky', 251: 'sky',
    
    # Gen 3
    252: 'fields', 253: 'forest', 254: 'forest', 255: 'fields', 256: 'fields', 257: 'fields',
    258: 'ocean', 259: 'ocean', 260: 'ocean', 261: 'fields', 262: 'fields', 263: 'fields',
    264: 'fields', 265: 'forest', 266: 'forest', 267: 'forest', 268: 'forest', 269: 'forest',
    270: 'ocean', 271: 'ocean', 272: 'ocean', 273: 'forest', 274: 'forest', 275: 'forest',
    276: 'forest', 277: 'forest', 278: 'ocean', 279: 'ocean', 280: 'urban', 281: 'urban',
    282: 'urban', 283: 'ocean', 284: 'ocean', 285: 'forest', 286: 'forest', 287: 'forest',
    288: 'forest', 289: 'forest', 290: 'forest', 291: 'forest', 292: 'forest', 293: 'cave',
    294: 'cave', 295: 'cave', 296: 'cave', 297: 'cave', 298: 'ocean', 299: 'cave',
    300: 'fields', 301: 'fields', 302: 'cave', 303: 'cave', 304: 'cave', 305: 'cave',
    306: 'cave', 307: 'mountain', 308: 'mountain', 309: 'fields', 310: 'fields', 311: 'fields',
    312: 'fields', 313: 'forest', 314: 'forest', 315: 'fields', 316: 'fields', 317: 'fields',
    318: 'ocean', 319: 'ocean', 320: 'ocean', 321: 'ocean', 322: 'mountain', 323: 'mountain',
    324: 'mountain', 325: 'fields', 326: 'fields', 327: 'fields', 328: 'desert', 329: 'desert',
    330: 'desert', 331: 'desert', 332: 'desert', 333: 'forest', 334: 'forest', 335: 'fields',
    336: 'fields', 337: 'mountain', 338: 'mountain', 339: 'ocean', 340: 'ocean', 341: 'ocean',
    342: 'ocean', 343: 'mountain', 344: 'mountain', 345: 'ocean', 346: 'ocean', 347: 'ocean',
    348: 'ocean', 349: 'ocean', 350: 'ocean', 351: 'sky', 352: 'forest', 353: 'urban',
    354: 'urban', 355: 'urban', 356: 'urban', 357: 'forest', 358: 'urban', 359: 'mountain',
    360: 'cave', 361: 'cave', 362: 'cave', 363: 'ocean', 364: 'ocean', 365: 'ocean',
    366: 'ocean', 367: 'ocean', 368: 'ocean', 369: 'ocean', 370: 'ocean', 371: 'mountain',
    372: 'mountain', 373: 'mountain', 374: 'mountain', 375: 'mountain', 376: 'mountain', 377: 'mountain',
    378: 'mountain', 379: 'mountain', 380: 'sky', 381: 'sky', 382: 'ocean', 383: 'mountain',
    384: 'sky', 385: 'sky', 386: 'sky',
    
    # Gen 4
    387: 'fields', 388: 'fields', 389: 'fields', 390: 'mountain', 391: 'mountain', 392: 'mountain',
    393: 'ocean', 394: 'ocean', 395: 'ocean', 396: 'fields', 397: 'fields', 398: 'fields',
    399: 'ocean', 400: 'ocean', 401: 'forest', 402: 'forest', 403: 'fields', 404: 'fields',
    405: 'fields', 406: 'forest', 407: 'forest', 408: 'mountain', 409: 'mountain', 410: 'cave',
    411: 'cave', 412: 'forest', 413: 'forest', 414: 'forest', 415: 'forest', 416: 'forest',
    417: 'urban', 418: 'ocean', 419: 'ocean', 420: 'forest', 421: 'forest', 422: 'ocean',
    423: 'ocean', 424: 'forest', 425: 'urban', 426: 'urban', 427: 'forest', 428: 'forest',
    429: 'urban', 430: 'urban', 431: 'fields', 432: 'fields', 433: 'urban', 434: 'fields',
    435: 'fields', 436: 'mountain', 437: 'mountain', 438: 'mountain', 439: 'urban', 440: 'urban',
    441: 'fields', 442: 'cave', 443: 'mountain', 444: 'mountain', 445: 'mountain', 446: 'mountain',
    447: 'mountain', 448: 'mountain', 449: 'mountain', 450: 'mountain', 451: 'desert', 452: 'desert',
    453: 'ocean', 454: 'ocean', 455: 'fields', 456: 'ocean', 457: 'ocean', 458: 'ocean',
    459: 'mountain', 460: 'mountain', 461: 'mountain', 462: 'mountain', 463: 'fields', 464: 'fields',
    465: 'forest', 466: 'urban', 467: 'mountain', 468: 'forest', 469: 'forest', 470: 'forest',
    471: 'mountain', 472: 'mountain', 473: 'mountain', 474: 'urban', 475: 'urban', 476: 'mountain',
    477: 'cave', 478: 'mountain', 479: 'urban', 480: 'sky', 481: 'sky', 482: 'sky',
    483: 'sky', 484: 'sky', 485: 'mountain', 486: 'sky', 487: 'sky', 488: 'sky',
    489: 'ocean', 490: 'ocean', 491: 'sky', 492: 'fields', 493: 'sky',
    
    # Gen 5
    494: 'sky', 495: 'fields', 496: 'fields', 497: 'fields', 498: 'fields', 499: 'fields',
    500: 'fields', 501: 'ocean', 502: 'ocean', 503: 'ocean', 504: 'fields', 505: 'fields',
    506: 'fields', 507: 'fields', 508: 'fields', 509: 'urban', 510: 'fields', 511: 'forest',
    512: 'forest', 513: 'forest', 514: 'forest', 515: 'forest', 516: 'forest', 517: 'urban',
    518: 'urban', 519: 'urban', 520: 'urban', 521: 'fields', 522: 'fields', 523: 'fields',
    524: 'cave', 525: 'cave', 526: 'cave', 527: 'cave', 528: 'cave', 529: 'cave',
    530: 'cave', 531: 'urban', 532: 'urban', 533: 'urban', 534: 'urban', 535: 'ocean',
    536: 'ocean', 537: 'ocean', 538: 'urban', 539: 'urban', 540: 'forest', 541: 'forest',
    542: 'forest', 543: 'forest', 544: 'forest', 545: 'forest', 546: 'fields', 547: 'fields',
    548: 'fields', 549: 'fields', 550: 'ocean', 551: 'desert', 552: 'desert', 553: 'desert',
    554: 'mountain', 555: 'mountain', 556: 'mountain', 557: 'forest', 558: 'forest', 559: 'mountain',
    560: 'urban', 561: 'urban', 562: 'mountain', 563: 'mountain', 564: 'ocean', 565: 'ocean',
    566: 'mountain', 567: 'mountain', 568: 'urban', 569: 'urban', 570: 'fields', 571: 'fields',
    572: 'fields', 573: 'fields', 574: 'urban', 575: 'urban', 576: 'urban', 577: 'cave',
    578: 'cave', 579: 'cave', 580: 'ocean', 581: 'ocean', 582: 'mountain', 583: 'mountain',
    584: 'mountain', 585: 'forest', 586: 'forest', 587: 'forest', 588: 'forest', 589: 'forest',
    590: 'forest', 591: 'forest', 592: 'ocean', 593: 'ocean', 594: 'ocean', 595: 'forest',
    596: 'forest', 597: 'cave', 598: 'cave', 599: 'urban', 600: 'urban', 601: 'urban',
    602: 'ocean', 603: 'ocean', 604: 'ocean', 605: 'urban', 606: 'urban', 607: 'urban',
    608: 'urban', 609: 'urban', 610: 'mountain', 611: 'mountain', 612: 'mountain', 613: 'mountain',
    614: 'mountain', 615: 'cave', 616: 'ocean', 617: 'ocean', 618: 'ocean', 619: 'mountain',
    620: 'mountain', 621: 'cave', 622: 'mountain', 623: 'mountain', 624: 'urban', 625: 'urban',
    626: 'fields', 627: 'mountain', 628: 'mountain', 629: 'fields', 630: 'fields', 631: 'mountain',
    632: 'forest', 633: 'mountain', 634: 'mountain', 635: 'mountain', 636: 'mountain', 637: 'mountain',
    638: 'sky', 639: 'sky', 640: 'sky', 641: 'sky', 642: 'sky', 643: 'sky',
    644: 'sky', 645: 'sky', 646: 'sky', 647: 'sky', 648: 'sky', 649: 'sky',
    
    # Gen 6
    650: 'fields', 651: 'fields', 652: 'fields', 653: 'fields', 654: 'fields', 655: 'fields',
    656: 'ocean', 657: 'ocean', 658: 'ocean', 659: 'fields', 660: 'fields', 661: 'fields',
    662: 'fields', 663: 'fields', 664: 'forest', 665: 'forest', 666: 'fields', 667: 'fields',
    668: 'fields', 669: 'fields', 670: 'fields', 671: 'fields', 672: 'fields', 673: 'mountain',
    674: 'mountain', 675: 'mountain', 676: 'urban', 677: 'urban', 678: 'urban', 679: 'urban',
    680: 'urban', 681: 'urban', 682: 'forest', 683: 'forest', 684: 'forest', 685: 'forest',
    686: 'ocean', 687: 'ocean', 688: 'ocean', 689: 'ocean', 690: 'ocean', 691: 'ocean',
    692: 'ocean', 693: 'ocean', 694: 'mountain', 695: 'mountain', 696: 'mountain', 697: 'mountain',
    698: 'mountain', 699: 'mountain', 700: 'fields', 701: 'fields', 702: 'fields', 703: 'cave',
    704: 'fields', 705: 'fields', 706: 'fields', 707: 'urban', 708: 'forest', 709: 'forest',
    710: 'fields', 711: 'fields', 712: 'mountain', 713: 'mountain', 714: 'mountain', 715: 'mountain',
    716: 'sky', 717: 'sky', 718: 'cave', 719: 'sky', 720: 'sky', 721: 'sky',
    
    # Gen 7
    722: 'fields', 723: 'fields', 724: 'fields', 725: 'fields', 726: 'fields', 727: 'fields',
    728: 'ocean', 729: 'ocean', 730: 'ocean', 731: 'forest', 732: 'forest', 733: 'forest',
    734: 'fields', 735: 'fields', 736: 'forest', 737: 'forest', 738: 'forest', 739: 'mountain',
    740: 'mountain', 741: 'fields', 742: 'forest', 743: 'forest', 744: 'mountain', 745: 'mountain',
    746: 'ocean', 747: 'ocean', 748: 'ocean', 749: 'fields', 750: 'fields', 751: 'ocean',
    752: 'forest', 753: 'forest', 754: 'forest', 755: 'forest', 756: 'forest', 757: 'forest',
    758: 'forest', 759: 'fields', 760: 'fields', 761: 'forest', 762: 'forest', 763: 'forest',
    764: 'forest', 765: 'forest', 766: 'mountain', 767: 'ocean', 768: 'ocean', 769: 'ocean',
    770: 'ocean', 771: 'ocean', 772: 'sky', 773: 'sky', 774: 'ocean', 775: 'forest',
    776: 'mountain', 777: 'mountain', 778: 'urban', 779: 'ocean', 780: 'mountain', 781: 'ocean',
    782: 'mountain', 783: 'mountain', 784: 'mountain', 785: 'sky', 786: 'sky', 787: 'sky',
    788: 'sky', 789: 'sky', 790: 'sky', 791: 'sky', 792: 'sky', 793: 'sky',
    794: 'sky', 795: 'sky', 796: 'sky', 797: 'sky', 798: 'sky', 799: 'sky',
    800: 'sky', 801: 'sky', 802: 'sky', 803: 'sky', 804: 'sky', 805: 'sky',
    806: 'sky', 807: 'sky',
    
    # Gen 8
    810: 'fields', 811: 'fields', 812: 'fields', 813: 'fields', 814: 'fields', 815: 'fields',
    816: 'ocean', 817: 'ocean', 818: 'ocean', 819: 'fields', 820: 'fields', 821: 'fields',
    822: 'fields', 823: 'fields', 824: 'forest', 825: 'forest', 826: 'forest', 827: 'cave',
    828: 'cave', 829: 'fields', 830: 'fields', 831: 'fields', 832: 'fields', 833: 'ocean',
    834: 'ocean', 835: 'fields', 836: 'fields', 837: 'cave', 838: 'cave', 839: 'cave',
    840: 'forest', 841: 'forest', 842: 'forest', 843: 'mountain', 844: 'mountain', 845: 'ocean',
    846: 'ocean', 847: 'ocean', 848: 'urban', 849: 'urban', 850: 'mountain', 851: 'mountain',
    852: 'ocean', 853: 'ocean', 854: 'forest', 855: 'forest', 856: 'urban', 857: 'urban',
    858: 'urban', 859: 'urban', 860: 'urban', 861: 'urban', 862: 'fields', 863: 'mountain',
    864: 'ocean', 865: 'fields', 866: 'urban', 867: 'mountain', 868: 'fields', 869: 'fields',
    870: 'urban', 871: 'ocean', 872: 'mountain', 873: 'mountain', 874: 'mountain', 875: 'mountain',
    876: 'fields', 877: 'fields', 878: 'fields', 879: 'fields', 880: 'ocean', 881: 'ocean',
    882: 'ocean', 883: 'ocean', 884: 'mountain', 885: 'mountain', 886: 'mountain', 887: 'fields',
    888: 'sky', 889: 'sky', 890: 'sky', 891: 'sky', 892: 'sky', 893: 'sky',
    894: 'sky', 895: 'sky', 896: 'sky', 897: 'sky', 898: 'sky', 899: 'sky',
    900: 'sky', 901: 'sky', 902: 'sky', 903: 'sky', 904: 'sky', 905: 'sky',
    
    # Gen 9 (808-809 and 906+)
    808: 'sky', 809: 'sky',
    906: 'fields', 907: 'fields', 908: 'fields', 909: 'fields', 910: 'fields', 911: 'fields',
    912: 'ocean', 913: 'ocean', 914: 'ocean', 915: 'fields', 916: 'fields', 917: 'fields',
    918: 'fields', 919: 'fields', 920: 'fields', 921: 'fields', 922: 'ocean', 923: 'ocean',
    924: 'urban', 925: 'urban', 926: 'urban', 927: 'mountain', 928: 'mountain', 929: 'forest',
    930: 'forest', 931: 'fields', 932: 'fields', 933: 'mountain', 934: 'mountain', 935: 'urban',
    936: 'urban', 937: 'urban', 938: 'mountain', 939: 'ocean', 940: 'ocean', 941: 'fields',
    942: 'fields', 943: 'fields', 944: 'fields', 945: 'fields', 946: 'fields', 947: 'mountain',
    948: 'mountain', 949: 'forest', 950: 'cave', 951: 'fields', 952: 'forest', 953: 'forest',
    954: 'mountain', 955: 'mountain', 956: 'fields', 957: 'fields', 958: 'fields', 959: 'fields',
    960: 'ocean', 961: 'forest', 962: 'fields', 963: 'ocean', 964: 'mountain', 965: 'forest',
    966: 'mountain', 967: 'mountain', 968: 'ocean', 969: 'cave', 970: 'mountain', 971: 'mountain',
    972: 'mountain', 973: 'mountain', 974: 'mountain', 975: 'mountain', 976: 'ocean', 977: 'ocean',
    978: 'mountain', 979: 'ocean', 980: 'mountain', 981: 'cave', 982: 'mountain', 983: 'sky',
    984: 'sky', 985: 'sky', 986: 'sky', 987: 'sky', 988: 'sky', 989: 'sky',
    990: 'sky', 991: 'sky', 992: 'sky', 993: 'sky', 994: 'sky', 995: 'sky',
    996: 'mountain', 997: 'mountain', 998: 'mountain', 999: 'mountain', 1000: 'mountain', 1001: 'sky',
    1002: 'sky', 1003: 'sky', 1004: 'sky', 1005: 'sky', 1006: 'sky', 1007: 'sky',
    1008: 'sky', 1009: 'sky', 1010: 'sky', 1011: 'sky', 1012: 'sky', 1013: 'sky',
    1014: 'sky', 1015: 'sky', 1016: 'sky', 1017: 'sky', 1018: 'sky', 1019: 'sky',
    1020: 'sky', 1021: 'sky', 1022: 'sky', 1023: 'sky', 1024: 'sky', 1025: 'sky',
}

def get_habitat(pokemon_id):
    """Get the habitat for a given Pokemon ID"""
    return POKEMON_HABITATS.get(pokemon_id, 'unknown')

def get_habitat_translation(habitat, language='en'):
    """Get translated habitat name"""
    translations = {
        'en': {
            'cave': 'Cave',
            'forest': 'Forest',
            'fields': 'Fields',
            'mountain': 'Mountain',
            'desert': 'Desert',
            'sky': 'Sky',
            'ocean': 'Ocean',
            'urban': 'Urban',
            'unknown': 'Unknown'
        },
        'fr': {
            'cave': 'Caverne',
            'forest': 'Forêt',
            'fields': 'Champs',
            'mountain': 'Montagne',
            'desert': 'Désert',
            'sky': 'Ciel',
            'ocean': 'Océan',
            'urban': 'Urbain',
            'unknown': 'Inconnu'
        }
    }
    
    lang_dict = translations.get(language, translations['en'])
    return lang_dict.get(habitat, habitat.title())
