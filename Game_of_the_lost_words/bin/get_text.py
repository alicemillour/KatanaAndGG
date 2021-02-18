import re
import os

def main():
	for i in ["001","002","002_Alice","004","005","006","007","008","009","010"]:		

		text_file="../data/Map{}_original.json".format(i)
		test_output="../data/Map{}.json".format(i)
		loc_file="../locales/en/Map{}.json".format(i)


		searched_strings=[]

		def get_repliques(text_file) :
			''' input : Map file generated by RPG Maker
			    output : list of repliques ([str])
			''' 
			with open(text_file) as f:
				# gets repliques from text file
				content=f.read()
				print(content)

				searched_strings = re.findall('\["([^]]*<br>)"', content)
				print(searched_strings)
				return searched_strings

		def write_loc_and_text_file(text_file, loc_file) :
			''' input : Map generated by RPG Maker 
				    Loc file 
			    Writes in loc_file the mappings and replace in text_file by mapping key
			'''
			name_map=text_file.split("/")[2].split(".")[0].split("_original")[0]
			print(name_map)
			searched_strings = get_repliques(text_file)
			print(searched_strings)
			with(open(loc_file, "w")) as f :
				f.write("{\n")
				i=0
				for replique in searched_strings:
					if i < len(searched_strings)-1 :			
						f.write("\t\"{}.R{}\": \"{}\",\n".format(name_map, str(i), replique))
					else :
						f.write("\t\"{}.R{}\": \"{}\"\n".format(name_map, str(i), replique))
					i += 1
				# remove last comma
				#f.seek(-1, os.SEEK_END)
				#f.truncate()
				f.write("}")
			content=""

			with open(text_file) as f :
				# create new Map content with mapping key
				i=0
				content=f.read()
				for replique in searched_strings:		
					print("réplique {} \n".format(replique))
					content=re.sub(re.escape(replique), "{{{}.R{}}}".format(name_map, str(i)) , content, count=0, flags=0)	
					#content=re.sub(re.escape(replique), "{{Map001.R{}}}".format(str(i)) , content, count=0, flags=0)			

					i+=1
			with open(test_output, "w") as f :
				f.write(content)

		write_loc_and_text_file(text_file, loc_file)


main()
