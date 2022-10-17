#!/bin/bash

function sort_file_contents() {
	while true
		do
			echo ''
			echo '===== SORT FILE CONTENT MENU ====='
			echo '1. Ascending Order'
			echo '2. Descending Order'
			echo '3. List of Numbers'
			echo '4. List of Version Numbers'
			echo '0. Exit'
			echo ''
			
			read -p 'Enter your choice: ' ch
			echo ''
			
			if [ $ch -ne 0 ]
			then
				read -p 'Enter the file path: ' file
			fi
			
			case "$ch" in
				1)
					echo -e '\n===== Ascending Order Sorting ====='
					sort $file
				;;
				2)
					echo -e '\n===== Descending Order Sorting ====='
					sort -r $file
				;;
				3)
					echo -e '\n===== Numbers Sorting ====='
					sort -n $file
				;;
				4)
					echo -e '\n===== Version Numbers Sorting ====='
					sort --version-sort --field-separator=. $file
				;;
				0)
					echo 'Exiting...'
					exit
				;;
				*)
				echo "INVALID CHOICE\!\!! TRY AGAIN\!\!!"
				;;
			esac
	done
}

while true
	do
		echo ''
		echo '===== SORT MENU ====='
		echo '1. Alphabetically'
		echo '2. Size'
		echo '3. Time Modified'
		echo '4. File Extension'
		echo '5. Sort File Contents'
		echo '0. Exit'
		echo ''
		
		read -p 'Enter your choice: ' choice
		echo ''
		
		if [ $choice -ne 0 ] && [ $choice -gt 0 ] && [ $choice -lt 6 ]
		then
			read -p 'Enter the path: ' path
		fi
	
		case "$choice" in
			1)
				echo -e '\n===== Alphabetical Sorting ====='
				ls -l $path
			;;
			2)
				echo -e '\n===== Size Sorting ====='
				ls -lS $path
			;;
			3)
				echo -e '\n===== Time Modified Sorting ====='
				ls -lt $path
			;;
			4)
				echo -e '\n===== File Extension Sorting ====='
				ls -lX $path
			;;
			5)
				sort_file_contents
			;;
			0)
				echo 'Exiting...'
				exit
			;;
			*)
			echo -e "\nINVALID CHOICE\!\!! TRY AGAIN\!\!!"
			;;
		esac
done
