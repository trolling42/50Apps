<?php
$data_array = array(
	0 => array("RHT", rand(1, 100)),
	1 => array("DG", rand(1, 100)),
	2 => array("SPB", rand(1, 100)),
	3 => array("AE", rand(1, 100)),
	4 => array("DFS", rand(1, 100)),
	5 => array("TEAR", rand(1, 100)),
	6 => array("SCVL", rand(1, 100)),
	7 => array("TNE", rand(1, 100)),
	8 => array("RGR", rand(1, 100)),
	9 => array("ERT", rand(1, 100))
);

echo json_encode($data_array);


?>
