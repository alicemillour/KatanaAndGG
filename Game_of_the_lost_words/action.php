<?php
//print_r($_GET)

switch($_GET['action'])
{
  case 'store_name': 
     //number1 = (int)$_GET['number1'];
     //number2 = (int)$_GET['number2'];
     //result = number1 + number2;
     
     echo "In store_name \n";
     echo $_GET['name'];
     file_put_contents("names.txt",$_GET['name'],FILE_APPEND); 
     file_put_contents("names.txt","\n",FILE_APPEND);
     break;  

} 
?>

