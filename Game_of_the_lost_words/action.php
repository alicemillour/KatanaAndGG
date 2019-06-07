<?php
//print_r($_GET)

switch($_GET['action'])
{
  case 'store_text': 
     //number1 = (int)$_GET['number1'];
     //number2 = (int)$_GET['number2'];
     //result = number1 + number2;
     
     echo "\nPHP : In store_text \n";
     echo $_GET['text'];
     echo file_put_contents("flower-text.txt",$_GET['text'],FILE_APPEND); 
     file_put_contents("flower-text.txt","\n",FILE_APPEND);
     break;  

} 
?>

