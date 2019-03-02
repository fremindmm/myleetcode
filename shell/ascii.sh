$ MESSAGE=`echo "84, 104, 101, 32, 115, 111, 108, 117, 116, 105, 111, 110, 32, 105, 115, 58, 32, 97, 112, 100, 99, 103, 97, 105, 115, 100, 115, 105, 99" | tr -d ','`

$ for ordinal in $MESSAGE; do printf "\x$(printf '%x' $ordinal)"; done; echo;
