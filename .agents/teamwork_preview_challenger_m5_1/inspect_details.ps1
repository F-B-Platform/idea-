$api = Get-Content 'd:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\03_Thiet_Ke_API_Contract.md' -Encoding UTF8
Write-Host '=== HEADINGS IN 03_Thiet_Ke_API_Contract.md ==='
$api | Where-Object { $_ -match '^##\s+' -or $_ -match '^###\s+' } | ForEach-Object { Write-Host $_ }

Write-Host "`n=== TABLE branch_wifi_configs IN 02_Thiet_Ke_Database.md ==="
$db = Get-Content 'd:\Idea_DoAn\03_Quy_Trinh_Trien_Khai\02_Thiet_Ke_Database.md' -Encoding UTF8
$start = $false
foreach ($line in $db) {
    if ($line -match 'CREATE TABLE branch_wifi_configs') { $start = $true }
    if ($start) {
        Write-Host $line
        if ($line -match '\);') { $start = $false }
    }
}

Write-Host "`n=== TABLE loyalty_cup_transactions IN 02_Thiet_Ke_Database.md ==="
$start = $false
foreach ($line in $db) {
    if ($line -match 'CREATE TABLE loyalty_cup_transactions') { $start = $true }
    if ($start) {
        Write-Host $line
        if ($line -match '\);') { $start = $false }
    }
}
