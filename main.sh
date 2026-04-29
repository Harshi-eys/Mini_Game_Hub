#!/bin/bash

check(){
	#Asks for usernames and passwords
	echo "Enter username:"
	read usr
	echo "Enter password:"
	read -s pass
	hash=$(echo -n "$pass" | sha256sum | awk '{print $1}') #Hashed passwords
	
	#Checking if user already exists.
	if grep -q "^$usr\t" users.tsv ; then
		orig_pass=$(grep "^$usr\t" users.tsv | awk -F '\t' '{print $2}')
		
		if [[ "$hash" == "$orig_pass" ]]; then #Checking the password
			echo "Successfully Logged in!"
		else 
			echo "Incorrect password!"
			check

		fi

	else
		echo "This username doesn't exist."
		echo "Do you want to register the new username?(yes/no)"
		read ans

		if [[ "$ans" == yes ]]; then
			echo -e "$usr\t$hash" >> users.tsv
		else
			check
		fi


	fi
}

echo "User 1: "
check
user1=$usr

echo "User 2: "
check
user2=$usr

python3 game.py "$user1" "$user2" #Calls the main file "game.py"
