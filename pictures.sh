read input_variable
LINES_COUNT=`echo $input_variable | wc -w`
echo "Квадрат со стороной $LINES_COUNT"
for i in $(seq 1 $LINES_COUNT);
do
    echo $input_variable
done

#read input_variable
#echo "Квадрат со стороной $input_variable\n"
#for i in $(seq 1 $input_variable);
#do
#    echo $@
#done

#while read line
#do
#  LINES_COUNT=`echo $line | wc -w`
#  echo "Квадрат со стороной $LINES_COUNT"
#  echo ""
#    for i in $(seq 1 $LINES_COUNT);
#    do
#        echo $line
#    done
#  done
#done < "${1:-/dev/stdin}"

#for i in $(seq 1 $#);
#do
#    echo $@
#done
