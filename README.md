

	Gladiator Game Thingy
Made by Kevin Brown and Eric Krauss
Written in Python2 with PyGame 10/6/2015


Files

	run -->
		Bash script that runs the game
		can be used to automate testing
		and to include runtime arguments

	updateDoc -->
		Updates the Doxygen documentation's
		HTML files

	readDoc -->
		Opens the Doxygen documentation's
		HTML files in Chromium

	Main.py -->
		Ties the game files together and
		makes them run in tandem...
		it does what a main is supposed to

	UI.py -->
		Handles user-input and the final
		output as handed to it by Graphics

	Graphics.py -->
		Takes the arrays from Arena and the
		output from UI and layers them
		together before displaying them as
		symbols/sprites*

	Gladiator.py -->
		Receptical for stats and equipment
		for players' gladiators, and it
		handles combat between gladiators

	Arena.py -->
		Controls the boundaries, environment,
		and player positions and it handles
		player movement

	Referee.py -->
		Handles match start, match end
		conditions, turn order, and
		random events*

Styling

	Commenting -->	
		##Comments start with two pound symbols and
		##  continue with two pound symbols and two
		##  spaces as long as it's about one subject
		##
		##If you go into another subject, write two 
		##  pounds and a newline and then start the
		##  new comment
		##
		##Parameters are described with the following
		##  @param - Description
		##
		##TODO:  is used to announce plans for changes
		##  or additions to the function/method/class

	Functions -->
		Keep functions short and sweet, calling other
		functions in order to break up the required
		tasks and make the necessary documentation for
		that function small

	Documentation -->
		Every file is described in this README, all
		functions, methods, and class variables must
		have commenting to describe their purpose

	Doxygen -->
		Doxygen is a program that evaluates the code
		and the documentation therein and creates a
		series of HTML files that can be viewed in a
		web browser in order to access in depth
		documentation of all code in the project
		complete with search functionality.  This
		is why we go to such lengths in documenting
