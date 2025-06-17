import subprocess

def stream_to_icecast(
	flac_file_path, 
	host = "192.168.10.100",
	port = 8000,
	mount = "/stream",
	password = "hackme",
	format = "ogg"
):
		command = [
			"ffmpeg",
			"-re", # Stream at real time
			"-i", flac_file_path, # Input flac file
			"-c:a", "libvorbis", # OGG codec 
			"-f", format, #format
			"-content_type", f"audio/{format}",
			f"icecast://source:{password}@{host}:{port}{mount}"
		]	
		try: 
			subprocess.run(command, check = True)
		except subprocess.CalledProcessError as e:
			print(e.output)

if __name__ == "__main__":
	#stream_to_icecast(flac_file_path = "../Machine Girl/Machine_Girl.flac", password = "hackme")
	stream_to_icecast(flac_file_path = "../Santana/Santana.flac", password = "hackme")