# @author LotharieSlayer (2022)
# @version 1.0.2

import requests as rq
import obspython as obs

# Threading avoid frame dropping (instead of obs_time_add) when fetching stream info
from threading import Timer

title_source_name = ""
category_source_name = ""
interval = 1
refresh_button = False

def update_text():
	title_source = obs.obs_get_source_by_name(title_source_name)
	category_source = obs.obs_get_source_by_name(category_source_name)

	header = {"Client-ID": client_id, "Authorization": f"Bearer {oauth}"}
	response = rq.get(f"https://api.twitch.tv/helix/streams?user_login={channel}", headers = header)
	try:
		# Refresh
		data = response.json()['data']
		title = data[0]['title']
		category = data[0]['game_name']
	except:
		# Refresh but offline stream
		title = ""
		category = "Offline"

	settings = obs.obs_data_create()
	obs.obs_data_set_string(settings, "text", title)
	obs.obs_source_update(title_source, settings)
	obs.obs_data_set_string(settings, "text", category)
	obs.obs_source_update(category_source, settings)
	obs.obs_data_release(settings)

	global refresh_button
	if refresh_button:
		# If refresh button pressed, update and return to not start a new thread
		refresh_button = False
		return
	
	# Start the thread (again)
	Timer(interval, update_text).start()

		
def refresh_pressed(props, prop):
	global refresh_button
	refresh_button = True
	update_text()


# ------------------------------------------------------------

# OBS Script Functions

def script_update(settings):

	global channel
	global client_id
	global oauth
	global title_source_name
	global category_source_name
	global interval
	global refresh_button

	interval = obs.obs_data_get_int(settings, "interval")
	channel = obs.obs_data_get_string(settings, "channel_name")
	# channel = "mistermv" # Only for testing when you're not on-live on Twitch

	client_id = obs.obs_data_get_string(settings, "client_id")
	oauth = obs.obs_data_get_string(settings, "oauth")
	title_source_name = obs.obs_data_get_string(settings, "title_source")
	category_source_name = obs.obs_data_get_string(settings, "category_source")

	#print("Settings JSON", obs.obs_data_get_json(settings))
	
	if client_id != "" and oauth != "" and title_source_name != "" and category_source_name != "":
		Timer(interval, update_text).start()
		# obs.timer_add(update_text, interval * 1000) # More natural but drop frames ~20 frames/interval :(



def script_description():
	return "<b>StreamInfo</b>" + \
			"<hr>" + \
			"Python script to get stream informations." + \
			"<br/>" + \
			"(title + category)" + \
			"<br/><br/>" + \
			"Made by LotharieSlayer" + \
			"<br/>" + \
			"github.com/LotharieSlayer/OBS-scripts"



def script_properties():
	props = obs.obs_properties_create()

	obs.obs_properties_add_text(props, "channel_name", "Channel", obs.OBS_TEXT_DEFAULT)
	obs.obs_properties_add_text(props, "client_id", "Client ID", obs.OBS_TEXT_PASSWORD)
	obs.obs_properties_add_text(props, "oauth", "Oauth", obs.OBS_TEXT_PASSWORD)

	p = obs.obs_properties_add_list(props, "title_source", "Title Source", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING)
	sources = obs.obs_enum_sources()
	if sources is not None:
		for source in sources:
			source_id = obs.obs_source_get_unversioned_id(source)
			if source_id == "text_gdiplus" or source_id == "text_ft2_source":
				name = obs.obs_source_get_name(source)
				obs.obs_property_list_add_string(p, name, name)

		obs.source_list_release(sources)

	q = obs.obs_properties_add_list(props, "category_source", "Category Source", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING)
	sources = obs.obs_enum_sources()
	if sources is not None:
		for source in sources:
			source_id = obs.obs_source_get_unversioned_id(source)
			if source_id == "text_gdiplus" or source_id == "text_ft2_source":
				name = obs.obs_source_get_name(source)
				obs.obs_property_list_add_string(q, name, name)

		obs.source_list_release(sources)

	obs.obs_properties_add_int(props, "interval", "Update Interval (seconds)", 1, 3600, 1)
	obs.obs_properties_add_button(props, "button", "Refresh", refresh_pressed)

	return props

def script_defaults(settings):
	obs.obs_data_set_default_int(settings, "interval", 5)