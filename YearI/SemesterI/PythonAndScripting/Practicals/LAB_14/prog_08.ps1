# Multiarray

$mdarray1 = @() 
$mdarray1_counter ++ 

$mdarray1 += @($mdarray1_counter, 'Earth',12742) 
$mdarray1_counter ++ 

$mdarray1 += @($mdarray1_counter, 'Mars',6779)
$mdarray1_counterr ++ 

$mdarray1 += @($mdarray1_counter, 'Venus',12104)
$mdarray1_counter ++ 

$mdarray1 += @($mdarray1_counter, 'Saturn',116464)


foreach($array10 in $mdarray1) {
  Write-host ($array10)
}

$array3 | Sort-Object
# $array8 = @("Earth","Mercury","Venus","Jupiter","Saturn","Mars", "Neptune", "Pluto")
