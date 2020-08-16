  
#/bin/bash
#
# If you get permission error, you can try
# chmod +rx autoformat.sh 

echo 'Running isort'
isort -rc ./scripts
isort -rc ./prediction_api

echo 'Running black'
black ./scripts
black ./prediction_api

echo 'Finished auto formatting'
