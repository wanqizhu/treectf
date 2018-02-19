while true; do
  echo "BEGIN";
  sleep 1;
  nc -l 80 < index.html;
  echo "END";
done
