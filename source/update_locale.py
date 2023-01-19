"""
upadte_locale.py
v. 1.7
28.06.2022
Info, updates, how to use: https://basecamp.com/1962648/projects/996833/messages/100723977
"""

import os
import webbrowser


EXCLUDE_ITEMS_CONTAIN = {} # {"background", "screen", "light", "shading", "shadow"} 

SHOW_ITEM_SIZE = True
ALLOWED_NOTCH_OVERLAY = 0.45
HTML_FILE_NAME = "localeNew.html"
OPEN_AFTER_COMPLETION = True

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
	<head>
		<title>*GAME_NAME* - localization</title>
		<meta charset="utf-8">
	</head>
	<body lang="en-US">
	<style>
   td,
	th {
		border: 1px solid rgb(190, 190, 190);
		margin: 10px;        
	}
	table button {
		font-family: 'Calibri';
		font-size: 1.1rem;
	}
	body {
		font-family: 'Calibri';
	}
	td > * {
		max-width: 20rem;
	}
	td {
		text-align: center;
	}

	tbody > tr > * {
		min-width: max-content;
		display: table-cell;
	}
	tr {
		border: 1px solid rgb(190, 190, 190);
	}
	th[scope="col"] {
		background-color: #696969;
		color: #fff;
	}
	th[scope="row"] {
		background-color: rgb(196, 217, 216);
	}
	caption {
		padding: 10px;
		caption-side: bottom;
	}
	table {
		border-collapse: collapse;
		border: 2px solid rgb(200, 200, 200);
		letter-spacing: 1px;
		font-family: 'Calibri';
		font-size: 1.1rem;
	}
	select {
		border: thin solid blue;
		border-radius: 4px;
		display: inline-block;
		font: inherit;
		line-height: 1.5em;
		min-width: 12rem;
	}
	img {
		border: 1px solid black;
		align-self: center;
	}
	td {
		max-width: 12rem;
	}
	#toolbar {
		position:fixed;
		top:0;
		left:0;
		width:100%;
		height:30px;
		background-color:black;
		display: inline-flex;
		align-items: center;
	}    
	#toolbar > * {
		margin-right:5px;
	}
	#toolbar > p {
		color: white;
	}
	.additionalInfo {
		align-content: center;
	}
	.additionalInfoTd {
		align-content: center;
		display: grid;
		border: none;
	}
	.additionalInfoTd > tr {
		align-content: center;
		display: grid;
	}	
	.additionalInfoTd > * {
		border: 1px solid darkgrey;
	}
	.red {
		background-color: rgb(255, 59, 48);
	}
	.orange {
		background-color: rgb(255, 149, 0);
	}
	.green {
		background-color: rgb(48, 209 ,88);
	}
	.greengray {
		background-color: #93ae93;
	}
	.blue {
		background-color: rgb(47, 202, 228);
	}
	.switch {
	position: relative;
	display: inline-block;
	width: 44px;
	height: 24px;
	}

	/* Hide default HTML checkbox */
	.switch input {
	opacity: 0;
	width: 0;
	height: 0;
	}

	/* The slider */
	.slider {
	position: absolute;
	cursor: pointer;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	background-color: #ccc;
	-webkit-transition: .4s;
	transition: .4s;
	}

	.slider:before {
	position: absolute;
	content: "";
	height: 24px;
	width: 24px;
	left: 0px;
	bottom: 0px;
	background-color: white;
	-webkit-transition: .4s;
	transition: .4s;
	}

	input:checked + .slider {
	background-color: rgb(52, 199, 89);
	}

	input:focus + .slider {
	box-shadow: 0 0 1px #2196F3;
	}

	input:checked + .slider:before {
	-webkit-transform: translateX(20px);
	-ms-transform: translateX(20px);
	transform: translateX(20px);
	}

	/* Rounded sliders */
	.slider.round {
	border-radius: 34px;
	}

	.slider.round:before {
	border-radius: 50%;
	}

	#errors_log {
		color: red;
		background-color: rgb(38, 38, 49);
		font-size: 20px;
		display: none;
	}
	
	#warningMessage {
		position: fixed;
		top: 100px;
		color: white;
		background-color: #696969;
		align-self: center;
		max-width: 50em;
		left: 0;
		right: 0;
		margin-left: auto;
		margin-right: auto;
		text-align: center;
		display: none;
	}

	*CSS*	

	.passiveItem {
	background-color: rgb(179, 255, 179);
	display: table-row;
	}

	.passiveItem .additionalInfo tr {
		display: table-row;
	}
	.passive.passiveItem th {
		background-color: inherit !important;
	}

	</style>
	<script>
		
		function showWarning(text) {
			message = document.getElementById("warningMessage");
			message.innerText = text;
			message.style.display = 'block';
			/*
			setTimeout(function () {
				message = document.getElementById("warningMessage");
				message.style.display = 'none';
			}, 1500);*/
		}

		function jumpTo(n) {
			var top = document.getElementById(n).offsetTop;
			window.scrollTo(0, top);
		}
		function jumpToId(objectId) {

			obj = document.getElementById(objectId);
			if (obj != undefined) {
				if (obj.type == "submit"){
					parentTd = obj.parentElement.parentElement;
				}
				else {
					parentTd = obj.parentElement.parentElement.parentElement.parentElement;
				}
				prev = document.querySelector(".passiveItem");
				if (prev != undefined) {
					prev.classList.remove("passiveItem")
				}
				if (parentTd.className == "passive" &&  document.getElementById("showOnlyActiveCheckBox").checked) {
					parentTd.classList.add("passiveItem");
					// showWarning("Это пассивный предмет");
				}
				else if (obj.className == "passive") {
					obj.classList.add("passiveItem");
					// showWarning("Это пассивный предмет");
				}
				document.getElementById(objectId).scrollIntoView(); 
				window.scrollBy(0, -150);							
			}
		}
		function jumpToBug() {
			bugId = "bug_"+document.getElementById("bugCounter").value;
			jumpToId(bugId);
		}
		function jumpToWarning() {
			warningId = "warning_"+document.getElementById("warningCounter").value;
			jumpToId(warningId);
		}
		function fillErrorTextArea() {
			var errors=`*ERRORS*`
			tArea = document.getElementById("errors_log");
			if (errors.length>8){
				tArea.style.display="block"
			}
			tArea.value = `Найдены синтаксические ошибки!!! (это важно)\nПроверьте правильность написания тегов <name>, <rect> и <image>, а также их атрибуты. Возможно, где-то незакрытая кавычка или в значение размеров или координат затесался буквенный символ.\n`+errors;
		}
		window.onload = function () {
			fillErrorTextArea();
			headers = document.getElementsByTagName("h2");
			window.onscroll = function () { pinHeaderToTop() };
		}

		function pinHeaderToTop() {
			for (i = 0; i < headers.length; i++) {			
				if (window.pageYOffset >  headers[i].offsetTop-10) {
					document.getElementById("opt_"+headers[i].id).selected = 'selected';
				}
			}
		}

		function getElementStyle(elementClass) {
			const stylesheet = document.styleSheets[0];
			let elementRules;

			for (let i = 0; i < stylesheet.cssRules.length; i++) {
				if (stylesheet.cssRules[i].selectorText === elementClass) {
					elementRules = stylesheet.cssRules[i];
				}
			}

			return elementRules;
		}

		function showOnlyActiveChange() {
			onlyActiveCheckbox = document.getElementById("showOnlyActiveCheckBox");
			const passiveItems = getElementStyle('.passive');
			const itemTypeRow = getElementStyle('.itemAdditionalInfoLabel.itemType');
			if (onlyActiveCheckbox.checked) {
				passiveItems.style.display = 'none';
				itemTypeRow.style.display = 'none';
			}
			else {
				passiveItems.style.display = 'table-row';
				itemTypeRow.style.display = 'table-row';
			}
		}


	</script>

	<div id="toolbar">
		<select id="title" name="title" onchange="location = this.value;">*OPTIONS*		</select>
		<p>Ошибок: *BUG_MAX*</p>
		<input type="number" id="bugCounter" min=1 max=*BUG_MAX* onchange="jumpToBug()">
		<p>Предупреждений: *WARNING_MAX*</p>
		<input type="number" id="warningCounter" min=1 max=*WARNING_MAX* onchange="jumpToWarning()">
		<p>Только активные: </p>

		<label class="switch">
		<input type="checkbox" id="showOnlyActiveCheckBox" onchange="showOnlyActiveChange()" checked="checked">
		<span class="slider round"></span>
		</label>
	</div>
	<div id="warningMessage"></div>
	<br>
	<br>
	<h1>*GAME_NAME*</h1>
	<textarea id="errors_log" cols="150" rows="30">
		Найдены синтаксические ошибки
	</textarea>
	*ITEMS_TABLES*
	</body>
</html>
"""

TABLE_TEMPLATE="""
	<h2 id="*TABLE_ID*">*TABLE_NAME*</h2>
	<table width="100%">
		*ITEMS*
	</table>
"""

ITEM_TEMPLATE = """
		<tr id="*ITEM_ID*" class="*ITEM_TYPE*">
			<th scope="row">*ITEM_NAME*</th>
			<td><img src="*ITEM_IMAGE_PATH*"/></td>
			<td>*ITEM_RU_NAME*</td>
			<td>*ITEM_IMAGE_NAME*</td>
			<td class="additionalInfoTd">
				<table class="additionalInfo">		*ITEM_ADDITIONAL_INFO*		</table>
			</td>
		</tr>
"""


CSS_HIDDEN_PASSIVE_STYLE = """
.passive {
	display: none;
}
.itemAdditionalInfoLabel.itemType {
	display: none;
}
"""


def get_text_between(text, start_text, end_text):
	start_index = text.find(start_text)
	if start_index == -1:
		return ""
	end_index = text.find(end_text, start_index+len(start_text))
	res_text = text[start_index+len(start_text):end_index]
	return res_text


class Image:
	def __init__(self) -> None:
		self.path = ""
		self.width = 0
		self.height = 0
		self.x_position = 0
		self.y_position = 0


class Item:
	def __init__(self) -> None:
		self.name = ""
		self.image = Image()
		self.unique_name = ""
		self.translated_name = ""
		self.error_opening_image = False
		self.active = True
		self.exclusive_group_with = []


class Location:
	def __init__(self, name = "", folder = "") -> None:
		self.name = name
		self.folder = folder


class HTMLWriter:
	def __init__(self, file_name="localeNew.html") -> None:
		self._file_name = file_name
		self._file_content = ""

	def name(self):
		return self._file_name

	def add(self, content):
		self._file_content += content + "\n"

	def save(self):
		with open(self._file_name, "w", encoding="UTF8") as locale_file:
			locale_file.write(self._file_content)


class HTMLTemplate:
	def __init__(self, template: str, keyword_prefix="*", keyword_suffix="*") -> None:
		self._template = template
		self._keyword_prefix = keyword_prefix
		self._keyword_suffix = keyword_suffix

	def _get_template_keyword(self, keyword):
		return self._keyword_prefix+keyword+self._keyword_suffix

	def template(self):
		return self._template

	def insert(self, keyword, element):
		template_keyword = self._get_template_keyword(keyword)
		if template_keyword in self._template:
			self._template = self._template.replace(template_keyword, element+"\n")

	def insertInline(self, keyword, element):
		template_keyword = self._get_template_keyword(keyword)
		if template_keyword in self._template:
			self._template = self._template.replace(template_keyword, element)
	
	def insertList(self, keyword, elements_list):
		template_keyword = self._get_template_keyword(keyword)
		if template_keyword in self._template:
			for element in elements_list:
				self.insertInline(keyword, "\n"+element+template_keyword)
			self.insert(keyword, "")

	def insertErrors(self, keyword, elements_dict:dict):
		template_keyword = self._get_template_keyword(keyword)
		if template_keyword in self._template:
			for key in elements_dict.keys():
				self.insert(keyword, key+":\n"+template_keyword)
				for error in elements_dict[key]:
					self.insert(keyword, "\t\""+error+"\"\n"+template_keyword)

			self.insert(keyword, "")	


class Square:
	def __init__(self, x1, y1, x2, y2) -> None:
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
  

class Game:
	def __init__(self) -> None:
		self.name = self._get_game_name()
		self.levels_folder = self._get_levels_folder_name()  
		self.prefix = self._get_prefix()
		self.xml_folder = self._get_XML_folder()
		self.roadmap = self._get_roadmap()

	def _get_levels_folder_name(self):
		all_dirs = os.listdir('./')

		for dir_name in all_dirs:
			if "Levels" in dir_name:
				return dir_name

	def _get_prefix(self):
		fname = self.levels_folder
		prefix_name = fname[:-6]
		return prefix_name

	def _get_game_name(self):
		return os.path.dirname(__file__).split("\\")[-1].split("/")[-1]

	def _get_XML_folder(self):
		all_dirs = os.listdir('./')

		for dir_name in all_dirs:
			if self.prefix+"Game" == dir_name:
				return dir_name

	def _get_roadmap(self):

		route_file_content = ""
		route = []

		if os.path.exists(self.prefix+"Game/gamemap_1024.xml"): 
			with open(self.prefix+"Game/gamemap_1024.xml", "r", encoding="UTF8") as route_file:
				route_file_content = route_file.read()
			
			start_search_index = 0

			while(route_file_content.find("<location", start_search_index) != -1):
				location_raw_data = get_text_between(route_file_content[start_search_index:], "<location", "</location>")
				level_name = get_text_between(location_raw_data, "file=\"", "\"")
				level_folder = get_text_between(location_raw_data, "folder=\"", "\"")
				if not level_folder:
					level_folder = get_text_between(location_raw_data, "name=\"", "\"")
				if not sum(el.name == level_name for el in route):
					route.append(Location(level_name, level_folder))
					if not os.path.exists('./'+self.xml_folder+'/Levels/'+level_name):
						route = []
						break
				start_search_index += len(location_raw_data)

			# else:
			# 	folderValue = get_text_between(location_raw_data, "folder=\"", "\"")
			# 	if folderValue != "":
			# 		route[route.index(lambda x: x.name == level_name)].folder = folderValue



		if len(route) == 0 and os.path.exists(self.prefix+"Game/route.xml"):
			with open(self.prefix+"Game/route.xml", "r", encoding="UTF8") as route_file:
				lines = route_file.readlines()

			for line in lines:
				if line.find("routePoint step") != -1:
					level_name = get_text_between(line, "location=\"", "\"")
					level_folder = level_name.replace(".xml", "")
					if not sum(el.name[:-4] in level_name for el in route):
						route.append(Location(level_name+".xml", level_folder))
						if not os.path.exists('./'+self.xml_folder+'/Levels/'+level_name+'.xml'):
							route = []
							break

		if route == []:
			roadmap_buff = []
			for xml_file in os.listdir('./'+self.xml_folder+'/Levels'):
				roadmap_buff.append(Location(xml_file, xml_file.replace(".xml", "")))
			return roadmap_buff

		return route


class SquareIntersectionAreaCalculator:
	def __init__(self) -> None:
		pass

	def calculateSquare(self, square:Square):
		s = abs(square.y2-square.y1)*abs(square.x1-square.x2)
		return s

	def calculate_area_of_intersection(self, s1:Square, s2:Square):
		
		if s1.x2<s2.x1 or s1.x1>s2.x2:
			return 0
		
		if s1.y2<s2.y1 or s1.y1>s2.y2:
			return 0		

		overlay_x1 = max(s1.x1, s2.x1)		
		overlay_y1 = max(s1.y1, s2.y1)

		overlay_x2 = min(s1.x2, s2.x2)
		overlay_y2 = min(s1.y2, s2.y2)
		
		overlay_square = Square(overlay_x1, overlay_y1, overlay_x2, overlay_y2)
		overlay_area = self.calculateSquare(overlay_square)

		return overlay_area


class ItemImagePositionValidator:
	def __init__(self, game:Game) -> None:
		self.game = game
		self._iPhone10_size = (2436, 1125)
		self._iPhone10_notch_width = 100
		self._iPhone10_notch_height = 800
		self._iPhone10_notch_size = Square(2286, 250, 2436, 875)
		self._overlay_relative_boundaries = ALLOWED_NOTCH_OVERLAY
		self._backgrounds = self._fill_in_backgrounds_dict()
		self._overlay_calculator = SquareIntersectionAreaCalculator()

	def set_overlay_error_boundaries(self, new_value:float):
		self._overlay_relative_boundaries = new_value

	def _fill_in_backgrounds_dict(self):
		backgrounds = {}
		for location in self.game.roadmap:
			xml = './' + self.game.xml_folder + '/Levels/' + location.name
			content = ""
			with open(xml, "r", encoding="UTF8") as xmlfile:
				content = xmlfile.read()
			
			if "<name>background</name>" in content:
				background_raw_data = get_text_between(content, "<name>background</name>", "</item>")
				background = Image()
				background.width = int(get_text_between(background_raw_data, "width=\"", "\""))
				background.height = int(get_text_between(background_raw_data, "height=\"", "\""))
				backgrounds[location] = (background, self._get_relative_pixels_scale_coefficient(background))
		return backgrounds

	def _get_relative_pixels_scale_coefficient(self, background_image:Image):
		coefficient = 1
		if background_image.width/background_image.height > self._iPhone10_size[0]/self._iPhone10_size[1]:
			coefficient = background_image.height/self._iPhone10_size[1]
		else:
			coefficient = background_image.width/self._iPhone10_size[0]
		return coefficient

	def get_location_name(self, image:Image):
		location_name = ""
		if image.path.rfind('/'):
			location_name = image.path.split('/')[-2][len(self.game.prefix):]
		elif image.path.rfind('\\'):
			location_name = image.path.split('\\')[-2][len(self.game.prefix):]
		return location_name
			

	def get_overlay_coefficient(self, image:Image):

		location_name = self.get_location_name(image)

		if location_name in self._backgrounds.keys():

			background_image = self._backgrounds[location][0]
			transform_coefficient = self._backgrounds[location][1]

			image_relative_x = image.x_position/transform_coefficient
			image_relative_y = image.y_position/transform_coefficient
			image_relative_width = image.width/transform_coefficient
			image_relative_height = image.height/transform_coefficient
			image_box = Square(image_relative_x, image_relative_y, image_relative_x+image_relative_width, image_relative_y+image_relative_height)
			image_box_relative_area = image_relative_height*image_relative_width
			# right notch
			notch_x1 = background_image.width/transform_coefficient - self._iPhone10_notch_width
			notch_x2 = background_image.width/transform_coefficient
			overlay_right = self._overlay_calculator.calculate_area_of_intersection(image_box, Square(notch_x1, self._iPhone10_notch_size.y1, notch_x2, self._iPhone10_notch_size.y2))
			# left notch
			notch_x1 = 0
			notch_x2 = self._iPhone10_notch_width
			overlay_left = self._overlay_calculator.calculate_area_of_intersection(image_box, Square(notch_x1, self._iPhone10_notch_size.y1, notch_x2, self._iPhone10_notch_size.y2))

			overlay = max(overlay_left, overlay_right)
			coefficient = overlay/image_box_relative_area
			return coefficient
		return 0

	def validate(self, image:Image):
		overlay = self.get_overlay_coefficient(image)
		if overlay > self._overlay_relative_boundaries:
			return False
		return True


class ExclusiveGroupItem:
	def __init__(self, name="", link="") -> None:
		self.name = name
		self.link = link.replace(" ", "_").replace("'", "")

class XMLItemReader:
	def __init__(self, game:Game) -> None:
		self.game = game
		self._exclusive_groups = {}
		self.errors = {}
  
	def read_location_items(self, location):

		xml_path = './'+ game.xml_folder +'/Levels/'+location.name
		items = []
		content = ""
		ru_translates = ""
		translates_path = "./Strings/ru.lproj/"+self.game.prefix+"Localizable.strings"
  
		if os.path.exists(translates_path):
			with open(translates_path, "r", encoding="UTF8") as ru_text:
				ru_translates = ru_text.read()
    
		location_name = location.name
		# xml_file = xml_file.replace("_diff", "")
		with open(xml_path, "r", encoding="UTF8") as xmlfile:
			content = xmlfile.read()
		
		
		
		exclusive_group_marker = "<exclusive_group items=\""
		exclusive_group_index = 0
		self._exclusive_groups[location_name] = []
		while content.find(exclusive_group_marker, exclusive_group_index) != -1:
			exclusive_groups_list = []
			exclusive_group_start_index = content.find(exclusive_group_marker, exclusive_group_index)
			exclusive_group_end_index = content.find("\"", exclusive_group_start_index+len(exclusive_group_marker))
			exclusive_group_index = exclusive_group_end_index

			exclusive_group_objects_str = content[exclusive_group_start_index+len(exclusive_group_marker):exclusive_group_end_index]
			exclusive_group_objects = exclusive_group_objects_str.split(',')
			for object in exclusive_group_objects:
				exclusive_groups_list.append(ExclusiveGroupItem(object, location_name+'_'+object))

			self._exclusive_groups[location_name].append(exclusive_groups_list)
		

		items_types = {"active", "passive"}

		is_any_error = False
		for item_type in items_types:
			item_start_text = "<item type=\""+item_type+"\""
			index = 0

			while content.find(item_start_text, index) != -1:
				start_index = content.find(item_start_text, index)
				end_index = content.find("</item>", start_index)
				index = end_index

				item_raw_data = content[start_index+len(item_start_text):end_index]
				is_exclude_word_in_list = False

				try:
					for word in EXCLUDE_ITEMS_CONTAIN:
						if word in item_raw_data:
							is_exclude_word_in_list = True

					if is_exclude_word_in_list == False:
						item = Item()
						item.name = get_text_between(item_raw_data, "<name>", "</name>")

						item.image.width = int(get_text_between(item_raw_data, "width=\"", "\""))
						item.image.height = int(get_text_between(item_raw_data, "height=\"", "\""))

						item.image.x_position = int(get_text_between(item_raw_data, " x=\"", "\""))
						item.image.y_position = int(get_text_between(item_raw_data, " y=\"", "\""))
						if not len(get_text_between(item_raw_data, "<image path=\"", "\"></image>")):
							continue
						item.image.path =  './'+game.levels_folder +'/'+ game.prefix + location.folder + '/' +get_text_between(item_raw_data, "<image path=\"", "\"></image>")
						item.error_opening_image = not os.path.exists(item.image.path)

						item.translated_name = "--" if item_type == "active" else ""
						item_translated_name_index = ru_translates.find("\""+item.name+"\"")
						
						if item_translated_name_index != -1:
							item.translated_name = get_text_between(ru_translates, "\""+item.name+"\"", "\";").split("\"")[-1]
						

						item.unique_name = ""
						if "<unique>" in item_raw_data:
							item.unique_name = get_text_between(item_raw_data, "<unique>", "</unique>")
						item.active = True if item_type == "active" else False
						
						for group in self._exclusive_groups[location_name]:
							for group_item in group:
								if group_item.name == item.name or group_item.name == item.unique_name:
									for gr_item in group:
										if gr_item.name != item.name and gr_item.name != item.unique_name:
											item.exclusive_group_with.append(gr_item)
						

						items.append(item)
				except:
					if location_name in self.errors.keys():
						self.errors[location_name].append(item_raw_data)
					else:
						self.errors[location_name] = [item_raw_data]
					is_any_error = True
		if is_any_error:
			print(location_name, " - обработано с ошибками")
		else:
			print(location_name, " - обработано")
		items.sort(key=lambda test_list: test_list.name)
		return items


if __name__ == "__main__":
    
	game = Game()

	locale_template = HTMLTemplate(HTML_TEMPLATE)
	locale_template.insertInline("GAME_NAME", game.name)
 
	selector_options = []

	for location in game.roadmap:
		selector_options.append("\t\t\t<option id=\"opt_"+location.name+"\" value=\"#"+location.name+"\"><a href=\"#" + location.name+"\">"+location.name.replace(".xml", "")+"</a></option>")

	locale_template.insertList("OPTIONS", selector_options)

	error_number = 0
	warning_number = 0
	tables_html_list = []
	item_reader = XMLItemReader(game)
	position_validator = ItemImagePositionValidator(game)

	css_templates_list = []
	css_templates_list.append(CSS_HIDDEN_PASSIVE_STYLE)

	errors_list = []

	for location in game.roadmap:
		location_folder = location.folder
		table_template = HTMLTemplate(TABLE_TEMPLATE)
		
		table_template.insertInline("TABLE_ID", location.name)
		table_template.insertInline("TABLE_NAME", location.name)

		items = item_reader.read_location_items(location)

		items_html_list = []

		for item in items:

			item_id = location.name+"_"+item.name.replace(" ", "_").replace("'", "")

			if item.unique_name != "":
				item_id = location.name+"_"+item.unique_name.replace(" ", "_").replace("'", "")

			item_template = HTMLTemplate(ITEM_TEMPLATE)

			item_template.insertInline("ITEM_ID", item_id)
			item_template.insertInline("ITEM_NAME", item.name)
			item_template.insertInline("ITEM_TYPE", ("active" if item.active else "passive"))
			item_template.insertInline("ITEM_IMAGE_PATH", item.image.path) #game.levels_folder()+'/' + game.prefix + location_name + '/' + i
			item_template.insertInline("ITEM_RU_NAME", item.translated_name)
			item_template.insertInline("ITEM_IMAGE_NAME", item.image.path.split("/")[-1].split("\\")[-1])

			additional_info = []

			if item.unique_name != "":
				unique = "<tr class = \"blue\"><td>unique: "+item.unique_name+"</td></tr>"
				additional_info.append(unique)

			if item.error_opening_image:
				error_number += 1
				errors_list.append((location.name, item.name, item.image.path, "Неправильный путь к изображению предмета"))
				html_error_marker = "<tr class=\"error red\" id=\"bug_" +  str(error_number)+"\"><td>(no image)</td></tr>"
				additional_info.append(html_error_marker)



			html_item_type = "<tr class='itemAdditionalInfoLabel itemType'><td>" + ("active" if item.active else "passive") + "</td></tr>"
			additional_info.append(html_item_type)
			
			if SHOW_ITEM_SIZE:
				html_item_size = "<tr><td>" +str(item.image.width)+"×" + str(item.image.height) + "px</td></tr>"
				additional_info.append(html_item_size)	

			if item.active and item.image.width < 100 and item.image.height < 100:
				warning_number+=1
				html_small_size_warning = "<tr class = \"orange\" id=\"warning_"+str(warning_number)+"\"><td>(low res)</td></tr>"
				additional_info.append(html_small_size_warning)
    
			if item.active and not position_validator.validate(item.image):
				error_number += 1
				errors_list.append((location.name, item.name, item.image.path, "Изображение сильно заступает за вырез под камеру на iPhone X"))
				html_error_marker = "<tr class=\"error red\" id=\"bug_" +  str(error_number)+"\"><td>(notch overlay)</td></tr>"
				additional_info.append(html_error_marker)
			
			notch_overlay = position_validator.get_overlay_coefficient(item.image)
			if item.active and notch_overlay>0.005:
				warning_number+=1
				html_overlay_warning = "<tr class = \"orange\" id=\"warning_"+str(warning_number)+"\"><td>notch overlay: "+str(int(round(notch_overlay*100, 0)))+"%</td></tr>"
				additional_info.append(html_overlay_warning)

			for ex_group in item.exclusive_group_with:
				
				html_exclusive_group_link = "<tr><button class = \"green\" onclick=\"jumpToId('"+ex_group.link+"')\">group: "+ex_group.name+"</button></tr>"
				

				group_item_exists = False
				for an_item in items:
					if ex_group.name == an_item.name or ex_group.name == an_item.unique_name:
						group_item_exists = True
						break
				if not group_item_exists:
					error_number += 1
					errors_list.append((location.name, item.name, item.image.path, "Изображение в exclusive group с несуществующим предметом "+ex_group.name))
					html_exclusive_group_link = "<tr><button class = \"error red\" id=\"bug_" +  str(error_number)+"\">group: "+ex_group.name+" (missing)</button></tr>"
				
				additional_info.append(html_exclusive_group_link)
			
			# You can write your own additional info labels here, then do not forget to append them to additional_info list
			
			item_template.insertList("ITEM_ADDITIONAL_INFO", additional_info)
			items_html_list.append(item_template.template())

		table_template.insertList("ITEMS", items_html_list)
		tables_html_list.append(table_template.template())

	if item_reader.errors != {}:
		locale_template.insertErrors("ERRORS", item_reader.errors)

	
	locale_template.insertList("ITEMS_TABLES", tables_html_list)
	locale_template.insertInline("BUG_MAX", str(error_number))
	locale_template.insertInline("WARNING_MAX", str(warning_number))


	locale_template.insertList("CSS", css_templates_list)

	locale = HTMLWriter(HTML_FILE_NAME)	
	locale.add(locale_template.template())
	locale.save()

	for err in errors_list:
		print("\t".join(err))

	print("Файл сохранён как \""+HTML_FILE_NAME+"\"")
	if OPEN_AFTER_COMPLETION:
		webbrowser.get().open("file:///" + os.path.dirname(os.path.abspath(__file__))+'/'+HTML_FILE_NAME, new=1)
	