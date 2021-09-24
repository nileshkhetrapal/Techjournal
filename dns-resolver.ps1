$Mask=$args[0]
$Dns=$args[1]
for (($i =1); ($i -lt 256); ($i++)){
    $ip=$mask+"."+$i
    Resolve-DnsName -DnsOnly $ip -Server $Dns -ErrorAction Ignore
}
