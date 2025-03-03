import { Icon } from "leaflet";
import BLUE from "../img/marker-icon-2x-blue.png"

import GOLD from "../img/marker-icon-2x-gold.png"
import GREEN from "../img/marker-icon-2x-green.png"
import GREY from "../img/marker-icon-2x-grey.png"
import ORANGE from "../img/marker-icon-2x-orange.png"
import RED from "../img/marker-icon-2x-red.png"

export var blueIcon = new Icon({
	iconUrl: BLUE,
	iconSize: [50, 82],
	iconAnchor: [9, 30],
});

export var goldIcon = new Icon({
	iconUrl: GOLD,
	iconSize: [17, 30],
    iconAnchor: [9, 30],
});

export var greenIcon = new Icon({
	iconUrl: GREEN,
	iconSize: [17, 30],
    iconAnchor: [9, 30],
});

export var greyIcon = new Icon({
	iconUrl: GREY,
	iconSize: [17, 30],
    iconAnchor: [9, 30],
});

export var orangeIcon = new Icon({
	iconUrl: ORANGE,
	iconSize: [17, 30],
    iconAnchor: [9, 30],
});

export var redIcon = new Icon({
	iconUrl: RED,
	iconSize: [17, 30],
    iconAnchor: [9, 30],
});