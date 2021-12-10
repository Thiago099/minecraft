<?php


header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");
header("Access-Control-Allow-Headers: Origin, Content-Type, Accept, Authorization");

$input = json_decode(file_get_contents('php://input'));


echo file_get_contents('mods.json');



// $mods[$input['id']]['enabled'] = $input['enabled'];


