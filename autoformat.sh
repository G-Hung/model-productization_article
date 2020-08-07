  
#/bin/bash
#
# If you get permission error, you can try
# chmod +rx autoformat.sh 

echo 'Running isort'
isort -rc ./scripts

echo 'Running black'
black ./scripts

echo 'Finished auto formatting'
