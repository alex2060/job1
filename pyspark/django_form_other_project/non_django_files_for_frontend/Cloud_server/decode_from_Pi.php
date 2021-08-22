

<?php

$mynumber = $_GET["number"];



if (strlen ($myoutput)==9 ) {

	#pass and log

}
else{

	if ( strlen ($myoutput)>=9 ) {
		# log out of bounds
	}


}


include("web_name.php");
include("config.php");




$sql = "SELECT * FROM `post_placer2` WHERE `keyer` LIKE 'mykey';";



$result = $conn->query($sql);


if ($result->num_rows==1) {
    while($row = $result->fetch_assoc()) {
            $output=$row["loc"];
        }

}




#path to django host
$sendurl= $output."/dat2/Dj.php?numb=".$mynumber;
$holdurl=$sendurl;
$make=$sendurl;
$ch1 = curl_init();
curl_setopt($ch1, CURLOPT_RETURNTRANSFER, 1);
curl_setopt ($ch1, CURLOPT_VERBOSE,TRUE);
curl_setopt($ch1, CURLOPT_URL,  str_replace(' ', '', $make)   );
$test2 =  curl_exec($ch1);
curl_close($ch1);


$out=json_decode($test2, true);

#echo $out["status"]." Number ".$out["Number"];
$status="No status";
$number="NA";
foreach($out as $key=>$value){
	if ($key=="status") {
		//echo "now is status";
		$status=$value;
	}

	if ($key=="Number") {
		$number=$value;
	}
    //echo $key . "=>" . $value . "<br>";
}
if ($status=="Ok") {
	echo $number;
}
else{
	echo $status;
}
?>

