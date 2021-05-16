#Erase previous folder for fresh start
rm folderscount.txt
touch folderscount.txt
rm folders.txt
touch folders.txt


#Save current path
mpath=$(pwd)
echo "Current Directory: $mpath"

#Get the destination part
echo "Enter complete path to your directory: "
read cpath
cd $cpath

#List Folders
ls -LR > folderslist.txt

#Copy the list of folders from folderslist.txt to folders.txt in our directory
mv folderslist.txt "${mpath}/folders.txt"

#Change to our directory
cd $mpath

#Run the python program and save the output to folderscount.txt
python main.py
