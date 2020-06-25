<?php
unlink("stop-script");  //Delete any existing stop-script

if((strpos($command,'vuza ihoni') === false)&&(strpos($command,'\n') === false)){
	$signal = "beepTwice()\n";
}

$blinkGreen = "blinkGreen()\n";

if((strpos($command,'burundu:') !== false)||(strpos($command,'gerageza:') !== false)){
	$removeStopScript = "os.remove('/var/www/html/1.0/stop-script')\n";
	$command = str_replace('@', '  ',$command);
}

file_put_contents('executor.py', $signal, FILE_APPEND);
//file_put_contents('executor.py', $blinkGreen, FILE_APPEND);

$command = str_replace('bisubiremo', 'for i in range',$command);
$command = str_replace('burundu:', 'while (True):
 if os.path.exists("stop-script"):
  break
 else:',$command);
$command = str_replace('gerageza:', 'count = 0
while(count < 5):
  count += 1',$command);
$command = str_replace('genzura imbere', 'senseRange()',$command);  
$command = str_replace('genzura ibumoso', 'senseRangeLeft()',$command);
$command = str_replace('genzura hagati', 'senseRangeMiddle()',$command);
$command = str_replace('genzura iburyo', 'senseRangeRight()',$command);
$command = str_replace('niba', 'if',$command);
$command = str_replace('bitabaye ibyo', 'else',$command);
$command = str_replace('bitari ibyo', 'else',$command);
$command = str_replace('bitihi se', 'else',$command);
$command = str_replace('intera', 'y.distance',$command);
$command = str_replace('intera ibumoso', 'y.distanceLeft',$command);
$command = str_replace('intera hagati', 'y.distanceMiddle',$command);
$command = str_replace('intera iburyo', 'y.distanceRight',$command);
$command = str_replace('jya imbere', 'forward',$command);
$command = str_replace('ますぐ', 'forward',$command);
$command = str_replace('genda kinyumanyuma', 'backward',$command);
$command = str_replace('バック', 'backward',$command);
$command = str_replace('kata ibumoso', 'left',$command);
$command = str_replace('ひだり', 'left',$command);
$command = str_replace('kata iburyo', 'right',$command);
$command = str_replace('みぎ', 'right',$command);
$command = str_replace('genda kinyumaburyo', 'rightBackward',$command);
$command = str_replace('genda kinyumabumoso', 'leftBackward',$command);
$command = str_replace('vuza ihoni', 'beepOnce',$command);
$command = str_replace('hagarara', 'stop()',$command);
$command = str_replace('ruhuka', 'pause',$command);
$command = str_replace('あいだ', 'pause',$command);
$command = str_replace(' =', '',$command);
$command = str_replace(' = ', '',$command);
$command = str_replace('= ', '',$command);
$command = str_replace('(igihe=', '(',$command);
$command = str_replace('( igihe=', '(',$command);
$command = str_replace(',umuvuduko=', ',',$command);
$command = str_replace(', umuvuduko=', ',',$command);
$command = str_replace('incuro=', '',$command);
$command = str_replace('inshuro=', '',$command);
$command = str_replace('@', ' ',$command);	
$command = str_replace('cana umutuku', 'turnONredLED',$command);
$command = str_replace('cana icyatsi', 'turnONgreenLED',$command);
$command = str_replace('zimya agatara', 'clearLED()',$command);	
$command = str_replace('::', 'def ',$command);
$command = str_replace('fungura ikiganza', 'handOpen()',$command);
$command = str_replace('funga ikiganza', 'handClose()',$command);	
	
file_put_contents("executor.py", $command."\n", FILE_APPEND);
file_put_contents("executor.py", $removeStopScript."\n", FILE_APPEND);

						
$bottom="\nfinish()\n";
file_put_contents('executor.py', $bottom, FILE_APPEND);
exec("sudo python executor.py");

?>
