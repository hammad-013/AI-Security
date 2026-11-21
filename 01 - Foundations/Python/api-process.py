import urllib.request
import urllib.parse
import urllib.error
import urllib.robotparser

try:
	robot_parser = urllib.robotparser.RobotFileParser()
	robot_parser.set_url("https://student.qualityobe.com/robots.txt")
	robot_parser.read()
	print("robots.txt Check: ", robot_parser.can_fetch("*", "https://student.qualityobe.com/"))

	response = urllib.request.urlopen("https://student.qualityobe.com/")
	print("Status Code: ", response.status)
	print("100 Response Bytes: ", response.read()[:100])

	parsed_url = urllib.parse.urlparse("https://student.qualityobe.com/")
	print("Parsed URL: ", parsed_url)
except urllib.error.HTTPError as e:
	print("HTTP ERROR: ", e.code, " Reason: ", e.reason)
