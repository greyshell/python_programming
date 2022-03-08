import requests
from bs4 import BeautifulSoup
import json
import wget
import ssl
import os
import subprocess
import time 
import sys, getopt
from os import path
from requests.packages.urllib3.exceptions import InsecureRequestWarning


class PacktPub:

	http_proxy  = "127.0.0.1:9999"
	https_proxy = "127.0.0.1:9999"

	proxyDict = { 
	              "http"  : http_proxy, 
	              "https" : https_proxy, 
	            }
	
	# clipid of the course can be extracted from the response of https://app.pluralsight.com/library/
	def __init__(self, clipId,dest):
		self.clipId = clipId
		self.dest = dest

	#send request to https://app.pluralsight.com/course-player?clipId=54557aca-b0a2-438b-b586-b4132779c350
	#and extract the contentid and verionid of each module
	def extract_course_details(self):
		requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


		print(f"{self.clipId}")
		r = requests.get('https://subscription.packtpub.com/api/products/'+self.clipId+'/summary', proxies=PacktPub.proxyDict,verify=False)
		
		resp = r.json()
		#print(f"{resp['data']['toc']['chapters']}")

		print(f"Title ------- {resp['data']['title']} ")
		ctr1 =1 

		for module in resp['data']['toc']['chapters'] :
			mod_dir = module['title']
			print(f"module dir {mod_dir} ---- {module['id']}")
			ctr2 = 1
			if not os.path.exists(self.dest+"/"+str(ctr1)+" "+mod_dir):
				os.makedirs(self.dest+"/"+str(ctr1)+" "+mod_dir)

			module_id = module['id']

			for content in module['sections'] :
				file_path = self.dest+"/"+str(ctr1)+" "+mod_dir+"/"+str(ctr2)+" "+content['title'] + '.mp4'
				#print(f"--------file {file_path}")
				if path.exists(file_path):
					print(f"skipping the file {file_path}")
					ctr2 = ctr2 +1
					continue
				print(content['title'] )
				time.sleep(5)
				download_vid= self.get_download_link(content['id'],module_id)
				print(f"{download_vid}")
				self.download(download_vid,str(ctr1)+" "+mod_dir+"/"+str(ctr2)+" "+content['title'])
				ctr2 = ctr2 +1
				#exit()
			ctr1 = ctr1+1


		#if r.status_code == 400:
		#	r = requests.get('https://app.pluralsight.com/course-player?courseId='+self.clipId, proxies=PluralSight.proxyDict,verify=False)
		'''
		soup = BeautifulSoup(r.text, "html.parser")
		course_data= soup.find(id= "__NEXT_DATA__")
		course_props = str(course_data)[51:len(course_data)-10]
		data = json.loads(course_props)

		main_title = data['props']['pageProps']['tableOfContents']['title']
		self.dest = self.dest+main_title
		if not os.path.exists(self.dest):
			os.makedirs(self.dest)

		table_of_contents = data['props']['pageProps']['tableOfContents']
		ctr1 = 1

		for module in table_of_contents['modules']:
			mod_dir = module['title']
			print(f"module diur {mod_dir} ")
			ctr2 = 1
			if not os.path.exists(self.dest+"/"+str(ctr1)+" "+mod_dir):
				os.makedirs(self.dest+"/"+str(ctr1)+" "+mod_dir)
			
			for content in module['contentItems'] :
				file_path = self.dest+"/"+str(ctr1)+" "+mod_dir+"/"+str(ctr2)+" "+content['title'] + '.mp4'
				#print(f"--------file {file_path}")
				if path.exists(file_path):
					print(f"skipping the file {file_path}")
					ctr2 = ctr2 +1
					continue
				print( content['title'] )
				time.sleep(1)
				download_vid= self.get_download_link(content['id'],content['version'])
				self.download(download_vid,str(ctr1)+" "+mod_dir+"/"+str(ctr2)+" "+content['title'])
				ctr2 = ctr2 +1
				#exit()
			ctr1 = ctr1+1
			'''	


	#get the download link by sending POST request to https://app.pluralsight.com/video/clips/v3/viewclip
	def get_download_link(self,contentid,modid):
		#data = {"clipId":contentid,"mediaType":"mp4","quality":"1024x768","online":True,"boundedContext":"course","versionId":versionid}
		#headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0'}
		r = requests.get('https://subscription.packtpub.com/api/products/'+self.clipId+'/'+modid+'/'+contentid,proxies=PacktPub.proxyDict,verify=False)
		json_data = json.loads(r.text)
		download_url= json_data['data']

		return download_url


	#download the video with the title name
	def download(self,download_vid,title):
		#print(self.dest)
		#ssl._create_default_https_context = ssl._create_unverified_context
		#wget.download(download_vid, self.dest+"/"+str(title)+'.mp4')
		path=  self.dest+"/"+str(title)+'.mp4'
		#path ="/Users/speddala/Downloads/"
		args = f'curl --proxy "http://127.0.0.1:9999" "{download_vid}" --insecure -o "{path}"'
		print(args)
		subprocess.call([args],shell=True)


def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["courseId=","downloadloc="])
   except getopt.GetoptError:
      print('test.py -cid <courseId> -o <download_location>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <courseId> -o <downloadloc>')
         sys.exit()
      elif opt in ("-cid", "--courseId"):
         courseId = arg
      elif opt in ("-o", "--downloadloc"):
         downloadloc = arg
   print('content id  is ', courseId)
   print('downloadloc file is ', downloadloc)
   pl = PacktPub(courseId,downloadloc)
   pl.extract_course_details()

#call the Pluralight class with the clipdid
#clipid can be fetched through the https://app.pluralsight.com/library/

if __name__ == "__main__":
	main(sys.argv[1:])
	#pl = PluralSight("65568293-3622-4a80-87f5-c4134032bf38","/Users/speddala/Downloads/")
	#pl.extract_course_details()

