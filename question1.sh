# I am creating a loop to create directory-1 to directory-5

for i in {1..5}; do
    dir="directory-$i" 
    # defining the directory name 

    mkdir -p "$dir" 
    #Creating the new directory 

    echo "{\"directory_name\": \"$dir\"}" > "$dir/$dir.json"
    #Creating the new Json and I am adding them with an initial element with the directory name 
    
done

echo "Directories and .json files created successfully."
# This will print me the end of script to know all the directories and .json files has been created