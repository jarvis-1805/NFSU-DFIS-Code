# Array to List

$array5 = "one", "two", "three", "four", "five" 
$array5.gettype()

[System.Collections.ArrayList]$ArrayList1 = $array5 

$ArrayList1.GetType()
$ArrayList1.Add("six") 
$ArrayList1.Remove("three") 
$ArrayList1

$array6 = @(1,2,3,4,5,6)
$array6
