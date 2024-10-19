# Daily Bible Verse Wallpaper:

Daily bible verse wallpaper, is a tool for linux gnome desktops. This tool is a Python-based program that fetches text from a website, integrates it into a randomly selected background image, and automatically sets the image as the desktop wallpaper. The program can be applied flexibly to different websites by providing CSS selectors.


# Requirements

 - Python 3.x
 - the following Python libraries:
	 - requests
	 - beautifulsoup4
	 - Pillow
	
 To install the required libraries, run:

    pip install requests beautifulsoup4 Pillow

## Installation
**Clone the repository**: Clone the repository to your local machine:

    git clone https://github.com/MatthiasElbel/daily_bible_verse.git


## Setup & Customization

 1. Create an folder and add .jpg background images
 2. Set the Path to the folder (main.py):

![grafik](https://github.com/user-attachments/assets/bd15cad4-60e9-4006-b020-325359829b9f)


3. Set the Url to any bible verse Website:

![grafik](https://github.com/user-attachments/assets/41bd7866-44eb-42d4-9176-a310b663258a)

4. Set the CSS-Sectors of the text:

   4.1 Go to the chosen Website:

	![grafik](https://github.com/user-attachments/assets/4f3b27fa-8bac-403b-a047-a81fa50cee4c)

   4.2 Right click the text you want to fetch and press on inspect:

   	![grafik](https://github.com/user-attachments/assets/9632f628-9877-410d-9d96-f3e824153788)

   4.3 Right click the selected line choose copy > CSS-Selector

   	![grafik](https://github.com/user-attachments/assets/8300bdee-965d-441e-9ec3-5706c328c160)

   4.4 Paste the CSS-Selector:

	![grafik](https://github.com/user-attachments/assets/9be0adab-12b2-43cb-b556-6345e229ff53)

   4.5 Repeat the process with as much CSS-Selectors you want:

   	![grafik](https://github.com/user-attachments/assets/f4441180-2b93-4adf-90bd-d1309316ade6)


   4.6 Set the max words per line:

    	![grafik](https://github.com/user-attachments/assets/1a3262bf-e77b-4161-b831-6ced47d319ed)

   4.7 Choose the destination for the output images

   	![grafik](https://github.com/user-attachments/assets/467bed61-24d3-4d34-b154-ddd5ab136a72)

   4.8 Run the python script

## Questions

Any Question feel free to write me: 

matthi.elbel@gmail.com

   	
