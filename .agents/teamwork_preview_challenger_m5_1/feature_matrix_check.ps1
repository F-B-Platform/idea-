$targetDir = "d:\Idea_DoAn\03_Quy_Trinh_Trien_Khai"
$f01 = Get-Content "$targetDir\01_Phan_Tich_Yeu_Cau.md" -Raw -Encoding UTF8
$f03 = Get-Content "$targetDir\03_Thiet_Ke_API_Contract.md" -Raw -Encoding UTF8
$f04 = Get-Content "$targetDir\04_Thiet_Ke_UI_UX.md" -Raw -Encoding UTF8
$f07 = Get-Content "$targetDir\07_Ke_Hoach_Kiem_Thu.md" -Raw -Encoding UTF8
$fRd = Get-Content "$targetDir\README.md" -Raw -Encoding UTF8

$features = @()
1..20 | ForEach-Object { $features += @{ Code = ('C-{0:D2}' -f $_); Actor = 'Customer' } }
1..13 | ForEach-Object { $features += @{ Code = ('S-{0:D2}' -f $_); Actor = 'Staff' } }
1..12 | ForEach-Object { $features += @{ Code = ('M-{0:D2}' -f $_); Actor = 'Manager' } }
1..17 | ForEach-Object { $features += @{ Code = ('A-{0:D2}' -f $_); Actor = 'Admin' } }

Write-Host "================================================================"
Write-Host "AUDITING 62 FEATURES DETAILS"
Write-Host "Total Features to check: $($features.Count)"
Write-Host "================================================================"

$passCount = 0
foreach ($feat in $features) {
    $c = $feat.Code
    $has01 = $f01 -match "\b$c\b"
    $has03 = $f03 -match "\b$c\b"
    $has04 = $f04 -match "\b$c\b"
    $has07 = $f07 -match "\b$c\b"
    $hasRd = $fRd -match "\b$c\b"
    
    if ($has01 -and $has03 -and $has04 -and $has07 -and $hasRd) {
        $passCount++
        # Write-Host "PASS: $c [$($feat.Actor)]"
    } else {
        Write-Host "FAIL: $c [$($feat.Actor)]: 01=$has01, 03=$has03, 04=$has04, 07=$has07, Rd=$hasRd"
    }
}

Write-Host "`nAll features checked: $passCount / $($features.Count) passed 100% matrix presence across 5 core documents!"
