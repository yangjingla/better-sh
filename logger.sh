

function loginfo(){
    echo "[INFO] [$(date +"%Y-%m-%d %H:%M:%S")] $1"
}


function logerror(){
    echo "[ERROR] [$(date +"%Y-%m-%d %H:%M:%S")] $1"
}


fmt="lalala"


logerror ${fmt}

loginfo ${fmt}
