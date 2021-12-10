<?php


header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");
header("Access-Control-Allow-Headers: Origin, Content-Type, Accept, Authorization");

$input = json_decode(file_get_contents('php://input'));


$mods = json_decode(file_get_contents('mods.json'));



// $mods[$input['id']]['enabled'] = $input['enabled'];

foreach($mods as $mod)
{
    if($mod->id == $input->id)
    {
        $mod->enabled = $input->enabled;
        unlink('mods.json');
        file_put_contents('mods.json', json_encode($mods));
        break;
    }
}

