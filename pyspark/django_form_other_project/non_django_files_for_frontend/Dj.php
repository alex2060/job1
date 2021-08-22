<?php


$numb_value=$_GET["numb"];




$sendurl= "http://127.0.0.1:8080/number?number=".$numb_value;
$make=$sendurl;
$ch1 = curl_init();
curl_setopt($ch1, CURLOPT_RETURNTRANSFER, 1);
curl_setopt ($ch1, CURLOPT_VERBOSE,TRUE);
curl_setopt($ch1, CURLOPT_URL,  str_replace(' ', '', $make)   );
$test2 =  curl_exec($ch1);
curl_close($ch1);

echo $test2;
?>
