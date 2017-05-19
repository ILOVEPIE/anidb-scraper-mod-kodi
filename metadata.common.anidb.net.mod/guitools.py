import xbmc
import xbmcgui
import xbmcaddon
import traceback

def provideInstructionsForSetting(addon_id,setting_type,setting_id,setting_name,instruction_text):
	addon = xbmcaddon.Addon(addon_id)
	try:
		instruction_text = addon.getLocalizedString(int(instruction_text))
	except ValueError:
		pass # do nothing
	try:
		setting_name = addon.getLocalizedString(int(setting_name))
	except ValueError:
		pass # do nothing
	dialog = xbmcgui.Dialog()
	current = ""
	try:
		current = addon.getSetting(setting_id)
		dialog.ok(setting_name,instruction_text)
		fresult = current
		result = current
		if setting_type == 'text':
			result = dialog.input(setting_name,current,xbmcgui.INPUT_ALPHANUM)
		elif setting_type == 'number':
			try:
				test = int(current)
			except ValueError:
				current = ""
			result = dialog.input(setting_name,current,xbmcgui.INPUT_NUMERIC)
		else:
			result = dialog.input(setting_name,current,xbmcgui.INPUT_ALPHANUM)
		if result != "" or setting_type == "text":
			fresult = result
		addon.setSetting(setting_id,fresult)
	except:
		raise
		
def displayOkDialog(addon_id,title,message):
	addon = xbmcaddon.Addon(addon_id)
	try:
		message = addon.getLocalizedString(int(message))
	except ValueError:
		pass # do nothing
	try:
		title = addon.getLocalizedString(int(title))
	except ValueError:
		pass # do nothing
	dialog = xbmcgui.Dialog()
	dialog.ok(title,message)

def chooseSetting(addon_id,setting_id,setting_name,question_text):
	addon = xbmcaddon.Addon(addon_id)
	try:
		question_text = addon.getLocalizedString(int(question_text))
	except ValueError:
		pass # do nothing
	try:
		setting_name = addon.getLocalizedString(int(setting_name))
	except ValueError:
		pass # do nothing
	dialog = xbmcgui.Dialog()
	if dialog.yesno(setting_name,question_text):
		addon.setSetting(setting_id,"true")
	else:
		addon.setSetting(setting_id,"false")

method_list = {
	'set_setting_with_instructions': provideInstructionsForSetting,
	'display_message': displayOkDialog,
	'choice_and_set_setting': chooseSetting
}
gui_tool_method = sys.argv[1]
gui_tool_args = sys.argv[2:]
local_addon = xbmcaddon.Addon("metadata.common.anidb.net.mod")
try:
	try:
		method_list[gui_tool_method](*gui_tool_args)
	except:
		xbmc.log(local_addon.getLocalizedString(30300)+" "+gui_tool_method+"\n"+traceback.format_exc(),xbmc.LOGERROR)
except AttributeError:
	xbmc.log(local_addon.getLocalizedString(30300)+" "+gui_tool_method+"\t"+"Method Not Found.",xbmc.LOGERROR)
