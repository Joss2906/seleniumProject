# seleniumProject
Web Scraping Test using Selenium

Set the required configuration with this format in the config.json file
The actions must be set in order of execution

Table types -> table, div, list
Click types -> button, a
Export types -> json, xls

Scroll value is in percentage of the total height of the page


{
	"config": [
		{	
			"URL": "https://www.example.com",
			"ACTIONS": [
				{
					"ACTION": "findTable",
					"TYPE": "table",
					"XPATH": "//table"
				},
				{
					"ACTION": "click",
					"TYPE": "button",
					"XPATH": "//button"
				},
				{
					"ACTION": "click",
					"TYPE": "link",
					"XPATH": "//a"
				},
				{
					"ACTION": "scroll",
					"VALUE": "100"
				},
				{
					"ACTION": "select",
					"XPATH": "//select",
					"VALUE": "100"
				},
				{
					"ACTION": "input",
					"XPATH": "//input",
					"VALUE": "100"
				},
				{
					"ACTION": "export",
					"TYPE": "json",
					"FILENAME": "output.json"
				},
				{
					"ACTION": "export",
					"TYPE": "xls",
					"FILENAME": "output.xls"
				},
				{
					"ACTION": "wait",
					"VALUE": "1000"
				}
			]
		}	
	]
}
