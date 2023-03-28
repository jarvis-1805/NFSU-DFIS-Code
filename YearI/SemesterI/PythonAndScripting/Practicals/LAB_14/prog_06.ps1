# IF condition

Clear-Host

$x = 10

if ($x -le 20) {
  write-host("This is if statement")
}

$x = 30

if ($x -le 20) {
  write-host("This is if statement")
} else {
  write-host("This is else statement")
}

$x = 30
$y = 10
if ($x -eq 30) {
  if ($y -eq 10) {
  write-host("X = 30 and Y = 10")
  }
}
