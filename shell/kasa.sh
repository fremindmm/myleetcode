#!/bin/bash
 
letter=(a b c d e f g h i j k l m n o p q r s t u v w x y z)
LETTER=(A B C D E F G H I J K L M N O P Q R S T U V W X Y Z)
 
read line
for ((i = 1; i <= 25; i++))
do
        printf "ROT%2d: " $i
        echo $line | tr 'A-Za-z' ${LETTER[$i]}-${LETTER[25]}${LETTER[0]}-${LETTER[$i-1]}${letter[$i]}-${letter[25]}${letter[0]}-${letter[$i-1]}
done
