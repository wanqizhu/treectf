while true; do 
  echo "BEGIN"; 
  python3 -m http.server 80; 
  PID=$!; 
  wait $PID; 
  echo "END";
done
