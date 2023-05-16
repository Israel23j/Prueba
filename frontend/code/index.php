<?php

    $url = "http://backend";
    $data = json_decode(file_get_contents($url),true);

    echo($data['message']);

?>